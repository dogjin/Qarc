# Qarc
Qss theme based on arc-theme.

# Usage

To use this theme:

```python
from PySide import QtCore, QtGui

ui = QtGui.QMainWindow()
with open("qarc-dark.css", "r") as f:
    print(f)
    ui.setStyleSheet("".join(f.readlines()))
```

# Test

Run test sciprt:
```
python test_gui.py
```