---
tag: YY5ZM93GBY
kind: concept
name: BCH code
msc: [94B15, 11T71]
specializes: [E04GGZ1Q91]
sources:
  - url: https://en.wikipedia.org/wiki/BCH_code
same_as:
  wikidata: Q795705
  wikipedia: BCH code
---

## Summary

A BCH code is a [[cyclic code|E04GGZ1Q91]] over a [[finite field|0ZXZ82FTX2]].
Its generator polynomial vanishes at a run of consecutive powers of a [[primitive root of unity|0EHM5ZP5QH]].
The [[BCH bound|CT69XTRW2K]] then guarantees that the [[minimum distance|M2X88AXM17]] is at least the length of the run plus one.
So the designer can fix the number of errors to correct in advance.
BCH codes are among the most used algebraic codes, and [[Reed–Solomon codes|5VBWJ7EFTX]] are a special case.

## Explanations

### L1 human

Codewords of a cyclic code are polynomials, and a polynomial is pinned down by its roots.
A BCH code asks every codeword to have the roots $\alpha, \alpha^2, \dots, \alpha^{\delta - 1}$, where $\alpha$ is a root of unity in a larger field.
Having many consecutive roots forces every nonzero codeword to have many nonzero coefficients, so codewords are far apart.
For example, over $\F_2$ with $\alpha$ a root of $x^3 + x + 1$, asking for the roots $\alpha$ and $\alpha^2$ gives the $[7, 4, 3]$ [[Hamming code|D68NF1S2NW]], which corrects one error.
