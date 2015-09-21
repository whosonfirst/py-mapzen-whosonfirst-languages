# py-mapzen-whosonfirst-languages

Python tools for working with languages (specifically RFC5646) and Who's On First data

## Usage

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

* https://tools.ietf.org/html/rfc5646
* https://tools.ietf.org/html/rfc4647
* http://www.unicode.org/reports/tr35/
* http://www.loc.gov/standards/iso639-2/faq.html
* http://www.w3.org/International/articles/language-tags/
