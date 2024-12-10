import os
import unittest
from muthur.llm.prompt import files_to_markdown, files_to_markdown_file, Result
from glob import glob


class TestFilesToMarkdown(unittest.TestCase):
    def setUp(self):
        self.src_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "src")
        )
        self.test_files = self._get_files()
        self.markdown_file = "test.md"

    def tearDown(self):
        if os.path.exists(self.markdown_file):
            os.remove(self.markdown_file)

    def _get_files(self):
        files = glob(os.path.join(self.src_dir, "**", "*.py"), recursive=True)
        return [f for f in files if not f.endswith("__init__.py")]

    def test_files_to_markdown(self):
        result = files_to_markdown(self.test_files)
        self.assertIsNone(result.error)
        self.assertTrue(result.is_ok())

        self.assertGreater(len(result.data), 0)

    def test_files_to_markdown_file(self):
        result = files_to_markdown_file(
            self.test_files, self.markdown_file, self.src_dir
        )
        self.assertIsNone(result.error)
        self.assertTrue(result.is_ok())

        with open(self.markdown_file, "r") as f:
            content = f.read()

        # expected_content = "\n```a/file1.txt\n\n```"
        # self.assertEqual(content, expected_content)


if __name__ == "__main__":
    unittest.main()
