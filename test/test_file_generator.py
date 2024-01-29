# tests/test_generate_file.py
from file_generator import FileGenerator
from unittest.mock import mock_open, patch

def test_create_folder(tmpdir):
    generator = FileGenerator(tmpdir)
    folder_path = tmpdir.join("devices")
    
    generator.create_folder()

    assert folder_path.check(dir=True)

