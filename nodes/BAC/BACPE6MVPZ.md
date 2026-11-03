---
tag: BACPE6MVPZ
kind: concept
name: Variable-length code
msc: [94A45, 94A29]
sources:
  - url: https://en.wikipedia.org/wiki/Variable-length_code
same_as:
  wikidata: Q2981616
  wikipedia: Variable-length code
---

## Summary

A variable-length code maps each symbol of a source alphabet to a string over a code alphabet.
Different symbols may get strings of different lengths.
Giving short strings to frequent symbols and long strings to rare ones reduces the average length, which is the idea of data compression.
A useful code must be uniquely decodable: a concatenation of codewords must split back in only one way.
[[Prefix codes|GNB3T6TD0M]] have this property.
By [[Shannon's source coding theorem|PC8ASRWARE]], the average length of a uniquely decodable code is at least the [[Shannon entropy|Y86E072V0V]] of the source.

## Explanations

### L1 human

Morse code is a variable-length code: the frequent letter E is a single dot, while a rare letter like Q is four signals long.
This makes typical messages shorter than with a code that uses the same length for every letter.
For example, coding $a, b, c$ as $0, 10, 11$ uses one bit for $a$ and two bits for $b$ and $c$.
If $a$ appears half of the time, the average length is $1.5$ bits per letter instead of $2$.
The string $01011$ splits in only one way, as $0, 10, 11$, so it decodes to $abc$.
