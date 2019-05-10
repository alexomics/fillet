"""core.py
"""
import platform
import os


OS = platform.system()


def _minknow_path():
    return {
        "Darwin": os.path.join(os.sep, "Applications", "MinKNOW.app", "Contents", "Resources"),
        "Linux": os.path.join(os.sep, "opt", "ONT", "MinKNOW"),
        "Windows": os.path.join(os.sep, "Program Files", "OxfordNanopore", "MinKNOW"),
    }.get(OS, None)


def _python_path():
    return {
        "Darwin": os.path.join("ont-python", "bin", "python"),
        "Linux": os.path.join("ont-python", "bin", "python"),
        "Windows": os.path.join("ont-python", "python.exe"),
    }.get(OS, None)


def ont_python_path():
    return os.path.join(_minknow_path(), _python_path())


def bream_path():
    bream = os.path.join(
        "ont-python", "lib", "python2.7", "site-packages", "bream4", "configuration"
    )
    return os.path.join(_minknow_path(), bream)


def binaries_path():
    return os.path.join(_minknow_path(), "bin")


def full_config_path(filename):
    return os.path.join(bream_path(), filename)


def full_binaries_path(filename):
    return os.path.join(binaries_path(), filename)


def minknow_config_path(filename):
    return os.path.join(_minknow_path(), "conf", filename)
