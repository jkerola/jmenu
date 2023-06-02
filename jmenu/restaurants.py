from collections import namedtuple

Restaurant = namedtuple("Restaurant", ["name", "url"])
Marking = namedtuple("Marking", ["letters", "explanation"])
RESTAURANTS = [
    Restaurant("Foobar", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=84"),
    Restaurant("Foodoo", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=89"),
    Restaurant("Kastari", "https://fi.jamix.cloud/apps/menu/?anro=95663&k=5&mt=2"),
    Restaurant("Kylmä", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=92"),
    Restaurant("Mara", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=111"),
    Restaurant("Napa", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=79"),
]

MARKINGS = [
    Marking("G", "Gluteeniton"),
    Marking("M", "Maidoton"),
    Marking("L", "Laktoositon"),
    Marking("SO", "Sisältää soijaa"),
    Marking("SE", "Sisältää selleriä"),
    Marking("MU", "Munaton"),
    Marking("[S], *", "Kelan korkeakouluruokailunsuosituksen mukainen"),
    Marking("SIN", "Sisältää sinappia"),
    Marking("<3", "Sydänmerkki"),
    Marking("VEG", "Vegaani"),
]
