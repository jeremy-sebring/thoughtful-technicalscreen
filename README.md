# Jeremy Sebring's submission for the Thoughtful Automation Technical Screen

## Rules:

Here are the rules:

>Sort the packages using the following criteria:
>
>- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
>- A package is **heavy** when its mass is greater or equal to 20 kg.
>
>You must dispatch the packages in the following stacks:
>
>- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
>- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
>- **REJECTED**: packages that are **both** heavy and bulky are rejected.

## Command intro

Here is the command help:

```bash
usage: main.py [-h] [--package WIDTH HEIGHT LENGTH MASS] [--json JSON]

Dispatching packages based on dimensions and mass.

options:
  -h, --help            show this help message and exit
  --package WIDTH HEIGHT LENGTH MASS
                        Specify a single package with width, height, length (in cm), and mass (in kg).
  --json JSON           Path to a JSON file containing a list of packages with their dimensions and mass.

```

## Usage

Sample JSON input: `python main.py --json sample_packages.json`

Sample output:

```bash
Dispatching packages:   0%|                                                                                            | 0/3 [00:00<?, ?it/s]
Package dispatched as: STANDARD
Package dispatched as: SPECIAL
Package dispatched as: REJECTED
Dispatching packages: 100%|████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 12826.62it/s]
```

Sample single input: `python main.py --package 10 10 10 10`

Sample output:

```bash
Package dispatched as: STANDARD
```
