# py-mapzen-whosonfirst-languages

Python tools for working with languages (specifically RFC5646) and Who's On First data

## Usage

### mapzen.whosonfirst.languages.iso639

```
import mapzen.whosonfirst.languages
import pprint

codes = mapzen.whosonfirst.languages.iso639()
print pprint.pformat(codes.compile())
```

This would print something like:

```
{'alpha2': {'aa': {'alpha2': 'aa',
                   'alpha3': '\xef\xbb\xbfaar',
                   'english': 'Afar'},
            'ab': {'alpha2': 'ab', 'alpha3': 'abk', 'english': 'Abkhazian'},
            'ae': {'alpha2': 'ae', 'alpha3': 'ave', 'english': 'Avestan'},
            'af': {'alpha2': 'af', 'alpha3': 'afr', 'english': 'Afrikaans'},
            'ak': {'alpha2': 'ak', 'alpha3': 'aka', 'english': 'Akan'},
            'am': {'alpha2': 'am', 'alpha3': 'amh', 'english': 'Amharic'},
	    # and so on...
 'alpha3': {'abk': {'alpha2': 'ab', 'alpha3': 'abk', 'english': 'Abkhazian'},
            'ace': {'alpha2': '', 'alpha3': 'ace', 'english': 'Achinese'},
            'ach': {'alpha2': '', 'alpha3': 'ach', 'english': 'Acoli'},
            'ada': {'alpha2': '', 'alpha3': 'ada', 'english': 'Adangme'},
            'ady': {'alpha2': '',
                    'alpha3': 'ady',
                    'english': 'Adyghe; Adygei'},
            'afa': {'alpha2': '',
                    'alpha3': 'afa',
                    'english': 'Afro-Asiatic languages'},
            # and so on...
```

### mapzen.whosonfirst.languages.subtags

```
import mapzen.whosonfirst.languages
import pprint

st = mapzen.whosonfirst.languages.subtags()
print pprint.pformat(st.compile())
```

This would print something like:

```
{'extlang': {'aao': {'Added': '2009-07-29',
                     'Description': ['Algerian Saharan Arabic'],
                     'Macrolanguage': 'ar',
                     'Preferred-Value': 'aao',
                     'Prefix': 'ar',
                     'Subtag': 'aao',
                     'Type': 'extlang'},
             'abh': {'Added': '2009-07-29',
                     'Description': ['Tajiki Arabic'],
                     'Macrolanguage': 'ar',
                     'Preferred-Value': 'abh',
                     'Prefix': 'ar',
                     'Subtag': 'abh',
                     'Type': 'extlang'},

             # and so on...		     
```

## See also

* http://www.w3.org/International/articles/language-tags/
* http://www.iso.org/iso/home/standards/language_codes.htm
* https://tools.ietf.org/html/rfc5646
* https://tools.ietf.org/html/rfc4647
* http://www.loc.gov/standards/iso639-2/faq.html
* http://www.unicode.org/reports/tr35/
