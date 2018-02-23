import io
import sys
import tempfile
import unittest

import mock
import six

from flake8_expandtab import FileProcessor


class ExpandTabTestMixin(object):
    tab_width = 4

    data = (
        b'\t    foo\n'
        b'\t    \tbar\n'
    )

    expected_data = [
        tab_width * ' ' + '    foo\n',
        tab_width * ' ' + '    \tbar\n'
    ]

    def setUp(self):
        self.tab_width_patcher = mock.patch(
            "flake8_expandtab.TabExpander", tab_width=self.tab_width)
        self.tab_width_patcher.start()

    def tearDown(self):
        mock.patch.stopall()

    def test_read_lines(self):
        self.assertEqual(self.file_processor.read_lines(), self.expected_data)


class TestReadFile(ExpandTabTestMixin, unittest.TestCase):
    def setUp(self):
        super(TestReadFile, self).setUp()

        self.tmpfile = tempfile.NamedTemporaryFile()
        self.tmpfile.write(self.data)
        self.tmpfile.flush()

        self.file_processor = FileProcessor(
            self.tmpfile.name, mock.MagicMock())


class TestReadStdin(ExpandTabTestMixin, unittest.TestCase):
    def setUp(self):
        super(TestReadStdin, self).setUp()

        mock_stdin_buffer = six.BytesIO(self.data)
        mock_stdin_buffer.readable = lambda: True
        mock_stdin_buffer.writable = lambda: False
        mock_stdin_buffer.seekable = lambda: False

        if sys.version_info < (3, 0):
            mock_stdin = mock_stdin_buffer
        else:
            mock_stdin = io.TextIOWrapper(mock_stdin_buffer, 'utf-8')

        self.stdin_patcher = mock.patch("sys.stdin", mock_stdin)
        self.stdin_patcher.start()

        self.file_processor = FileProcessor('-', mock.MagicMock(stdin_display_name="-"))
