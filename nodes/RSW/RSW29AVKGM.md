---
tag: RSW29AVKGM
kind: statement
role: theorem
name: Clifford's theorem on special divisors
msc: [14H51, 14C20]
uses: [XJM2MT4S3Y, Z9DN23DAE2, GHRPE8CXJ9, W05VYY4HBR, 5SB8EKSQRN, WMVAT9MBZ1]
about: [GHRPE8CXJ9, Z9DN23DAE2]
sources:
  - url: https://en.wikipedia.org/wiki/Clifford%27s_theorem_on_special_divisors
same_as:
  wikidata: Q5132840
  wikipedia: Clifford's theorem on special divisors
---

## Statement

Let $X$ be a smooth projective [[algebraic curve|XJM2MT4S3Y]] of genus $g$ over an algebraically closed field, with [[canonical divisor|W05VYY4HBR]] $K$.
For a [[divisor|Z9DN23DAE2]] $D$, let $\ell(D)$ be the dimension of the space of rational functions $f$ with $\operatorname{div}(f) + D \ge 0$.
Then the [[complete linear system|GHRPE8CXJ9]] $\abs{D}$ has dimension $\ell(D) - 1$.
Let $D$ be an effective divisor that is special, meaning $\ell(K - D) > 0$.
Then
$$\ell(D) - 1 \le \frac{\deg D}{2}.$$
Equality holds if and only if one of the following holds:

1. $D = 0$;
2. $D$ is linearly equivalent to $K$;
3. $X$ is [[hyperelliptic|5SB8EKSQRN]], and $D$ is linearly equivalent to a multiple of a fibre of the degree-$2$ map $X \to \mathbb{P}^1$.

## Remarks

The inequality comes from adding linear systems.
Since $D$ and $K - D$ are both effective up to linear equivalence, the addition map $\abs{D} \times \abs{K - D} \to \abs{K}$ is finite-to-one, so $\dim \abs{D} + \dim \abs{K - D} \le \dim \abs{K} = g - 1$.
Adding the [[Riemann–Roch theorem|WMVAT9MBZ1]] $\ell(D) - \ell(K - D) = \deg D - g + 1$ gives $2(\ell(D) - 1) \le \deg D$.
The hypothesis that $D$ is special is needed: for $\deg D > 2g - 2$, Riemann–Roch gives $\ell(D) - 1 = \deg D - g$, which exceeds $\deg D / 2$ once $\deg D > 2g$.
Example: on a hyperelliptic curve with degree-$2$ map divisor $g^1_2$, the divisor $D = r \cdot g^1_2$ with $r \le g - 1$ has $\ell(D) = r + 1$ and $\deg D = 2r$, so equality holds.

## Explanations

### L1 human

A special divisor is one that is still small compared to the canonical divisor.
Clifford's theorem bounds how many functions can have poles bounded by such a divisor: the dimension of the linear system is at most half the degree.
So small divisors cannot move in large families.
The bound is reached only in trivial cases and on hyperelliptic curves.

### L2 human

Riemann–Roch computes $\ell(D)$ exactly for nonspecial divisors, and Clifford's theorem is the first general bound in the special range $0 \le \deg D \le 2g - 2$.
It is used to show that a non-hyperelliptic curve has a canonical embedding, and that a divisor of degree $2$ moving in a pencil forces the curve to be hyperelliptic.
Brill–Noether theory refines the bound for a general curve, where the true dimensions are much smaller.
