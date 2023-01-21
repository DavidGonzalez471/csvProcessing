import pandas as pd

names = {}

data = pd.read_csv("C:/Users/Sexy/Downloads/AmazonItems.csv", usecols=("Shipping Address Name", "Total Charged"))
data['Total Charged'] = data["Total Charged"].str.replace('$', '', regex=True)
data["Total Charged"].astype('float')

for n in data["Shipping Address Name"]:
    names[n] = 1 + names.get(n,0)

for n in names:

    filtered_data = data[data["Shipping Address Name"].str.contains(n)]
    sum = (filtered_data["Total Charged"].astype('float')).sum()
    print("%s ordered %d times for a total of: %.2f" % (n, names[n], sum))
    

