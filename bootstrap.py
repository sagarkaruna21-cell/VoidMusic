import sys
import types
import os
import pathlib

print("=" * 50)
print("BOOTSTRAP: Patching anony environment")
print("=" * 50)

for path in ["/usr/local/bin", "/usr/bin", "/bin", "/root/.deno/bin"]:
    if os.path.exists(path) and path not in os.environ.get("PATH", ""):
        os.environ["PATH"] = path + os.pathsep + os.environ.get("PATH", "")

print(f"PATH: {os.environ.get('PATH')}")

fake_dir = types.ModuleType("anony.core.dir")
fake_dir.__file__ = "/workspace/anony/core/dir.py"

def ensure_dirs():
    for d in ["/tmp/anony", "/workspace/data", "/workspace/cache"]:
        pathlib.Path(d).mkdir(parents=True, exist_ok=True)
    print("[bootstrap] ensure_dirs() patched - directories created")

fake_dir.ensure_dirs = ensure_dirs

sys.modules["anony.core.dir"] = fake_dir
sys.modules["anony.core"] = types.ModuleType("anony.core")
sys.modules["anony.core"].dir = fake_dir

print("[bootstrap] Monkey patch applied, importing anony...")

import anony

print("[bootstrap] an
