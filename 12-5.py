def unique_symbols(fst_str, scd_str, trd_str):
    fst_set = set(fst_str)
    scd_set = set(scd_str)
    trd_set = set(trd_str)
    fst_new = fst_set - scd_set - trd_set
    scd_new = scd_set - fst_set - trd_set
    trd_new = trd_set - fst_set - scd_set
    result = list(fst_new) + list(scd_new) + list(trd_new)
    for symbol in result:
        print(symbol, end=' ')


string1 = "hello"
string2 = "goodbye"
string3 = "billie"

unique_symbols(string1, string2, string3)
