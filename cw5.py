python = {"Abhi","Meera","Nived"}
Data_science = {"Anand","Mahadevan","Ganga","Nived","Abhi"}

python.add("Sneha")
print(python)

Data_science.remove("Anand")
print(Data_science)

print(python & Data_science)

print(python - Data_science)

print(python | Data_science)

courses = {
    "python" : len(python),
    "Data_science" : len(Data_science)
}

for x,y in courses.items() : 
 print("course: ",x,", students : ",y)

courses_new = {x : y * 2 for x,y in courses.items()}
print(courses_new)




