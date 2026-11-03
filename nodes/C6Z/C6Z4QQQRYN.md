---
tag: C6Z4QQQRYN
kind: statement
role: lemma
name: Addition of integer classes of pairs is well defined
msc: [11A99]
uses: [0NS58JP68E, 0MWKJ44V5A, 0C4JS9RF5M]
about: [0NS58JP68E]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_prop-integers.ptx#L13
    locator: source/s_background_prop-integers.ptx:13
---

## Statement

Work in the [[construction of the integers|0NS58JP68E]] from pairs of [[natural numbers|0MWKJ44V5A]]. Write $\langle(a,b)\rangle$ for the class of the pair $(a,b)$, and add classes by the rule $\langle(a,b)\rangle + \langle(e,f)\rangle = \langle(a+e,\, b+f)\rangle$.

Let $a, b, c, d, e, f, g, h$ be natural numbers. Suppose that $\langle(a,b)\rangle = \langle(c,d)\rangle$ and $\langle(e,f)\rangle = \langle(g,h)\rangle$. Then
$$\langle(a,b)\rangle + \langle(e,f)\rangle = \langle(c,d)\rangle + \langle(g,h)\rangle.$$

## Remarks

The sum of two classes does not depend on which pairs are chosen to represent them. This is what makes addition an operation on the [[integers|0C4JS9RF5M]].
