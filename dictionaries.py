import string

def word_count(s):
    """
    Find the number of occurrences of each word
    in a string(Don't consider punctuation characters)
    """
    y=s.split()
    for i in y:
        x=y.index(i)
        print(y[x])
        for j in string.punctuation:
            y[x]=y[x].strip(j)
            y[x]=y[x].strip()
    words_count = dict()
    for i in y:
        words_count[i]=y.count(i)
    return words_count




def dict_items(d):
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    """
    # lst=[]
    # for a,b in d:
    #     temp=(a,b)
    #     lst.append(temp)
    # return lst
    return list(d.items())


def dict_items_sorted(d):
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    sorted by `d`'s keys
    """
    return list(sorted(d.items()))
