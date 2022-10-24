import csv
import datetime


def main(fileName):
    outputFile = fileName.replace(".csv", "")
    outputFile += "_pv.csv"
    with open(fileName, mode='r', encoding='utf-8-sig') as file:
        csvFile = csv.reader(file)
        assets = ""
        usdIndex = 0
        for line in csvFile:
            trade = ""
            if "Date" in line:
                usdIndex = line.index("$USD")
                line.remove("$USD")
                s = ', '.join(line).replace(" ","")
                assets += "Date,"
                assets += s[18:len(s)]
                write(assets, outputFile)
            if "Yes" in line:
                del line[usdIndex]
                s = ', '.join(line)
                date = s[0:10]
                trade += date
                trade += ','
                trade += s[17:len(s)].replace("-", "").replace(" ", "")
                write(trade, outputFile)
            if "No" in line:
                del line[usdIndex]
                s = ', '.join(line)
                date = s[0:10]
                trade += date
                trade += ','
                trade += s[16:len(s)].replace("-", "").replace(" ","")
                write(trade, outputFile)

    print("Finished converting to :", outputFile)

def write(line, outputFile):
    file1 = open(outputFile, "a")  # append mode
    line += '\n'
    file1.write(line)
    file1.close()


if __name__ == "__main__":
    file = input("Enter name of Composer file to convter to Portfolio Visualizer: ")
    main(file)
    #main("HFEA.csv")
