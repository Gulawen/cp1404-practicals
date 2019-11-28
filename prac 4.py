
course_room_number = {'CS101': '3004', 'CS102': '4501','CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
instructor_number = {'CS101': 'Haynes', 'CS102': 'Alvarado','CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
time = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.','CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}
number = input('Please enter a course number: ').upper()
if number in course_room_number:
    print('Room number :'+ course_room_number[number])
    print('Instructor :'+ instructor_number[number])
    print('Meeting Time :'+ time[number])
