#!/usr/bin/env python3
"""Entry program: copy the bundled image to the output path.

Standard library only, no network. Reads asset.png next to this file and
writes it to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png).
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "asset.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    size = os.path.getsize(dst)
    print(f"Wrote {dst} ({size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
