---
tag: CV013KHVJG
kind: concept
name: Free monoid
msc: [20M05]
specializes: [0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/Free_monoid
same_as:
  wikidata: Q5500266
  wikipedia: Free monoid
---

## Summary

The free monoid on a set $A$ is the [[monoid|0N6R902FG1]] $A^*$ of all finite words over the alphabet $A$.
Its operation is concatenation, and its identity is the empty word.
It is free in the sense that any map from $A$ to a monoid extends in exactly one way to a monoid homomorphism from $A^*$.
Free monoids are the setting of formal languages and automata, and they are the monoid analogue of [[free groups|0KTW26C80J]].

## Explanations

### L1 human

Take an alphabet, such as the letters $a$ and $b$.
The free monoid consists of all strings you can write with them, including the empty string: $a$, $ba$, $abba$, and so on.
To multiply two strings, write one after the other, so $ab$ times $ba$ is $abba$.
No two different strings are ever identified, which is what "free" means.
