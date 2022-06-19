# Python Data Package Example

Simple example of a package that includes data.

## Usage

You can run these python files as scripts (i.e. withouth pip installing them), or
you can us `pip install .` from the root dir to install the pacakge called `data_pkg`
in your active python environment. After doing that, you can import it from any python
file while using the environment.

For example, try running this after pip installing the package:

```python
from data_pkg import read_data
from nbformat import read

read_data.read_csv_0()
```
