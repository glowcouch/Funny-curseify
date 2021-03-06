def replaceWithInArray(array, replace, replaceWith):
    for i in range(0, len(array)):
        if array[i] == replace:
            array[i] = replaceWith
    return(array)


def curseify(sentence):

    words = sentence.split(" ")
    output = ""

    # replace all instances of oops with balderdash
    replaceWithInArray(words, "oops", "balderdash")
    replaceWithInArray(words, "Oops", "Balderdash")
    replaceWithInArray(words, "oops,", "balderdash,")
    replaceWithInArray(words, "Oops,", "Balderdash,")

    # add son of a monkey to you are a
    for i in range(0, len(words)):
        if str(words[i]).lower() == "you" and str(words[i+1]).lower() == "are" and str(words[i+2]).lower() == "a":
            for i2 in range(i+3, len(words)):
                if "." in words[i2]:
                    words[i2] = ""
                    break
                else:
                    words[i2] = ""
            words[i+3] = "son of a monkey."

    for i in range(0, len(words)):
        if words[i] != "":
            output += words[i] + " "
        #if words[i] != "":
        #    if "." in words and words[i] != "." and words[i+1] != ".":
        #        output += words[i] + " "
        #    else:
        #        output += words[i]
    return output
