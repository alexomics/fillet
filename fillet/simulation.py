"""simulation.py
"""
from pathlib import Path
import toml
from fillet.core import full_config_path


def run(parser, args):
    args.toml = full_config_path(args.toml)
    print(args.toml)

    d = toml.load(args.toml)

    if args.bulkfile is not None:
        args.bulkfile = str(Path(args.bulkfile).expanduser())
        print("Adding simulation file")
        d["custom_settings"]["simulation"] = args.bulkfile
    else:
        print("Removing simulation parameter")
        d["custom_settings"].pop("simulation", None)

    with open(args.toml, "w") as fh:
        toml.dump(d, fh)

    print("File edited.")
