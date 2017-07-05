import spec	# as in utils/mk-spec.py > mapzen/whosonfirst/languages/spec.py
import json

class language:

    def __init__(self, tag):

        self.tag = tag

        major, minor = tag.split("_x_")
        major = major.replace("_", "-")

        self.qualifier = minor

        parts = major.split("-")
        
        lang = parts[0]        
        lang = spec.__SPEC__["iso639"]["alpha3"].get(lang, None)

        if not lang:
            raise Exception, "Unrecognized language"

        self.macrolang = lang
        self.extlang = None

        if len(parts) > 1:

            subtag = "-".join(parts[1:])
            subtag = spec.__SPEC__["subtags"]["extlang"].get(subtag, None)

            if not subtag:
                raise Exception, "Unrecognized subtag"

            macro = subtag["Macrolanguage"]
            macro = spec.__SPEC__["iso639"]["alpha2"].get(macro, None)

            if not macro:
                raise Exception, "Unrecognizaed macrolanguage"

            if macro != self.macrolang["alpha3"]:
                raise Exception, "Invalid macrolanguage for extlang"

            self.subtag = subtag

    def __str__ (self):

        return json.dumps(self.macrolang) + "\n" + json.dumps(self.extlang)
            
            
        
