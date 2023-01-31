subject_dictionary = {}

with open("subject.txt", encoding='utf-8') as study_hours:
    for line in study_hours:
        study = line.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "")
        subject, lecture, practice, labs = study.split()
        lec, pr, lab = 0, 0, 0
        if lecture != "-":
            lec = int(lecture)
        if practice != "-":
            pr = int(practice)
        if labs != "-":
            lab = int(labs)
        subject_dictionary[subject] = lec + pr + lab
    print(f'{subject_dictionary}')
study_hours.close()
