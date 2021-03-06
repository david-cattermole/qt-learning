"""
Defines a helping class that creates attribute widgets.
"""

import qtLearn.widgets.comboBoxAttr as comboBoxAttr
import qtLearn.widgets.comboBox2Attr as comboBox2Attr
import qtLearn.widgets.comboBox3Attr as comboBox3Attr

import qtLearn.widgets.integerAttr as integerAttr
import qtLearn.widgets.integer2Attr as integer2Attr
import qtLearn.widgets.integer3Attr as integer3Attr

import qtLearn.widgets.floatAttr as floatAttr
import qtLearn.widgets.float2Attr as float2Attr
import qtLearn.widgets.float3Attr as float3Attr

import qtLearn.widgets.lineEditAttr as lineEditAttr


class AttributeHelper(object):

    def __init__(self, layout=None):
        self._layout = None
        if layout is not None:
            self._layout = layout

    def setLayout(self, layout):
        assert isinstance(layout, object)
        self._layout = layout

    @staticmethod
    def _lookupWidgetClass(name):
        assert isinstance(name, str)
        result = None
        n = name.lower()
        if 'combobox1' in n:
            result = comboBoxAttr.ComboBoxAttr
        elif 'combobox2' in n:
            result = comboBox2Attr.ComboBox2Attr
        elif 'combobox3' in n:
            result = comboBox3Attr.ComboBox3Attr
        elif 'combobox' in n:
            result = comboBoxAttr.ComboBoxAttr
        elif 'integer1' in n:
            result = integerAttr.IntegerAttr
        elif 'integer2' in n:
            result = integer2Attr.Integer2Attr
        elif 'integer3' in n:
            result = integer3Attr.Integer3Attr
        elif 'integer' in n:
            result = integerAttr.IntegerAttr
        elif 'float1' in n:
            result = floatAttr.FloatAttr
        elif 'float2' in n:
            result = float2Attr.Float2Attr
        elif 'float3' in n:
            result = float3Attr.Float3Attr
        elif 'float' in n:
            result = floatAttr.FloatAttr
        elif 'lineedit' in n:
            result = lineEditAttr.LineEditAttr
        else:
            result = None
            raise ValueError
        return result

    def addWidget(self, class_name, label=None, **kwargs):
        if label is None:
            label = 'label'
        Model = None
        if isinstance(class_name, str):
            Model = self._lookupWidgetClass(class_name)
        else:
            msg = 'Incorrect class name given.'
            raise ValueError(msg)
        widget = Model(label=label, **kwargs)
        self._layout.addWidget(widget)
        return widget

    def addComboBoxAttr(self, label=None):
        return self.addWidget('ComboBox1', label=label)

    def addComboBox2Attr(self, label=None):
        return self.addWidget('ComboBox2', label=label)

    def addComboBox3Attr(self, label=None):
        return self.addWidget('ComboBox3', label=label)

    def addIntegerAttr(self, label=None):
        return self.addWidget('Integer1', label=label)

    def addInteger2Attr(self, label=None):
        return self.addWidget('Integer2', label=label)

    def addInteger3Attr(self, label=None):
        return self.addWidget('Integer3', label=label)

    def addFloatAttr(self, label=None):
        return self.addWidget('Float1', label=label)

    def addFloat2Attr(self, label=None):
        return self.addWidget('Float2', label=label)

    def addFloat3Attr(self, label=None):
        return self.addWidget('Float3', label=label)

    def addLineEditAttr(self, label=None, withLabel=True, withButton=False,
                        buttonText=None, buttonIcon=None):
        return self.addWidget('LineEdit', label=label, withLabel=withLabel,
                              withButton=withButton, buttonText=buttonText,
                              buttonIcon=buttonIcon)

