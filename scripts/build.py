#!/usr/bin/env python3
"""Builds ros2_ws with colcon (pixi run build). Extra arguments go to colcon.

Windows: so101_interfaces is a C++ package, it needs the MSVC compiler
(Visual Studio Build Tools, "Desktop development with C++" workload).
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

WS = Path(__file__).resolve().parent.parent / "ros2_ws"
VC_TOOLS = "Microsoft.VisualStudio.Component.VC.Tools.x86.x64"


def msvc_env() -> dict:
    """The environment vcvars64.bat leaves behind, so CMake finds cl.exe."""
    if shutil.which("cl"):
        return dict(os.environ)  # already set up (pixi activation or a developer prompt)
    vswhere = Path(os.environ.get("ProgramFiles(x86)", "")) / "Microsoft Visual Studio/Installer/vswhere.exe"
    found = []
    if vswhere.is_file():
        found = subprocess.run(
            [str(vswhere), "-latest", "-products", "*", "-requires", VC_TOOLS,
             "-property", "installationPath", "-format", "value"],
            capture_output=True, text=True, check=False,
        ).stdout.strip().splitlines()
    vcvars = Path(found[0]) / "VC/Auxiliary/Build/vcvars64.bat" if found else None
    if vcvars is None or not vcvars.is_file():
        sys.exit(
            "MSVC compiler not found. Install it once, then open a new terminal:\n"
            "  winget install Microsoft.VisualStudio.2022.BuildTools --override "
            '"--quiet --wait --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"'
        )
    # vcvars stays its own argument: cmd cannot find it once its spaces are re-quoted.
    out = subprocess.run(["cmd", "/c", str(vcvars), "&&", "set"],
                         capture_output=True, text=True, check=True).stdout
    return {**os.environ, **dict(line.split("=", 1) for line in out.splitlines() if "=" in line)}


if os.name == "nt":
    # Symlinks need admin rights on Windows: Python edits need a rebuild (launch does it).
    args, env = ["--merge-install"], msvc_env()
else:
    args, env = ["--symlink-install"], None
# python -m colcon: the colcon.exe shim breaks when the Python path holds a space.
cmd = [sys.executable, "-m", "colcon", "build", *args, "--cmake-args", "-GNinja", "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev", *sys.argv[1:]]
sys.exit(subprocess.call(cmd, cwd=WS, env=env))
