## card: a list of 2 elements

def flipcolor(C):
    val = C[0]
    s = C[1]
    if s == "hearts": return [val, "spades"]
    if s == "spades": return [val, "hearts"]
    if s == "clubs": return [val, "diamonds"]
    return [val, "clubs"]

def fliphand(H):
    return map (flipcolor, H)


    