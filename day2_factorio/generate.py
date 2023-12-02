import re
from typing import Callable, Optional
from draftsman.blueprintable import Blueprint
from draftsman.constants import Direction
from draftsman.entity import ConstantCombinator, DeciderCombinator, ElectricPole

POLE_DIST = 7


def apply_round_info(com: ConstantCombinator, round_string: str):
    cursor = 0
    for m in re.finditer(r"(\d+) (red|green|blue)", round_string):
        count = int(m.group(1))
        name = f"signal-{m.group(2)}"
        com.set_signal(cursor, name, count)
        cursor += 1


def apply_reset_info(com: ConstantCombinator):
    com.set_signal(0, "signal-R", 2147483647)


def apply_end_of_game_info(com: ConstantCombinator, game_no: int):
    com.set_signal(0, "signal-E", 1)
    com.set_signal(1, "signal-G", game_no)


def add_data(
    bp: Blueprint,
    head_pos: int,
    last_decider: Optional[DeciderCombinator],
    data_func: callable,
    *args,
) -> DeciderCombinator:
    com_name = f"com_{head_pos}"
    dec_name = f"dec_{head_pos}"
    com = ConstantCombinator(
        id=com_name, tile_position=(head_pos, 1), direction=Direction.NORTH
    )
    com.set_signal(com.item_slot_count - 1, "signal-M", head_pos)

    dec = DeciderCombinator(
        id=dec_name, tile_position=(head_pos, -2), direction=Direction.NORTH
    )
    dec.set_decider_conditions("signal-N", "=", "signal-M", "signal-everything", True)
    data_func(com, *args)

    bp.entities.append(com)
    bp.entities.append(dec)

    bp.add_circuit_connection(
        "red", com_name, dec_name, side2=1
    )  # connect constant to decider input
    if last_decider is not None:
        bp.add_circuit_connection(
            "red", dec_name, last_decider.id, 2, 2
        )  # connect outputs
        bp.add_circuit_connection(
            "green", dec_name, last_decider.id, 1, 1
        )  # connect clock wire

    if head_pos % 7 == 1:
        # Add a Medium electric pole
        last_pole_name = f"pole_{head_pos - 7}"
        curr_pole_name = f"pole_{head_pos}"
        current_pole = ElectricPole(
            "medium-electric-pole", id=curr_pole_name, tile_position=(head_pos, 0)
        )
        bp.entities.append(current_pole)
        if head_pos > 1:  # don't connect the first pole
            bp.add_power_connection(last_pole_name, curr_pole_name)

    return dec


def generate():
    bp = Blueprint()
    bp.label = f"AOC2023 Day 2: Data block"
    bp.description = (
        "[font=default-bold]Usage[/font]\n"
        "Connect the red wire from the [entity=decider-combinator] top port to the leftmost electric pole.\n"
        "Connect other wires as described in Timing blueprint description.\n"
        "Connect both red and green wires from leftmost electric pole to Logic section."
    )
    with open("2.in") as f:
        data = f.read().splitlines()

    head_index = (
        1  # start at 1. cycle 0 is reserved for clearing anything from last run
    )
    decider: Optional[DeciderCombinator] = None

    for line in data:
        if line.strip() == "":
            continue
        # round 1; round 2; ...; round N; set E=1, G=<game number>; set R=2.1G; next game
        game_no, game_content = re.match(r"^Game (\d+): (.*)$", line).groups()
        for round in game_content.split(";"):
            decider = add_data(bp, head_index, decider, apply_round_info, round.strip())
            head_index += 1

        decider = add_data(
            bp, head_index, decider, apply_end_of_game_info, int(game_no)
        )
        head_index += 1
        decider = add_data(bp, head_index, decider, apply_reset_info)
        head_index += 1
        print(f"\rgame {game_no} translated".ljust(75), end="", flush=True)
    print("\rall done".ljust(76))

    print("writing... ", flush=True, end="")
    with open("bp.txt", "w") as f:
        f.write(bp.to_string())
    print("done! output to bp.txt", flush=True)


if __name__ == "__main__":
    generate()
