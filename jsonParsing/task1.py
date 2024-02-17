import json
with open('sample-data.json') as f:
	data = json.load(f)
dnList=[
    {
        "dn":"",
        "speed":"",
        "mtu":"",
        "descr":""
    },
{
        "dn":"",
        "speed":"",
        "mtu":"",
        "descr":""
    },
{
        "dn":"",
        "speed":"",
        "mtu":"",
        "descr":""
    }
]
count=0
for n in range(33, 36):
    for x in data["imdata"]:
        if x["l1PhysIf"]["attributes"]["dn"] == f"topology/pod-1/node-201/sys/phys-[eth1/{n}]":
            dnList[n-33]["dn"]=x["l1PhysIf"]["attributes"]["dn"]
            dnList[n-33]["speed"]=x["l1PhysIf"]["attributes"]["speed"]
            dnList[n-33]["mtu"]=x["l1PhysIf"]["attributes"]["mtu"]
            dnList[n-33]["descr"]=x["l1PhysIf"]["attributes"]["descr"]
print("Interface Status")
print("=" * 160)
print("{:<70} {:<50} {:<16} {:<16}".format("DN", "Description", "Speed", "MTU"))
print("-" * 160)
for x in dnList:
    print("{:<70} {:<50} {:<16} {:<16}".format(x["dn"], x["descr"], x["speed"], x["mtu"]))