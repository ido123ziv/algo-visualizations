import os
from unittest.mock import patch
from common.visualizer import visualize_algorithm_progress
import networkx as nx


@patch('common.visualizer.FuncAnimation.save')
def test_visualization(mock_save):
    # Mock graph and steps
    graph = nx.DiGraph()
    graph.add_edge(1, 2, weight=1)
    steps = [{'current_node': 1, 'updated_edges': [(1, 2)], 'annotation': "Test Step"}]
    pos = nx.spring_layout(graph)
    os.environ['CI_RUN'] = "True"
    # Call visualization
    visualize_algorithm_progress(graph, pos, steps, output_file="test.gif")

    # Assert save method was called
    mock_save.assert_called_once_with("test.gif", writer='pillow')
