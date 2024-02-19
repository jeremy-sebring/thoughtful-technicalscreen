import argparse
import json
from tqdm import tqdm

def SortPackage(width, height, length, mass):
    volume = width * height * length
    bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

#
parser = argparse.ArgumentParser(description="Dispatching packages based on dimensions and mass.")
parser.add_argument("--package", nargs=4, metavar=("WIDTH", "HEIGHT", "LENGTH", "MASS"),
                    help="Specify a single package with width, height, length (in cm), and mass (in kg).")
parser.add_argument("--json", type=str, 
                    help="Path to a JSON file containing a list of packages with their dimensions and mass.")
args = parser.parse_args()

# Process single package
if args.package:
    width, height, length, mass = map(float, args.package)
    classification = SortPackage(width, height, length, mass)
    print(f"Package dispatched as: {classification}")

# Process JSON file
elif args.json:
    reqKeys = ['width', 'height', 'length', 'mass']
    with open(args.json) as file:
        packages = json.load(file)
        for package in tqdm(packages, desc="Dispatching packages"):
            if not all(key in package.keys() for key in reqKeys):
                raise ValueError(f"Missing required keys: {reqKeys}")

            width = package['width']
            height = package['height']
            length = package['length']
            mass = package['mass']
            classification = SortPackage(width, height, length, mass)
            print(f"Package dispatched as: {classification}")

else:
    print("Please provide a single package or a JSON file of packages.")
