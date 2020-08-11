import spec	# as in utils/mk-spec.py > mapzen/whosonfirst/languages/spec.py
import json

class language:

    def __init__(self, tag):

        self.tag = tag

        parts = tag.split("_x_")

        major = parts[0]
        minor = ""

        if len(parts) > 1:
            minor = parts[1]

        major = major.replace("_", "-")

        self.qualifier = minor

        parts = major.split("-")
        
        lang = parts[0]        
        lang = spec.__SPEC__["iso639"]["alpha3"].get(lang, None)

        if not lang:
            raise Exception("Unrecognized language")

        self.macrolang = lang
        self.region = None
        self.extlang = None

        if len(parts) > 1:

            region = parts[1]
            region = region.upper()

            region = spec.__SPEC__["subtags"]["region"].get(region, None)

            if not region:
                raise Exception("Unrecognized region")

            self.region = region

        if len(parts) > 2:

            extlang = parts[2:]

            extlang = spec.__SPEC__["subtags"]["extlang"].get(extlang, None)

            if not extlang:
                raise Exception("Unrecognized extlang")

            self.extlang = extlang

    def __str__ (self):

        possible = []
        label = []

        name = " ".join(self.macrolang["english"])
        possible.append(name)

        if self.region:
            region = " ".join(self.region["Description"])
            possible.append(region)

        # possible.append(self.qualifier)

        for p in possible:
            if p != "":
                label.append(p)

        return " ".join(label)
            
            
        
