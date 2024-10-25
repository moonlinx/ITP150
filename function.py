def cigar_party(cigars, is_weekend):
    if cigars < 40:
        return False

    if is_weekend:
        return True

    return cigars <=60
