import beincrypto
import kriptocoin
import muhabbit
import cointelegraph


class CNS:
    "Crpyto NEWS SEARCHER"

    def __init__(self, word):
        self.word = word

    def founds(self):
        mixed = []
        mixed.extend(beincrypto.search(self.word))
        mixed.extend(kriptocoin.search(self.word))
        mixed.extend(muhabbit.search(self.word))
        mixed.extend(cointelegraph.search(self.word))
        return [i['link'] for i in mixed]
