# RSA

## Introduction

> This script has for funtionality translate one text to voice in
the International Radiotelephony Spelling Alphabet.
    
#### Translate text 
```python
traducction = transalte(string)
```

#### Say text with parameters predefinites
```python
voice = 10, velocity = 40
say(traducction, voice , velocity)
```
## Installation

### Dependencies in linux:
```
$ sudo apt-get install --upgrade speak
```

### Instalation project
```
$ git clone https://www.github.com/deltahat/RSA.git
```

## Code example
```python
# -*- coding: utf-8 -*-

import rsa

string = input("Enter your text: ")
voice = 10, velocity = 40
traduction = translate(string)
say(traduction, voice, velocity)

```
