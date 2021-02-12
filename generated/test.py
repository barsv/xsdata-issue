from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Shiporder:
    class Meta:
        name = "shiporder"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "nillable": True,
        }
    )
