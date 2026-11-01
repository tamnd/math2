---
tag: R43K0GTTDS
kind: statement
role: theorem
name: Bruck–Ryser–Chowla theorem
msc: [05B05, "51E15"]
uses: [TGZATGBHTH, 9DNFN8M83X]
about: [4JCSS2Z1BA, 2HWB7P1DZN]
sources:
  - url: https://en.wikipedia.org/wiki/Bruck%E2%80%93Ryser%E2%80%93Chowla_theorem
same_as:
  wikidata: Q2226624
  wikipedia: Bruck–Ryser–Chowla theorem
---

## Statement

Let $v, k, \lambda$ be integers with $0 < \lambda < k < v$.
Suppose that there is a symmetric $2$-$(v, k, \lambda)$ [[block design|TGZATGBHTH]], that is, one with exactly $v$ blocks.
Then:

1. If $v$ is even, then $k - \lambda$ is a perfect square.
2. If $v$ is odd, then the equation $x^2 = (k - \lambda) y^2 + (-1)^{(v-1)/2} \lambda z^2$ has a solution in integers $x, y, z$ that are not all zero.

## Remarks

Proof idea: the [[incidence matrix|9DNFN8M83X]] $N$ of the design is a square matrix with $N N^T = (k - \lambda) I + \lambda J$, where $J$ is the all-ones matrix.
For $v$ even, taking determinants gives $\det(N)^2 = k^2 (k - \lambda)^{v - 1}$, and since $v - 1$ is odd, $k - \lambda$ must be a square.
For $v$ odd, the identity says that two quadratic forms are equivalent over $\Q$; Lagrange's four-square theorem and a variable-by-variable reduction turn this into the stated equation.
For a [[finite projective plane|2HWB7P1DZN]] of order $n$, take $v = n^2 + n + 1$, $k = n + 1$ and $\lambda = 1$.
If $n \equiv 1$ or $2 \pmod 4$, then $(v-1)/2 = n(n+1)/2$ is odd, and the condition becomes: $n$ is a [[sum of two squares|04NPWJMA6H]].
Example: $6 \equiv 2 \pmod 4$ and $6$ is not a sum of two squares, so there is no projective plane of order $6$.
The theorem gives only a necessary condition: $10 = 1^2 + 3^2$ passes the test, yet there is no plane of order $10$.

## Explanations

### L1 human

The theorem says that some parameter sets for symmetric designs are impossible, by a test from number theory.
For projective planes it says, for instance, that there is no plane of order $6$, $14$ or $21$.

### L2 human

The theorem is the main known non-existence result for symmetric designs and projective planes.
It refines [[Fisher's inequality|M9XF82GGW8]], whose equality case defines symmetric designs, by looking at the incidence matrix over the rationals instead of only its rank.
The open question of whether every projective plane has prime power order lies beyond its reach.
