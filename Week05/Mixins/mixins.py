import json
import xml.etree.ElementTree as ET

class Jsonable:
    def to_json(self, indent=4):
        return json.dumps(self, default=lambda o: {'type': o.__class__.__name__, 'dict': o.__dict__}, indent=indent)

    @classmethod
    def from_json(cls, json_string):
        dict_repr = json.loads(json_string)
        if cls.__name__ != dict_repr['type']:
            raise ValueError()
        return cls(**dict_repr['dict'])

class Xmlable:
    def to_xml(self):
        xml_string = '<' + self.__class__.__name__ + '>'
        for attribute, value in self.__dict__.items():
            xml_string += '<' + attribute + '>' + str(value) + '</' + attribute + '>'
        xml_string += '</' + self.__class__.__name__ + '>'
        return xml_string

    @classmethod
    def from_xml(cls, xml_string):
        xml_object = ET.fromstring(xml_string)
        if cls.__name__ != xml_object.tag:
            raise ValueError()
        object_dict = {}
        for node in xml_object:
            object_dict[node.tag] = int(node.text) if node.text.isnumeric() else node.text
        return cls(**object_dict)


class Panda(Jsonable, Xmlable):
    def __init__(self, **kwargs):
        for arg, value in kwargs.items():
            setattr(self, arg, value)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def play(self):
        print('playing')