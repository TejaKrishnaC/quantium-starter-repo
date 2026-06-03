from app import app


def test_header(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.wait_for_element("#header", timeout=4)
    assert "Pink Morsel Visualizer" in header.text


def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    visualization = dash_duo.wait_for_element("#visualization", timeout=4)
    assert visualization


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.wait_for_element("#region_picker", timeout=4)
    assert region_picker