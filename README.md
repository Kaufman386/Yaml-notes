<p align="center">
  <a href="https://yaml.org/" target="blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Official_YAML_Logo.svg/512px-Official_YAML_Logo.svg.png?20220206165621" width="200" height="200" alt="Yaml Logo" /></a>
</p>
  <p align="center"><a href="https://yaml.org/" target="blank">YAML</a> is a human-friendly <a href="https://en.wikipedia.org/wiki/Serialization" target="blank">data serialization language</a> for all progarmming languages.</p>
<p align="center">

# :book: Table of Contents <!-- omit in toc -->
- [YAML Basics](#star-yaml-basics)
    - [Overview](#arrow_right-overview)
    - [Basic Syntax](#arrow_right-basic-syntax)
    - [What is YAML?](#arrow_right-what-is-yaml)
    - [YAML Use Cases](#arrow_right-yaml-use-cases)
    - [YAML Features](#arrow_right-yaml-features)
    - [YAML vs JSON](#arrow_right-yaml-vs-json)
    - [Block vs Flow Style](#arrow_right-block-vs-flow-style)
    - [YAML Building Blocks](#arrow_right-yaml-building-blocks)
- [YAML Advanced Syntax](#star-yaml-advanced-syntax)
    - [Overview](#arrow_right-overview-1)
    - [Folding and Chomping](#arrow_right-folding-and-chomping)
    - [Nested Sequences](#arrow_right-nested-sequences)
    - [Nested Mappings](#arrow_right-nested-mappings)
    - [Combine Sequences and Mappings](#arrow_right-combine-sequences-and-mappings)
    - [Dates](#arrow_right-dates)
    - [Repeated Nodes](#arrow_right-repeated-nodes)
    - [Tags](#arrow_right-tags)
    - [Schemas](#arrow_right-schemas)
- [Parsing and Validation](#star-parsing-and-validation)
    - [Overview](#arrow_right-overview-2)
    - [Parsing](#arrow_right-parsing)
    - [Validating](#arrow_right-validating)
    - [Parsing and Validating YAML with Python](#arrow_right-parsing-and-validating-yaml-with-python)
    - [Dump to YAML file with Python](#arrow_right-dump-to-yaml-file-with-python)
    - [Common YAML mistakes](#arrow_right-common-yaml-mistakes)
- [YAML in Practice](#star-yaml-in-practice)
    - [Overview](#arrow_right-overview-3)
    - [YAML in Everyday Life](#arrow_right-yaml-in-everyday-life)
    - [Compare YAML and JSON](#arrow_right-compare-yaml-and-json)
    - [Compate YAML and XML](#arrow_right-compate-yaml-and-xml)


# :star: YAML Basics
### :arrow_right: Overview
  - [Basic Syntax](#arrow_right-basic-syntax)
  - [What is YAML?](#arrow_right-what-is-yaml)
  - [YAML Use Cases](#arrow_right-yaml-use-cases)
  - [YAML Features](#arrow_right-yaml-features)
  - [YAML vs JSON](#arrow_right-yaml-vs-json)
  - [Block vs Flow Style](#arrow_right-block-vs-flow-style)
  - [YAML Building Blocks](#arrow_right-yaml-building-blocks)

### :arrow_right: Basic Syntax
- Indentation
- Sequences/Lists
- Mapping/dictionarys
- Scalars (basic values like strings and numbers)
- Comments
- Documents

### :arrow_right: What is YAML?
- Data Serialization Lanugage
  - YAML syntax can be used to infer data objects to text, which is useful for sending data around and storing it.
- The format can later be interpreted and converted back to the original data object. 
  - The text of serialized data in YAML consitst of unicode printable characters 
  - (Letter, Digits, Punctuation) can be used to represent data.
  - Unprintable characters would be whitespace for example
- Commonly used for data about hosts and infrastructure

### :arrow_right: YAML Use Cases
- Cross-language data sharing
  - Serialize objects in javascript and transfer to a PHP applicaiton
  - The php applicaiton can deserialize the data and use the object in the applicaiton
- Configuration files
- Logging Files
  - Allows dashboards that support YAML to automatically process log files
  - Easily readable by humands
- Object Persistence
  - Serialized objects and storing them to be deserialized later, YAML can be used to do the storing (Definitely not common)
- Works with many Laguages
  - Works great with languages that match it's data structure
  - Ex: PHP, JS, Python, Perl, and Ruby

### :arrow_right: YAML Features
1. Very readable for humans
   - Note that it is not easy to write good YAML code, but it shouldn't be too hard to understand
2. Portable between languages and tools
3. Consistent
4. Transition between some languages in YAML is very smooth
   - It matches data structure of many programming languages (python, php, js, perl, ruby)
   - Has variables that can be numbers, strings, booleans, lists (called sequences), and key-value pairs called mappings
5. Expressive Languages
   - Can be used to represent all sorts of data
6. Extensible
   - Custom data types can be added

### :arrow_right: YAML vs JSON
- YAML is a superset of JSON
  - All portable JSON is valid YAML; although, they're not fully interchangeable
- When to use JSON vs YAML?
  - When you do not need any fancy YAML features, use JSON. 
  - Since all JSON is valid YAML, it's easy to switch later if you require more complex features
    - JSON can still be processed when working with YAML

  | YAML  | JSON |
  | ------------- | ------------- |
  | Superset of JSON | Data-interchange format |
  | Focuses on human readability | Aims to be as simple as possible |
  | Focuses on supporting native data structures  | Aims to be universally supported |
  | Harder for programming environments to parse and process YAML | Easy to process for programming languages |

### :arrow_right: Block vs Flow Style
- Supporting JSON (back in 2009) tended to complicate the syntax
- Now there are two styles when programming in YAML: Block and Flow Style
  - They can be mized and used interchangeably in the YAML file
  - NOTE: If you do this randomly, it doesn't become very human readable or understandable
- Block Style is preferred

    | Block Style  | Flow Style |
    | ------------- | ------------- |
    | Preferred style | Best used for one-line situations |
    | YAML's own format for data structure | Well-known, but less human readable JSON syntax |

### :arrow_right: YAML Building Blocks
- Indentation
  - Default indentation is two spaces
- Sequences (Lists, Arrays)
  - Here is a [Block style sequence](Demos/sequences-block.yaml) file and a [Flow style sequence](Demos/sequences-flow.yaml) demo file
  - Here is a combination of Block and Flow style in a [demo](Demos/sequences-block-and-flow.yaml) file
  ```YAML
  # Syntax - Sequences Block Style
  - first item in the list
  - second item in the list
  - third item in the list

  # Syntax - Sequences Flow Style (Like JSON)
  [just, a list, in flow style]
  ```
- Mappings (Key-value pairs, Dictionaries, Hashes, Objects)
  - indicated by a ": " (colon and space)
  - Here is a [Block style mapping](Demos/mappings-block.yaml) file and a [Flow style mapping](Demos/mappings-flow.yaml) demo file
  ```YAML
  # Syntax - Mapping Block Style
  key: value
  list:
    - first item
    - second item
    - third item
  # Here is a Block Style mapping that uses a flow-style List
  flowlist: [just, a list, in flow style]

  # Syntax - Mapping Flow Style
  { key: value, another: value, flowlist: [just, a list, in flow style] }
  ```
- Scalars (Actual values, Strings, Numbers, Booleans, Dates)
  - Escaping can be done with a \
  - Here is a [scalar demo](Demos/scalars.yaml) file
  ```YAML
  # Scalar - Regular Style
  tool: yaml
  version: 1.2
  awesome: true
  nothing: null
  duplicateKeys: not allowed
  ```
- Comments
  - Just a presentation detail
  - No effect on serialization tree
  - Start with a #
  ```YAML
  # This is a comment
  # These will be discarded at serialization
  key: value        # we can have a comment after a key-value pair

  # If "#" is in quotes...it is NOT a comment
  "#": This is not a comment
  ```
- Documents
  - One file can contain multiple documents
  - An example of a [yaml document](Demos/documents.yaml) file
  - Documents are separated by 3 hyphens (---)
  - Can be ended with suffix of 3 dots (...)
  ```YAML
  tool: yaml
  version: 1.2
  awesome: true
  nothing: null
  duplicateKeys: not allowed
  ---
  This is a new Document
  ---
  One file can contain multiple documents
  ```

# :star: YAML Advanced Syntax
### :arrow_right: Overview
- [Folding and Chomping](#arrow_right-folding-and-chomping)
- [Nested Sequences](#arrow_right-nested-sequences)
- [Nested Mappings](#arrow_right-nested-mappings)
- [Combine Sequences and Mappings](#arrow_right-combine-sequences-and-mappings)
- [Dates](#arrow_right-dates)
- [Repeated Nodes](#arrow_right-repeated-nodes)
- [Tags](#arrow_right-tags)
- [Schemas](#arrow_right-schemas)

### :arrow_right: Folding and Chomping
- There are two types of concepts: Folding and Chomping
- For a detailed difference between the two, look at the [Demo](Demos/folding-and-chomping.yaml) file
    | <p align="center">Folding</p>  | <p align="center">Chomping</p> |
    | ------------- | ------------- |
    | Dealing with new lines in multi-line strings | How to deal with trailing newlines in multi-line strings |
    | Should the new line be interpreted as an actual line-breaking string? | Chomping is about the lines at the end of the string |
    | Should the new line be removed? | Chomping indicators signal that a new line must NOT be created by default at the end of a string |
    | Indicated with the <b>></b> or <b>\|</b> symbol | Indicated with the second indicator after the <b>></b> or <b>\|</b> symbol (Ex: <b >></b>, <b>>-</b>, <b>>+</b>, <b >\|</b>, <b>\|-</b>, <b>\|+</b>) |

    | <p align="center">></p> | <p align="center">\|</p> |
    | ------------- | ------------- |
    | Removes line breaks in between texts, except for white lines | Includes all line breaks in between texts and white lines |

### :arrow_right: Nested Sequences
- Sequence of sequences
    ```YAML
    # Block-list with flow-style lists (block-list of flow-lists) -> [[yaml, json], [python, javascript]]
    flow_lists:
    - [yaml, json]
    - [python, javascript]
    
    # Block-List style with block-style lists (block-list of block-lists) -> [[yaml, json], [python, javascript]]
    block_lists:
    - - yaml
    - json
    - - python
    - javascript
    ```

### :arrow_right: Nested Mappings
- Mapping of mappings
- **NOTE:** You cannot use the block-style mapping within a parent flow-style mapping! But you can do the vice-versa
    ```YAML
    person:
        name: Mike
        age: 30
        address:
            streetname: Langstraat
            number: 1
            zipcode: 1234AB
            city: Amsterdam
            country: The Netherlands
        dog: { name: Bobby, breed: labradoodle } # Example of a flow-style mapping within a parent block-style mapping
    ```

### :arrow_right: Combine Sequences and Mappings
- For a detailed explanation view this [demo](Demos/combining-sequences-and-mappings.yaml) file
- **NOTE:** You shouldn't mix block-style with flow-style in yaml files. Stick to one style
    ```YAML
    languages:
        - programming:
            - frontend:
                - html
                - css
                - js
            - backend:
                - java
                - python
                - c#
        - data serialization:
            - yaml
            - json
    ```

### :arrow_right: Dates
- Considered a scalar
- Used for Dates and Timestamps
- You can return a DATE as a STRING using explicit typing
    ```YAML
    timestamp: 2022-03-22T22:19:56.10+02:00
    simple_date: 2022-03-22
    # Below is not a date. It is a str due to the explicit typing (!!str)
    not_a_date: !!str 2022-03-22
    ```

### :arrow_right: Repeated Nodes
- **Nodes** represent a single native data structure (Scalar, Sequence, Mapping)
- Results in cleaner YAML: DRY (Don't Repeat Yourself)

    | <p align="center">Syntax</p> | <p align="center">Name</p> | <p align="center">Description</p> |
    | ----------- | ----------- | ----------- |
    | &name | Anchor Name | This defines the scalar or data structure to be repeated | 
    | *name | Next Referenced Alias | This repeats the defined anchor |
    | << | Merge | This allows us to overwrite a particular part of a repeated node |
    ___
    ```YAML
    # Simple example of using Anchor and Alias
    key: &repeated Hi there     # Stores "Hi there" inside the anchor called "repeated"
    new_key: *repeated          # repeated is replaced with "Hi there"

    # You can also copy entire objects
    person: &person             # Current line to the next line that occurs at the same indentation as "person" is copied to anchor 
        name: Mike
        age: 30
        address:
            streetname: Langstraat
            number: 1
            zipcode: 1234AB
            city: Amsterdam
            country: The Netherlands

    # This "another_person" mapping becomes identical to the "person" mapping above
    another_person: *person

    # If you want to overwrite the "name" key of our "person" mapping, we can use the `merge` syntax
    yet_another_person:
        <<: *person             # Copies "person" mapping but changes "name: Mikael" --> "name: Makayla"
        name: Makayla
    ```

### :arrow_right: Tags
- Also known as a "type"
- Tags give a node a type
- Untagged nodes are given a type by default
- Explicit typing can be done with the "!" character
- How the tags are interpreted depends on the exact [**schema**](#arrow_right-schemas) that is used to interpret that YAML
    ```YAML
    no_date: !!str 2022-03-21   # This DATE is being tagged as a STRING
    no_number: !!str 20         # This INTEGER is being tagged as a STRING
    unncessary: !!int 20        # No need to add an "int" tag to a INTEGER scalar
    ```

### :arrow_right: Schemas
- **YAML Validation:** Contain the rules of YAML and used to validate whether a certain file adheres to the rules
- Used to create data types
  - Custom Data Types can be added with language-specific schemas
- **Default Schemas** of YAML:
  - Failsafe schema
  - JSON schema
  - Core schema (*The Preferred Schema*)
- Programming languages have their own schemas that map YAML to the language native data structure
- Interoperable schemas use global tags to represent the same data across different languages
  - This makes communication between languages really easy

  | <p align="center">Failsafe Schema</p> | <p align="center">JSON Schema</p> | <p align="center">Core Schema</p> |
  | ----------- | ----------- | ----------- |
  | **Three tags**: string, mapping, sequence | Has All Failsafe tags pluse few more | Extension of the JSON schema plus more tag resolutions | 
  | !!str: a string value | !!null: a null value | All the nodes with '**!**' are resolved in a slightly more advanced way than it's done for JSON schema |
  | !!map: a mapping | !!bool: boolean | Strongly recommended deafult schema |
  | !!seq: a sequence | !!int: integer | Best practice to base custom schemas on Core Schema |
  | **!!** is shorthand for **!\<tag:yaml.org,2002:...\>** | !!float: float | Overall, you should always use this one |
  ___


# :star: Parsing and Validation
### :arrow_right: Overview
- [Parsing](#arrow_right-parsing)
- [Validating](#arrow_right-validating)
- [Parsing and Validating YAML with Python](#arrow_right-parsing-and-validating-yaml-with-python)
- [Dump to YAML file with Python](#arrow_right-dump-to-yaml-file-with-python)
- [Common YAML mistakes](#arrow_right-common-yaml-mistakes)

### :arrow_right: Parsing
- Conversion of one format to another
- Proccessing YAML 
  1. Loading YAML into our application
     1. YAML file is processed (A stream of characters sent to the parser)
     2. Serialization Tree is created
     3. Tree is converted into a node craft (For representation)
     3. Node Craft is translated to Native Data Structures
  2. Dumping Objects to YAML file
     1. Start from Native Data Structures in our code
     2. Convert them into node crafts
     2. Serialize data
     4. Send character stream for parsing (YAML file)

### :arrow_right: Validating
- Making sure the syntax of the YAML content is valid
- Checking against formatting rules of YAML
- Find problems with certain parts of the file
- External tools are needed to validate YAML (e.g. VSCode or Browser tools)

### :arrow_right: Parsing and Validating YAML with Python
- Python requires you to use the external PyYAML module to allow python to interpret YAML code
  - Install PyYAML with `pip install pyyaml`
  - If using pip3, `pip3 install pyyaml`
- Validating & Parsing YAML while coding can be seen in these two files
  1. [Parsing in Python](Demos/parsing.py) demo file and [Parsing in YAML](Demos/parsing.yaml) demo file
  2. [Using Custom tags - Python](Demos/custom_tags.py) demo file and [Using custom tags - YAML](Demos/custom_tags.yaml) demo file
- **NOTE**: When using `safe_load` import, you cannot use custom types. You must use `unsafe_load`
  - If you do not need to use custom types, always use `safe_load`
  - If you want to read a mult-document YAML file all at once, you can use `safeLoadAll` function

### :arrow_right: Dump to YAML file with Python
- This demonstrates how you can dump other code into a YAML file
- You can dump custom/native Python (or any supported language) objects to YAML code
- Dumping into a YAML while coding can be seen in these files
  1. This [demo](Demos/dump.py) file demonstrates native Python Object dumping
  2. This [demo](Demos/dump_person.py) file demonstrates custom Python Object dumping

### :arrow_right: Common YAML mistakes
1. Bad Quotes
   - It's important to use the right type of quotes if when working with...
     - Paths
     - RegEx
     - Escape characters (only double quotes can be used for them)
2. Indentation
   - There is no explicit error when indentation is wrong
   - YAML will serialize it incorrectly and you need to trace the indentation carefully
3. Number Type
   - Octal and Hex variables in YAML reserve the first digit to be a zero
4. Duplicate Keys
   - Duplicate keys are **not** allowed in YAML, but are allowed in JSON and XML
   - Keep notice when you are parsing XML/JSON to YAML code
5. Accidental List Entry
   - Anything that starts with a dash is a list entry
   - If you want to use a '-', you should put it in quotes
6. List as Keys in Languages
   - Not all languages allow this and will result in an error

   | <p align="center">Error</p> | <p align="center">Feature</p> | <p align="center">Solution</p> |
   | ----------- | ----------- | ----------- |
   | Bad Quotes | Using Paths? | Use single Quotes |
   | Bad Quotes | Using regular expressions? | Use single quotes (depends on parser though) |
   | Indentation | No explicit Indentation Error | Trace carefully |
   | Number Type | Assigning phone numbers? | Store them in strings in case it starts with zero |
   | Duplicate Keys | Converting code to YAML? | Check for duplicate keys |
   | Accidental List Entry | Does your parse file use dashes? | Store it in quotes before parsing to YAML file |
   | Duplicate Keys | Converting code to YAML? | Check for duplicate keys |
   | List as Keys in Languages | Dumping YAML lists to a file? | Make sure keys are not lists |


# :star: YAML in Practice
### :arrow_right: Overview
- [YAML in Everyday Life](#arrow_right-yaml-in-everyday-life)
- [Compare YAML and JSON](#arrow_right-compare-yaml-and-json)
- [Compate YAML and XML](#arrow_right-compate-yaml-and-xml)

### :arrow_right: YAML in Everyday Life
  - YAML is commonly used when deploying projects using...
    1. Docker Compose
    2. Kubernetes
    3. CI/CD Pipeline Tools
       - GitHub Actions
       - GitHub Pipelines
       - BitBucket Pipelines
  - An example of a **deployment file** is [here](Demos/example-deployment.yaml)
    - Here is a good excercise to descramble a large [docker compose file](Demos/docker-compose.yaml) (which is a yaml file)

### :arrow_right: Compare YAML and JSON

  | <p align="center">YAML</p> | <p align="center">JSON</p> |
  | ------------- | ------------- |
  | Can be parsed with a YAML parser | Can be parsed with a YAML parser (YAML is a superset of JSON) |
  | Comments with a # | Comments not allowed |
  | Objects and lists are denoted with *indentation* or **{}** and **[]** | Objects and lists are denoted with **{}** and **[]** |
  | String quotes are optional, and can be double or single | String quotes are mandatory, must be double quotes |
  | Root node can be any valid data type | Root node must be object or list |
  | Standard for configuration | Standard for APIs |
  | [YAML v JSON.yaml](Demos/yaml_v.yaml) | [YAML v JSON.json](Demos/yaml_v_json.json) |


### :arrow_right: Compate YAML and XML

  | <p align="center">YAML</p> | <p align="center">XML</p> |
  | ------------- | ------------- |
  | Data Serialization Language | Markup language |
  | Easier to read | Harder to read |
  | Querying YAML relise on many different external tools | Well established options to query data in XML file |
  | Typically, preferred option for configuration | Decreasing in popularity because of JSON and YAML |
  | [YAML v XML.yaml](Demos/yaml_v.yaml) | [YAML v XML.xml](Demos/yaml_v_xml.xml) |
