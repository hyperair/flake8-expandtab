import tempfile
import unittest

import mock

from flake8_expandtab import TabFilteredFile


class TabFilteredFileTestCase(unittest.TestCase):
    def setUp(self):
        self.data = (
            "\t    foo\n"
            "\t    \tbar\n"
        )

        self.tmpfile = tempfile.NamedTemporaryFile()
        self.tmpfile.write(self.data)
        self.tmpfile.flush()

        self.filtered_file = TabFilteredFile(self.tmpfile.name)

        self.tab_width_patcher = mock.patch(
            "flake8_expandtab.TabExpander", tab_width=4)
        self.tab_width_patcher.start()

    def tearDown(self):
        self.tab_width_patcher.stop()

        self.filtered_file.close()
        self.tmpfile.close()

    def test_readline(self):
        self.assertEqual(
            self.filtered_file.readline(),
            "        foo\n"
        )

        self.assertEqual(
            self.filtered_file.readline(),
            "        \tbar\n"
        )

    def test_readlines(self):
        self.assertEqual(
            self.filtered_file.readlines(),
            [
                "        foo\n",
                "        \tbar\n"
            ]
        )
