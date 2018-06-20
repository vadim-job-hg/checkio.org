class Network:
    def __init__(self, network=()):
        self.con = {}  # conections array
        for con in network:
            r1, r2 = con.split('-')
            self.con.setdefault(r1, []).append(r2)
            self.con.setdefault(r2, []).append(r1)

    def check(self, first, second):
        self.checked = set()  # this need to check every connection only single time
        return self.connected(first, second)

    def connected(self, first, second):
        if (first in self.checked):  # if we already check this
            return False
        self.checked.add(first)  # save that this no need to be checked again
        if (second in self.con[first]):  # check if needed conection in list
            return True
        return any([self.connected(x, second) for x in self.con[first]])  # go on to search recursively


def check_connection(network, first, second):
    network = Network(network)
    return network.check(first, second)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."