---
tag: JXK6NRDH4V
kind: problem
name: Banach measure problem
msc: [28C10, 43A07, 28A12]
uses: [2Z2QVWZ262, KFWQ24D9M6, 0HFREYRSZP, 087VJM5Q77]
about: [2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_measure
history:
  posed_by: "Felix Hausdorff"
  first_stated: "1914"
---

## Problem

Let $n \ge 1$.
Is there a function $\mu$, defined on all subsets of $\R^n$, with values in $[0, \infty]$, such that:

1. $\mu$ is finitely additive: $\mu(A \cup B) = \mu(A) + \mu(B)$ for disjoint $A, B \subseteq \R^n$.
2. $\mu$ is invariant under isometries: $\mu(g(A)) = \mu(A)$ for every isometry $g$ of $\R^n$, such as a [[translation|087VJM5Q77]] or a [[rotation|0HFREYRSZP]].
3. $\mu([0, 1]^n) = 1$.

## Remarks

Such a function is a [[finitely additive measure|KFWQ24D9M6]] on the power set.
The countably additive version has a negative answer, by the Vitali set.
Hausdorff showed with his paradox on the sphere that the answer is negative for $n \ge 3$.
Banach showed in 1923 that the answer is positive for $n = 1$ and $n = 2$; such a function can even be chosen to agree with [[Lebesgue measure|2Z2QVWZ262]] on Lebesgue measurable sets.
These functions are called Banach measures, and they are not unique.
The difference between the dimensions is explained by amenability.
The isometry groups of $\R$ and $\R^2$ are amenable, and the rotation group of $\R^3$ contains a free group on two generators.

## Explanations

### L1 human

The question asks whether every set of points, however wild, can be given a length, an area or a volume.
The size should add up for two pieces and should not change when a set is moved rigidly.
On the line and in the plane this is possible, but in space of dimension three or more it is not.
In space, the Banach–Tarski paradox even cuts a ball into finitely many pieces that can be reassembled into two balls of the same size.
