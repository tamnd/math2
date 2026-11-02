---
tag: FW2JKAN14B
kind: concept
name: Lambert W function
msc: ["33E20", "33B10"]
sources:
  - url: https://en.wikipedia.org/wiki/Lambert_W_function
same_as:
  wikidata: Q429331
  wikipedia: Lambert W function
---

## Summary

The Lambert W function is the [[inverse|0J2WAR83WP]] of the map $w \mapsto w e^w$, so $W(x)\, e^{W(x)} = x$.
Over the complex numbers it is multivalued, with countably many branches $W_k$; on the reals it has two branches $W_0$ and $W_{-1}$.
It solves many equations that mix exponentials and polynomials, such as $x = e^{-x}$ or $a^x = x$.
It appears in combinatorics, in delay differential equations and in physics.

## Explanations

### L1 human

The function $w e^w$ is not inverted by logarithms or roots, so its inverse gets a name of its own.
To solve $x e^x = 1$, one writes $x = W(1) \approx 0.567$.
To solve $x = e^{-x}$, one multiplies by $e^x$ to get $x e^x = 1$, so the answer is the same number.
On the real line, $w e^w$ has a minimum $-1/e$ at $w = -1$, so the equation $w e^w = x$ has two real solutions for $-1/e < x < 0$, and this is why there are two real branches.
