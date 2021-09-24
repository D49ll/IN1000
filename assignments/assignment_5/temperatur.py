def create_dict_from_file(filename):
    new_dict = dict()
    for line in open(filename,'r'):
        key,value = line.split(",")
        new_dict[key] = float(value)
    return new_dict
    
def compare_temp(max_temps,filename):
    for line in open(filename,'r'):
        month, *val = line.split(',')
        val[0] = int(val[0])
        val[1] = float(val[1])
        if  max_temps[month] < val[1]:
            #print(f"Ny varmerekord {val[0]} {month}! {val[1]} grader Celsius (gammel rekord {max_temps[month]} grader Celsius)")
            max_temps[month] = val[1]
    return max_temps

def main():
    max_temps = create_dict_from_file('max_temperatures_per_month.csv')

    for key, val in max_temps.items():
        print(key,val)

    max_temps= compare_temp(max_temps, 'max_daily_temperature_2018.csv')
    print()

    for key, val in max_temps.items():
        print(key,val)

main()