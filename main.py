import csv
import operator


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


##
def create_gender_average_csv(men, women):
    print(men['Afghanistan']['1980'])
    print(women)


print("\n A simple data analysis program\n")

life = readfile('life.csv', True)
men = readfile('bmi_men.csv', False)
women = readfile('bmi_women.csv', False)

print("\n ------Step 1--------- \n All data set has been read to memory\n")

print(life)

bmi_all = create_gender_average_csv(men, women)
print("\n ------Step 2--------- \n Gender average BMI values stored in new dictionary\n")
