import unittest
import os
import time

from pythontesting import s3

class S3IntegrationTest(unittest.TestCase):

	__FILE_1_PATH = '/tmp/test.txt'
	__FILE_2_PATH = '/tmp/test2.txt'

	def setUp(self):
		self._remove_file(self.__FILE_1_PATH)
		self._remove_file(self.__FILE_2_PATH)

	@staticmethod
	def _remove_file(file_path):
		try:
			os.remove(file_path)
		except OSError:
			pass

	def test_download_file(self):

		s3.download_file('pythontesting-beeva', 'test.txt', self.__FILE_1_PATH)

		self._check_file_content(self.__FILE_1_PATH, 'TEST 1 FILE CONTENT')

	def test_download_files(self):

		files = ['test.txt', 'test2.txt']
		s3.download_files('pythontesting-beeva', files, '/tmp')

		self._check_file_content(self.__FILE_1_PATH, 'TEST 1 FILE CONTENT')
		self._check_file_content(self.__FILE_2_PATH, 'TEST 2 FILE CONTENT')

	def _check_file_content(self, file_path, expected_content):
		with open(file_path) as f:
			content = f.read()
			self.assertEqual(content, expected_content)
