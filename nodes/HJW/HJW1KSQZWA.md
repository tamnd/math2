---
tag: HJW1KSQZWA
kind: definition
name: Berlekamp's algorithm
msc: [11T06, 11Y16, 68W30]
defines: EM8MFGFAGN
uses: [08RTDHX1SK, 0BDX4MBKT4, 99J1WXG3F7, 0PQ2GGY1QV, 0W97J8QED7]
sources:
  - url: https://en.wikipedia.org/wiki/Berlekamp%27s_algorithm
---

## Definition

Let $\F_q$ be the [[finite field|08RTDHX1SK]] with $q$ elements and let $f \in \F_q[x]$ be a [[monic|0BDX4MBKT4]] square-free polynomial of degree $n \ge 1$.
Let $V$ be the $\F_q$-vector space of polynomials of degree less than $n$.
The Berlekamp subalgebra of $f$ is
$$B = \set{g \in V : g^q \equiv g \pmod{f}}.$$
Berlekamp's algorithm factors $f$ as follows.

1. Compute the matrix $Q$ of the $\F_q$-linear map $V \to V$, $h \mapsto h^q \bmod f$, and a basis of $B$ as the [[null space|0PQ2GGY1QV]] of $Q - I$.
2. If $\dim B = 1$, then $f$ is irreducible.
3. Otherwise take $g \in B$ of positive degree; then $f = \prod_{s \in \F_q} \gcd(f, g - s)$, and at least two of these factors have positive degree.
4. Apply step 3 to the factors, with other elements of $B$, until there are $\dim B$ factors.

## Remarks

By the [[Chinese remainder theorem|0W97J8QED7]], $B \cong \F_q^k$, where $k$ is the number of irreducible factors of $f$, so $\dim B = k$.
Step 3 holds because $g^q - g = \prod_{s \in \F_q} (g - s)$ and $f$ divides $g^q - g$; the factors $g - s$ are pairwise coprime, and none of them is divisible by $f$.
Example: $f = x^2 + 1$ over $\F_5$; since $x^5 \equiv x \pmod{f}$, $B = V$ has dimension $2$, and $g = x$ gives $\gcd(f, x - 2) = x - 2$ and $\gcd(f, x - 3) = x - 3$.
Non-example: $f = x^2 + 1$ over $\F_3$; since $x^3 \equiv -x \pmod{f}$, $(a + bx)^3 \equiv a - bx$, so $B$ is the constants, $\dim B = 1$, and $f$ is irreducible.
The algorithm needs $f$ square-free; a repeated factor is first removed with $\gcd(f, f')$.
The running time is polynomial in $n$ and $q$, so it suits small fields; for large $q$ randomised variants are used.

## Explanations

### L1 human

The algorithm computes the $q$-th power map on remainders modulo $f$ and finds its fixed points by Gaussian elimination.
Each fixed point that is not a constant lets one split $f$ with greatest common divisors.
