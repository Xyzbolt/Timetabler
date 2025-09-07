from timetable import Timetable
def main():
    newtable = Timetable(5, 6, 2)

    newtable.addsubjects()
    newtable.addtables()
    newtable.createlinks()
    newtable.filltables()
    newtable.printtables()




if __name__ == "__main__":
    main()
