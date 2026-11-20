"""make.fun entry for news-image-20261120.

Writes the entry image (entry.png, beside this file) to the output directory:
$MAKEFUN_OUTPUT_DIR when set, else /output. Python 3.13, standard library only.
The image sums up the world news of Friday 20 November 2026; see README.md.
"""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().with_name("entry.png")
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
