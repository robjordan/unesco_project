import sys, json

j_in = json.load(sys.stdin)
j_out = []

for line in j_in:
    if line["model"] == "whsites.state":
#        print line
        states = set(str(line["fields"]["name"]).split(","))
        new_name = ','.join(str(x) for x in states)
        line["fields"]["name"] = new_name

    j_out.append(line)

print json.dumps(j_out)




#        print "{\"pk\": " line["fields"]["pk"] ", \"model\": \"whsites.state\", \"fields\": {\"name\": " new_name "}}"

