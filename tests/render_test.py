#! /usr/bin/python

import unittest
from scriptrender import getInstance
import os
import sys


class TestRender(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_wiki2pdf(self):
        self.wikipdf = self.instance.wiki2pdf("http://ml.wikipedia.org/wiki/%E0%B4%AD%E0%B4%97%E0%B4%A4%E0%B5%8D_%E0%B4%B8%E0%B4%BF%E0%B4%99%E0%B5%8D")
        self.test_pdf = os.path.join(sys.path[0], "static", "output",
                                 self.wikipdf)
        self.assertTrue(os.path.isfile(self.test_pdf) and os.path.getsize(self.test_pdf) > 0)

    def test_render_text(self):
            self.render = self.instance.render_text("This is some text")
            self.test_png = os.path.join(sys.path[0], "static", "output",
                                         self.render)
            self.assertTrue(os.path.isfile(self.test_png) and
                            os.path.getsize(self.test_png) > 0)

    def tearDown(self):
        try:
            os.remove(self.test_pdf)
        except AttributeError:
            pass

        try:
            os.remove(self.test_png)
        except AttributeError:
            pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRender)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
