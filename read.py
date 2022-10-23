import csv
import datetime

SYMPH = "pv-samples/bb.csv"
PV = "pv-samples/bb5.csv"


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
                assets += s[24:len(s)]
            #    print(assets)
            if "Yes" in s:
                date = s[0:10]
                d = datetime.datetime.strptime(date, '%Y-%m-%d')
                #        print(datetime.date.strftime(d, "%m/%d/%y"))
                trade += date
                trade += ',"'
                trade += assets
                print(assets.count(','))
                trade += '","'
                trade += s[20:len(s)].replace("-", "0%")
                print(s[20:len(s)].replace("-", "0%").count(','))
                trade += '"'
                #        print(s[20:len(s)])
                write(trade)


def write(line):
    file1 = open(PV, "a")  # append mode
    line += '\n'
    file1.write(line)
    file1.close()


if __name__ == "__main__":
    main()
