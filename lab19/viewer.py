class Viewer:
    def __init__(self):
        self.max_length = (0, None)
        self.word_count = 0

    def main_logic(self, line):
        self.word_count += len(line.split())
        line_len = len(line)
        if line_len > self.max_length[0]:
            self.max_length = line_len, line


class Publisher:
    def __init__(self,  listener):
        self.file_obj = None
        self.listener = listener

    def set_file_obj(self, file_obj):
        self.file_obj = file_obj

    def notify(self, line: str):
        self.listener.main_logic(line)

    def update(self):
        assert self.file_obj is not None
        for line in self.file_obj:
            self.notify(line)


viewer = Viewer()
publisher = Publisher(viewer)

with open("input.txt", "r") as f:
    publisher.set_file_obj(f)
    publisher.update()

print("Result:")
print("Max length: {} for {}".format(viewer.max_length[0], viewer.max_length[1]))
print("Count of words: {}".format(viewer.word_count))
