import urllib.request
import xmltodict
import json

states={
'ad': {'name': 'Andorra'},
'ae': {'name': 'United Arab Emirates'},
'af': {'name': 'Afghanistan'},
'ag': {'name': 'Antigua and Barbuda'},
'ai': {'name': 'Anguilla'},
'al': {'name': 'Albania'},
'am': {'name': 'Armenia'},
'ao': {'name': 'Angola'},
'aq': {'name': 'Antarctica'},
'ar': {'name': 'Argentina'},
'as': {'name': 'American Samoa'},
'at': {'name': 'Austria'},
'au': {'name': 'Australia'},
'aw': {'name': 'Aruba'},
'ax': {'name': 'Aland Islands'},
'az': {'name': 'Azerbaijan'},
'ba': {'name': 'Bosnia and Herzegovina'},
'bb': {'name': 'Barbados'},
'bd': {'name': 'Bangladesh'},
'be': {'name': 'Belgium'},
'bf': {'name': 'Burkina Faso'},
'bg': {'name': 'Bulgaria'},
'bh': {'name': 'Bahrain'},
'bi': {'name': 'Burundi'},
'bj': {'name': 'Benin'},
'bl': {'name': 'Saint Bartholemy'},
'bm': {'name': 'Bermuda'},
'bn': {'name': 'Brunei Darussalam'},
'bo': {'name': 'Bolivia'},
'bq': {'name': 'Caribbean Netherlands '},
'br': {'name': 'Brazil'},
'bs': {'name': 'Bahamas'},
'bt': {'name': 'Bhutan'},
'bv': {'name': 'Bouvet Island'},
'bw': {'name': 'Botswana'},
'by': {'name': 'Belarus'},
'bz': {'name': 'Belize'},
'ca': {'name': 'Canada'},
'cc': {'name': 'Cocos (Keeling) Islands'},
'cd': {'name': 'Congo, Democratic Republic of'},
'cf': {'name': 'Central African Republic'},
'cg': {'name': 'Congo'},
'ch': {'name': 'Switzerland'},
'ci': {'name': "Cote d'Ivoire"},
'ck': {'name': 'Cook Islands'},
'cl': {'name': 'Chile'},
'cm': {'name': 'Cameroon'},
'cn': {'name': 'China'},
'co': {'name': 'Colombia'},
'cr': {'name': 'Costa Rica'},
'cu': {'name': 'Cuba'},
'cv': {'name': 'Cape Verde'},
'cw': {'name': 'Curacao'},
'cx': {'name': 'Christmas Island'},
'cy': {'name': 'Cyprus'},
'cz': {'name': 'Czech Republic'},
'de': {'name': 'Germany'},
'dj': {'name': 'Djibouti'},
'dk': {'name': 'Denmark'},
'dm': {'name': 'Dominica'},
'do': {'name': 'Dominican Republic'},
'dz': {'name': 'Algeria'},
'ec': {'name': 'Ecuador'},
'ee': {'name': 'Estonia'},
'eg': {'name': 'Egypt'},
'eh': {'name': 'Western Sahara'},
'er': {'name': 'Eritrea'},
'es': {'name': 'Spain'},
'et': {'name': 'Ethiopia'},
'fi': {'name': 'Finland'},
'fj': {'name': 'Fiji'},
'fk': {'name': 'Falkland Islands'},
'fm': {'name': 'Micronesia, Federated States of'},
'fo': {'name': 'Faroe Islands'},
'fr': {'name': 'France'},
'ga': {'name': 'Gabon'},
'gb': {'name': 'United Kingdom'},
'gd': {'name': 'Grenada'},
'ge': {'name': 'Georgia'},
'gf': {'name': 'French Guiana'},
'gg': {'name': 'Guernsey'},
'gh': {'name': 'Ghana'},
'gi': {'name': 'Gibraltar'},
'gl': {'name': 'Greenland'},
'gm': {'name': 'Gambia'},
'gn': {'name': 'Guinea'},
'gp': {'name': 'Guadeloupe'},
'gq': {'name': 'Equatorial Guinea'},
'gr': {'name': 'Greece'},
'gs': {'name': 'South Georgia and the South Sandwich Islands'},
'gt': {'name': 'Guatemala'},
'gu': {'name': 'Guam'},
'gw': {'name': 'Guinea-Bissau'},
'gy': {'name': 'Guyana'},
'hk': {'name': 'Hong Kong'},
'hm': {'name': 'Heard and McDonald Islands'},
'hn': {'name': 'Honduras'},
'hr': {'name': 'Croatia'},
'ht': {'name': 'Haiti'},
'hu': {'name': 'Hungary'},
'id': {'name': 'Indonesia'},
'ie': {'name': 'Ireland'},
'il': {'name': 'Israel'},
'im': {'name': 'Isle of Man'},
'in': {'name': 'India'},
'io': {'name': 'British Indian Ocean Territory'},
'iq': {'name': 'Iraq'},
'ir': {'name': 'Iran'},
'is': {'name': 'Iceland'},
'it': {'name': 'Italy'},
'je': {'name': 'Jersey'},
'jm': {'name': 'Jamaica'},
'jo': {'name': 'Jordan'},
'jp': {'name': 'Japan'},
'ke': {'name': 'Kenya'},
'kg': {'name': 'Kyrgyzstan'},
'kh': {'name': 'Cambodia'},
'ki': {'name': 'Kiribati'},
'km': {'name': 'Comoros'},
'kn': {'name': 'Saint Kitts and Nevis'},
'kp': {'name': 'North Korea'},
'kr': {'name': 'South Korea'},
'kw': {'name': 'Kuwait'},
'ky': {'name': 'Cayman Islands'},
'kz': {'name': 'Kazakhstan'},
'la': {'name': "Lao People's Democratic Republic"},
'lb': {'name': 'Lebanon'},
'lc': {'name': 'Saint Lucia'},
'li': {'name': 'Liechtenstein'},
'lk': {'name': 'Sri Lanka'},
'lr': {'name': 'Liberia'},
'ls': {'name': 'Lesotho'},
'lt': {'name': 'Lithuania'},
'lu': {'name': 'Luxembourg'},
'lv': {'name': 'Latvia'},
'ly': {'name': 'Libya'},
'ma': {'name': 'Morocco'},
'mc': {'name': 'Monaco'},
'md': {'name': 'Moldova'},
'me': {'name': 'Montenegro'},
'mf': {'name': 'Saint-Martin (France)'},
'mg': {'name': 'Madagascar'},
'mh': {'name': 'Marshall Islands'},
'mk': {'name': 'Macedonia'},
'ml': {'name': 'Mali'},
'mm': {'name': 'Myanmar'},
'mn': {'name': 'Mongolia'},
'mo': {'name': 'Macau'},
'mp': {'name': 'Northern Mariana Islands'},
'mq': {'name': 'Martinique'},
'mr': {'name': 'Mauritania'},
'ms': {'name': 'Montserrat'},
'mt': {'name': 'Malta'},
'mu': {'name': 'Mauritius'},
'mv': {'name': 'Maldives'},
'mw': {'name': 'Malawi'},
'mx': {'name': 'Mexico'},
'my': {'name': 'Malaysia'},
'mz': {'name': 'Mozambique'},
'na': {'name': 'Namibia'},
'nc': {'name': 'New Caledonia'},
'ne': {'name': 'Niger'},
'nf': {'name': 'Norfolk Island'},
'ng': {'name': 'Nigeria'},
'ni': {'name': 'Nicaragua'},
'nl': {'name': 'The Netherlands'},
'no': {'name': 'Norway'},
'np': {'name': 'Nepal'},
'nr': {'name': 'Nauru'},
'nu': {'name': 'Niue'},
'nz': {'name': 'New Zealand'},
'om': {'name': 'Oman'},
'pa': {'name': 'Panama'},
'pe': {'name': 'Peru'},
'pf': {'name': 'French Polynesia'},
'pg': {'name': 'Papua New Guinea'},
'ph': {'name': 'Philippines'},
'pk': {'name': 'Pakistan'},
'pl': {'name': 'Poland'},
'pm': {'name': 'St. Pierre and Miquelon'},
'pn': {'name': 'Pitcairn'},
'pr': {'name': 'Puerto Rico'},
'ps': {'name': 'Palestine, State of'},
'pt': {'name': 'Portugal'},
'pw': {'name': 'Palau'},
'py': {'name': 'Paraguay'},
'qa': {'name': 'Qatar'},
're': {'name': 'Reunion'},
'ro': {'name': 'Romania'},
'rs': {'name': 'Serbia'},
'ru': {'name': 'Russian Federation'},
'rw': {'name': 'Rwanda'},
'sa': {'name': 'Saudi Arabia'},
'sb': {'name': 'Solomon Islands'},
'sc': {'name': 'Seychelles'},
'sd': {'name': 'Sudan'},
'se': {'name': 'Sweden'},
'sg': {'name': 'Singapore'},
'sh': {'name': 'Saint Helena'},
'si': {'name': 'Slovenia'},
'sj': {'name': 'Svalbard and Jan Mayen Islands'},
'sk': {'name': 'Slovakia'},
'sl': {'name': 'Sierra Leone'},
'sm': {'name': 'San Marino'},
'sn': {'name': 'Senegal'},
'so': {'name': 'Somalia'},
'sr': {'name': 'Suriname'},
'ss': {'name': 'South Sudan'},
'st': {'name': 'Sao Tome and Principe'},
'sv': {'name': 'El Salvador'},
'sx': {'name': 'Sint Maarten (Dutch part)'},
'sy': {'name': 'Syria'},
'sz': {'name': 'Swaziland'},
'tc': {'name': 'Turks and Caicos Islands'},
'td': {'name': 'Chad'},
'tf': {'name': 'French Southern Territories'},
'tg': {'name': 'Togo'},
'th': {'name': 'Thailand'},
'tj': {'name': 'Tajikistan'},
'tk': {'name': 'Tokelau'},
'tl': {'name': 'Timor-Leste'},
'tm': {'name': 'Turkmenistan'},
'tn': {'name': 'Tunisia'},
'to': {'name': 'Tonga'},
'tr': {'name': 'Turkey'},
'tt': {'name': 'Trinidad and Tobago'},
'tv': {'name': 'Tuvalu'},
'tw': {'name': 'Taiwan'},
'tz': {'name': 'Tanzania'},
'ua': {'name': 'Ukraine'},
'ug': {'name': 'Uganda'},
'um': {'name': 'United States Minor Outlying Islands'},
'us': {'name': 'United States'},
'uy': {'name': 'Uruguay'},
'uz': {'name': 'Uzbekistan'},
'va': {'name': 'Vatican'},
'vc': {'name': 'Saint Vincent and the Grenadines'},
've': {'name': 'Venezuela'},
'vg': {'name': 'Virgin Islands (British)'},
'vi': {'name': 'Virgin Islands (U.S.)'},
'vn': {'name': 'Vietnam'},
'vu': {'name': 'Vanuatu'},
'wf': {'name': 'Wallis and Futuna Islands'},
'ws': {'name': 'Samoa'},
'ye': {'name': 'Yemen'},
'yt': {'name': 'Mayotte'},
'za': {'name': 'South Africa'},
'zm': {'name': 'Zambia'},
'zw': {'name': 'Zimbabwe'}
}


categories = {}
sites = {}
regions = {}
model = []
pk = 0

xmldata = urllib.request.urlopen('http://whc.unesco.org/en/list/xml').read()
# xmldata = open('/home/jordan/django/unesco_project/data/xml').read()
doc = xmltodict.parse(xmldata)
row = doc["query"]["row"][0]

# Load a dict with all States and ISO codes and give each a private key
pk = 0
for i in states:
    pk += 1
    states[i]["pk"] = pk

    # Create the model for states
    element = {}
    fields = {}
    element["model"] = "sites.state"
    fields["name"] = states[i]["name"]
    fields["iso_code"] = i
    element["fields"] = fields
    element["pk"] = pk
    model.append(element)

# Load a dict with all Categories and give each a private key
pk = 0
for row in doc["query"]["row"]:
    if row["category"] not in categories:
        pk += 1
        categories[row["category"]] = pk

        # create the model for categories
        element = {}
        fields = {}
        element["model"] = "sites.category"
        fields["name"] = row["category"]
        element["fields"] = fields
        element["pk"] = pk
        model.append(element)

# Load a dict with all Regions and give each a private key
pk = 0
for row in doc["query"]["row"]:
    if row["region"] not in regions:
        pk += 1
        regions[row["region"]] = pk

        # create the model for regions
        element = {}
        fields = {}
        element["model"] = "sites.region"
        fields["name"] = row["region"]
        element["fields"] = fields
        element["pk"] = pk
        model.append(element)

# Finally load all of the sites with corresponding state, category and region
pk = 0
for row in doc["query"]["row"]:
    pk += 1

    # create the model for sites
    element = {}
    fields = {}
    element["model"] = "sites.whsite"
    fields["category"] = categories[row["category"]]
    fields["id_number"] = row["id_number"]
    fields["short_description"] = row["short_description"]
    fields["name"] = row["site"]
    fields["slug"] = str(hash(row["site"]))
    if row["justification"]:
        fields["justification"] = row["justification"]
    fields["http_url"] = row["http_url"]
    fields["longitude"] = row["longitude"]
    fields["image_url"] = row["image_url"]
    fields["inscribed_date"] = row["date_inscribed"]
    fields["latitude"] = row["latitude"]
    fields["region"] = regions[row["region"]]

    fields["states"] = []
    for iso in set(str(row["iso_code"]).split(",")):
        if iso in states:
            # print("iso:", iso)
            # print("states[iso]:", states[iso])
            fields["states"].append(states[iso]["pk"])

    element["fields"] = fields
    element["pk"] = pk
    model.append(element)


print (json.dumps(model))

#print(regions)





