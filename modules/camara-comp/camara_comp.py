# empty_component.py - sample code for a Simics configuration component
# Use this file as a skeleton for your own component implementations.

import simics
from comp import (StandardComponent, SimpleConfigAttribute, Interface)

class camara_comp(StandardComponent):
    """instantiates all devices for the pci camara"""
    _class_desc = "PCI Camara"
    _help_categories = ('PCI',)

    def setup(self):
        super().setup()
        if not self.instantiated.val:
            self.add_objects()
        self.add_connectors()

    def add_objects(self):
        sd = self.add_pre_obj('dev', 'pci_camara')
        
    def add_connectors(self):
        self.add_connector(slot = 'pci_bus', type = 'pci-bus', hotpluggable = True, required = False, multi = False,
                           direction = simics.Sim_Connector_Direction_Up)
           
    
    class basename(StandardComponent.basename):
        """The default name for the created component"""
        val = "pci_camara"
                        

    class component_connector(Interface):
        """Uses connector for handling connections between components."""
        def get_check_data(self, cnt):
            return []
        def get_connect_data(self, cnt):
            return [[[0, self._up.get_slot('dev')]]]
        def check(self, cnt, attr):
            return True
        def connect(self, cnt, attr):
            self._up.get_slot('dev').pci_bus = attr[1]
        def disconnect(self, cnt):
            self._up.get_slot('dev').pci_bus = None
