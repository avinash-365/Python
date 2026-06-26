students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]

for i in students:
    print(i["name"])

total=0
for i in students:
    total=total+i["score"]
print(total)

n_s={"id":104,"name":"John","score":85}
students.append(n_s)

print(students)

for i in students:
    if i["id"]==102:
        i["score"]=88
        break

print(students)

for i in students:
    if i["name"]=="Charlie":
        students.remove(i)
        break

print(students)

for i in students:
    if i["score"]>85:
        print(i["name"])

students.sort(key=lambda x: x["score"],reverse=True)   

print(students)