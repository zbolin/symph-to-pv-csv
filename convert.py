import csv
import datetime

SYMPH = "bb.csv"
PV = "bb3.csv"

SYMPH = "HFEA.csv"
PV = "HFEA2.csv"

def main():
    with open(SYMPH, mode='r', encoding='utf-8-sig') as file:
        csvFile = csv.reader(file)
        assets = ""
        for line in csvFile:
            s = ', '.join(line)
            trade = ""
            if "Date" in s:
                assets += "Date,"
                assets += s[18:len(s)]
                write(assets)
            if "Yes" in s:
                date = s[0:10]
                trade += date
                trade += ','
                trade += s[17:len(s)].replace("-", "").replace(" ", "")
                write(trade)
            if "No" in s:
                date = s[0:10]
                trade += date
                trade += ','
                trade += s[16:len(s)].replace("-", "").replace(" ","")
                write(trade)


def write(line):
    file1 = open(PV, "a")  # append mode
    line += '\n'
    file1.write(line)
    file1.close()
    #print(line)


if __name__ == "__main__":
    main()
