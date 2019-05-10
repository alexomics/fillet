"""main.py
"""
import traceback
from pathlib import Path
from argparse import ArgumentParser, HelpFormatter, SUPPRESS
from fillet.version import __version__
from fillet.core import bream_path


class NoneDefaultsHelpFormatter(HelpFormatter):
    """Help message formatter that adds default values to argument help string unless SUPPRESS or None"""

    def _get_help_string(self, action):
        help_str = action.help
        if action.default is not SUPPRESS and action.default is not None:
            help_str += " (default: " + str(action.default) + ")"
        return help_str


def run_command(parser, args):
    """..."""
    if args.command == "sim":
        import fillet.simulation as submodule
    elif args.command == "add":
        import fillet.add_device as submodule

    # run the chosen submodule.
    submodule.run(parser, args)


def main():
    """Execute the bulkvis command and pass args to sub-commands

    Returns
    -------
    None

    The available sub-commands:
    * sim    fillet.simulation
    * add    fillet.add_device
    """
    # TODO: Move arguments to each sub-command and build here (see serve)
    parser = ArgumentParser(
        prog="fillet",
        epilog="See '<command> --help' to read about a specific sub-command.",
    )
    parser.add_argument(
        "-v", "--version", action="version", version="fillet {}".format(__version__)
    )
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    """Create individual sub-commands"""

    """simulation"""
    sim_parser = subparsers.add_parser(
        "sim", help="Add or remove simulation parameters to an ONT config file"
    )
    sim_input = sim_parser.add_argument_group(title="Input sources")
    sim_input.add_argument(
        "-b",
        "--bulkfile",
        help="The bulk FAST file to use for the simulation, if not "
        "provided the simulation parameter will be removed from "
        "the toml file.",
        default=None,
    )
    toml_files = [
        f.name
        for f in Path(bream_path()).iterdir()
        if ".toml" in f.suffixes and "sequencing" in f.name
    ]
    sim_input.add_argument(
        "-t",
        help="The configuration file to add a simulation parameter to.",
        default=None,
        choices=toml_files,
        required=True,
        dest="toml",
    )
    sim_parser.set_defaults(func=run_command)

    """Add device"""
    add_parser = subparsers.add_parser("add", help="Add a simulation MinION to MinKNOW")
    add_parser.add_argument(
        "-r", help="Remove a simulated device.", action="store_true", dest="remove"
    )
    add_parser.set_defaults(func=run_command)

    """Parse arguments"""
    args = parser.parse_args()
    if args.command is not None:
        try:
            args.func(parser, args)
        except KeyboardInterrupt:
            print("Caught KeyboardInterrupt")
        except Exception as e:
            traceback.print_exc()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
