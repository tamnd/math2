---
tag: EV03FVHX37
kind: concept
name: Encoding of data
msc: [68Q01, 68P30, 03D10]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel_numbering
---

## Summary

An encoding of a set of objects, such as numbers, graphs or programs, writes each object as a [[string|1P6EP01HZF]] over a finite [[alphabet|RABRP2KG81]].
Different objects get different strings.
Machines read and write only strings, so an encoding is what lets them work on other objects.
A [[Gödel numbering|MFJXPAF0R0]] is the related idea of coding objects by natural numbers.
In complexity theory the choice of encoding matters, since the input size is the length of the code.

## Explanations

### L1 human

A computer only stores bits, yet it handles numbers, pictures and texts.
This works because each object is written as a string of symbols in an agreed way.
The number $6$ can be written as the binary string $110$, and a graph can be written as the list of its edges.
The only firm rule is that two different objects never get the same string, so the object can be read back.
