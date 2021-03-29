
EXPERIMENTS = {
    "xenonnt": {
        "url_prefix": "",
        "name_suffix": "",
        "mongo_prefix": "MONGO",
        "detectors":  ["tpc", "nveto", "muveto"],
    },
    "xenon1t": {
        "url_prefix": "xenon1t",
        "name_suffix": "1t",
        "mongo_prefix": "MONGO",
        "detectors": ["tpc", "muveto"],
    },
}

INCLUDE_AS_IS = ["accounts",]