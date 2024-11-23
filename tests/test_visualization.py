import os
from unittest.mock import patch
from common.visualizer import visualize_algorithm_progress
import networkx as nx


@patch('common.visualizer.FuncAnimation.save')
@patch('common.visualizer.patch_file_permissions')  # Mock patch_file_permissions
@patch('os.path.exists', return_value=True)  # Mock os.path.exists to avoid file system checks
def test_visualization(mock_exists,  mock_patch_permissions, mock_save):
    # Mock graph and steps
    graph = nx.DiGraph()
    graph.add_edge(1, 2, weight=1)
    steps = [{'current_node': 1, 'updated_edges': [(1, 2)], 'annotation': "Test Step"}]
    pos = nx.spring_layout(graph)
    os.environ['CI_RUN'] = "True"
    # Call visualization
    visualize_algorithm_progress(graph, pos, steps,
                                 title=f"MOCK Algorithm Animation",
                                 output_file="test.gif")

    # Assert FuncAnimation.save was called correctly
    mock_save.assert_called_once_with("test.gif", writer='pillow')

    # Assert patch_file_permissions was called with the correct argument
    mock_patch_permissions.assert_called_once_with("test.gif")

    # Assert that the file existence check was called
    mock_exists.assert_called_once_with("test.gif")
