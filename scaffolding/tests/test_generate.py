from unittest.mock import patch, mock_open

from scaffolding.generate_routes import generate_file


@patch('os.path.join')
def test_generate_file_valid_inputs(mock_join):
    # Arrange
    routes_name = "test_routes"
    template_file = "routes.py"
    destination_folder = "../farms_api/routes"
    _type = 'route'
    expected_content = "content with test_routes"
    base_path = 'mocked/path/to/file.txt'
    mock_join.return_value = base_path

    # Act
    with patch('os.path.exists', return_value=(True)) as mocked_exists:
        with patch("builtins.open", mock_open(read_data=expected_content)) as mocked_file:
            generate_file(routes_name, template_file, destination_folder, _type)
            mocked_file.assert_called()

    # Assert
    mock_join.assert_called()
