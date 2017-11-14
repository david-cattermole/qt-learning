"""
Controls conversion to and from 'path tags'.

See 'test_paths.py' for details of expected usage.
"""

import re
import sys
import os

class PathSchema(object):
    # TODO: Looks up a path format based on a configuration file.
    def __init__(self, value):
        assert isinstance(value, str)
        self._pathFormatStr = value
        self._validator = None
        super(PathSchema, self).__init__()


# TODO: Integrate Schemas into path format.
class PathFormat(object):
    def __init__(self, *args):
        super(PathFormat, self).__init__()
        arg = None
        if len(args) == 1:
            arg = args[0]

        self._pathFormatStr = None
        self._validator = None
        if arg:
            assert isinstance(arg, str)
            self._pathFormatStr = arg

    def getString(self):
        return self._pathFormatStr

    def setString(self, value):
        self._pathFormatStr = value
        return

    def getValidator(self):
        # TODO: Support validation with the 'namingcon' project.
        return self._validator

    def setValidator(self, value):
        # TODO: Support validation with the 'namingcon' project.
        self._validator = value
        return

    @classmethod
    def _computeOrderedTagKeys(cls, pathFormatStr):
        ordered_keys = []
        prev_len = 0
        tmp_path = pathFormatStr
        while len(tmp_path) != prev_len:
            prev_len = len(tmp_path)
            i = tmp_path.find('{')
            if i != -1:
                j = tmp_path.find('}')
                if j != -1:
                    key = tmp_path[i:j+1]
                    key = key.replace('{', '').replace('}', '')
                    ordered_keys.append(key)
                    tmp_path = tmp_path[j+1:]
        return ordered_keys

    @classmethod
    def _computeTagKeyIndex(cls, tagKey, pathFormatStr):
        assert isinstance(tagKey, str)
        result = None
        ordered_keys = cls._computeOrderedTagKeys(pathFormatStr)
        if tagKey in ordered_keys:
            result = ordered_keys.index(tagKey)
        else:
            result = -1
        return result

    def computeOrderedTagKeys(self):
        pathFormatStr = self.getString()
        return self._computeOrderedTagKeys(pathFormatStr)

    def computeTagKeyIndex(self, tagKey):
        pathFormatStr = self.getString()
        return self._computeTagKeyIndex(tagKey, pathFormatStr)


class Path(object):
    def __init__(self, *args, **kwargs):
        path = kwargs.get('path')
        tags = kwargs.get('tags')
        format = kwargs.get('format')
        arg = None
        if len(args) == 1:
            arg = args[0]

        self._pathUpToDate = False
        self._tagsUpToDate = False

        if isinstance(arg, str):
            path = arg
            tags = None
            self._pathUpToDate = True
        elif isinstance(arg, dict):
            path = None
            tags = arg
            self._tagsUpToDate = True

        if path is not None:
            self._pathUpToDate = True
        if tags is not None:
            self._tagsUpToDate = True

        self._path = path
        self._tags = tags

        if format is None:
            self._pathFormat = None
        else:
            if isinstance(format, str):
                format = PathFormat(format)
            self._pathFormat = format
        assert self._pathFormat is None or isinstance(self._pathFormat, PathFormat)

        super(Path, self).__init__()

    @classmethod
    def _computePath(cls, tags, fmt, showMissingKeys=False):
        assert isinstance(fmt, PathFormat)
        assert isinstance(tags, dict)
        result = fmt.getString()
        keys = fmt.computeOrderedTagKeys()
        index = 0
        if showMissingKeys is True:
            for key in keys:
                value = tags.get(key)
                if value is None:
                    continue
                k = '{' + key + '}'
                result = result.replace(k, value)
        elif showMissingKeys is False:
            for key in keys:
                value = tags.get(key)
                k = '{' + key + '}'
                if value is None:
                    if index == 0:
                        # This ensures the first part of a path format is still
                        # maintained, even if the first key does not have a tag.
                        find_index = result.find(k)
                        if find_index != -1:
                            index = find_index
                    # The key doesn't exist or is None, we should quit now.
                    break
                find_index = result.find(k)
                if find_index != -1:
                    result = result.replace(k, value)
                    index = find_index + len(value)
                else:
                    break

            result = result[:index]
        else:
            raise ValueError
        return result

    @classmethod
    def _splitPathIntoTags(cls, path, fmt):
        # print('Path splitPathIntoTags:', path, fmt.getString())
        tmp = fmt.getString()
        tagKeys = fmt.computeOrderedTagKeys()
        # print('Path splitPathIntoTags tagKeys:', tagKeys)
        split = []
        newTags = {}
        for key in tagKeys:
            k = '{' + key + '}'
            frontPart = tmp.partition(k)
            split.append(frontPart[0])
            if '{' not in frontPart[-1] and '}' not in frontPart[-1]:
                split.append(frontPart[-1])
            tmp = frontPart[-1]

        s = 0
        e = len(path)
        split_next = split[1:] + ['']
        assert len(split) == len(split_next) == (len(tagKeys) + 1)
        for key, value, value_next in zip(tagKeys, split, split_next):
            # print('=', key, repr(value), repr(value_next), s, e)
            start_index = path.find(value, s)
            if start_index == -1:
                continue
            start_index = start_index + len(value)
            if len(value_next) == 0:
                end_index = len(path)
            else:
                end_index = path.find(value_next, start_index)
                if end_index == -1:
                    continue
                end_index += len(value_next) - 1
            s = end_index
            v = path[start_index:end_index]
            # print('v:', repr(v), start_index, end_index)
            if len(v) > 0:
                newTags[key] = v

        # print('Path splitPathIntoTags newTags:', newTags)
        return newTags

    def getPathFormat(self):
        return self._pathFormat

    def setPathFormat(self, value):
        assert isinstance(value, PathFormat)
        self._pathFormat = value
        return

    def getPath(self, showMissingKeys=False):
        path = None
        if self._pathUpToDate is True and self._tagsUpToDate is True:
            pass

        elif self._pathUpToDate is True and self._tagsUpToDate is False:
            fmt = self.getPathFormat()
            if fmt is None:
                return None
            tags = self._splitPathIntoTags(self._path, fmt)
            if len(tags) > 0:
                self._tags = tags
                self._tagsUpToDate = True

        elif self._pathUpToDate is False and self._tagsUpToDate is True:
            fmt = self.getPathFormat()
            if fmt is None:
                return None
            tags = self.getTags()
            self._path = self._computePath(tags, fmt, showMissingKeys=False)
            self._pathUpToDate = True

        elif self._pathUpToDate is False and self._tagsUpToDate is False:
            self._path = None
            return self._path

        else:
            raise ValueError

        if showMissingKeys is True:
            fmt = self.getPathFormat()
            path = self._computePath(self._tags, fmt, showMissingKeys=True)
        elif showMissingKeys is False:
            path = self._path
        else:
            raise ValueError
        return path

    def setPath(self, value):
        if self._path != value:
            # path has changed, therefore the tags are invalidated.
            self._tags = {}
            self._tagsUpToDate = False
        self._path = value
        self._pathUpToDate = True
        return

    def getTags(self):
        if self._tagsUpToDate is True and self._pathUpToDate is True:
            return self._tags.copy()

        elif self._tagsUpToDate is True and self._pathUpToDate is False:
            fmt = self.getPathFormat()
            if fmt is None:
                return None
            self._path = self._computePath(self._tags, fmt)
            self._pathUpToDate = True
            return self._tags.copy()

        elif self._tagsUpToDate is False and self._pathUpToDate is True:
            fmt = self.getPathFormat()
            if fmt is None:
                return None
            path = self._path
            self._tags = self._splitPathIntoTags(path, fmt)
            self._tagsUpToDate = True

        elif self._tagsUpToDate is False and self._pathUpToDate is False:
            return None

        else:
            raise ValueError

        return self._tags

    def getTagKeysOrdered(self):
        pathFormat = self.getPathFormat()
        keys = pathFormat.computeOrderedTagKeys()
        return keys

    def getTagValuesOrdered(self):
        pathFormat = self.getPathFormat()
        keys = pathFormat.computeOrderedTagKeys()
        values = []
        for key in keys:
            value = self.getTagValue(key)
            values.append(value)
        return values

    def getTagKeyIndex(self, tag):
        pathFormat = self.getPathFormat()
        index = pathFormat.computeTagKeyIndex(tag)
        return index

    def setTags(self, value):
        if self._tags != value:
            self._path = None
            self._pathUpToDate = False
        self._tags = value
        self._tagsUpToDate = True
        return

    def getTagValue(self, key, default=None):
        if self._tagsUpToDate is True and self._pathUpToDate is True:
            return self._tags.get(key, default)

        elif self._tagsUpToDate is True and self._pathUpToDate is False:
            fmt = self.getPathFormat()
            if fmt is None:
                return None
            self._path = self._computePath(self._tags, fmt)
            self._pathUpToDate = True
            return self._tags.get(key, default)

        elif self._tagsUpToDate is False and self._pathUpToDate is True:
            fmt = self.getPathFormat()
            if fmt is None:
                return None
            path = self._path
            self._tags = self._splitPathIntoTags(path, fmt)
            self._tagsUpToDate = True

        elif self._tagsUpToDate is False and self._pathUpToDate is False:
            return None

        else:
            raise ValueError

        return self._tags.get(key, default)

    def setTagValue(self, key, value):
        if self._tags.get(key) != value:
            self._path = None
            self._pathUpToDate = False
        self._tags[key] = value
        return

    def exists(self):
        pathName = self.getPath()
        return os.path.exists(pathName)

    def isValid(self):
        # TODO: Use 'namingcon' to test if the current Path object is valid.
        return True
