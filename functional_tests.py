#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common import alert
import  unittest2

class NewVisitorTest(unittest2.TestCase):
    def setUp(self):
        self.brower = webdriver.Chrome()

    def tearDown(self):
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.brower.get("http://localhost:8000")
        self.assertIn("To-Do" , self.brower.title)
        self.fail("finish  the  test")



if __name__ == '__main__':
    unittest2.main()