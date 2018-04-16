# RSA

## Introduction

> This script has for funtionality translate one text to voice in
the International Radiotelephony Spelling Alphabet.

## Code Samples

    string = input("Enter your text: ")
#  
#### Translate text 

    traducction = transalte(string)

#  
#### Say text with parameters predefinites
    
    voice = 10, velocity = 40
    say(traducction, voice , velocity)

## Installation

### Dependencies in linux:

    sudo apt-get install --upgrade speak

### Instalation project
    mkdir project
    
    cd project

    git clone https://www.github.com/deltahat/RSA.git
    
### In your code
    import rsa
