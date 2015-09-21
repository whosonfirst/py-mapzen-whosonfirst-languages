# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import sys
import logging
import requests
import json
import StringIO

class subtags:

    # https://tools.ietf.org/html/rfc5646
    # https://tools.ietf.org/html/rfc4647

    def __init__(self, url='https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry'):

        self.__source__ = url
        self.__registry__ = None

    def compile(self):

        records = self.to_json()
        compiled = {}

        for record in self.to_json():

            t = record.get('Type')
            st = record.get('Subtag')

            if not compiled.get(t, False):
                compiled[t] = {}

            compiled[t][st] = record

        return compiled

    def to_json(self):

        fh = self.load_registry()

        registry = []

        for record in self.parse_recordjar(fh):

            subtag = record.get('Subtag', None)
            
            if not subtag:
                continue

            yield record

    def load_registry(self):

        if not self.__registry__:

            rsp = requests.get(self.__source__)
            self.__registry__ = StringIO.StringIO()
            self.__registry__.write(rsp.content)

        self.__registry__.seek(0)
        return self.__registry__

    def parse_recordjar(self, fh):

        for stuff in fh.read().split('%%'):

            record = {}
            last = None

            for ln in stuff.split('\n'):

                ln = ln.strip()
            
                if ln == '':
                    continue

                try:

                    k, v = ln.split(':', 2)
                    k = k.strip()
                    v = v.strip()
                    
                    if k == 'Description':

                        descriptions = record.get(k, [])
                        descriptions.append(v)
                        record[k] = descriptions
                    
                    else:
                        record[k] = v

                    last = k

                except Exception, e:

                    if last == 'Description':
                        v = "%s %s" % (record[last][-1], ln)
                        record[last][-1] = v
                    else:
                        record[last] = "%s %s" % (record[last], ln)

            yield record

if __name__ == '__main__':

    import pprint

    r = subtags()
    print pprint.pformat(r.compile())
    
