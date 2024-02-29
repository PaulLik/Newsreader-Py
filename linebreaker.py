l = "Новая Alone in the Dark получила «безумный» трейлер и системные требования — напугать они не смогут"

def hyphen(string):
    txt = ""
    if len(string) > 57:
        words = string.split()
        txtLines = 1
        for w in words:
            if len(txt + w) > 59 * txtLines:
                txt = txt + "\n" + " " * 28 + "\t" + w
                txtLines += 1
            else:
                txt = txt + " " + w
    return "\u2022 02:15 3D News Software\t" + txt.lstrip()


print(hyphen(l))