# Goal
To be able to identify and implement a simple feature set extension of python rule based filtering 
module [rule_engine](https://zerosteiner.github.io/rule-engine/#)

This module uses [PLY](https://www.dabeaz.com/ply/) under the hoods, to parse the string instruction and apply 
 parsing rules. It is non-trivial but very interesting. 
 
 To learn more on PLY, Read the documentation first then watch this video from its author [David Beazley - Reinventing the Parser Generator - PyCon 2018](https://www.youtube.com/watch?v=zJ9z6Ge-vXs)
__
 
 ## Feature Set 
 
 * ORACLE _NVL_ Function - Write a simple NVL function that mimics oracle NVL function. 
 
 Lexical Token split and parsers are part of `custom_rules_engine/CustomRuleEngine.py`
 Rule Engine extensions are part of `custom_rules_engine/CustomRuleEngine.py`
 Abstract Syntax Tree implementation `custom_rules_engine/CustomRuleExpressions.py`
 
Installations
* pip install pipenv
* pipenv install --dev
* pipenv graph 

Should show the installation dependencies as below 

```
rule-engine==2.0.0
  - ply [required: >=3.9, installed: 3.11]
  - python-dateutil [required: ~=2.7, installed: 2.8.1]
    - six [required: >=1.5, installed: 1.15.0]
```