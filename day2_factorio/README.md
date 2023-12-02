# Day 2, Factorio edition: usage instructions
![Image of completed setup. Text plates show result for my input.](https://raw.githubusercontent.com/penguinencounter/advent-of-code-2023/main/day2_factorio/completed-setup-overview.png)
## Mods
This set of blueprints use the following mods in order to annotate and make displaying signals easier.
The components from the mods could theoretically be removed or replaced with vanilla combinators.

* **Text Plates** (annotations)
* **Pushbutton** (subst: constant combinator and decider to invert the signal after 1 tick)
* **Santa's Nixie Tube Display** (subst: just hover the electric pole to see signals)

### Recommended but not required
* **Editor Extensions** easily accessible infinite power, sandbox world highly recommended

## Setup
Install the `requirements.txt` file to get the `factorio-draftsman` library for programmatically generating blueprints.

Create a file in the current working directory named `2.in` and paste your input inside. Then run `generate.py`.
In Factorio, import the `blueprints.txt` (static) blueprint book and the `bp.txt` generated from your input.

Paste the generated blueprint first - it's very large! Travel all the way to the right end and ensure that all the combinators are powered. Then travel to the left end and paste the **Timing** blueprint below and **Logic** blueprint above.

Connect the power poles into a network and provide a suitable power source.

Follow instructions in blueprint description (you may need to right-click to open the blueprint book to view the description), adding electric poles as needed, to connect everything together.

Activate the *restart* button and wait for the numbers to settle :)

> [!WARNING]
> Do not mash the restart button. This causes inaccuracies because of
> data getting stuck in the memory cells during the reset process.
