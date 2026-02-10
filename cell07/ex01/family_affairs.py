#!/usr/bin/env python3

def find_the_redheads(family):
    def is_red(name):
        return family[name] == "red"

    return list(filter(is_red, family.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
