import sys
import logging
import requests
import json
from io import StringIO

class iso639:

    # http://www.loc.gov/standards/iso639-2/ascii_8bits.html

    """
    These files may be used to download the list of language codes with their
    language names, for example into a database. To read the files, please note
    that one line of text contains one entry. An alpha-3 (bibliographic) code,
    an alpha-3 (terminologic) code (when given), an alpha-2 code (when given),
    an English name, and a French name of a language are all separated by pipe
    (|) characters. If one of these elements is not applicable to the entry, the
    field is left empty, i.e., a pipe (|) character immediately follows the
    preceding entry. The Line terminator is the LF character.
    """

    def __init__(self, source='http://www.loc.gov/standards/iso639-2/ISO-639-2_utf-8.txt'):
        self.__source__ = source
        self.__codes__ = None

    def compile(self):

        alpha2 = {}
        alpha3 = {}

        for codes in self.to_json():

            a2 = codes['alpha2']
            a3 = codes['alpha3']
            
            alpha3[a3] = codes
            
            if a2 != '':
                alpha2[a2] = codes
                
        return { 'alpha2': alpha2, 'alpha3': alpha3 }

    def to_json(self):
        
        fh = self.load_codes()
        
        for ln in fh.readlines():
            ln = ln.strip()

            alpha3, alpha3_term, alpha2, eng, fre = ln.split('|')

            eng = eng.split('; ')

            yield { 'alpha3': alpha3, 'alpha2': alpha2, 'english': eng }

    def load_codes(self):

        if not self.__codes__:

            rsp = requests.get(self.__source__)
            self.__codes__ = StringIO()
            self.__codes__.write(rsp.content)

        self.__codes__.seek(0)
        return self.__codes__
            
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

                except Exception as e:

                    if last == 'Description':
                        v = "%s %s" % (record[last][-1], ln)
                        record[last][-1] = v
                    else:
                        record[last] = "%s %s" % (record[last], ln)

            yield record

if __name__ == '__main__':

    import pprint

    r = iso639()
    print(pprint.pformat(r.compile()))
    
