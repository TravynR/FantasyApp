import streamlit as st

# Predefined list of players with their rankings and positions
players = [
    {"name": "Nikola Jokic", "positions": ["C"], "ranking": 1},
    {"name": "Victor Wembanyama", "positions": ["C"], "ranking": 2},
    {"name": "Luka Doncic", "positions": ["PG", "SG"], "ranking": 3},
    {"name": "Shai Gilgeous-Alexander", "positions": ["PG"], "ranking": 4},
    {"name": "Joel Embiid", "positions": ["C"], "ranking": 5},
    {"name": "Anthony Davis", "positions": ["PF", "C"], "ranking": 6},
    {"name": "Jayson Tatum", "positions": ["SF", "PF"], "ranking": 7},
    {"name": "Tyrese Haliburton", "positions": ["PG", "SG"], "ranking": 8},
    {"name": "Giannis Antetokounmpo", "positions": ["PF", "C"], "ranking": 9},
    {"name": "Trae Young", "positions": ["PG"], "ranking": 10},
    {"name": "Stephen Curry", "positions": ["PG", "SG"], "ranking": 11},
    {"name": "Donovan Mitchell", "positions": ["PG", "SG"], "ranking": 12},
    {"name": "Anthony Edwards", "positions": ["SG", "SF"], "ranking": 13},
    {"name": "Devin Booker", "positions": ["PG", "SG"], "ranking": 14},
    {"name": "Domantas Sabonis", "positions": ["C", "PF"], "ranking": 15},
    {"name": "James Harden", "positions": ["PG", "SG"], "ranking": 16},
    {"name": "Kevin Durant", "positions": ["SF", "PF"], "ranking": 17},
    {"name": "Damian Lillard", "positions": ["PG"], "ranking": 18},
    {"name": "Jalen Brunson", "positions": ["PG"], "ranking": 19},
    {"name": "Kyrie Irving", "positions": ["PG", "SG"], "ranking": 20},
    {"name": "LaMelo Ball", "positions": ["PG", "SG"], "ranking": 21},
    {"name": "Scottie Barnes", "positions": ["SG", "SF", "PF"], "ranking": 22},
    {"name": "LeBron James", "positions": ["SF", "PF"], "ranking": 23},
    {"name": "Chet Holmgren", "positions": ["PF", "C"], "ranking": 24},
    {"name": "Karl-Anthony Towns", "positions": ["PF", "C"], "ranking": 25},
    {"name": "Tyrese Maxey", "positions": ["PG", "SG"], "ranking": 26},
    {"name": "Lauri Markkanen", "positions": ["SF", "PF"], "ranking": 27},
    {"name": "De'Aaron Fox", "positions": ["PG"], "ranking": 28},
    {"name": "Paul George", "positions": ["SG", "SF", "PF"], "ranking": 29},
    {"name": "Fred VanVleet", "positions": ["PG"], "ranking": 30},
    {"name": "Ja Morant", "positions": ["PG"], "ranking": 31},
    {"name": "Dejounte Murray", "positions": ["PG", "SG"], "ranking": 32},
    {"name": "Alperen Sengun", "positions": ["C"], "ranking": 33},
    {"name": "Cade Cunningham", "positions": ["PG", "SG"], "ranking": 34},
    {"name": "Bam Adebayo", "positions": ["C"], "ranking": 35},
    {"name": "Kawhi Leonard", "positions": ["SG", "SF", "PF"], "ranking": 36},
    {"name": "DeMar DeRozan", "positions": ["PF", "SF"], "ranking": 37},
    {"name": "Evan Mobley", "positions": ["PF", "C"], "ranking": 38},
    {"name": "Jaren Jackson Jr.", "positions": ["PF", "C"], "ranking": 39},
    {"name": "Desmond Bane", "positions": ["SG", "SF"], "ranking": 40},
    {"name": "Jalen Williams", "positions": ["SG", "SF", "PF"], "ranking": 41},
    {"name": "Jimmy Butler", "positions": ["PF", "SF", "SG"], "ranking": 42},
    {"name": "Immanuel Quickley", "positions": ["PG", "SG"], "ranking": 43},
    {"name": "Jalen Johnson", "positions": ["PF"], "ranking": 44},
    {"name": "Paolo Banchero", "positions": ["SF", "PF"], "ranking": 45},
    {"name": "Derrick White", "positions": ["PG", "SG"], "ranking": 46},
    {"name": "Franz Wagner", "positions": ["PF", "SF"], "ranking": 47},
    {"name": "Jaylen Brown", "positions": ["SG", "SF"], "ranking": 48},
    {"name": "Jamal Murray", "positions": ["PG", "SG"], "ranking": 49},
    {"name": "Pascal Siakam", "positions": ["PF", "SF"], "ranking": 50},
    {"name": "Darius Garland", "positions": ["PG"], "ranking": 51},
    {"name": "Mikal Bridges", "positions": ["SG", "SF", "PF"], "ranking": 52},
    {"name": "Jarrett Allen", "positions": ["C"], "ranking": 53},
    {"name": "Myles Turner", "positions": ["C"], "ranking": 54},
    {"name": "Miles Bridges", "positions": ["SF", "PF"], "ranking": 55},
    {"name": "Zion Williamson", "positions": ["PF", "C"], "ranking": 56},
    {"name": "Tobias Harris", "positions": ["SF", "PF"], "ranking": 57},
    {"name": "Nikola Vucevic", "positions": ["PF", "C"], "ranking": 58},
    {"name": "Jalen Duren", "positions": ["C"], "ranking": 59},
    {"name": "Josh Giddey", "positions": ["PG", "SG", "SF"], "ranking": 60},
    {"name": "Cam Thomas", "positions": ["SG"], "ranking": 61},
    {"name": "Zach LaVine", "positions": ["SG", "SF"], "ranking": 62},
    {"name": "D'Angelo Russell", "positions": ["PG", "SG"], "ranking": 63},
    {"name": "Brandon Miller", "positions": ["SG", "SF"], "ranking": 64},
    {"name": "Deandre Ayton", "positions": ["C"], "ranking": 65},
    {"name": "Julius Randle", "positions": ["PF"], "ranking": 66},
    {"name": "Rudy Gobert", "positions": ["C"], "ranking": 67},
    {"name": "Tyler Herro", "positions": ["PG", "SG"], "ranking": 68},
    {"name": "Bradley Beal", "positions": ["PG", "SF", "SG"], "ranking": 69},
    {"name": "Austin Reaves", "positions": ["PG", "SG", "SF"], "ranking": 70},
    {"name": "Bogdan Bogdanovic", "positions": ["SG", "SF"], "ranking": 71},
    {"name": "Anfernee Simons", "positions": ["PG", "SG"], "ranking": 72},
    {"name": "Jrue Holiday", "positions": ["PG", "SG"], "ranking": 73},
    {"name": "Isaiah Hartenstein", "positions": ["C"], "ranking": 74},
    {"name": "Brandon Ingram", "positions": ["SG", "SF", "PF"], "ranking": 75},
    {"name": "Jabari Smith Jr.", "positions": ["PF", "C"], "ranking": 76},
    {"name": "Kyle Kuzma", "positions": ["SF", "PF"], "ranking": 77},
    {"name": "Jordan Poole", "positions": ["PG", "SG"], "ranking": 78},
    {"name": "Michael Porter Jr.", "positions": ["SF", "PF"], "ranking": 79},
    {"name": "Nic Claxton", "positions": ["C"], "ranking": 80},
    {"name": "OG Anunoby", "positions": ["SF", "PF"], "ranking": 81},
    {"name": "Keegan Murray", "positions": ["SF", "PF"], "ranking": 82},
    {"name": "Jalen Suggs", "positions": ["PG", "SG"], "ranking": 83},
    {"name": "Ivica Zubac", "positions": ["C"], "ranking": 84},
    {"name": "CJ McCollum", "positions": ["PG", "SG"], "ranking": 85},
    {"name": "Jonas Valanciunas", "positions": ["C"], "ranking": 86},
    {"name": "Coby White", "positions": ["PG", "SG"], "ranking": 87},
    {"name": "Alex Caruso", "positions": ["PG", "SG", "SF"], "ranking": 88},
    {"name": "Herbert Jones", "positions": ["SF", "PF"], "ranking": 89},
    {"name": "Devin Vassell", "positions": ["SG", "SF"], "ranking": 90},
    {"name": "Collin Sexton", "positions": ["PG", "SG"], "ranking": 91},
    {"name": "Jonathan Kuminga", "positions": ["PF", "SF"], "ranking": 92},
    {"name": "Terry Rozier", "positions": ["PG", "SG"], "ranking": 93},
    {"name": "Draymond Green", "positions": ["PF", "C"], "ranking": 94},
    {"name": "Naz Reid", "positions": ["PF", "C"], "ranking": 95},
    {"name": "Tyus Jones", "positions": ["PG"], "ranking": 96},
    {"name": "Jakob Poeltl", "positions": ["C"], "ranking": 97},
    {"name": "Brook Lopez", "positions": ["C"], "ranking": 98},
    {"name": "Trey Murphy III", "positions": ["PF", "SF", "SG"], "ranking": 99},
    {"name": "Jusuf Nurkic", "positions": ["C"], "ranking": 100},
    {"name": "Khris Middleton", "positions": ["SG", "SF"], "ranking": 101},
    {"name": "Amen Thompson", "positions": ["PF", "SF", "SG"], "ranking": 102},
    {"name": "Jalen Green", "positions": ["PG", "SG"], "ranking": 103},
    {"name": "Walker Kessler", "positions": ["C"], "ranking": 104},
    {"name": "Brandin Podziemski", "positions": ["SG"], "ranking": 105},
    {"name": "Mark Williams", "positions": ["C"], "ranking": 106},
    {"name": "Onyeka Okongwu", "positions": ["PF", "C"], "ranking": 107},
    {"name": "Mike Conley", "positions": ["PG"], "ranking": 108},
    {"name": "Klay Thompson", "positions": ["SG", "SF"], "ranking": 109},
    {"name": "Dereck Lively II", "positions": ["C"], "ranking": 110},
    {"name": "Chris Paul", "positions": ["PG"], "ranking": 111},
    {"name": "Marcus Smart", "positions": ["PG", "SG"], "ranking": 112},
    {"name": "John Collins", "positions": ["PF", "C"], "ranking": 113},
    {"name": "RJ Barrett", "positions": ["SG", "SF", "PF"], "ranking": 114},
    {"name": "Donte DiVincenzo", "positions": ["SG", "SF"], "ranking": 115},
    {"name": "Daniel Gafford", "positions": ["PF", "C"], "ranking": 116},
    {"name": "Keyonte George", "positions": ["PG", "SG"], "ranking": 117},
    {"name": "Bobby Portis Jr.", "positions": ["PF", "C"], "ranking": 118},
    {"name": "Josh Hart", "positions": ["SG", "SF", "PF"], "ranking": 119},
    {"name": "Cameron Johnson", "positions": ["SF", "PF"], "ranking": 120},
    {"name": "Buddy Hield", "positions": ["SG", "SF"], "ranking": 121},
    {"name": "Dennis Schroder", "positions": ["PG"], "ranking": 122},
    {"name": "Kristaps Porzingis", "positions": ["PF", "C"], "ranking": 123},
    {"name": "Malik Monk", "positions": ["SG", "SF"], "ranking": 124},
    {"name": "Trayce Jackson-Davis", "positions": ["PF", "C"], "ranking": 125},
    {"name": "Jerami Grant", "positions": ["SF", "PF"], "ranking": 126},
    {"name": "Norman Powell", "positions": ["SG", "SF"], "ranking": 127},
    {"name": "Deni Avdija", "positions": ["SF", "PF"], "ranking": 128},
    {"name": "P.J. Washington Jr.", "positions": ["PF"], "ranking": 129},
    {"name": "Grayson Allen", "positions": ["PG", "SG", "SF"], "ranking": 130},
    {"name": "Kentavious Caldwell-Pope", "positions": ["SG", "SF"], "ranking": 131},
    {"name": "Clint Capela", "positions": ["C"], "ranking": 132},
    {"name": "Aaron Gordon", "positions": ["PF", "C"], "ranking": 133},
    {"name": "Scoot Henderson", "positions": ["PG"], "ranking": 134},
    {"name": "Aaron Nesmith", "positions": ["SF", "PF"], "ranking": 135},
    {"name": "Shaedon Sharpe", "positions": ["SG", "SF"], "ranking": 136},
    {"name": "Jeremy Sochan", "positions": ["PF", "SF"], "ranking": 137},
    {"name": "Ausar Thompson", "positions": ["PF", "SF"], "ranking": 138},
    {"name": "Jaden Ivey", "positions": ["PG", "SG"], "ranking": 139},
    {"name": "Taylor Hendricks", "positions": ["SF", "PF"], "ranking": 140},
    {"name": "De'Anthony Melton", "positions": ["PG", "SG"], "ranking": 141},
    {"name": "Wendell Carter Jr.", "positions": ["C"], "ranking": 142},
    {"name": "Zach Edey", "positions": ["C"], "ranking": 143},
    {"name": "T.J. McConnell", "positions": ["PG"], "ranking": 144},
    {"name": "Gary Trent Jr.", "positions": ["PG", "SG"], "ranking": 145},
    {"name": "Al Horford", "positions": ["PF", "C"], "ranking": 146},
    {"name": "Max Strus", "positions": ["SG", "SF"], "ranking": 147},
    {"name": "Kelly Oubre Jr.", "positions": ["SF", "SG"], "ranking": 148},
    {"name": "Kelly Olynyk", "positions": ["PF", "C"], "ranking": 149},
    {"name": "Jaime Jaquez Jr.", "positions": ["SF", "SG"], "ranking": 150},
    {"name": "Tari Eason", "positions": ["SF", "PF"], "ranking": 151},
    {"name": "Andrew Nembhard", "positions": ["PG", "SG"], "ranking": 152},
    {"name": "Rui Hachimura", "positions": ["SF", "PF"], "ranking": 153},
    {"name": "Keldon Johnson", "positions": ["SG", "SF", "PF"], "ranking": 154},
    {"name": "Russell Westbrook III", "positions": ["PG"], "ranking": 155},
    {"name": "Malcolm Brogdon", "positions": ["PG", "SG"], "ranking": 156},
    {"name": "Andrew Wiggins", "positions": ["SF", "PF"], "ranking": 157},
    {"name": "Keon Ellis", "positions": ["SG", "SF"], "ranking": 158},
    {"name": "Alex Sarr", "positions": ["C", "PF"], "ranking": 159},
    {"name": "Jonathan Isaac", "positions": ["SF", "PF"], "ranking": 160},
    {"name": "Caris LeVert", "positions": ["SG", "SF"], "ranking": 161},
    {"name": "Dyson Daniels", "positions": ["PG", "SG"], "ranking": 162},
    {"name": "Terance Mann", "positions": ["SG", "SF"], "ranking": 163},
    {"name": "Ayo Dosunmu", "positions": ["PG", "SG", "SF"], "ranking": 164},
    {"name": "Nick Richards", "positions": ["C"], "ranking": 165},
    {"name": "Jordan Clarkson", "positions": ["SG", "SF"], "ranking": 166},
    {"name": "Jalen Smith", "positions": ["PF", "C"], "ranking": 167},
    {"name": "Luguentz Dort", "positions": ["SG", "SF"], "ranking": 168},
    {"name": "Tre Jones", "positions": ["PG"], "ranking": 169},
    {"name": "Jaden McDaniels", "positions": ["SF", "PF"], "ranking": 170},
    {"name": "Ben Simmons", "positions": ["PG", "PF"], "ranking": 171},
    {"name": "Corey Kispert", "positions": ["SG", "SF"], "ranking": 172},
    {"name": "Patrick Williams", "positions": ["PF"], "ranking": 173},
    {"name": "Vince Williams Jr.", "positions": ["PG", "SG", "SF", "PF"], "ranking": 174},
    {"name": "Bennedict Mathurin", "positions": ["SG", "SF"], "ranking": 175},
    {"name": "Noah Clowney", "positions": ["SF", "PF", "C"], "ranking": 176},
    {"name": "Payton Pritchard", "positions": ["PG"], "ranking": 177},
    {"name": "De'Andre Hunter", "positions": ["SF", "PF"], "ranking": 178},
    {"name": "Reed Sheppard", "positions": ["SG"], "ranking": 179},
    {"name": "Royce O'Neale", "positions": ["SF", "PF"], "ranking": 180},
    {"name": "Caleb Martin", "positions": ["SG", "SF", "PF"], "ranking": 181},
    {"name": "Kevin Porter Jr.", "positions": ["PG", "SG"], "ranking": 182},
    {"name": "Harrison Barnes", "positions": ["SF", "PF"], "ranking": 183},
    {"name": "Andre Drummond", "positions": ["C"], "ranking": 184},
    {"name": "Nickeil Alexander-Walker", "positions": ["SG", "SF"], "ranking": 185},
    {"name": "Nikola Jovic", "positions": ["C", "PF"], "ranking": 186},
    {"name": "Brandon Clarke", "positions": ["PF", "C"], "ranking": 187},
    {"name": "Cole Anthony", "positions": ["PG"], "ranking": 188},
    {"name": "Duncan Robinson", "positions": ["SG", "SF"], "ranking": 189},
    {"name": "Bojan Bogdanovic", "positions": ["SG", "SF", "PF"], "ranking": 190},
    {"name": "Kyle Lowry", "positions": ["PG"], "ranking": 191},
    {"name": "Gradey Dick", "positions": ["SG", "SF"], "ranking": 192},
    {"name": "Isaiah Jackson", "positions": ["PF", "C"], "ranking": 193},
    {"name": "Kyle Anderson", "positions": ["SF", "PF"], "ranking": 194},
    {"name": "Obi Toppin", "positions": ["PF"], "ranking": 195},
    {"name": "Mitchell Robinson", "positions": ["C"], "ranking": 196},
    {"name": "Christian Braun", "positions": ["SG", "SF"], "ranking": 197},
    {"name": "Miles McBride", "positions": ["PG", "SG"], "ranking": 198},
    {"name": "Dillon Brooks", "positions": ["SG", "SF"], "ranking": 199},
    {"name": "Zachcharie Risacher", "positions": ["PF", "SF"], "ranking": 200},
    {"name": "Daniel Theis", "positions": ["C"], "ranking": 201},
    {"name": "Josh Green", "positions": ["SG", "SF"], "ranking": 202},
    {"name": "Kevin Huerter", "positions": ["SG", "SF"], "ranking": 203},
    {"name": "Spencer Dinwiddie", "positions": ["PG", "SG"], "ranking": 204},
    {"name": "Malik Beasley", "positions": ["SG"], "ranking": 205},
    {"name": "Cason Wallace", "positions": ["PG", "SG"], "ranking": 206},
    {"name": "Jarred Vanderbilt", "positions": ["PF"], "ranking": 207},
    {"name": "Luke Kennard", "positions": ["SG"], "ranking": 208},
    {"name": "Matisse Thybulle", "positions": ["SG", "SF"], "ranking": 209},
    {"name": "Delon Wright", "positions": ["PG", "SG"], "ranking": 210},
    {"name": "Bruce Brown Jr.", "positions": ["SG", "SF"], "ranking": 211},
    {"name": "Marvin Bagley III", "positions": ["PF", "C"], "ranking": 212},
    {"name": "Zach Collins", "positions": ["PF", "C"], "ranking": 213},
    {"name": "Bilal Coulibaly", "positions": ["SG", "SF"], "ranking": 214},
    {"name": "Kris Dunn", "positions": ["PG", "SG"], "ranking": 215},
    {"name": "Rob Dillingham", "positions": ["PG"], "ranking": 216},
    {"name": "Stephon Castle", "positions": ["PG", "SG"], "ranking": 217},
    {"name": "Sam Hauser", "positions": ["SF", "PF"], "ranking": 218},
    {"name": "Donovan Clingan", "positions": ["C"], "ranking": 219},
    {"name": "Grant Williams", "positions": ["PF", "C"], "ranking": 220},
    {"name": "Carlton Carrington", "positions": ["PG", "SG"], "ranking": 221},
    {"name": "Josh Richardson", "positions": ["PG", "SG", "SF"], "ranking": 222},
    {"name": "Dorian Finney-Smith", "positions": ["SF", "PF", "C"], "ranking": 223},
    {"name": "Derrick Jones Jr.", "positions": ["SF", "PF"], "ranking": 224},
    {"name": "Robert Williams III", "positions": ["C"], "ranking": 225},
    {"name": "Karlo Matkovic", "positions": ["PF"], "ranking": 226},
    {"name": "Paul Reed", "positions": ["PF", "C"], "ranking": 227},
    {"name": "Isaiah Stewart", "positions": ["PF", "C"], "ranking": 228},
    {"name": "Moritz Wagner", "positions": ["PF", "C"], "ranking": 229},
    {"name": "Tre Mann", "positions": ["PG", "SG"], "ranking": 230},
    {"name": "Isaac Okoro", "positions": ["SG", "SF", "PF"], "ranking": 231},
    {"name": "Kel'el Ware", "positions": ["C"], "ranking": 232},
    {"name": "Eric Gordon", "positions": ["SG", "SF"], "ranking": 233},
    {"name": "Taurean Prince", "positions": ["SG", "SF"], "ranking": 234},
    {"name": "Larry Nance Jr.", "positions": ["PF", "C"], "ranking": 235},
    {"name": "Dalano Banton", "positions": ["PG", "SG", "SF"], "ranking": 236},
    {"name": "Julian Strawther", "positions": ["SF", "SG"], "ranking": 237},
    {"name": "Nicolas Batum", "positions": ["PF", "SF"], "ranking": 238},
    {"name": "Pat Connaughton", "positions": ["SG", "SF"], "ranking": 239},
    {"name": "Naji Marshall", "positions": ["SG", "SF"], "ranking": 240},
    {"name": "Reggie Jackson", "positions": ["PG", "SG"], "ranking": 241},
    {"name": "Moses Moody", "positions": ["SG", "SF"], "ranking": 242},
    {"name": "Ron Holland II", "positions": ["SF"], "ranking": 243},
    {"name": "Bones Hyland", "positions": ["PG", "SG"], "ranking": 244},
    {"name": "Isaiah Joe", "positions": ["PG", "SG"], "ranking": 245},
    {"name": "Tim Hardaway Jr.", "positions": ["SG", "SF"], "ranking": 246},
    {"name": "Peyton Watson", "positions": ["SF", "PF"], "ranking": 247},
    {"name": "Mason Plumlee", "positions": ["C"], "ranking": 248},
    {"name": "Georges Niang", "positions": ["SF", "PF"], "ranking": 249},
    {"name": "Brice Sensabaugh", "positions": ["SF", "PF"], "ranking": 250},
    {"name": "Cam Whitmore", "positions": ["SF", "PF"], "ranking": 251},
    {"name": "Matas Buzelis", "positions": ["SF", "PF"], "ranking": 252},
    {"name": "Lonzo Ball", "positions": ["PG"], "ranking": 253},
    {"name": "Saddiq Bey", "positions": ["SF", "PF"], "ranking": 254},
    {"name": "Jarace Walker", "positions": ["PF"], "ranking": 255},
    {"name": "Mo Bamba", "positions": ["C"], "ranking": 256},
    {"name": "Dalton Knecht", "positions": ["SG", "SF"], "ranking": 257},
    {"name": "Simone Fontecchio", "positions": ["SF", "PF"], "ranking": 258},
    {"name": "Jaden Hardy", "positions": ["PG", "SG"], "ranking": 259},
    {"name": "Santi Aldama", "positions": ["PF", "C"], "ranking": 260},
    {"name": "Neemias Queta", "positions": ["C"], "ranking": 261},
    {"name": "Quentin Grimes", "positions": ["SG", "SF"], "ranking": 262},
    {"name": "Davion Mitchell", "positions": ["PG", "SG"], "ranking": 263},
    {"name": "Precious Achiuwa", "positions": ["PF", "C"], "ranking": 264},
    {"name": "Marcus Sasser", "positions": ["PG"], "ranking": 265},
    {"name": "Jabari Walker", "positions": ["SF", "PF"], "ranking": 266},
    {"name": "Scotty Pippen Jr.", "positions": ["PG", "SG"], "ranking": 267},
    {"name": "Dario Saric", "positions": ["PF", "C"], "ranking": 268},
    {"name": "Aaron Wiggins", "positions": ["SG", "SF"], "ranking": 269},
    {"name": "GG Jackson II", "positions": ["SF", "PF"], "ranking": 270},
    {"name": "Day'Ron Sharpe", "positions": ["C"], "ranking": 271},
    {"name": "Anthony Black", "positions": ["PG", "SG", "SF"], "ranking": 272},
    {"name": "Christian Wood", "positions": ["PF", "C"], "ranking": 273},
    {"name": "Matas Buzelis-DUP", "positions": ["F"], "ranking": 274},
    {"name": "Gabe Vincent", "positions": ["PG", "SG"], "ranking": 275},
    {"name": "Duop Reath", "positions": ["C"], "ranking": 276},
    {"name": "Cam Reddish", "positions": ["SG", "SF"], "ranking": 277},
    {"name": "Julian Champagnie", "positions": ["PF", "SF"], "ranking": 278},
    {"name": "Luke Kornet", "positions": ["C"], "ranking": 279},
    {"name": "Jae'Sean Tate", "positions": ["SF", "PF"], "ranking": 280},
    {"name": "Tidjane Salaun", "positions": ["PF"], "ranking": 281},
    {"name": "Monte Morris", "positions": ["PG", "SG"], "ranking": 282},
    {"name": "Nassir Little", "positions": ["SF", "PF"], "ranking": 283},
    {"name": "Alec Burks", "positions": ["PG", "SG", "SF"], "ranking": 284},
    {"name": "AJ Griffin", "positions": ["SF", "PF"], "ranking": 285},
    {"name": "Amir Coffey", "positions": ["SG", "SF", "PF"], "ranking": 286},
    {"name": "Steven Adams", "positions": ["C"], "ranking": 287},
    {"name": "Maxi Kleber", "positions": ["PF", "C"], "ranking": 288},
    {"name": "Marcus Morris Sr.", "positions": ["PF", "C", "SF"], "ranking": 289},
    {"name": "Jaxson Hayes", "positions": ["PF", "C"], "ranking": 290},
    {"name": "Jose Alvarado", "positions": ["PG"], "ranking": 291},
    {"name": "Yves Missi", "positions": ["C"], "ranking": 292},
    {"name": "Trey Lyles", "positions": ["PF", "C"], "ranking": 293},
    {"name": "Vasilije Micic", "positions": ["PG", "SG"], "ranking": 294},
    {"name": "Jake LaRavia", "positions": ["SF", "PF"], "ranking": 295},
    {"name": "Sam Merrill", "positions": ["SG"], "ranking": 296},
    {"name": "Toumani Camara", "positions": ["SF", "PF"], "ranking": 297},
    {"name": "Goga Bitadze", "positions": ["C"], "ranking": 298},
    {"name": "Drew Eubanks", "positions": ["C"], "ranking": 299},
    {"name": "Dean Wade", "positions": ["SF", "PF"], "ranking": 300},
    {"name": "Cody Martin", "positions": ["SG", "SF"], "ranking": 301},
    {"name": "Cameron Payne", "positions": ["PG", "SG"], "ranking": 302},
    {"name": "Ben Sheppard", "positions": ["SG", "SF"], "ranking": 303},
    {"name": "Xavier Tillman Sr.", "positions": ["PF", "C"], "ranking": 304},
    {"name": "Jaylin Williams", "positions": ["PF", "C"], "ranking": 305},
    {"name": "Ziaire Williams", "positions": ["SG", "SF"], "ranking": 306},
    {"name": "Malaki Branham", "positions": ["PG", "SG"], "ranking": 307},
    {"name": "John Konchar", "positions": ["SG", "SF"], "ranking": 308},
    {"name": "Max Christie", "positions": ["SG", "SF"], "ranking": 309},
    {"name": "Ochai Agbaji", "positions": ["SG", "SF", "PF"], "ranking": 310},
    {"name": "Damion Lee", "positions": ["SG", "SF"], "ranking": 311},
    {"name": "Shake Milton", "positions": ["PG", "SG"], "ranking": 312},
    {"name": "Jordan Hawkins", "positions": ["SG"], "ranking": 313},
    {"name": "Cody Williams", "positions": ["SF", "SG"], "ranking": 314},
    {"name": "Kobe Bufkin", "positions": ["PG", "SG"], "ranking": 315},
    {"name": "Haywood Highsmith", "positions": ["SF", "PF"], "ranking": 316},
    {"name": "Joe Ingles", "positions": ["SG", "SF"], "ranking": 317},
    {"name": "Tobias Harris", "positions": ["SF", "PF"], "ranking": 318},
    {"name": "Jerami Grant", "positions": ["SF", "PF"], "ranking": 319},
    {"name": "Trey Murphy III", "positions": ["SF", "PF"], "ranking": 320}
]

# Collect lineup from user input
def collect_lineup(players):
    st.write("### Select Your Players:")
    player_names = [player["name"] for player in players]
    selected_players = st.multiselect("Choose players to add to your lineup:", player_names)

    my_player_info = []
    for player_name in selected_players:
        matched_player = next((player for player in players if player["name"].strip().lower() == player_name.strip().lower()), None)
        if matched_player:
            my_player_info.append(matched_player)
            st.success(f"Added: {player_name}")
    
    return my_player_info

# Find available players to draft
def available_players(players, best_player_ranking):
    try:
        best_player_ranking = int(best_player_ranking)
    except ValueError:
        st.error("Invalid ranking value. Please enter a number.")
        return []

    matched_player = next((player for player in players if int(player["ranking"]) == best_player_ranking), None)
    if matched_player:
        return [player for player in players if int(player["ranking"]) >= best_player_ranking]
    else:
        st.error("No matching players found.")
        return []

# Count positions of players
def count_positions(my_player_info):
    priority_list = {"C": 0, "SF": 0, "SG": 0, "PF": 0, "PG": 0}
    for player in my_player_info:
        positions = player["positions"]
        if isinstance(positions, list):
            for position in positions:
                position = position.strip().upper()
                if position in priority_list:
                    priority_list[position] += 1
        else:
            position = positions.strip().upper()
            if position in priority_list:
                priority_list[position] += 1
    return priority_list

# Suggest best players to draft based on needed positions
def best_players(priority_list, available_players):
    needed_positions = [position for position, count in priority_list.items() if count == 0]
    st.write("### Best Players to Draft:")

    if needed_positions:
        for position in needed_positions:
            st.write(f"**Top players for position {position}:**")
            position_players = [player for player in available_players if position in player["positions"]]
            position_players = sorted(position_players, key=lambda x: x['ranking'])[:3]
            for player in position_players:
                st.write(f"- {player['name']}")
    else:
        st.write("You have filled all required positions. Here are the top available players:")
        all_available_players = sorted(available_players, key=lambda x: x['ranking'])[:5]
        for player in all_available_players:
            st.write(f"- {player['name']}")

# Main function for Streamlit app
def main():
    st.title("🏀 Fantasy Draft Helper")
    st.sidebar.header("Player Selection")

    # Directly using the predefined list of players
    if players:
        my_player_info = collect_lineup(players)
        
        if my_player_info:
            priority_list = count_positions(my_player_info)
            best_player_ranking = st.sidebar.text_input("Enter the best available player ranking in your draft (1-316):", "")
            
            if st.sidebar.button("Find Available Players"):
                available_players_list = available_players(players, best_player_ranking)
                if available_players_list:
                    best_players(priority_list, available_players_list)
    else:
        st.error("No players data found.")

if __name__ == "__main__":
    main()
