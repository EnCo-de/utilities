file_name = "large_dataset.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)

# figure out the average amount raised per company in a series A round
def get_series_a():
    n = 0
    for company_dict in company_dicts:
        if company_dict["round"] == "a":
            n += 1
            yield int(company_dict["raisedAmt"])
    return n

company_count = 0
def get_funding():
    global company_count
    company_count = yield from get_series_a()

funding = get_funding()
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a:_}")
print(f"Average series A fundraising: ${total_series_a/company_count:,}")
