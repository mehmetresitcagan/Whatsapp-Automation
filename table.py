def column_width_detect(rows, labels):
    cellWidths = []
    for i in range(len(rows[0])):
        maxWide = 0
        for row in rows:
            if len(str(row[i])) > maxWide:
                maxWide = len(str(row[i]))
        if labels is not None and len(str(labels[i])) > maxWide:
            maxWide = len(str(labels[i]))
        cellWidths.append(maxWide + 2)
    return cellWidths


def last_line(columnWidth):
    line = "└"
    exit = 0
    for i in columnWidth:
        exit += 1
        for j in range(i):
            line = line + "─"

        if exit == len(columnWidth):
            line = line + "┘"
            break
        line = line + "┴"
    return line


def label_last_line(columnWidth):
    line = "├"
    exit = 0
    for i in columnWidth:
        exit += 1
        for j in range(i):
            line = line + "─"

        if exit == len(columnWidth):
            line = line + "┤"
            break
        line = line + "┼"
    return line


def first_line(columnWidth):
    line = "┌"
    exit = 0
    for i in columnWidth:
        exit += 1
        for j in range(i):
            line = line + "─"

        if exit == len(columnWidth):
            line = line + "┐"
            break
        line = line + "┬"
    return line


def make_table(data):
    labels = [label for label in data]
    rows = [[name, contact] for name, contact in zip(data["name"], data["contact"])]
    columnWidth = column_width_detect(rows, labels)
    table = first_line(columnWidth) + "\n"

    for i in range(len(labels)):
        table = table + "│" + str(labels[i]).center(columnWidth[i])
    table = table + "│\n" + label_last_line(columnWidth) + "\n"

    for i in range(len(rows)):
        for elementIndex in range(len(rows[i])):
            table = table + "│" + str(rows[i][elementIndex]).center(columnWidth[elementIndex])
        table = table + "│\n"
    table = table + last_line(columnWidth)

    return table
