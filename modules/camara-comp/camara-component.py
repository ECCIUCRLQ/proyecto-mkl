# This Software is part of Simics. The rights to copy, distribute,
# modify, or otherwise make use of this Software may be licensed only
# pursuant to the terms of an applicable license agreement.
# 
# Copyright 2010-2022 Intel Corporation

# <add id="sample_components.py" label="sample_components.py">
# <insert-until text="# END sample_components.py"/>
# </add>
import simics
from comp import StandardComponent, SimpleConfigAttribute, Interface

class sample_pci_card(StandardComponent):
    """A sample component containing a sample PCI device."""
    _class_desc = "UNa camara PCI"
    _help_categories = ('PCI',)

    def setup(self):
        super().setup()
        if not self.instantiated.val:
            self.add_objects()
        self.add_connectors()

    def add_objects(self):
        sd = self.add_pre_obj('dev', 'camara-pci')
        sd.int_attr = self.integer_attribute.val

    def add_connectors(self):
        self.add_connector(slot = 'pci_bus', type = 'pci-bus',
                           hotpluggable = True, required = False, multi = False,
                           direction = simics.Sim_Connector_Direction_Up)

    class basename(StandardComponent.basename):
        """The default name for the created component"""
        val = "camara_comp"

    class integer_attribute(SimpleConfigAttribute(None, 'i',
                                                  simics.Sim_Attr_Required)):
        """Example integer attribute."""

    class component_connector(Interface):
        """Uses connector for handling connections between components."""
        def get_check_data(self, cnt):
            return []
        def get_connect_data(self, cnt):
            return [[[0, self._up.get_slot('sample_dev')]]]
        def check(self, cnt, attr):
            return True
        def connect(self, cnt, attr):
            self._up.get_slot('sample_dev').pci_bus = attr[1]
        def disconnect(self, cnt):
            self._up.get_slot('sample_dev').pci_bus = None

# END sample_components.py
