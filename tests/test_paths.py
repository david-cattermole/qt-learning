"""
Tests for the 'paths' module.
"""

import sys
import os
import unittest

import qtLearn.paths as paths


class TestPathSchema(unittest.TestCase):
    def test_init(self):
        schema = paths.PathSchema('myValueGoesHere???')


class TestPathFormat(unittest.TestCase):
    def test_init(self):
        fmt = paths.PathFormat()
        value = fmt.getString()
        self.assertEqual(value, None)

        data = '/{project}/{shot}/{assetType}/{name}/{user}_{version}.{ext}'
        fmt = paths.PathFormat(data)
        value = fmt.getString()
        self.assertEqual(value, data)

    def test_getString(self):
        data = '/{project}/{shot}/{assetType}/{name}/{user}_{version}.{ext}'
        fmt = paths.PathFormat(data)
        value = fmt.getString()
        self.assertEqual(value, data)

    def test_setString(self):
        fmt = paths.PathFormat()
        data = '/{project}/{sequence}{shot}/{user}.{ext}'
        fmt.setString(data)
        value = fmt.getString()
        self.assertEqual(value, data)


class TestPath(unittest.TestCase):
    def test_init(self):
        fmtStr = '/{path}/{name}/{version}.{ext}'
        fmt = paths.PathFormat(fmtStr)

        pth = paths.Path()
        self.assertEqual(pth.getPath(), None)
        self.assertEqual(pth.getTags(), None)

        data = '/path/to/file.txt'
        pth = paths.Path(data)
        self.assertEqual(pth.getPath(), None)
        pth.setPathFormat(fmt)
        self.assertEqual(pth.getPath(), data)

        pth = paths.Path(path=data, format=fmt)
        self.assertEqual(data, pth.getPath())

        data = {'key': 'value'}
        pth = paths.Path(data)
        self.assertEqual(pth.getTags(), None)
        pth.setPathFormat(fmt)
        self.assertEqual(pth.getTags(), data)

        pth = paths.Path(tags=data, format=fmt)
        self.assertEqual(data, pth.getTags())

        pth1 = paths.Path('/my/path/goes/here', format=fmtStr)
        fmt2 = pth1.getPathFormat()
        self.assertEqual(fmt.getString(), fmt2.getString())

    def test_getPath(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        value = '/myAsset_v001.obj'
        pth = paths.Path(value, format=fmt)
        self.assertEqual(pth.getPath(), value)
        path = pth.getPath()
        self.assertEqual(pth.getPath(), path)

        pth.setPath('/myAsset_v001.')
        path = pth.getPath(showMissingKeys=True)
        self.assertEqual(path, '/myAsset_v001.{ext}')

        fmt = paths.PathFormat('/projects/{project}/{name}_{version}.{ext}')
        pth = paths.Path({'name': 'myAsset', 'version': 'v001', 'ext': 'obj'}, format=fmt)
        self.assertEqual(pth.getPath(), '/projects/')

        fmt = paths.PathFormat('/projects/{project}/{name}_{version}.{ext}')
        pth = paths.Path({'name': 'myAsset', 'version': 'v001', 'ext': 'obj'}, format=fmt)
        self.assertEqual(pth.getPath(), '/projects/')

    def test_setPath(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        pth = paths.Path(format=fmt)
        value = '/myAsset_v001.obj'
        pth.setPath(value)
        self.assertEqual(pth.getPath(), value)

    def test_getTags(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        tags1 = {'name': 'myAsset', 'version': 'v001', 'ext': 'obj'}
        pth = paths.Path(tags1, format=fmt)
        tags2 = pth.getTags()
        self.assertTrue(tags1 is not tags2)
        self.assertEqual(tags1, tags2)

    def test_getTagValue(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        value = '/myAsset_v001.obj'
        pth = paths.Path(value, format=fmt)
        self.assertEqual(pth.getTagValue('name'), 'myAsset')
        self.assertEqual(pth.getTagValue('nonexistantkey'), None)

        pth = paths.Path()
        self.assertEqual(pth.getTagValue('key'), None)

    def test_getTagKeysOrdered(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        pth = paths.Path('/myAsset_v001.obj', format=fmt)
        keys = ['name', 'version', 'ext']
        self.assertEqual(keys, pth.getTagKeysOrdered())

    def test_getTagValuesOrdered(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        pth = paths.Path('/myAsset_v001.obj', format=fmt)
        values = ['myAsset', 'v001', 'obj']
        self.assertEqual(values, pth.getTagValuesOrdered())

    def test_getTagKeyIndex(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        pth = paths.Path('/myAsset_v001.obj', format=fmt)
        keys = fmt.computeOrderedTagKeys()
        for i, key in enumerate(keys):
            j = pth.getTagKeyIndex(key)
            self.assertEqual(j, i)

    def test_setTags(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        tags = {'name': 'myAsset', 'version': 'v001', 'ext': 'obj'}
        pth = paths.Path(tags, format=fmt)
        tags_copy = pth.getTags()
        tags.update(version='v002')
        pth.setTags(tags)
        self.assertTrue(tags is not tags_copy)
        self.assertNotEqual(pth.getTags(), tags_copy)

    def test_setTagValue(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        tags = {'name': 'myAsset', 'version': 'v001', 'ext': 'obj'}
        pth = paths.Path(tags, format=fmt)
        self.assertEqual(pth.getTagValue('name'), 'myAsset')
        pth.setTagValue('name', 'myFile')
        self.assertEqual(pth.getTagValue('name'), 'myFile')

    def test_exists(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        tags = {'name': 'myAsset', 'version': 'v001', 'ext': 'obj'}
        pth = paths.Path(tags, format=fmt)
        self.assertFalse(pth.exists())

    def test_isValid(self):
        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        tags = {'name': 'myAsset', 'version': 'v001', 'ext': 'obj'}
        pth = paths.Path(tags, format=fmt)
        self.assertTrue(pth.isValid())

    def test_splitPathIntoTags(self):
        fmt = paths.PathFormat('/projects/{project}/{sequence}/{shot}/{department}/{task}/{name}_{major}.{minor}.{ext}')
        value = '/projects/xmen/fin/fin0020/{department}/{task}/{name}_{major}.{minor}.{ext}'
        pth = paths.Path(value, format=fmt)
        self.assertEqual(pth.getPath(showMissingKeys=True), value)

        fmt = paths.PathFormat('/{name}_{version}.{ext}')
        value = '/myAsset_v001.obj'
        # pth = paths.Path(, format=fmt)
        tags = paths.Path._splitPathIntoTags(value, fmt)
        values = {'name': 'myAsset', 'version': 'v001', 'ext': 'obj'}
        self.assertEqual(values, tags)

    def test_pathAndTagsConversion(self):
        fmt = paths.PathFormat('/{project}/{shot}/{assetType}/{name}/{user}_{version}.{ext}')
        pth = paths.Path({'project': 'dunkirk', 'shot': 'sh0010', 'assetType': 'rig'}, format=fmt)
        pth.setTagValue('user', 'davidc')
        pth.setTagValue('ext', 'doc')
        pth.setTagValue('name', 'myAsset')
        pth.setTagValue('version', 'v001')
        path = pth.getPath()
        path = path.replace('myAsset', 'car001')
        pth.setPath(path)
        tags = pth.getTags()
        self.assertIn('version', tags)
        tags['shot'] = 'sh0020'
        pth.setTags(tags)


if __name__ == '__main__':
    prog = unittest.main()
