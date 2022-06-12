import unittest
import pencil
import paper

class PencilTest(unittest.TestCase):

    def tearDown(self):
        paper.display_text = ""

    def test_write_returns_input_text(self):
        text = pencil.Pencil(10)
        self.assertEqual('Hello', text.write('Hello'))

    def test_pencil_durability_is_setup_on_instantiation(self):
        point = pencil.Pencil(10)
        self.assertEqual(10, point.pencil_durability)

    def test_durability_decreases_by_one_when_writing_lowercase_letters(self):
        point = pencil.Pencil(10)
        point.write("x")
        self.assertEqual(9, point.pencil_durability)

    def test_durability_decreases_by_two_when_writing_uppercase_letters(self):
        point = pencil.Pencil(10)
        point.write("X")

        self.assertEqual(8, point.pencil_durability)

    def test_pencil_outputs_space_when_writing_on_durability_zero(self):
        point = pencil.Pencil(4)
        display_text = paper.Paper()

        point.write("Test")

        self.assertEqual("Tes ", display_text.display())

    def test_sharpening_pencil_returns_full_durability(self):
        point = pencil.Pencil(pencil_durability=4, length=1)

        point.write("test")

        point.sharpen()

        self.assertEqual(4, point.pencil_durability)

    def test_sharpening_pencil_reduces_length(self):
        point = pencil.Pencil(length=2)

        point.sharpen()

        self.assertEqual(1, point.length)

    def test_sharpening_pencil_doesnt_restore_durability_when_length_is_zero(self):
        point = pencil.Pencil(pencil_durability=2, length=0)

        point.write("hi")

        point.sharpen()

        self.assertEqual(0, point.pencil_durability)

    def test_erase_letter_deletes_last_occurance_of_input_text(self):
        eraser = pencil.Pencil(eraser_durability=100)
        paper.display_text = "abab"

        self.assertEqual("ab b", eraser.erase("a"))

    def test_erase_word_deletes_last_occurance_of_input_text_twice(self):
        eraser = pencil.Pencil(eraser_durability=100)
        paper.display_text = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

        self.assertEqual("How much wood would a woodchuck chuck if a woodchuck could       wood?", eraser.erase("chuck"))
        self.assertEqual("How much wood would a woodchuck chuck if a wood      could       wood?", eraser.erase("chuck"))

    def test_eraser_durability_decreases_when_erasing_letters(self):
        eraser = pencil.Pencil(eraser_durability=4)
        paper.display_text = "abab"

        eraser.erase("ab")

        self.assertEqual(2, eraser.eraser_durability)

    def test_eraser_doesnt_erase_past_its_durability(self):
        eraser = pencil.Pencil(eraser_durability=3)
        paper.display_text = "Test"

        eraser.erase("Test")

        self.assertEqual("T   ", paper.display_text)

    def test_edit_inserts_text_where_deleted_word_was(self):
        editor = pencil.Pencil(pencil_durability=20, eraser_durability=10)
        paper.display_text = "I am drinking coffee"

        editor.erase("am", "hi")

        self.assertEqual("I hi drinking coffee", paper.display_text)

    def test_edit_inserts_text_where_deleted_word_was_when_replacement_text_is_shorter(self):
        editor = pencil.Pencil(pencil_durability=20, eraser_durability=10)
        paper.display_text = "I am drinking coffee"

        editor.erase("drinking", "hi")

        self.assertEqual("I am hi       coffee", paper.display_text)

    def test_edit_inserts_at_symbol_when_replacement_text_is_longer_than_deleted_text(self):
        editor = pencil.Pencil(pencil_durability=50, eraser_durability=50)
        paper.display_text = "An apple a day keeps the doctor away"

        editor.erase("apple", "artichoke")

        self.assertEqual("An artich@k@ay keeps the doctor away", paper.display_text)