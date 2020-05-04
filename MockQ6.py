def generate_sentences(subjects, predicates, objects):
    subjects.sort()
    predicates.sort()
    objects.sort()
    string = ""
    for s in subjects:
        for p in predicates:
            for o in objects:
                string += " " + s+" " + p + " " + o + "."
    string = string[1:]
    return(string)