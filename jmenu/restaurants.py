from collections import namedtuple

Restaurant = namedtuple("Restaurant", ["name", "main", "soup"])

RESTAURANTS = [
    Restaurant(
        "Foobar",
        "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=84",
        "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=82",
    ),
    Restaurant(
        "Foodoo",
        "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=89",
        "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=86",
    ),
    Restaurant(
        "Kastari", "https://fi.jamix.cloud/apps/menu/?anro=95663&k=5&mt=2", None
    ),
    Restaurant(
        "Kylmä", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=92", None
    ),
    Restaurant(
        "Mara",
        "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=111",
        "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=51",
    ),
    Restaurant("Napa", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=79", None),
]
