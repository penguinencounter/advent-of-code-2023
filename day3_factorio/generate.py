import re
from typing import Callable, Optional
from draftsman.blueprintable import Blueprint
from draftsman.constants import Direction
from draftsman.entity import ConstantCombinator, DeciderCombinator, ElectricPole, Lamp
from draftsman.classes.group import Group

POLE_DIST = 7


class ROMCell(Group):
    """
    Represents a single memory cell in the ROM array.
    Set signals are attached to the embedded Constant Combinator.
    """

    def __init__(
        self,
        id,
        name="rom-cell",
        position=(0, 0),
        internal_data_wire="red",
        internal_lamp_wire="green",
        **kwargs
    ):
        super(ROMCell, self).__init__(id, position=position)
        
        # Cell ID (required)
        self.id = id
        self.data_id = f'{self.id}_data'
        self.lamp_id = f'{self.id}_lamp'
        self.gate_id = f'{self.id}_gate'

        # Entity name
        self.name = name
        # Entity type for queries
        self._type = "rom-cell"

        comb_name = "constant-combinator"
        lamp_name = "small-lamp"
        
        # top left corner
        self.position = position
        self.direction = Direction.NORTH
        if "direction" in kwargs:
            self.direction = kwargs["direction"]
        
        data = ConstantCombinator(comb_name, id=self.data_id, position=(0, 0), direction=Direction.SOUTH) # type: ignore
        lamp = Lamp(lamp_name, id=self.lamp_id, position=(1, 0)) # type: ignore
        lamp.use_colors = True
        lamp.set_circuit_condition("signal-anything", ">", 0)
        gate = DeciderCombinator(id=self.gate_id, position=(1, 1), direction=Direction.EAST) # type: ignore
        gate.set_decider_conditions("signal-E", ">", 0, "signal-everything", True)

        self.maxsize = data.item_slot_count

        self._collision_mask = data.collision_mask | lamp.collision_mask | gate.collision_mask

        self.entities.append(data)
        self.entities.append(lamp)
        self.entities.append(gate)

        self.add_circuit_connection(internal_data_wire, self.data_id, self.gate_id, 1, 1)
        self.add_circuit_connection(internal_lamp_wire, self.gate_id, self.lamp_id, 2, 1)
    
    def set_data(self, kv: dict[str, int]):
        assert len(kv) <= self.maxsize
        for i, (k, v) in enumerate(kv.items()):
            comb: ConstantCombinator = self.entities[self.data_id]
            comb.set_signal(
                index = i,
                signal = k,
                count = v
            )


def generate():
    bp = Blueprint()
    bp.label = f"AOC2023 Day 3 ROM"
    bp.description = "[font=default-bold]Usage[/font]\n"
    # with open("3.in") as f:
    #     data = f.read().splitlines()
    r = ROMCell('test')
    mapping = {}
    for k in ['anything', 'everything', 'each', 'X', 'Y', 'Z', '2']:
        mapping[f'signal-{k}'] = 1
    r.set_data(mapping)
    bp.entities.append(r)
    print(bp.to_string())


if __name__ == "__main__":
    generate()
