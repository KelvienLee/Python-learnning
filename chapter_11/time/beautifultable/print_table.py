from beautifultable import BeautifulTable


table = BeautifulTable()
table.rows.append(["Jacob", 1, "boy"])
table.rows.append(["Isabella", 1, "girl"])
table.rows.append(["Ethan", 2, "boy"])
table.rows.append(["Sophia", 2, "girl"])
table.rows.append(["Michael", 3, "boy"])
table.rows.header = ["S1", "S2", "S3", "S4", "S5"]
table.columns.header = ["name", "rank", "gender"]
print(table)