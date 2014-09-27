BEGIN { print "[" }
NR != 1 {print ","}
{
# STATES
#    print "{ \"model\": \"whsites.state\", \"pk\":", $1,", \"fields\": { \"name\": \"" $2 "\"  }}"

# SITES
    print "{\"pk\": " $1 ", \"model\": \"whsites.whsite\", \"fields\": { \"latitude\":" $4 ", \"state\":" $7 ", \"longitude\":" $5 ", \"name\": \"" $2 "\" , \"inscribed_date\":" $3 "}}"

}
END { print "]"}
