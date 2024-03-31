file_name = "large_dataset.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)

avg = {}
n = {}
for company_dict in company_dicts:
    if company_dict["round"] == "a":
        avg[company_dict["company"]] = avg.get(company_dict["company"], 0) + int(company_dict["raisedAmt"])
        n[company_dict["company"]] = n.get(company_dict["company"], 0) + 1
avg[company_dict["company"]] /= n.get(company_dict["company"])

for e in avg:
    print(f"Total series A fundraising: {e} ${avg[e]}")

# figure out the average amount raised per company in a series A round

