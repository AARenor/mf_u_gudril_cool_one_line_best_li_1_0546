"""Write the one-line make.fun entry to the requested output folder."""

import os
import sys
from pathlib import Path

TEXT = "The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been dead since Tuesday. The tag is new."

assert 1 <= len(TEXT) <= 280

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
