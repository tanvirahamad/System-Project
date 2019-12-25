import nltk as mahed

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(p):
    val = edits1(p)
    wf = open('input.txt', 'w')
    wf.write(p + "\n")
    for i in val:
        wf.write(i + "\n")
        x = edits1(i)
        for line in x:
            line += "\n"
            wf.write(line)
    wf.close()

    uasn = "tnvit"
    f = open("input.txt", "r")
    s = f.readlines()

    for line in s:
        if uasn.lower() + "\n" == line.lower():
            return True
            break

