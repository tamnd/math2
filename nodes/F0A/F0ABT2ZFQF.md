---
tag: F0ABT2ZFQF
kind: definition
name: Projection operation
msc: [08A40, 08A02]
defines: 769B35T6WG
uses: [EJ8YJVM9BW, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(mathematics)
---

## Definition

Let $A$ be a set and let $1 \le k \le n$ be integers.
The $k$-th $n$-ary *projection* on $A$ is the [[operation|EJ8YJVM9BW]] $\pi^n_k \colon A^n \to A$ on the [[Cartesian power|09CEDJYBKP]] $A^n$ given by
$$\pi^n_k(a_1, \dots, a_n) = a_k.$$

## Remarks

Example: on $A = \Z$, the operation $\pi^2_1(a, b) = a$ is a projection; it returns the first of its two arguments for every input.
Non-example: on $\Z$, the operation $(a, b) \mapsto \max(a, b)$ is not a projection, since $\max(1, 0) = 1 \ne 0$ rules out $\pi^2_2$ and $\max(0, 1) = 1 \ne 0$ rules out $\pi^2_1$.
The unary projection $\pi^1_1$ is the identity map of $A$.
In any algebra with universe $A$, the term $x_k$, read as a term in the variables $x_1, \dots, x_n$, has the term operation $\pi^n_k$.
