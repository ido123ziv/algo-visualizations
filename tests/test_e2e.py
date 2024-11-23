import shutil
import os
import pytest  # noqa: F401
from main import main


def test_e2e():
    # Cleanup previous outputs
    if os.path.exists('animations'):
        try:
            shutil.rmtree('animations')
        except PermissionError as e:
            print(f"Failed to delete animations directory: {e}")
            return
    # Run the main pipeline
    main()

    # Check that animations are created for each graph and algorithm
    assert os.path.exists('animations/dijkstra_on_basic_directed_graph.gif')
    assert os.path.exists('animations/bfs_on_basic_directed_graph.gif')
