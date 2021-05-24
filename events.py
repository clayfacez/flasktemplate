from replit import db

# generate fake delivery order
id0 = "UBER12340000"
id2 = "UBER12340000"
id3 = "UBER12340000"
id4 = "UBER12340000"


# generate 'Zeke' tracking ID
zid0 = 82743636
zid1 = 82743638
zid2 = 82743639
zid3 = 82743640


# store both values in the database
db[id0] = zid0
db[id2] = zid1
db[id3] = zid2
db[id4] = zid3


# list database values
print(db.keys())
print(db["UBER12340000"])