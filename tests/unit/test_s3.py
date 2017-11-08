import unittest

from mock import patch, call
from pythontesting import s3

class S3Test(unittest.TestCase):

	@patch('pythontesting.s3.boto3')
	@patch('pythontesting.s3.S3Transfer')
	def test_get_transfer(self, s3_transfer_mock, boto3_mock):
		transfer = s3.get_transfer()

		self.assertEqual(transfer, s3_transfer_mock.return_value)

		s3_transfer_mock.assert_called_once_with(boto3_mock.client.return_value, None)
		boto3_mock.client.assert_called_once_with('s3')

	@patch('pythontesting.s3.get_transfer')
	def test_download_file(self, get_transfer_mock):

		s3.download_file('pythontesting-beeva', 'test.txt', '/tmp/test.txt')

		transferer = get_transfer_mock.return_value
		transferer.download_file.assert_called_once_with('pythontesting-beeva', 'test.txt', '/tmp/test.txt')
		get_transfer_mock.assert_called_once_with()

	def test_download_files_empty_list(self):

		with self.assertRaises(Exception) as c:
			s3.download_files('pythontesting-beeva', [], '/tmp')

		self.assertEqual(str(c.exception), 'list cannot be empty')

	@patch('pythontesting.s3.download_file')
	def test_download_files_one_file(self, download_file_mock):

		files = ['test.txt']

		s3.download_files('pythontesting-beeva', files, '/tmp')

		download_file_mock.assert_called_once_with('pythontesting-beeva', 'test.txt', '/tmp/test.txt')

	@patch('pythontesting.s3.download_file')
	def test_download_files_two_files(self, download_file_mock):

		files = ['test.txt', 'test2.txt']

		s3.download_files('pythontesting-beeva', files, '/tmp')

		download_file_mock.assert_has_calls([call('pythontesting-beeva', 'test.txt', '/tmp/test.txt'), 
			                                 call('pythontesting-beeva', 'test2.txt', '/tmp/test2.txt')])
