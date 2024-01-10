import os
import unittest
from unittest.mock import patch
from highlenium import get_chromedriver

class TestGetChromeDriver(unittest.TestCase):
    @patch('os.path.isfile')
    @patch('highlenium.get')
    def test_get_chromedriver(self, mock_get, mock_isfile):
        mock_isfile.return_value = False
        mock_get.return_value.content = b"chromedriver content"
        result = get_chromedriver()
        self.assertEqual(result, os.path.abspath('chromedriver'))
        if os.name == "posix":
            mock_get.assert_called_once_with('https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_linux64.zip')
        elif os.name == "nt":
            mock_get.assert_called_once_with('https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_win32.zip')

if __name__ == '__main__':
    unittest.main()