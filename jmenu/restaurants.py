from collections import namedtuple

Restaurant = namedtuple("Restaurant", ["name", "url"])

RESTAURANTS = [
    Restaurant("Foobar", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=84"),
    Restaurant("Foodoo", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=89"),
    Restaurant("Kastari", "https://fi.jamix.cloud/apps/menu/?anro=95663&k=5&mt=2"),
    Restaurant("Kylmä", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=92"),
    Restaurant("Mara", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=49&mt=111"),
    Restaurant("Napa", "https://fi.jamix.cloud/apps/menu/?anro=93077&k=48&mt=79"),
]
