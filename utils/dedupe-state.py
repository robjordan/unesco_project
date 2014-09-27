import sys, json

j_in = json.load(sys.stdin)
j_out = []
pk = {}
xlate = {}

for line in j_in:
    if line["model"] == "whsites.state":
        if line["fields"]["name"] not in pk:
            pk[line["fields"]["name"]] = str(line["pk"])
            xlate[line["pk"]] = int(line["pk"])
            j_out.append(line)
        else: 
            xlate[line["pk"]] = int(pk[line["fields"]["name"]])

for line in j_in:
    if line["model"] == "whsites.whsite":
        line["fields"]["state"] = xlate[line["fields"]["state"]]
        j_out.append(line)

print json.dumps(j_out)
