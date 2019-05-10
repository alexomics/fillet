"""add_device.py
"""
from fillet.core import full_binaries_path, minknow_config_path
import subprocess


def run(parser, args):
    p = full_binaries_path("config_editor")
    base_cmd = "{} --conf application --filename {} --set".format(
        p, minknow_config_path("app_conf")
    )
    if args.remove:
        """
        config_editor --conf application --filename ../conf/app_conf --set_default data_generation.simulated_device
        config_editor --conf application --filename ../conf/app_conf --set_default device.simulator_device_count
        """
        cmd = "{}{} && {}{}".format(
            base_cmd,
            "_default data_generation.simulated_device",
            base_cmd,
            "_default device.simulator_device_count",
        )
        print("Remove simulated device")
    else:
        """
        config_editor --conf application --filename ../conf/app_conf --set data_generation.simulated_device=1
        config_editor --conf application --filename ../conf/app_conf --set device.simulator_device_count=1
        """
        print("Add simulated device")
        cmd = "{}{} && {}{}".format(
            base_cmd,
            " data_generation.simulated_device=1",
            base_cmd,
            " device.simulator_device_count=1",
        )

    # print(cmd)

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True,
        # Aliased by `text=True` in 3.7
        universal_newlines=True,
    )
    out, err = proc.communicate()

    if out:
        print(out, "#" * 30)
    if err:
        print(err, "#" * 30)

    print("Complete")
