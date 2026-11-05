python_note = """     Python is a popular High-level programming language used for web development,
 data science, artificial intelligence, automation, and software development      """

length_ofp = len(python_note)
print(" length of the paragraph :", length_ofp)
print("first character :",python_note[0],"\n","Last character :", python_note[length_ofp - 1])
print(python_note[:51])
print(python_note.replace("Python","PYTHON"))
print(python_note.lower())
print(python_note.strip())
list = (python_note.split(" "))
print(list)
print("course" in python_note)
print("The course description is {} characters long and has {} words.".format(length_ofp,len(list)))
