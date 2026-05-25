# anony/core/dir.py - Modified ensure_dirs()
import os
import shutil

def ensure_dirs():
    # Add common paths to PATH
    for path in ["/usr/local/bin", "/usr/bin", "/bin", "/root/.deno/bin"]:
        if os.path.exists(path) and path not in os.environ.get("PATH", ""):
            os.environ["PATH"] = path + os.pathsep + os.environ.get("PATH", "")
    
    deno = shutil.which("deno")
    ffmpeg = shutil.which("ffmpeg")
    
    # Fallback: check common locations directly
    if not deno:
        for loc in ["/usr/local/bin/deno", "/usr/bin/deno", "/root/.deno/bin/deno"]:
            if os.path.exists(loc):
                os.environ["PATH"] = os.path.dirname(loc) + os.pathsep + os.environ.get("PATH", "")
                deno = loc
                break
    
    if not ffmpeg:
        for loc in ["/usr/bin/ffmpeg", "/usr/local/bin/ffmpeg"]:
            if os.path.exists(loc):
                ffmpeg = loc
                break
    
    # If still missing, try to install or provide better error
    if not deno or not ffmpeg:
        print(f"PATH: {os.environ.get('PATH', 'NOT SET')}")
        print(f"Deno found: {deno}")
        print(f"FFmpeg found: {ffmpeg}")
        raise RuntimeError("Deno and FFmpeg must be installed and accessible in the system PATH.")
