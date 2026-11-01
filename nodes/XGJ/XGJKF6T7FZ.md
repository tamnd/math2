---
tag: XGJKF6T7FZ
kind: concept
name: Regular semigroup
msc: [20M17]
specializes: [0XMEM406JM]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_semigroup
same_as:
  wikidata: Q3022119
  wikipedia: Regular semigroup
---

## Summary

A regular semigroup is a [[semigroup|0XMEM406JM]] in which each element $a$ has a partner $x$ with $axa = a$.
Groups, the full [[transformation semigroups|7ZB7MRKPQ9]], and the semigroups of all $n \times n$ matrices over a field under multiplication are regular.
Regular semigroups are the class in which [[Green's relations|S7WJW2YES2]] give the most detailed structure theory.
The [[inverse semigroups|3M724K3B50]] are the regular semigroups in which each $a$ has exactly one $x$ with $axa = a$ and $xax = x$.

## Explanations

### L1 human

In a group, every element can be undone by its inverse.
In a regular semigroup, every element can at least be undone partly: some $x$ brings $a$ back to itself in the product $axa$.
For a function $f$ that is not a bijection, one can take $x$ to map each value of $f$ back to one of its preimages.
Then applying $f$, then $x$, then $f$ again gives the same result as $f$.
