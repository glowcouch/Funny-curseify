def replaceWithInArray(array, replace, replaceWith):
    for i in range(0, len(array)):
        if array[i] == replace:
            array[i] = replaceWith
    return(array)


def curseify(string):

    words = string.split(" ")
    output = ""

    # replace all instances of oops with balderdash
    replaceWithInArray(words, "oops", "balderdash")

    # add son of a monkey to you are a
    for i in range(0, len(words)):
        if words[i] == "you" and words[i+1] == "are" and words[i+2] == "a":
            for i2 in range(i, len(words) - i):
                words[i2] = ""
            words[i+3] = "son of a monkey"
    for i in range(0, len(words)):
        output += words[i] + " "
    return output
