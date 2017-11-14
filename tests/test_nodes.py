"""
Tests for the 'paths' module.
"""

import sys
import os
import unittest

import qtLearn.nodes as nodes


class TestNode(unittest.TestCase):
    def test_init(self):
        name = 'myNode'
        n = nodes.Node(name)
        self.assertEqual(n.name(), name)

        data = {'cool': 'stuff'}
        n = nodes.Node(name, data=data)
        self.assertEqual(n.data(), data)

        n = nodes.Node(name, data=None)
        self.assertEqual(n.data(), {})

        tooltip = 'tooltip'
        n = nodes.Node(name, data=data, toolTip=tooltip)
        self.assertEqual(n.toolTip(), tooltip)

        statusTip = 'status line text'
        n = nodes.Node(name, data=data, toolTip=tooltip, statusTip=statusTip)
        self.assertEqual(n.statusTip(), statusTip)

        parent = nodes.Node('root')
        n1 = nodes.Node(name+'1', parent=parent)
        n2 = nodes.Node(name+'2', parent=parent)
        n3 = nodes.Node(name+'3', parent=parent)
        self.assertEquals(n1.parent(), parent)
        self.assertEquals(n2.parent(), parent)
        self.assertEquals(n3.parent(), parent)
        self.assertEqual(parent.childCount(), 3)

        n1 = nodes.Node(name, enabled=True)
        n2 = nodes.Node(name, enabled=False)
        n3 = nodes.Node(name)
        self.assertEqual(n1.enabled(), True)
        self.assertEqual(n2.enabled(), False)
        self.assertEqual(n3.enabled(), True)

        n1 = nodes.Node(name, editable=True)
        n2 = nodes.Node(name, editable=False)
        n3 = nodes.Node(name)
        self.assertEqual(n1.editable(), True)
        self.assertEqual(n2.editable(), False)
        self.assertEqual(n3.editable(), False)

        n1 = nodes.Node(name, selectable=True)
        n2 = nodes.Node(name, selectable=False)
        n3 = nodes.Node(name)
        self.assertEqual(n1.selectable(), True)
        self.assertEqual(n2.selectable(), False)
        self.assertEqual(n3.selectable(), True)

        n1 = nodes.Node(name, checkable=True)
        n2 = nodes.Node(name, checkable=False)
        n3 = nodes.Node(name)
        self.assertEqual(n1.checkable(), True)
        self.assertEqual(n2.checkable(), False)
        self.assertEqual(n3.checkable(), False)

        n1 = nodes.Node(name, neverHasChildren=True)
        n2 = nodes.Node(name, neverHasChildren=False)
        n3 = nodes.Node(name)
        self.assertEqual(n1.neverHasChildren(), True)
        self.assertEqual(n2.neverHasChildren(), False)
        self.assertEqual(n3.neverHasChildren(), False)

    def test_setName(self):
        name = 'myNode'
        newName = 'newNodeName'
        n = nodes.Node(name)
        self.assertEqual(n.name(), name)
        self.assertTrue(isinstance(n.name(), str))
        n.setName(newName)
        self.assertEqual(n.name(), newName)
        self.assertTrue(isinstance(n.name(), str))

    def test_setTooltip(self):
        toolTip = 'my tooltip'
        newToolTip = 'the new tooltip'
        n = nodes.Node('name', toolTip=toolTip)
        self.assertEqual(n.toolTip(), toolTip)
        self.assertTrue(isinstance(n.toolTip(), str))
        n.setToolTip(newToolTip)
        self.assertEqual(n.toolTip(), newToolTip)
        self.assertTrue(isinstance(n.toolTip(), str))

    def test_setStatusTip(self):
        statusTip = 'my statusTip'
        newStatusTip = 'the new statusTip'
        n = nodes.Node('name', statusTip=statusTip)
        self.assertEqual(n.statusTip(), statusTip)
        self.assertTrue(isinstance(n.statusTip(), str))
        n.setStatusTip(newStatusTip)
        self.assertEqual(n.statusTip(), newStatusTip)
        self.assertTrue(isinstance(n.statusTip(), str))

    def test_setData(self):
        data = {'key': 'value'}
        newData = {'new key': 'new value'}
        n = nodes.Node('name', data=data)
        self.assertEqual(n.data(), data)
        self.assertTrue(isinstance(n.data(), dict))
        n.setData(newData)
        self.assertEqual(n.data(), newData)
        self.assertTrue(isinstance(n.data(), dict))

    def test_setEnabled(self):
        newEnabled = False
        n = nodes.Node('name')
        self.assertTrue(isinstance(n.enabled(), bool))
        n.setEnabled(newEnabled)
        self.assertEqual(n.enabled(), newEnabled)
        self.assertTrue(isinstance(n.enabled(), bool))

    def test_setEditable(self):
        newEditable = True
        n = nodes.Node('name')
        self.assertTrue(isinstance(n.editable(), bool))
        n.setEditable(newEditable)
        self.assertEqual(n.editable(), newEditable)
        self.assertTrue(isinstance(n.editable(), bool))

    def test_setSelectable(self):
        newSelectable = False
        n = nodes.Node('name')
        self.assertTrue(isinstance(n.selectable(), bool))
        n.setSelectable(newSelectable)
        self.assertEqual(n.selectable(), newSelectable)
        self.assertTrue(isinstance(n.selectable(), bool))

    def test_setCheckable(self):
        newCheckable = True
        n = nodes.Node('name')
        self.assertTrue(isinstance(n.checkable(), bool))
        n.setCheckable(newCheckable)
        self.assertEqual(n.checkable(), newCheckable)
        self.assertTrue(isinstance(n.checkable(), bool))

    def test_setNeverHasChildren(self):
        newNeverHasChildren = True
        n = nodes.Node('name')
        self.assertTrue(isinstance(n.neverHasChildren(), bool))
        n.setNeverHasChildren(newNeverHasChildren)
        self.assertEqual(n.neverHasChildren(), newNeverHasChildren)
        self.assertTrue(isinstance(n.neverHasChildren(), bool))

    def test_insertChild(self):
        n1 = nodes.Node('node1')
        n2 = nodes.Node('node2')
        r = n1.insertChild(0, n2)
        self.assertTrue(r)
        self.assertEqual(n1.childCount(), 1)
        self.assertEquals(n1.child(0), n2)

        r = n1.insertChild(2, n2)
        self.assertFalse(r)

    def test_removeChild(self):
        n1 = nodes.Node('node1')
        n2 = nodes.Node('node2', parent=n1)
        self.assertEqual(n1.childCount(), 1)

        r = n1.removeChild(99)
        self.assertFalse(r)

        r = n1.removeChild(0)
        self.assertTrue(r)
        self.assertEqual(n1.childCount(), 0)

    def test_child(self):
        num = 9
        p = nodes.Node('parent')
        ns = []
        for i in range(num):
            n = nodes.Node('node'+str(i), parent=p)
            ns.append(n)
        self.assertEqual(p.childCount(), num)
        for i in range(p.childCount()):
            c = p.child(i)
            n = ns[i]
            self.assertEquals(n, c)

    def test_children(self):
        num = 9
        p = nodes.Node('parent')
        ns = []
        for i in range(num):
            n = nodes.Node('node'+str(i), parent=p)
            ns.append(n)
        self.assertEqual(p.childCount(), num)
        children = p.children()
        self.assertEquals(children, ns)

    def test_row(self):
        p = nodes.Node('parent')
        n1 = nodes.Node('node1', parent=p)
        n2 = nodes.Node('node2', parent=p)
        n3 = nodes.Node('node3', parent=p)
        n4 = nodes.Node('node4', parent=p)
        self.assertEqual(p.childCount(), 4)
        row1 = n1.row()
        row2 = n2.row()
        row3 = n3.row()
        row4 = n4.row()
        self.assertEqual(row1, 0)
        self.assertEqual(row2, 1)
        self.assertEqual(row3, 2)
        self.assertEqual(row4, 3)
        self.assertEqual(p.row(), 0)

    def test_allTags(self):
        # Tests parentTags, childrenTags, allTags and allTagsStr.
        n0 = nodes.Node('parent')
        n1 = nodes.Node('node1', parent=n0)
        n2 = nodes.Node('node2', parent=n1)
        n3 = nodes.Node('node3', parent=n2)
        n4 = nodes.Node('node4', parent=n3)
        n5 = nodes.Node('node5', parent=n4)

        n11 = nodes.Node('node11', parent=n0)
        n12 = nodes.Node('node12', parent=n11)
        n13 = nodes.Node('node13', parent=n12)

        tags0 = ['parent', 'node1', 'node2', 'node3', 'node4', 'node5', 'node11', 'node12', 'node13']
        tags1 = ['node1', 'parent', 'node2', 'node3', 'node4', 'node5']
        tags2 = ['node2', 'node1', 'parent', 'node3', 'node4', 'node5']
        tags3 = ['node3', 'node2', 'node1', 'parent', 'node4', 'node5']
        tags4 = ['node4', 'node3', 'node2', 'node1', 'parent', 'node5']
        tags5 = ['node5', 'node4', 'node3', 'node2', 'node1', 'parent']
        tags11 = ['node11', 'parent', 'node12', 'node13']

        self.assertEqual(n0.allTags(), tags0)
        self.assertEqual(n1.allTags(), tags1)
        self.assertEqual(n2.allTags(), tags2)
        self.assertEqual(n3.allTags(), tags3)
        self.assertEqual(n4.allTags(), tags4)
        self.assertEqual(n5.allTags(), tags5)
        self.assertEqual(n11.allTags(), tags11)

        value = 'parent|node1|node2|node3|node4|node5|node11|node12|node13'
        self.assertEqual(n0.allTagsStr(), value)


if __name__ == '__main__':
    prog = unittest.main()
