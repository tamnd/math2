---
tag: ZWPWF6NJC3
kind: statement
role: theorem
name: Mason–Stothers theorem
msc: [11C08, 12D05]
uses: [0SDC934R52, 0EGN1E1JPB, 03FKX7Z5DC, 04C5ZBG1WT]
about: [0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Mason%E2%80%93Stothers_theorem
same_as:
  wikidata: Q6783821
  wikipedia: Mason–Stothers theorem
---

## Statement

Let $K$ be a [[field|04C5ZBG1WT]] and let $a, b, c \in K[t]$ be polynomials in the [[polynomial ring|0SDC934R52]] with $a + b = c$.
Assume that $a$, $b$, $c$ are pairwise coprime and that not all of the [[formal derivatives|0EGN1E1JPB]] $a'$, $b'$, $c'$ are zero.
For a nonzero polynomial $f$, let $\operatorname{rad}(f)$ be the product of the distinct monic [[irreducible|03FKX7Z5DC]] factors of $f$.
Then
$$\max\set{\deg a, \deg b, \deg c} \le \deg \operatorname{rad}(abc) - 1.$$

## Remarks

When $K$ is algebraically closed, $\deg \operatorname{rad}(abc)$ is the number of distinct roots of $abc$.
If $K$ has characteristic $0$, the hypothesis on derivatives just says that $a$, $b$, $c$ are not all constant.
A short proof, due to Noah Snyder, studies the Wronskian $ab' - a'b$: it is nonzero, it is divisible by $abc/\operatorname{rad}(abc)$, and its degree is less than $\deg a + \deg b$.
Example: over $\Q$, take $a = t^2$, $b = 2t + 1$ and $c = (t + 1)^2$; then $\operatorname{rad}(abc) = t(2t + 1)(t + 1)$ has degree $3$, and the bound $2 \le 3 - 1$ is sharp.
The derivative hypothesis is necessary: over a field of characteristic $p > 0$, take $a = t^p$, $b = 1$, $c = (t + 1)^p$; then $a' = b' = c' = 0$, the radical has degree $2$, and $\deg c = p > 1$.
A consequence: for $n \ge 3$ there are no pairwise coprime polynomials $x, y, z$ over $\C$, not all constant, with $x^n + y^n = z^n$.

## Explanations

### L1 human

If two polynomials add up to a third, and they share no common factor, then the three together must have many different roots.
More precisely, the number of distinct roots is larger than every one of the degrees.
So you cannot make all three polynomials into high powers of a few simple factors.

### L2 human

The theorem is the polynomial form of the [[abc conjecture|G7JH2NXPC0]], with the degree playing the role of the logarithm of the size and the radical counting distinct prime factors.
In contrast with the integer case, it has a short and complete proof by differentiation.
It gives quick proofs of Fermat's Last Theorem for polynomials and of related results on equations such as $x^2 - y^3 = $ a polynomial.
