<p align="center">
  <a href="https://yaml.org/" target="blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Official_YAML_Logo.svg/512px-Official_YAML_Logo.svg.png?20220206165621" width="200" height="200" alt="Yaml Logo" /></a>
</p>
  <p align="center">A human-friendly data serialization language for all progarmming languages.</p>
<p align="center">

# Table of Contents <!-- omit in toc -->
- [YAML Basics](#arrow_right-yaml-basics)
    - [Basic Syntax](#arrow_right-basic-syntax)
    - [What is YAML?](#arrow_right-what-is-yaml)
    - [YAML Use Cases](#arrow_right-yaml-use-cases)
    - [YAML Features](#arrow_right-yaml-features)
    - [YAML vs JSON](#arrow_right-yaml-vs-json)
    - [Block vs Flow Style](#arrow_right-block-vs-flow-style)
    - [YAML Building Blocks](#arrow_right-yaml-building-blocks)
- [YAML Advanced Syntax](#yaml-advanced-syntax)
    - [Overview](#arrow_right-overview)
    - [Folding and Chomping](#arrow_right-folding-and-chomping)
    - [Nested Sequences](#arrow_right-nested-sequences)
    - [Nested Mappings](#arrow_right-nested-mappings)
    - [Combine Sequences and Mappings](#arrow_right-combine-sequences-and-mappings)
    - [Dates](#arrow_right-dates)
    - [Repeated Nodes](#arrow_right-repeated-nodes)
    - [Tags](#arrow_right-tags)
    - [Schemas](#arrow_right-schemas)
- [Parsing and Validation](#parsing-and-validation)
    - [Overview](#arrow_right-overview)
    - [Parsing](#arrow_right-parsing)
    - [Validating](#arrow_right-validating)
    - [Parsing and Validating YAML with Python](#arrow_right-parsing-and-validating-yaml-with-python)
    - [Common YAML mistakes](#arrow_right-common-yaml-mistakes)
    - [Debugging YAML](#arrow_right-debugging-yaml)

# YAML Basics
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
  ```YAML
  # Syntax - Mapping Block Style
  key: value
  list:
    - first item
    - second item
    - third item
  flowlist: [just, a list, in flow style]

  # Syntax - Mapping Flow Style
  { key: value, another: value, flowlist: [just, a list, in flow style] }
  ```
- Scalars (Actual values, Strings, Numbers, Booleans, Dates)
  - Escaping can be done with a \
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

# YAML Advanced Syntax
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
  | !!map: a sequence | !!int: integer | Best practice to base custom schemas on Core Schema |
  | **!!** is shorthand for **!\<tag:yaml.org,2002:...\>** | !!float: float | Overall, you should always use this one |
  ___


# Parsing and Validation

### :arrow_right: Overview
- [Parsing](#arrow_right-parsing)
- [Validating](#arrow_right-validating)
- [Parsing and Validating YAML with Python](#arrow_right-parsing-and-validating-yaml-with-python)
- [Common YAML mistakes](#arrow_right-common-yaml-mistakes)
- [Debugging YAML](#arrow_right-debugging-yaml)

### :arrow_right: Parsing

### :arrow_right: Validating

### :arrow_right: Parsing and Validating YAML with Python

### :arrow_right: Common YAML mistakes

### :arrow_right: Debugging YAML