def put_tab(N):
    _str = ""
    for i in range(0, N):
        _str += "    "
    return _str


def extract_file_values(file):
    doc = open(file, "r")

    data = {}

    for line in doc:
        key, val_str = line.strip().split("=")
        value = tuple(val_str.strip().split(","))
        data[key] = value

    return data

def periodic_table():
    data = extract_file_values("periodic_table.txt")
    
    html_table = "<div>\n"
    html_table += f"{put_tab(3)}<table>\n"
    pos = 0
    savePos = 0
    # print(data["Hydrogen "])
    for key, value in data.items():
        # for val in value:
        posVal = value[0].split(":")
        if posVal[0].strip() == "position":
            pos = int(posVal[1])
        print(posVal[1])
        if pos - (savePos+1) > 0:
            for i in range(0, pos - (savePos + 1)):
                html_table += f"{put_tab(5)}<td style=\"border:none;\">\n"
                html_table += f"{put_tab(6)}<ul>\n"
                html_table += f"{put_tab(6)}</ul>\n"
                html_table += f"{put_tab(5)}</td>\n"
        if pos == 0:
            html_table += f"{put_tab(4)}<tr>\n"
        html_table += f"{put_tab(5)}<td class=\"valid\">\n"
        html_table += f"{put_tab(6)}<h4>{key}</h4>\n"
        html_table += f"{put_tab(6)}<ul>\n"
        for val in value:
            val2 = val.split(":")
            if val2[0].strip() == "electron":
                nb = val2[1].split(" ")
                newVal = 0
                for ret in nb:
                    newVal += int(ret)
                    val2[1] = str(newVal)
                html_table += f"{put_tab(7)}<li>{val2[1]} {val2[0]}</li>\n"
            if val2[0].strip() == "number":
                html_table += f"{put_tab(7)}<li>No {val2[1]}</li>\n"
            if val2[0].strip() == "small":
                html_table += f"{put_tab(7)}<li>{val2[1]}</li>\n"
            if val2[0].strip() == "molar":
                html_table += f"{put_tab(7)}<li>{val2[1]}</li>\n"
        html_table += f"{put_tab(6)}</ul>\n"
        html_table += f"{put_tab(5)}</td>\n"
        if pos == 17:
            html_table += f"{put_tab(4)}</tr>\n"
        savePos = pos
    html_table += f"{put_tab(3)}</table>\n"
    html_table += f"{put_tab(2)}</div>"

    css_table = """:root {
                font-family: Helvetica;
                background: #424242;
                color: white;
                font-size: 10px;
                width: 100vw;
                height: 100vh;
                overflow: hidden;
            }

            .valid, table {
                border: solid 2px white;
                border-collapse: collapse;
                transition: .2s;
            }

            .valid:hover {
                transform: scale(1.2);
                background: #424242;
                box-shadow: 0 0 4px white,
                            inset 0 0 4px black;
            }

            div {
                margin-top: 100px;
            }

            table {
                background: black;
                box-shadow: 0 0 10px black;
            }"""

    html_string = f"""<!DOCTYPE html>
<html lang=\"en\">
    <head>
        <meta charset="utf-8">
        <title>Periodic Table</title>
        <style>
            {css_table}
        </style>
    </head>
    <body>
        {html_table}
    </body>
</html>"""

    try:
        with open("periodic_table.html", "x") as doc:
            doc.write(html_string)
    except:
        with open("periodic_table.html", "w") as doc:
            doc.write(html_string)
        

if __name__ == '__main__':
    periodic_table()