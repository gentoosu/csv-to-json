import csv
import json
import sys ### sys.stdout.write allows me to print without trailing space or newline
from sys import argv

#### Open the CSV
script_name, file_name = argv
#f = open( '/var/www/html/getinfo.txt', 'rU' )
f = open( file_name, 'rU' )

#### Change each fieldname to the appropriate field name. I know, so difficult.
#### reader = csv.DictReader( f, fieldnames = ( "Application","Hostname","Environment","Deployment Type", "Deployment Name", "State", "Enabled", "Last Check" ))
reader = csv.reader(f)
next(reader)
reader = list(reader)

### Generate a list of unique applications

app_list = []
for row in reader:
        app_list.append(row[0])

#### Create list of unique app names

unique_app_list = list(set(app_list))

#### Begin printing to json

sys.stdout.write("{")
unique_app_count = len(unique_app_list)

for app in unique_app_list:
        count = app_list.count(app) ## count the number of hosts from the app
        x = 0
        unique_app_count -= 1

        sys.stdout.write("\"" + app + "\": [")
        for line in reader:
                if line[0] == app:
                        if x == 0:
                                sys.stdout.write("{")
                        else:
                                sys.stdout.write(",{")

                        sys.stdout.write("\"Hostname\":" + "\"" + line[1] + "\",")
                        sys.stdout.write("\"Environment\":" + "\"" + line[2] + "\",")
                        sys.stdout.write("\"Last Check\":" + "\"" + line[7] + "\",")
                        sys.stdout.write("\"Enabled\":" + "\"" + line[6] + "\",")
                        sys.stdout.write("\"State\":" + "\"" + line[5] + "\",")
                        sys.stdout.write("\"Deployment Name\":" + "\"" + line[4] + "\",")
                        sys.stdout.write("\"Deployment Type\":" + "\"" + line[3] + "\",")
                        sys.stdout.write("\"Uptime\":" + "\"" + line[8] + "\",")
                        sys.stdout.write("\"Thread Count\":" + "\"" + line[9] + "\",")
                        sys.stdout.write("\"Peak Thread Count\":" + "\"" + line[10] + "\",")
                        sys.stdout.write("\"Current Thread CPU Time\":" + "\"" + line[11] + "\",")
                        sys.stdout.write("\"Current Thread User Time\":" + "\"" + line[12] + "\",")
                        sys.stdout.write("\"Total Started Thread Count\":" + "\"" + line[13] + "\",")
                        sys.stdout.write("\"Daemon Thread Count\":" + "\"" + line[14] + "\",")
                        sys.stdout.write("\"Datasource Test\":" + "\"" + line[15] + "\",")
                        sys.stdout.write("\"Active Count\":" + "\"" + line[16] + "\",")
                        sys.stdout.write("\"Available Count\":" + "\"" + line[17] + "\",")
                        sys.stdout.write("\"Average Blocking Time\":" + "\"" + line[18] + "\",")
                        sys.stdout.write("\"Average Creation Time\":" + "\"" + line[19] + "\",")
                        sys.stdout.write("\"Created Count\":" + "\"" + line[20] + "\",")
                        sys.stdout.write("\"Destroyed Count\":" + "\"" + line[21] + "\",")
                        sys.stdout.write("\"In Use Count\":" + "\"" + line[22] + "\",")
                        sys.stdout.write("\"Max Creation Time\":" + "\"" + line[23] + "\",")
                        sys.stdout.write("\"Max Used Count\":" + "\"" + line[24] + "\",")
                        sys.stdout.write("\"Max Wait Count\":" + "\"" + line[25] + "\",")
                        sys.stdout.write("\"Max Wait Time\":" + "\"" + line[26] + "\",")
                        sys.stdout.write("\"Timed Out\":" + "\"" + line[27] + "\",")
                        sys.stdout.write("\"Total Blocking Time\":" + "\"" + line[28] + "\",")
                        sys.stdout.write("\"Total Creation Time\":" + "\"" + line[29] + "\",")
                        sys.stdout.write("\"Heap Used\":" + "\"" + line[30] + "\",")
                        sys.stdout.write("\"Heap Max\":" + "\"" + line[31] + "\",")
                        sys.stdout.write("\"Heap Committed\":" + "\"" + line[32] + "\",")
                        sys.stdout.write("\"Non Heap Used\":" + "\"" + line[33] + "\",")
                        sys.stdout.write("\"Non Heap Committed\":" + "\"" + line[34] + "\"")
                        if x == count - 1:  ## Check for the last host in the app
                                sys.stdout.write("}]")
                                if unique_app_count != 0:
                                        sys.stdout.write(",")
                                else:
                                        sys.stdout.write("")
                        else:
                                sys.stdout.write("}")
                        x += 1

sys.stdout.write("}")
