from flask import Flask, render_template

app = Flask(__name__, static_folder=".", static_url_path="")

TEAM_MEMBERS = [
    {
        "name": "Prof. Lantao Liu",
        "image": "Media/lantao.jpg",
        "degree": "Faculty advisor, VAIL Lab",
        "bio": "Leading research in robotics and autonomous systems at Indiana University.",
    },
    {
        "name": "Evan Klimes",
        "image": "Media/evan-klimes.jpg",
        "degree": "B.S. in Informatics",
        "bio": "Building software and systems for the autonomous racing stack.",
    },
    {
        "name": "Dawson Schroeder",
        "image": "Media/dawson-schroeder.jpg",
        "degree": "B.S. in Intelligent Systems Engineering",
        "bio": "???",
    },
    {
        "name": "Alex Johnson",
        "image": "Media/alex-johnson.jpg",
        "degree": "B.S. in Computer Science",
        "bio": "I enjoy drifting cars because sometimes the fastest way through life's turns is sideways with a little tire smoke and questionable decision-making.",
    },
    {
        "name": "Anmol Munnolli",
        "image": "Media/anmol-munnolli.jpg",
        "degree": "M.S. in Computer Science",
        "bio": "Focus on perception, planning, and bringing ideas to the track.",
    },
    {
        "name": "Harrison Carter",
        "image": "Media/harrison-carter.png",
        "degree": "B.S. in Data Science",
        "bio": "Turning telemetry and models into actionable insight for the team.",
    },
    {
        "name": "Reed Turgeon",
        "image": "Media/reed-turgeon.jpg",
        "degree": "M.S. in Data Science",
        "bio": "Engineering leader and full stack developer with experience building web applications, managing technical teams, and solving business problems with software.",
    },
    {
        "name": "Jack DeWitt",
        "image": "Media/jack-dewitt.jpg",
        "degree": "B.S. in Informatics",
        "bio": "Contributing to IU LART across software and race operations.",
    },
    {
        "name": "Nilambar Halder Tonmoy",
        "image": "Media/nilambar-halder-tonmoy.jpg",
        "degree": "Ph.D. in Computer Science",
        "bio": "Advancing research at the intersection of autonomy and intelligent systems.",
    },
    {
        "name": "Vivek Reddy Munnangi",
        "image": "Media/vivek-reddy-munnangi.jpg",
        "degree": "M.S. in Computational Science",
        "bio": "Applying computational methods to autonomous racing challenges.",
    },
    {
        "name": 'James "Andrew" Sampson',
        "image": "Media/james-andrew-sampson.jpg",
        "degree": "B.S. in Informatics",
        "bio": "Supporting the team through software and integration work.",
    },
    {
        "name": "Anooshka Bajaj",
        "image": "Media/anooshka-bajaj.jpg",
        "degree": "M.S. in Data Science",
        "bio": "Data-driven approaches to performance and strategy.",
    },
    {
        "name": "Rodion Starostin",
        "image": "Media/rodion-starostin.jpg",
        "degree": "B.S. in Finance and Accounting",
        "bio": "Bridging operations, sponsorship, and team logistics.",
    },
    {
        "name": "Shreyaj Kankipati",
        "image": "Media/shreyaj-kankipati.jpg",
        "degree": "B.S. in Intelligent Systems Engineering",
        "bio": "Intelligent systems and control for autonomous platforms.",
    },
    {
        "name": "Charlie Nicholson",
        "image": "Media/charlie-nicholson.jpg",
        "degree": "B.S. in Data Science and M.S. in Data Science",
        "bio": "Dual focus on data science foundations and graduate applications.",
    },
    {
        "name": "Manav Malviya",
        "image": "Media/manav-malviya.jpg",
        "degree": "B.S. in Computer Science",
        "bio": "Software and systems for autonomous racing.",
    },
    {
        "name": "Joshua Butler",
        "image": "Media/joshua-butler.jpg",
        "degree": "B.S. in Computer Science",
        "bio": "Contributing to development across the autonomy stack.",
    },
    {
        "name": "Ahmad Abdullahi",
        "image": "Media/ahmad-abdullahi.jpg",
        "degree": "B.S. in Informatics",
        "bio": "Informatics and human-centered computing in motorsport.",
    },
]


@app.route("/about.html")
def about():
    return render_template("about.html", team_members=TEAM_MEMBERS)
