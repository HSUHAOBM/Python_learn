# pip install mypy

from typing import *

_shared_state: List[str]
_shared_state = ['1']

# mypy mypy.py
# Success: no issues found in 1 source file

_shared_state: List[str]
_shared_state = [1]

# mypy mypy.py
# Found 2 errors in 1 file (checked 1 source file)