Web_Devolopment = ["Abhi","Meera","Nived"]
Data_Science = ["sneha","Sidra","Asha"]
UI_OR_UX_Design = ["Abhijith","Anand","Amiz"]

all_participants = [Web_Devolopment , Data_Science , UI_OR_UX_Design]
print(all_participants)

Web_Devolopment.append("Arya")
print(Web_Devolopment)

Data_Science.insert(1,"Surya")
print(Data_Science)

UI_OR_UX_Design.pop()
print(UI_OR_UX_Design)

Data_Science_new = Data_Science.copy()
Data_Science.clear()
print(Data_Science_new)
print(Data_Science)

print(Web_Devolopment[:2])

Data_Science_new_len =[len(x) for x in Data_Science_new]
print(Data_Science_new_len)

if "Asha" in Web_Devolopment or "Asha" in Data_Science_new or "Asha" in UI_OR_UX_Design :
    print("Yes")
else:
    print("No")

tupleParticipants = (Web_Devolopment[:1],Data_Science_new[:1],UI_OR_UX_Design[:1])
print(tupleParticipants)