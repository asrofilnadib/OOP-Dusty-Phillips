import sys
from notebook import Note, Notebook


class Menu(object):
    def __init__(self):
        self.notebook = Notebook()
        self.choice = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        print("""
        Notebook menu
        
        1. Show all notes
        2. Search note
        3. Add note
        4. Modify note
        5. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choice.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
            for note in notes:
                print("{0}: {1} {2}".format(note.id, note.tags, note.memo))
            else:
                print("notes is empty")

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter new memo: ")
        self.notebook.new_note(memo)
        print("Your memo was been added")

    def modify_note(self):
        id = input("Enter id: ")
        memo = input("Enter memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thanks for using notebook today")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
