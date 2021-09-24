class Date:
    def __init__(self,new_day,new_month,new_year):
        self._day = new_day
        self._month = new_month
        self._year = new_year

    def get_year(self):
        return self._year

    def __str__(self):
        return "Datoen er: "+str(self._day)+"."+str(self._month)+"."+str(self._year)

    