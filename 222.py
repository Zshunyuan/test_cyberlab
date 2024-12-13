import unittest
import HTMLTestRunner
import os

class TestDemo3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("类前置")

    @classmethod
    def tearDownClass(self):
        print("类后置")


    def setUp(self):
        print("方法前置")

    def tearDown(self):
        print("方法后置")
        raise ValueError("This is a manually raised ValueError.")

    def test_case_3(self):
        print("this is case3")
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        print("22222222222")
        self.assertEqual(2 * 2, 4)

#     # 获取当前目录
#     current_directory = os.path.dirname(os.path.abspath(__file__))
#     print(current_directory)
#     # 定义报告文件路径
#     report_path = os.path.join(current_directory, 'test_report.html')
#     # 打开一个文件用于写入报告
#
