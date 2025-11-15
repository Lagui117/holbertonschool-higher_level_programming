#!/usr/bin/env python3
"""
XML serialization and deserialization module.
This module provides functions to serialize Python dictionaries to XML
and deserialize XML back to Python dictionaries.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    
    Args:
        dictionary: A Python dictionary to serialize
        filename: The name of the output XML file
    """
    # Create root element
    root = ET.Element('data')
    
    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    
    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.
    
    Args:
        filename: The name of the XML file to deserialize
        
    Returns:
        A Python dictionary with the deserialized data
    """
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Reconstruct dictionary
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    
    return dictionary
