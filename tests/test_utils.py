import os
from unittest import mock

from src.utils import create_objects_from_json, read_json_data


@mock.patch(
    "builtins.open",
    new_callable=mock.mock_open,
    read_data='[{"name": "А", "description": "Б", "products": []}]',
)
def test_read_json_data(mock_open) -> None:
    result = read_json_data("/path/to/products.json")
    expected_result = [{"name": "А", "description": "Б", "products": []}]
    assert result == expected_result
    mock_open.assert_called_once_with(
        os.path.abspath("/path/to/products.json"), "r", encoding="UTF-8"
    )


def test_create_objects_from_json(json_data_products) -> None:
    result = create_objects_from_json(json_data_products)
    assert result[0].name == "Смартфоны"
    assert (
        result[0].description
        == "Смартфоны, как средство не только коммуникации, но и удобства жизни"
    )
