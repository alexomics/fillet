"""add_device.py
"""
from fillet.core import full_binaries_path, minknow_config_path, sudoedit
import subprocess


def run(parser, args):
    mk_cfg_path = minknow_config_path("app_conf")
    cfg_editor = full_binaries_path("config_editor")

    opts = {
        True: (
            "Removing simulated device",
            ("--set_default",),
            (
                "data_generation.simulated_device",
                "device.simulator_device_count",
            ),
        ),
        False: (
            "Adding simulated device",
            ("--set",),
            (
                "data_generation.simulated_device=1",
                "device.simulator_device_count={}".format(args.num),
            ),
        ),
    }
    s, f, v = opts.get(args.remove)
    a = [(x, y) for x in f for y in v]

    with sudoedit(mk_cfg_path) as path:
        # Alternatively, we could just modify the JSON, but MK config editor
        #  has the default values, so stick to just using that.
        base_cmd = "{} --conf application --filename {}".format(
            cfg_editor,
            path,
        )

        print(s)

        for flag, value in a:
            cmd = "{} {} {}".format(base_cmd, flag, value)

            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                shell=True,
                # Aliased by `text=True` in 3.7
                universal_newlines=True,
            )
            proc.communicate()

    print("Complete")
