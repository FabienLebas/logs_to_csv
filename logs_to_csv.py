import csv

result = []

with open('smallRobotLog.csv', newline='') as csvSourceFile:
  reader = csv.reader(csvSourceFile, delimiter=',', quotechar='|')
  for row in reader:
    if len(row) > 1:
      if 'inventorylocation' in row[1]:
        result.append([row[2].split(" : ")[1], row[3], row[5], row[6], row[7]])


with open('result.csv', 'w') as csvResultFile:
  writer = csv.writer(csvResultFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  writer.writerows(result)
