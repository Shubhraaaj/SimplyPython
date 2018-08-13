from geopy.geocoders import Nominatim
import pandas
nom=Nominatim()
# a = nom.geocode("Jharia, Dhanbad, Jharkhand, India")
# print(str(a.latitude) + ", " + str(a.longitude))

df1 = pandas.read_excel("expenses.xlsx")
df1["COORDINATES"] = df1["LOCATION"].apply(nom.geocode)
print(df1)
