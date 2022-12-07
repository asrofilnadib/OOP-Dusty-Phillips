import datetime

# store the next available id for all new notes
last_id = 0


class Note:
    """merepresentasikan note didalam sebuah notebook
    dimana match() dalam search string dan diberikan tags
    pada setiap note"""

    def __init__(self, memo, tags=''):
        # inisialisasi note dengan memo dan opsional tags yang terpisah
        # secara otomatis mengatur tanggalan dan id yang unik
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """menyesuaikan dengan note yang terfilterisasi, True jika benar,
        False jika salah"""
        return filter in self.memo or filter in self.tags


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
