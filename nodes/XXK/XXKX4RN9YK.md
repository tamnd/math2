---
tag: XXKX4RN9YK
kind: concept
name: Reed–Muller code
msc: [94B05]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Reed%E2%80%93Muller_code
same_as:
  wikidata: Q201972
  wikipedia: Reed–Muller code
---

## Summary

A Reed–Muller code is a binary [[linear code|E85KREWV60]] built from [[Boolean functions|0X05GS525E]] in $m$ variables.
Its codewords are the truth tables of the polynomials of degree at most $r$.
It has length $2^m$, dimension $\sum_{i=0}^{r} \binom{m}{i}$ and [[minimum distance|M2X88AXM17]] $2^{m-r}$.
The family contains the repetition codes, the extended [[Hamming codes|D68NF1S2NW]] (up to equivalence) and the whole space, and it has a rich recursive structure.
Reed–Muller codes are also important in complexity theory, as low-degree tests and locally decodable codes.

## Explanations

### L1 human

Take all points of the cube $\set{0, 1}^m$, there are $2^m$ of them.
A codeword is the list of values, at all these points, of a polynomial in $m$ variables of degree at most $r$, with arithmetic modulo $2$.
For $m = 2$ and $r = 1$, the polynomials $0, 1, x_1, x_2, 1 + x_1, \dots$ give the eight words of length $4$ with an even number of ones.
Low degree polynomials cannot vanish on too many points, which is why codewords are far apart.
