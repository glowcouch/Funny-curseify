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
        if words[i] == "you" & words[i+1] == "are" & words[i+2] == "a":
            for i2 in range(i, len(words) - i):
                
    for i in range(0, len(words)):
        output += words[i] + " "
    return output
