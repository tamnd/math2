---
tag: EHY4PYSMGZ
kind: concept
name: Growth of algebras
msc: [16P90]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand–Kirillov_dimension
---

## Summary

The growth of a finitely generated [[associative algebra|3CTW1P4HBP]] over a field measures how fast a dimension increases with $n$.
This is the dimension of the span of all products of at most $n$ generators.
Up to a natural equivalence, this rate does not depend on the chosen generators.
Algebras then split into algebras of polynomial growth, of exponential growth and of intermediate growth.
The notion parallels the [[growth rate of a group|4CMRM3975W]], and its numerical summary is the [[Gelfand–Kirillov dimension|MDVSY2NMD2]].

## Explanations

### L1 human

Pick a few generators of an algebra and count how many linearly independent products of length at most $n$ they give.
For the polynomial ring $k[x]$ this number is $n + 1$, which grows like a line.
For $k[x, y]$ it is about $n^2/2$, which grows like an area.
For the free algebra on two generators, where $xy \ne yx$, it is $2^{n+1} - 1$, which grows exponentially.
The growth of an algebra is the shape of this counting function, ignoring constant factors in $n$.
