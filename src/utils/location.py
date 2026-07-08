KENYA_LOCATIONS = {
    "kenya",
    "nairobi",
    "mombasa",
    "kisumu",
    "nakuru",
    "eldoret",
    "thika",
    "kiambu",
    "machakos",
    "nyeri",
    "meru",
    "kakamega",
}


def is_kenya_job(location: str) -> bool:
    """
    Returns True if the job location is in Kenya.
    """

    if not location:
        return False

    location = location.lower()

    return any(place in location for place in KENYA_LOCATIONS)