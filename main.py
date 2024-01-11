class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, showid, movie_name, time):
        show = (showid, movie_name, time)
        self.__show_list.append(show)

        seat = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[showid] = seat

    def book_seats(self, showid, seats_tuples):
        if showid not in self.__seats:
            print(f"Failed !!! Invalid :: No show of showid : {showid}")
            return

        seats = self.__seats[showid]
        for tuple in seats_tuples:
            row, col = tuple

            if row < 0 or col < 0 or row >= self.__rows or col >= self.__cols:
                print(f"Failed !!! Invalid Seat row:: {row}, col: {col}")
                continue

            if seats[row][col] == 1:
                print(
                    f"Failed !!! Already booked :: Seat row: {row}, col: {col}"
                )
                continue

            seats[row][col] = 1
            print(f"Successfull !!! Seat booked:: row: {row}, col: {col}")

    def view_show_list(self):
        print("Available shows:")
        for show in self.__show_list:
            print(show)

    def view_available_seats(self, showid):
        if showid not in self.__seats:
            print(f"Failed !!! Invalid :: No show of showid : {showid}")
            return

        print(f"Available seats for showid {showid}:")
        seats = self.__seats[showid]
        for seat in seats:
            print(seat)


# -------------------------------------------------
hall = Hall(rows=5, cols=5, hall_no=1000)
hall.entry_show(showid=11, movie_name="Jawan", time="Jan 15, 2024")
hall.entry_show(showid=12, movie_name="Spider Man", time="Jan 15, 2024")

while True:
    print("Options ::")
    print("1. View All show today")
    print("2. View Available seats")
    print("3. Book ticket")
    print("4. Exit")

    print("--------------------------------")
    option = int(input("Enter Option : "))

    if option == 1:
        hall.view_show_list()
        print()

    elif option == 2:
        showid = int(input("Enter Show id: "))
        hall.view_available_seats(showid=showid)

    elif option == 3:
        showid = int(input("Enter Show id: "))
        noofticket = int(input("Enter No of ticket: "))

        seats_tuples = []
        for i in range(1, noofticket + 1):
            row = int(input(f"Enter Seat Row for seat {i}: "))
            col = int(input(f"Enter Seat Col for seat {i}: "))

            seats_tuples.append((row, col))
        hall.book_seats(showid=showid, seats_tuples=seats_tuples)

    else:
        break
    print("--------------------------------")
