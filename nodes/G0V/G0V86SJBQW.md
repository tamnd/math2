---
tag: G0V86SJBQW
kind: concept
name: Integral closure
msc: [13B22, 13B21]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_element
---

## Summary

The integral closure of a ring $A$ in a larger commutative ring $B$ is the set of elements of $B$ that are [[integral|1EHN4KPSFS]] over $A$.
It is a subring of $B$ that contains $A$, and it is the largest subring of $B$ that is [[integral over|B7X0KFY1S1]] $A$.
For an integral domain $A$, its integral closure in its own field of fractions is called its normalization.
The ring of integers of a number field is the integral closure of $\Z$ in that field.

## Explanations

### L1 human

Take all elements of the larger ring that satisfy a monic equation with coefficients in $A$; together they form a ring.
Inside $\Q(\sqrt{5})$, the integral closure of $\Z$ contains $\sqrt{5}$ but also the golden ratio $(1 + \sqrt{5})/2$, a root of $x^2 - x - 1$.
So the "integers" of $\Q(\sqrt{5})$ form the ring $\Z[(1 + \sqrt{5})/2]$, which is larger than $\Z[\sqrt{5}]$.
Passing to the integral closure repairs rings that miss some of their natural elements.
