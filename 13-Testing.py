import unittest  # it is used for testing

import main_for_testing  # import our main file

class TestMain(unittest.TestCase):  # make a class for testing

    def setUp(self):  # with setup, before every test function we run it one time
        print('about to test the function')


    def test_do_stuff(self):
        test_param = 10
        result = main_for_testing.do_stuff(test_param)  # run the function in other python file with a parameter
        self.assertEqual(result,15)  # check if the result is equal with what we thought

    def tearDown(self):  # it will be called at the end of each method to clean up or reset some variables
        print('cleanup')
unittest.main()  # it means call all the tests here and doesnt call the file name
