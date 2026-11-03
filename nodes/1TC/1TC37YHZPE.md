---
tag: 1TC37YHZPE
kind: concept
name: De Bruijn index
msc: [03B40, 68N18]
sources:
  - url: https://en.wikipedia.org/wiki/De_Bruijn_index
same_as:
  wikidata: Q5244288
  wikipedia: De Bruijn index
---

## Summary

De Bruijn indices write terms of the [[lambda calculus|BD756KR8FM]] without names for bound variables.
Each bound occurrence of a variable is replaced by a natural number that counts the abstractions between the occurrence and its binder.
Two terms that differ only by renaming of bound variables then become literally the same.
Nicolaas Govert de Bruijn introduced them in 1972, and they are widely used in proof assistants and compilers.

## Explanations

### L1 human

The functions $\lambda x.\, x$ and $\lambda y.\, y$ are the same function with different variable names.
De Bruijn's idea is to drop names and point to the binder by distance instead.
In $\lambda x.\, \lambda y.\, x$, the $x$ refers to the binder two levels up, so the term becomes $\lambda\, \lambda\, 2$.
The term $\lambda x.\, \lambda y.\, y$ becomes $\lambda\, \lambda\, 1$.
This removes all problems of renaming, at the price of terms that are harder for people to read.
