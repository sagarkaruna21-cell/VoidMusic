import shutil
import os

def ensure_dirs():
    # Add fallback paths
    for path in ["/usr/local/bin", "/usr/bin", "/bin"]:
        if path not in os.environ["PATH"]:
            os.environ["PATH"] = path + os.pathsep + os.environ["PATH"]
    
    deno = shutil.which("deno")
    ffmpeg = shutil.which("ffmpeg")
    
    if not deno:
        # Check fallback locations
        for loc in ["/usr/local/bin/deno", "/root/.deno/bin/deno"]:
            if os.path.exists(loc):
                os.environ["PATH"] = os.path.dirname(loc) + os.pathsep + os.environ["PATH"]
                deno = loc
                break
    
    if not deno or not ffmpeg:
        raise RuntimeError("Deno and FFmpeg must be installed and accessible in the system PATH.")
