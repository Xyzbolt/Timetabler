import random


class Timetable():
    def __init__(self, days, lectures, sections):
        self.dayno = days
        self.lectureno = lectures
        self.sections = sections
        self.sectiongroups = [] 
        self.subjects = list() 
        self.timetables = []
        
    def addsubjects(self):
        self.subjects = [{"CS": 2, "Bio": 1, "Acc": 1, "Math": 2, "Psy": 1, "Phy": 2, "Eco": 1, "Law": 1, "Chem": 2, "Bus" : 2, "Soc": 1, "Urd": 1},
                         {"CS": 2, "Bio": 1, "Acc": 1, "Math": 2, "Psy": 1, "Phy": cw2, "Eco": 1, "Law": 1, "Chem": 2, "Bus" : 2, "Soc": 1, "Urd": 1}]
        self.sectiongroups = [2 , 3]
        for x in range(self.sections):
        #     self.sectiongroups.append(0)
        #     self.subjects.append(dict())
        #     print(f"FOR SECTION {x}")
        #     while True:
        #         print("add subject: ")
        #         sub = input()
        #         if sub == "exit":
        #             break
        #         print("add number of sections")
        #         grps = int(input())
        #         if grps > self.sectiongroups[x]:
        #             self.sectiongroups[x] = grps
        #         self.subjects[x][sub] = grps
            self.subjects[x] = dict(sorted(self.subjects[x].items(), key= lambda sub: sub[1], reverse=True))  
            
        

    def addtables(self):
        for x in range(self.sections):
            self.timetables.append([])
            for _ in range(self.sectiongroups[x]):
                self.timetables[x].append( {f"day {day}": {x: [] for x in range(self.lectureno)} for day in range(self.dayno)})

    def createlinks(self):
        self.links = [["CS", "Bio", "Acc"], ["Math", "Psy"], ["Phy", "Eco", "Law"], ["Chem", "Bus"]]
    
    def createcombos(self):
        pass

    def filltables(self):
            for x in range(self.sections):
                for timetable in self.timetables[x]:
                    subs_to_add = []
                    for sub in self.subjects[x]:
                        if self.subjects[x][sub] != 0:
                            subs_to_add.append(sub)
                            self.subjects[x][sub] -= 1
                    
                    max_day_tries = 100
                    for day in timetable:
                        day_sub = subs_to_add[:]
                        
                        tries = 0
                        success = False
                        while tries < max_day_tries and not success:
                            tries += 1
                            
                            for lecture in range(self.lectureno):
                                timetable[day][lecture] = []
                            
                            all_placed = True
                            for subject in day_sub:
                                placed = False
                                lectures = list(range(self.lectureno))
                                random.shuffle(lectures)
                                
                                for lecture in lectures:
                                    clash = False
                                    for y in range(self.sections):
                                        for table in self.timetables[y]:
                                            if subject in table[day][lecture]:
                                                clash = True
                                                break
                                        if clash:
                                            break
                                    
                                    if not clash and not timetable[day][lecture]:
                                        timetable[day][lecture].append(subject)
                                        placed = True
                                        
                                        if len(subs_to_add) > self.lectureno:
                                            for link in self.links:
                                                if subject in link:
                                                    for linked_sub in link:
                                                        if linked_sub in day_sub and linked_sub != subject:
                                                            timetable[day][lecture].append(linked_sub)
                                                            day_sub.remove(linked_sub) 
                                                            
                                        break 
                                
                                if not placed:
                                    all_placed = False
                                    break 
                            
                            if all_placed:
                                success = True 
                        
                        if not success:
                            print(f"Warning: Could not create a valid schedule for day {day} after {max_day_tries} attempts.")

                                 

    def printtables(self):
        for x in range (self.sections):
            print("====SECTION====")
            for timetable in self.timetables[x]:
                print("==========")
                for day in timetable:
                    print(timetable[day])

    def passtable(self):
        return self.timetables


