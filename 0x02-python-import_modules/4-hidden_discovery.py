#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    con = dir(hidden_4)
    for str in con:
        if str[:2] != "__":
            print("{}".format(str))
