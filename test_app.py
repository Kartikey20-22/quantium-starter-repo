import pytest
from dash.testing.application_runners import import_app

# Import the app
app = import_app('app')


def test_header_present(dash_duo):
    """Test that the header is present."""
    dash_duo.start_server(app)

    # Check for header text
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualizer"




def test_visualization_present(dash_duo):
    """Test that the line chart visualization is present."""
    dash_duo.start_server(app)

    # Check for the graph component
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None




def test_region_picker_present(dash_duo):
    """Test that the region picker radio buttons are present."""
    dash_duo.start_server(app)

    # Check for radio items component
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None

    # Check that all 5 options are present
    options = dash_duo.find_elements('input[type="radio"]')
    assert len(options) == 5

