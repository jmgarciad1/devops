def load_file(file_name: str) -> dict:
    blacklist = {}
    file = open(file_name, "r")
    file.readline()

    line = file.readline()
    while len(line) > 0:
        datos = line.split(",")
        llave = datos[1]
        record = {
                'id': datos[0],
                'email': datos[1],
                'app_uuid': datos[2],
                'blocked_reason': datos[3],
                'ip': datos[4],
                'createdAt': datos[5]
            }
        blacklist[llave] = record
        line = file.readline()

    file.close()
    return blacklist

def save_line_file(file_name: str, record: dict):
    file = open(file_name, "a")
    file.write("\n" + record['id'] + "," + record['email'] + "," + record['app_uuid'] + "," + record['blocked_reason'] + "," + record['ip'] + "," + record['createdAt'])
    file.close()
    return { "message": "Item created" }