<p align="center">
  <a href="https://yaml.org/" target="blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Official_YAML_Logo.svg/512px-Official_YAML_Logo.svg.png?20220206165621" width="200" height="200" alt="Yaml Logo" /></a>
</p>
  <p align="center">A human-friendly data serialization language for all progarmming languages.</p>
<p align="center">

# Glossary
- [YAML Basics](#yaml-basics)
   - [Basic Syntax](#basic-syntax)
   - [What is YAML?](#what-is-yaml)
   - [YAML Use Cases](#yaml-use-cases)
   - [YAML Features](#yaml-features)
   - [YAML vs JSON](#yaml-vs-json)
   - [Block vs Flow Style](#block-vs-flow-style)
   - [YAML Building Blocks](#yaml-building-blocks)
- [YAML Advanced Syntax](#yaml-advanced-syntax)

# YAML Basics
### Basic Syntax
- Indentation
- Sequences/Lists
- Mapping/dictionarys
- Scalars (basic values like strings and numbers)
- Comments
- Documents

### What is YAML?
- Data Serialization Lanugage
  - YAML syntax can be used to infer data objects to text, which is useful for sending data around and storing it.
- The format can later be interpreted and converted back to the original data object. 
  - The text of serialized data in YAML consitst of unicode printable characters 
  - (Letter, Digits, Punctuation) can be used to represent data.
  - Unprintable characters would be whitespace for example
- Commonly used for data about hosts and infrastructure

### YAML Use Cases
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

### YAML Features
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

### YAML vs JSON
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

### Block vs Flow Style
- Supporting JSON (back in 2009) tended to complicate the syntax
- Now there are two styles when programming in YAML: Block and Flow Style
  - They can be mized and used interchangeably in the YAML file
  - NOTE: If you do this randomly, it doesn't become very human readable or understandable
- Block Style is preferred

    | Block Style  | Flow Style |
    | ------------- | ------------- |
    | Preferred style | Best used for one-line situations |
    | YAML's own format for data structure | Well-known, but less human readable JSON syntax |

### YAML Building Blocks
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
  key: value # we can have a comment after a key-value pair
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
### Overview
- Folding and Chomping
- Nested Sequences
- Nest Mappings
- Combine sequences and mappings
- Dates in YAML files
- Repeated Nodes
- Tags
- Schemas

### Folding and Chomping
- This has to deal with multi-line strings
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

### Nested Sequences
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

### Nested Mappings
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
    dog: { name: Bobby, breed: labradoodle} # Example of a flow-style mapping within a parent block-style mapping
```

### Combine Sequences and Mappings
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

