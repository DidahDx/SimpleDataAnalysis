import csv
import operator
import statistics


# from matplotlib import pyplot as plt


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
                mydict[country] = i
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


# get statistics and median
def get_year_statistics(bmi_all):
    validInput = True
    while validInput:
        # get user input
        try:
            number = int(input('Select year to find statistics (1980 to 2008)\n'))
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
            median = round(statistics.median(population_total), 3)

            message = "In {}, countries with minimum and maximum BMI values are were {} and {} respectively.\n " \
                      "Median BMI value in {} was {} \n".format(number, min_country, max_country, number, median)
            print(message)

            validInput = False
        except ValueError:
            print('invalid input. Try again\n')
            # return without anything to exit a method
        except:
            print('unknown error. Try again\n')


# calculate percentage difference
def percentage_diff(num1, num2):
    return abs(((num1 - num2) / ((num1 + num2) / 2)) * 100)


# compare the last five years
def compare_status(bmi_men, bmi_women):
    countries = bmi_men.keys()
    men_china = []
    women_china = []
    men_india = []
    women_india = []
    men_us = []
    women_us = []
    for c in countries:
        if c == 'China':
            years = bmi_men[c].keys()
            for y in years:
                if int(y) > 2003:
                    men_china.append(float(bmi_men[c][y]))
                    women_china.append(float(bmi_women[c][y]))
        if c == 'India':
            years = bmi_men[c].keys()
            for y in years:
                if int(y) > 2003:
                    men_india.append(float(bmi_men[c][y]))
                    women_india.append(float(bmi_women[c][y]))
        if c == 'United States':
            years = bmi_men[c].keys()
            for y in years:
                if int(y) > 2003:
                    men_us.append(float(bmi_men[c][y]))
                    women_us.append(float(bmi_women[c][y]))
    m_china = sum(men_china) / 5
    w_china = sum(women_china) / 5
    p_china = "Percentage difference: {}%".format(round(percentage_diff(m_china, w_china), 2))
    m_india = sum(men_india) / 5
    w_india = sum(women_india) / 5
    p_india = "Percentage difference: {}%".format(round(percentage_diff(m_india, w_india), 2))
    m_us = sum(men_us) / 5
    w_us = sum(women_us) / 5
    p_us = "Percentage difference: {}%".format(round(percentage_diff(m_us, w_us), 2))
    print(' China ')
    pre_china = "\nMen : {} \nWomen: {} \n{}\n".format(round(m_china, 2), round(w_china, 2), p_china)
    print(pre_china)
    print(' India ')
    pre_india = "\nMen : {} \nWomen: {} \n{}\n".format(round(m_india, 2), round(w_india, 2), p_india)
    print(pre_india)
    print(' United States ')
    pre_us = "\nMen : {} \nWomen: {} \n{}\n".format(round(m_us, 2), round(w_us, 2), p_us)
    print(pre_us)


def draw_life_expectancy(life, bmi_men):
    validInput = True
    while validInput:
        try:
            countries = list(bmi_men.keys())
            years = []

            for c in countries:
                years = [int(x) for x in list(bmi_men[c].keys())]

            countries1 = [x.lower() for x in countries]
            country = str(input('Enter the country to visualize life expectancy data\n'))
            values = countries1.index(country.lower())
            y_values = [float(x) for x in life[values]]

            # used to plot the graph
            # use variable years for x-axis
            # use variable y_values for y-axis

            # plt.plot(years,y_values)
            # plt.show()
            print("{} \n {}".format(years, y_values))

            validInput = False
        except:
            print('invalid input. Try again\n')


def draw_chart(life, bmi_all):
    validInput = True
    while validInput:
        try:
            countries = list(bmi_all.keys())
            years = []

            for c in countries:
                years = list(bmi_all[c].keys())

            countries1 = [x.lower() for x in countries]
            years1 = [int(x) for x in years]

            country = str(input('Enter the country to visualize life expectancy data and BMI world average\n'))
            values = countries1.index(country.lower())
            y_values = [float(x) for x in life[values]]
            y_values2 = [round(float(x), 2) for x in list(bmi_all[country.capitalize()].values())]

            # used to plot the graph
            # use variable years1 for x-axis
            # use variable y_values for y-axis

            # plt.plot(years1,y_values)
            # plt.plot(years1,y_values2)
            # plt.show()
            print("{} \n {}\n{}".format(years1, y_values2, y_values))
            validInput = False
        except:
            print('invalid input. Try again\n')


print("\n A simple data analysis program\n")
life = readfile('life.csv', True)
bmi_men = readfile('bmi_men.csv', False)
bmi_women = readfile('bmi_women.csv', False)
print("\n ------Step 1--------- \n All data set has been read to memory\n")
bmi_all = create_gender_average_csv(bmi_men, bmi_women)
print("\n ------Step 2--------- \n Gender average BMI values stored in new dictionary\n")
print("\n ------Step 3--------- ")
get_year_statistics(bmi_all)
print("\n ------Step 4--------- \n")
compare_status(bmi_men, bmi_women)
print("\n ------Step 5--------- ")
draw_life_expectancy(life, bmi_men)
print("\n ------Step 6--------- ")
draw_chart(life, bmi_all)
