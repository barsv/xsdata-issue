from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
class Shiporder:
    class Meta:
        name = "shiporder"

    order_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "orderTime",
            "type": "Element",
            "namespace": "",
            "required": True,
            "nillable": True,
        }
    )
