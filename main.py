from heapq import nlargest
import string

ks = []
full = {}
dl = ['а', 'в', 'на', 'В', 'На', 'A', 'и', 'И', 'из', 'Из', 'под', 'Под', 'по', 'По', 'С']


class Logic:
    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                if k in ks:
                    continue
                else:
                    ks.append(k)
                    return k

    def count(self, sps):
        for fs in sps:
            if fs.lower() == fs and (fs.capitalize() not in full.keys()):
                ful = sps.count(fs)
                full[fs] = ful
            elif fs.lower() != fs and fs.lower() not in full.keys():
                numm = sps.count(fs)
                num = sps.count(fs.lower())
                ful = numm + num
                full[fs] = ful
            elif fs.lower() != fs and fs.lower() in full.keys():
                ful = sps.count(fs)
                full[fs.lower()] += ful

    def main(self):
        summ = []
        txta = open("TextA.txt", encoding="utf8")
        x = txta.read()
        xx = x.split()
        for i in range(len(xx)):
            for j in string.punctuation:
                if j in xx[i]:
                    xx[i] = xx[i].replace(j, '')
        result = []
        for p in xx:
            if p.isdigit() or p == '—':
                continue
            else:
                result.append(p)
        xx = result
        s = ' '.join(xx)
        self.count(xx)
        top = nlargest(100, full.values())
        topp = []
        for o in top:
            t = self.get_key(full, o) + ' -> ' + str(o) + ' раз'
            if t in topp:
                continue
            else:
                topp.append(t)
        summ.append(len(xx))
        for i in topp:
            summ.append(i)
        return summ
