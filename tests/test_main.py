from jmenu.main import get_version, main
from importlib.metadata import version
from unittest.mock import patch
from conftest import mock_fetch_restaurant
import pytest


def test_version_system():
    assert get_version() == version("jmenu")


@patch("jmenu.api.requests.get", side_effect=mock_fetch_restaurant)
def test_main(self, capsys):
    with pytest.raises(SystemExit):
        main()

    out, _ = capsys.readouterr()
    assert "Creme" in out
    assert "lololol" not in out
