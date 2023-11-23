subjects = {}
with open('subjects.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        subject, lessons = line.split(':')
        lessons_list = lessons.split()
        lessons_hours = 0
        for lessons in lessons_list:
            lessons_hours += int(''.join(filter(str.isdigit, lessons)))
        subjects[subject] = lessons_hours

print(subjects)
