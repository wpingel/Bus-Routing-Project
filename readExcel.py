from pyexcel_xlsx import get_data
data = get_data("new.xlsx")
import json
print(json.dumps(data))
