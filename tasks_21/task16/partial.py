def printboard(partial):
    SIZE = len(partial)
    for digit in partial:
        col = int(digit)
        lin = ". "*(col-1) + "Q " + \
              ". "*(SIZE-col)
        print lin

def checkplacement(partial,col):
    row = len(partial)
    if partial :
        spread = 1
        for prow in range(row-1,-1,-1):
            if int(partial[prow]) in (col,col-spread,col+spread):
                return False
            spread += 1
        return True

