import paper
import pencil

def play_text():
    marker = pencil.Pencil(pencil_durability=20, length=3, eraser_durability=20)
    display_text = paper.Paper()

    marker.write("Hello ")
    print(display_text.display())
    marker.write("world ")
    print(display_text.display())
    marker.write("I am Naama Rivlin")
    print(display_text.display())
    marker.sharpen()
    marker.erase("N", "Eshed")
    print(display_text.display())
    marker.erase("world", "universe")
    print(display_text.display())
    marker.erase("univer@eam")
    print((display_text.display()))
if __name__ == '__main__':
    play_text()

