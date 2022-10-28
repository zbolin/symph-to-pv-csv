import csv
import datetime
import decimal
from decimal import Decimal
import os

def validate(fileName):
    outputFile = fileName
    with open(fileName, mode='r', encoding='utf-8-sig') as file:
        if os.path.exists(outputFile):
            os.remove(outputFile)
        csvFile = csv.reader(file)
        for line in csvFile:
            if "Date" not in line:
                numItems = 0
                sum = 0;
                for i, item in enumerate(line):
                    if "-" not in item and item != '':
                        val = item.strip('%')
                        numItems+=1
                        sum = Decimal(val) + sum
                if sum != 100.0:
                    remainder = Decimal(100.0) - sum
                    addToItems = round(Decimal(remainder) / Decimal(numItems),2)
                    for i, item in enumerate(line):
                        if "Date" not in line and "-" not in line[i] and line[i] != '':
                            line[i] = line[i].strip('%')
                            line[i] = Decimal(line[i])+addToItems
                            line[i] = str(line[i])+'%'
                
            write(','.join(line), outputFile)
    return outputFile
                      
def main(fileName):
    outputFile = fileName.replace(".csv", "")
    outputFile += "_pv.csv"
    if os.path.exists(outputFile):
        os.remove(outputFile)
    with open(fileName, mode='r', encoding='utf-8-sig') as file:
        csvFile = csv.reader(file)
        assets = ""
        usdIndex = 0
        for line in csvFile:
            trade = ""
            if "Date" in line:
                usdIndex = line.index("$USD")
                line.remove("$USD")
                s = ', '.join(line).replace(" ", "")
                assets += "Date,"
                assets += s[15:len(s)]
                write(assets, outputFile)
            if "Yes" in line:
                del line[usdIndex]
                s = ', '.join(line)
                s = s.replace(', 0.0%',', -')
                date = s[0:10]
                trade += date
                trade += ','
                trade += s[17:len(s)].replace("-", "").replace(" ", "")
                write(trade, outputFile)
            if "No" in line:
                del line[usdIndex]
                s = ', '.join(line)
                s = s.replace(', 0.0%',', -')
                date = s[0:10]
                trade += date
                trade += ','
                trade += s[16:len(s)].replace("-", "").replace(" ","")
                write(trade, outputFile)
    return outputFile

def write(line, outputFile):
    file1 = open(outputFile, "a")  # append mode
    line += '\n'
    file1.write(line)
    file1.close()


if __name__ == "__main__":
    file = input("Enter name of file to convert: ")
    outputFile = validate(main(file))
    print("SUCCESS! New file created :", outputFile)
