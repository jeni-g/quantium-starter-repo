import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    return import_app("app")


def test_header(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=5)
    assert "Pink Morsel Sales Dashboard" in dash_duo.find_element("h1").text


def test_graph(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-graph", timeout=5)
    assert dash_duo.find_element("#sales-graph")


def test_radio_buttons(dash_duo, app):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=5)
    assert dash_duo.find_element("#region-filter")