"""core.py
"""
import os
import platform
import subprocess


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


class sudoedit:
    def __init__(self, path, octal_str="0664"):
        self.path = path
        self.octal_str = octal_str
        self.old_oct = str(oct(os.stat(self.path).st_mode & 0o777)).replace("o", "")

    def __enter__(self):
        self.mod_perm(self.octal_str)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mod_perm(self.old_oct)
        return True

    def mod_perm(self, perms):
        p = subprocess.Popen(['sudo', "chmod", perms, self.path])
        p.communicate()
