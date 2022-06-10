import paper
import pencil
import unittest

class PaperTest(unittest.TestCase):
    paper_text = paper.Paper()
    text = pencil.Pencil(100)

    def tearDown(self):
        paper.display_text = ""
        pencil.Pencil().pencil_durability = 100

    def test_paper_displays_text_from_pencil(self):
        self.text.write("Hello")

        self.assertEqual("Hello", self.paper_text.display())

    def test_pencil_adds_to_existing_paper_text(self):
        self.text.write("Hello ")
        self.text.write("world")

        self.assertEqual("Hello world", self.paper_text.display())
