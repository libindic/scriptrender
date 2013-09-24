#! /usr/bin/python

import unittest
from scriptrender import getInstance
import os


class TestRender(unittest.TestCase):

    def setUp(self):
        self.instance = getInstance()

    def test_wiki2pdf(self):
        self.wikipdf = self.instance.wiki2pdf("http://ml.wikipedia.org/wiki/%E0%B4%AD%E0%B4%97%E0%B4%A4%E0%B5%8D_%E0%B4%B8%E0%B4%BF%E0%B4%99%E0%B5%8D")
        self.assertTrue(os.path.isfile(self.wikipdf) and os.path.getsize(self.wikipdf) > 0)

    def test_render_text(self):
            self.render = self.instance.render_text("This is some text")
            self.assertTrue(os.path.isfile(self.render) and
                            os.path.getsize(self.render) > 0)

    def tearDown(self):
        try:
            os.remove(self.wikipdf)
        except AttributeError:
            pass

        try:
            os.remove(self.render)
        except AttributeError:
            pass


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRender)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
