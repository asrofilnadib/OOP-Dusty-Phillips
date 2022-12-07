class AudioFile:
    def __init__(self, filename):
        self.ext = None
        if not filename.endswith(str(self.ext)):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'

    def play(self):
        print("Playing {} as mp3".format(self.filename))


class WAVFile(AudioFile):
    ext = 'wav'

    def play(self):
        print("Playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = 'ogg'

    def play(self):
        print("Playing {} as ogg".format(self.filename))


class FlecFile:
    def __init__(self, filename):
        if not filename.endswith("flac"):
            raise Exception("Invalid file format")
        self.filename = filename

    def play(self):
        print("Playing {} as flac".format(self.filename))
