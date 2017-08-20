# Space Filling Curves

A Python implementation of popular [space filling curves](https://en.wikipedia.org/wiki/Space-filling_curve). Run [demo notebook](/demo.ipynb) for a demonstration.

Usage example:

```python
from curves import Hilbert_Curve

square_size = 16
start_coor = (0,0)

Hilbert_Curve = Line_Curve(square_size, start_coor)
for coor in Hilbert_Curve: 
  print coor
```

## Available Curves

<img src="/demo_curves/line.gif" alt="Line Curve" width="150" height="100"/> <img src="/demo_curves/hilbert.gif" alt="Hilbert Curve" width="150" height="100" /> 
