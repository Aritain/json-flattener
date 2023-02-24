# Json flattener
Honestly I have no clue how to name it

Basically this small script transforms pure JSONs like this one:

```
{
    "header": "true",
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup",
                    "ExtraField": [   
                        { "firstName" : "John",  
                          "lastName"  : "Doe",
                          "age"       : 23 },
                        { "firstName" : "Mary",  
                          "lastName"  : "Smith",
                           "age"      : 32 },
                        { "firstName" : "Bob",  
                          "lastName"  : "Dole",
                           "age"      : 45 }
                    ] 
                }
            }
        }
    }
}
```

To something like this

```
header                                                         = true
glossary.title                                                 = example glossary
glossary.GlossDiv.title                                        = S
glossary.GlossDiv.GlossList.GlossEntry.ID                      = SGML
glossary.GlossDiv.GlossList.GlossEntry.SortAs                  = SGML
glossary.GlossDiv.GlossList.GlossEntry.GlossTerm               = Standard Generalized Markup Language
glossary.GlossDiv.GlossList.GlossEntry.Acronym                 = SGML
glossary.GlossDiv.GlossList.GlossEntry.Abbrev                  = ISO 8879:1986
glossary.GlossDiv.GlossList.GlossEntry.GlossDef.para           = A meta-markup language, used to create markup languages such as DocBook.
glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso.0 = GML
glossary.GlossDiv.GlossList.GlossEntry.GlossDef.GlossSeeAlso.1 = XML
glossary.GlossDiv.GlossList.GlossEntry.GlossSee                = markup
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.0.firstName  = John
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.0.lastName   = Doe
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.0.age        = 23
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.1.firstName  = Mary
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.1.lastName   = Smith
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.1.age        = 32
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.2.firstName  = Bob
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.2.lastName   = Dole
glossary.GlossDiv.GlossList.GlossEntry.ExtraField.2.age        = 45
```
