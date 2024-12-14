# Algo Visualizations

This repository is made for visualizing algorithms learned in [algo](https://www-e.openu.ac.il/courses/20417.htm)
course in the open university of Israel.

This project is made in order to see the algorithms in real life and learn how they work.

All algorithms will be written in Python, all code is written and tested with Python3.

Highly recommended to check out this repository: [AllAlgorithms](https://github.com/TheAlgorithms/Python)

## Curriculum

* Graph Theory
* Greedy Algorithms
* Dynamic Programming
* Flow Networks

## Algorithms Covered in this projects

* Dijkstra [see](algorithms/dijkstra) -> an algorithm made to find the shortest path between nodes in a weighted graph 
* BFS [see](algorithms/bfs) -> a searching algorithm on a graph
* DFS [see](algorithms/dfs) -> a searching algorithm on a graph
* Bellman-Ford [see](algorithms/bellman_ford/) -> is used to find the shortest paths from a single source vertex to all other vertices in a weighted graph

## Bootstrap

It is highly recommended to use a [venv](https://docs.python.org/3/library/venv.html) for this project.

### venv installation

```shell
pip install virtualenv
# can also use to limit for a user
python -m pip install --user virtualenv
```

### venv setup
```shell
# python -m venv /path/to/venv
python -m venv .
source ./bin/activate
```

### setup requirements
```shell
pip install -r 'requirements.txt'
```

## How Do I onboard an algorithm?

1. Create a python package under `algorithms` package
2. Add the algorithm implementation in python, make sure to add a `run_algorithm` function and import it in `__init__.py` 
3. Create a basic `README.md` file
4. Follow [guide](utils/README.md) for adding a diagram
5. run `main.py` of project to add to animations path
6. add to README.md the new algorithm

## Windows

```powershell
.\venv\Scripts\activate.bat
py -m pip install -r .\requirements.txt
$env:PYTHONPATH="."
py .\utils\enrich_example.py --undirected --algorithm bellman_ford
$env:CI_RUN="true"
py -m pytest .
```
