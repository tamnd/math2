---
tag: 993HPHG9VF
kind: definition
name: Admissible function
msc: [49K05, 49J05]
defines: G7T008BEWY
uses: [JRQZ803Q5Y, 0VW90BBSJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Definition

Let $a < b$ and $A, B \in \R$, and let $J(y) = \int_a^b L(x, y, y') \, dx$ be an [[integral functional|JRQZ803Q5Y]] with a continuous Lagrangian $L \colon [a, b] \times \R \times \R \to \R$.
In the fixed-endpoint problem for $J$, a function $y \colon [a, b] \to \R$ is *admissible* if:

1. $y \in C^1([a, b])$, that is, $y$ is [[continuously differentiable|0VW90BBSJ4]] on $[a, b]$;
2. $y(a) = A$;
3. $y(b) = B$.

The set $\mathcal{A}$ of admissible functions is the *admissible class*.
More generally, the admissible class of a variational problem is the set of functions in the domain of the functional that satisfy all its constraints.
Its elements are the admissible functions.

## Remarks

Example: for $a = 0$, $b = 1$, $A = 0$, $B = 1$, the function $y(x) = x^2$ is admissible: it is $C^1$, $y(0) = 0$ and $y(1) = 1$.
Non-example: for $a = 0$, $b = 1$, $A = B = 1$, the function $y(x) = \abs{x - 1/2} + 1/2$ satisfies $y(0) = y(1) = 1$ but is not differentiable at $1/2$, so it fails clause 1.
Many texts use the larger class of piecewise $C^1$ functions, which admits such broken curves.
If $y$ is admissible and $\eta \in C^1([a, b])$ has $\eta(a) = \eta(b) = 0$, then $y + t\eta$ is admissible for every $t \in \R$; such $\eta$ are the admissible variations.
