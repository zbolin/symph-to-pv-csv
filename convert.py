import csv
import datetime

SYMPH = "bb.csv"
PV = "bb3.csv"


def main():
    with open(SYMPH, mode='r', encoding='utf-8-sig') as file:
        csvFile = csv.reader(file)
        # print("Start Date, Assets, Weights")
        write("Start Date,Assets,Weights")
        assets = ""
        for line in csvFile:
            s = ', '.join(line)
            trade = ""
            if "Date" in s:
                #    print(s)
                assets += s[18:len(s)].replace("$USD", "VOO")
                print(assets)
#            if 1 == 2:
            if "Yes" in s:
                date = s[0:10]
                d = datetime.datetime.strptime(date, '%Y-%m-%d')
                #        print(datetime.date.strftime(d, "%m/%d/%y"))
                trade += date
                trade += ',"'
                trade += assets
                trade += '","'
#                print(s)
#                print(s[17:len(s)])
                trade += s[17:len(s)].replace("-", "0%")

                trade += '"'
                write(trade)


def write(line):
    file1 = open(PV, "a")  # append mode
    line += '\n'
    file1.write(line)
    file1.close()
    #print(line)


if __name__ == "__main__":
    main()
