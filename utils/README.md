# Utils

This folder is made to help automate stuff regarding algorithms

for instance, we keep here basic examples for both directed and undirected graphs

Structure:
```text
.
├── README.md
├── directed_graph.csv
└── enrich_example.py

```

the `enrich_example.py` is made to add examples for any new algorithm

## How To use

first of all you must set the python path env var temporarily:
```shell
export PYTHONPATH=.
```

```Powershell
$env:PYTHONPATH="."
```

```CMD
set PYTHONPATH=.
```

Then run **from repo root**
```shell
# -a or --algorithm is the name of algorithm
# --directed is whether to use a directed graph
# --undirected is whether to use a undirected graph
python utils/enrich_example.py --algorithm bfs --directed
```

