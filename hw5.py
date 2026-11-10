frontend = {"Ganga","Mahadevan","Roshni","Aparna"}
backend = {"Aparna","Sivani","Akshay"}

frontend.add("Amritha")
print(frontend)

backend.discard("Akshay")
print(backend)

print(frontend.intersection(backend))

print(backend.difference(frontend))

course = {
    "frontend" : len(frontend),
    "backend" : len(backend)
}
for x,y in course.items() :
    print(x," : ",y)
    
course_new = {key: value for key, value in course.items()}
course_new["Fullstack"] = course["frontend"] + course["backend"]
print(course_new)