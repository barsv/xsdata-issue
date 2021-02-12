from generated.test import Shiporder
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
import xmlschema

config = SerializerConfig(pretty_print=True)
xml_serializer = XmlSerializer(config=config)
schema = xmlschema.XMLSchema('test.xsd')

order = Shiporder()

xml = xml_serializer.render(order)
print(xml)
schema.validate(xml)
