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

    for i in range(0, len(words)):
        output += words[i] + " "
    return output
