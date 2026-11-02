---
tag: CBYB39FTFG
kind: problem
name: Ulam's stability problem
msc: [39B82, 39B52]
uses: [0JYTG5K9Y4, 0VKD1TP7F3]
about: [TPYXQTYND6]
sources:
  - url: https://en.wikipedia.org/wiki/Hyers%E2%80%93Ulam%E2%80%93Rassias_stability
history:
  posed_by: "Stanisław Ulam"
  first_stated: "1940"
---

## Problem

Let $G_1$ be a group and let $G_2$ be a group with a metric $d$.
Given $\varepsilon > 0$, does there exist $\delta > 0$ with the following property?
If a map $h \colon G_1 \to G_2$ satisfies $d(h(xy), h(x) h(y)) < \delta$ for all $x, y \in G_1$, then there is a [[group homomorphism|0JYTG5K9Y4]] $H \colon G_1 \to G_2$ with $d(h(x), H(x)) < \varepsilon$ for all $x \in G_1$.

## Remarks

The question asks when an approximate homomorphism lies close to an exact one.
Ulam posed it in a talk at the University of Wisconsin in 1940.
D. H. Hyers answered it in 1941 for additive maps between Banach spaces, with $\delta = \varepsilon$.
This answer is [[Hyers' theorem|VFRJ0P2P15]].
The answer depends on the groups: for some pairs of groups the property fails, so the problem is a family of questions rather than one.
Questions of this kind for other functional equations form the theory of [[Hyers–Ulam stability|TPYXQTYND6]].

## Explanations

### L1 human

Suppose a map respects the group law only up to a small error.
Ulam asked whether such a map must be close to a map that respects the law exactly.
For additive maps between Banach spaces the answer is yes, and this started a large field.
