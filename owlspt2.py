def owl_count():
    count = 0
    result = []
    text = input("Enter some text: ")
    text = text.lower()
    for index, word in enumerate(text.split()):
        if word.find("owl") > -1:
            count += 1
            result += [index,]
    print("There were " + str(count) + " words that contained owl.")
    print("They occurred at indices: " + str(result))

owl_count()