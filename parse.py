import mysql.connector

def splitString(str):
    results = []
    chunks = str.split(';')
    for c in chunks:s
        results.append(c.strip().replace("\n", "").replace('\\', '\\\\') .replace("'", "\\'"))
    return results

def insertStatement(arr):
    sql = "INSERT INTO acars (dateTime, flight, n_number, blk_id, msg_label, text_label, msg_text) VALUES "
    return sql


def insertValues(arr):
    dateTime = arr[0] +" " + arr[1]
    flight = arr[2]
    nNumber = arr[3].lstrip('.')
    blk_id = arr[4]
    msg_label = arr[5]
    text_label = arr[6]
    msg_text = arr[7]

    if nNumber.replace("_", "") == "":
        nNumber = ""

    sql = "("
    sql += "STR_TO_DATE('" + dateTime + "','%d/%m/%Y %H:%i'), "
    sql += "'" + flight +"', "
    sql += "'" + nNumber +"', "
    sql += "'" + blk_id +"', "
    sql += "'" + msg_label +"', "
    sql += "'" + text_label +"', "
    sql += "'" + msg_text +"');\n"
    return sql.replace("'\\'", "'\\\'")


array = []
with open("raw.ssv", "r") as ins:
    for line in ins:
        array.append(line)

header = splitString(array[0])
array.pop(0)
totalLength = len(array)
counter = 1
sql = ""
for a in array:
    sql += insertStatement(header) + insertValues(splitString(a));
    #print(sql)
with open("Output.txt", "w") as text_file:
    print(sql, file=text_file)