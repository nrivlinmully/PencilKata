import paper


class Pencil:

    def __init__(self, pencil_durability=0, length=0, eraser_durability=0):
        self.initial_durability = pencil_durability
        self.pencil_durability = pencil_durability
        self.eraser_durability = eraser_durability
        self.length = length

    def write(self, text):
        for letter in text:
            if self.pencil_durability > 0:
                self.point_degradation(letter)
                paper.display_text += letter
            else:
                paper.display_text += " "
        return text

    def point_degradation(self, letter):
        if letter.isupper():
            self.pencil_durability -= 2
        else:
            self.pencil_durability -= 1

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
            self.pencil_durability = self.initial_durability

    def erase(self, text_to_erase, text_to_replace=None):
        text_position = 0
        temporary_display = paper.display_text[::-1]
        substring_index = temporary_display.index(text_to_erase[::-1])
        temporary_display = list(temporary_display)
        while self.eraser_durability > 0 and text_position < len(text_to_erase):
            temporary_display[substring_index] = " "
            self.eraser_durability -= 1
            substring_index += 1
            text_position += 1
        if text_to_replace is not None:
            self.edit(substring_index, temporary_display, text_to_replace)
        paper.display_text = "".join(temporary_display[::-1])
        return paper.display_text

    def edit(self, substring_index, temporary_display, text_to_replace):
        for letter in text_to_replace:
            if str(temporary_display[substring_index - 1]).isalpha():
                temporary_display[substring_index - 1] = "@"
            else:
                temporary_display[substring_index - 1] = letter
            substring_index -= 1
