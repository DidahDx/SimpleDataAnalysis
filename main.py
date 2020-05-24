import csv
import operator
import statistics

years = []
countries = []


# used to read the csv file
def readfile(file_name, is_list):
    with open(file_name) as file:
        reader = csv.reader(file)

        if is_list:
            values = []
            for row, reader in enumerate(reader, start=0):
                if row > 0:
                    values.append(reader[1:])

            return values[1:]
        else:
            reader_dict = csv.DictReader(file)
            values = []
            mydict = {}

            for row, reader_dict in enumerate(reader_dict, start=0):
                values.append(dict(reader_dict))

            for i in values:
                country = i['country']
                i.pop('country')
                the_list = i
                mydict[country] = the_list

            return mydict


##creating another dictionary
def create_gender_average_csv(men, women):
    countries = men.keys()
    new_dict = {}

    for c in countries:
        years = men[c].keys()
        new_list = {}
        for y in years:
            average = (float(men[c][y]) + float(women[c][y])) / 2
            new_list[y] = average
        new_dict[c] = new_list

    return new_dict


# get statistics
def get_year_statistics(bmi_all):
    validInput = True
    while validInput:
        # get user input
        try:
            number = int(input('Select year to find statistics (1980 to 2008)\n'))
            print(number)
            new_dict = {}
            population_total = []

            countries = bmi_all.keys()
            for c in countries:
                years = bmi_all[c].keys()
                new_list = []
                for y in years:
                    if int(y) == number:
                        new_list = bmi_all[c][y]
                        population_total.append(float(bmi_all[c][y]))

                new_dict[c] = new_list

            max_country = max(new_dict.items(), key=operator.itemgetter(1))[0]
            min_country = min(new_dict.items(), key=operator.itemgetter(1))[0]
            median = statistics.median(population_total)

            message = "In {}, countries with minimum and maximum BMI values are were {} and {} respectively.\n " \
                      "Median BMI value in {} was {}".format(number, min_country, max_country, number, median)
            print(message)

            validInput = False
        except ValueError:
            print('invalid input. Try again\n')
            # return without anything to exit a method
        except:
            print('unknown error. Try again\n')


print("\n A simple data analysis program\n")

life = readfile('life.csv', True)
bmi_men = readfile('bmi_men.csv', False)
bmi_women = readfile('bmi_women.csv', False)

print("\n ------Step 1--------- \n All data set has been read to memory\n")

bmi_all = create_gender_average_csv(bmi_men, bmi_women)

print("\n ------Step 2--------- \n Gender average BMI values stored in new dictionary\n")

print("\n ------Step 3--------- \n")
get_year_statistics(bmi_all)
print("\n ------Step 4--------- \n")