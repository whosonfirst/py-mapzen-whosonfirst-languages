#!/usr/bin/env python

import sys
import json
import datetime
import mapzen.whosonfirst.languages.utils

if __name__ == "__main__":

	codes = mapzen.whosonfirst.languages.utils.iso639()
        subtags = mapzen.whosonfirst.languages.utils.subtags()

        spec = {
                'iso639': codes.compile(),
                'subtags': subtags.compile()
        }
        
        now = datetime.datetime.utcnow().isoformat()
        
        fh = sys.stdout
        
        fh.write("# This file was generated by robots (%s) at %s\n\n" % ("utils/mk-spec.py", now))
        fh.write("__SPEC__ = %s" % json.dumps(spec))
        
        sys.exit(0)
