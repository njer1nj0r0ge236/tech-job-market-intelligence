KENYA_KEYWORDS = {
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

ALLOWED_REMOTE = {
    "worldwide",
    "global",
    "anywhere",

    "remote worldwide",
    "remote (worldwide)",

    "remote global",
    "remote (global)",

    "remote africa",
    "remote-africa",
    "remote (africa)",

    "remote emea",
    "remote-emea",
    "remote (emea)",
}

BLOCKED_REGIONS = {
    "united states",
    "usa",
    "us only",

    "canada",

    "latin america",
    "latam",

    "germany",
    "france",
    "italy",
    "spain",

    "united kingdom",
    "uk only",

    "india",
    "japan",
    "singapore",

    "australia",
    "new zealand",
}


def is_kenya_job(location: str) -> bool:

    if not location:
        return False

    location = location.lower().strip()

    # Kenya always passes
    if any(k in location for k in KENYA_KEYWORDS):
        return True

    # Block known restricted regions
    if any(region in location for region in BLOCKED_REGIONS):
        return False

    # Explicit global/EMEA/Africa remote
    if any(remote in location for remote in ALLOWED_REMOTE):
        return True

    # Plain "Remote"
    if location == "remote":
        return True

    return False