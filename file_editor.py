class FileEditor:
    def __init__(self, path):
        self.path = path
    def rewrite(self, aeroflots):
        s = ''
        for el in aeroflots:
            s += str(el) + '\n'
        with open(self.path, 'w') as f:
            f.writelines(s)
    def append_row(self, s):
        with open(self.path, 'a') as f:
            f.write(s + '\n')
    def append_collection(self, collection):
        s = '\n' + str(collection) + '\n'
        with open(self.path, 'a') as f:
            f.write(s)
    def make_change(self, aeroflots):
        s = input("to rewrite file push '+':\n")
        if s == '+':
            self.rewrite(aeroflots)
