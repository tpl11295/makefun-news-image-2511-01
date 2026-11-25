"""One-day news image entry (Python 3.13, standard library only).

Copies the prepared image to /output/entry.png. The image sums up
Wednesday 25 November 2026 in three panels: the Strait of Hormuz
tanker attacks, the Asian market plunge, and the Huawei verdict in a
U.S. court, under a banner naming the day. It is a JPEG stored as
entry.png, which the rules allow (the file is told apart by its
first bytes). The copy is deterministic: the same bytes every run,
with no network.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
src = os.path.join(HERE, "entry.png")
dst = os.path.join(OUT, "entry.png")
shutil.copyfile(src, dst)
# Confirm the copy is whole: same byte count as the image in the repo,
# so a truncated write can never pass silently.
assert os.path.getsize(dst) == os.path.getsize(src)
print("wrote", dst, os.path.getsize(dst), "bytes")
