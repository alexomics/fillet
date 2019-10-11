"""simulation.py
"""
from pathlib import Path
import toml
from fillet.core import full_config_path, sudoedit


def run(parser, args):
    args.toml = full_config_path(args.toml)
    print(args.toml)

    with sudoedit(args.toml) as path:
        d = toml.load(path)

        if args.bulkfile is not None:
            args.bulkfile = str(Path(args.bulkfile).expanduser())
            print("Adding simulation file")
            d["custom_settings"]["simulation"] = args.bulkfile
        else:
            print("Removing simulation parameter")
            d["custom_settings"].pop("simulation", None)

        with open(path, "w") as fh:
            toml.dump(d, fh)

    print("File edited.")
