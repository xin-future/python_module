# coding=utf-8
import unittest
import HTMLTestRunner
from BeautifulReport import BeautifulReport

class GetUserTest(unittest.TestCase):

    def tearDown(self):
        print('tear down...')

    def setUp(self):
        print('tear...up')

    def test_get_user(self):
        self.assertEquals(10, 10)

    def test_get_user2(self):
        self.assertIn(10, [10, 9])

if __name__ == '__main__':
    my_test_suite = unittest.TestSuite()
    my_test_suite.addTest(GetUserTest('test_get_user'))
    my_test_suite.addTest(GetUserTest('test_get_user2'))
    # fp = open('my_report_01.html', 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title='unite test',
    #     description='This demonstrates the report output by HTMLTestRunner.'
    # )
    # runner.run(my_test_suite)

    result = BeautifulReport(my_test_suite)
    result.report(filename='测试报告', description='测试deafult报告', report_dir='report', theme='theme_default')
