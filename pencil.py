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

    def erase(self, text):
        text_position = 0
        temporary_display = paper.display_text[::-1]
        substring_index = temporary_display.index(text[::-1])
        temporary_display = list(temporary_display)
        while self.eraser_durability > 0 and text_position < len(text):
            temporary_display[substring_index] = " "
            self.eraser_durability -= 1
            substring_index += 1
            text_position += 1
        paper.display_text = "".join(temporary_display[::-1])
        return paper.display_text
