---
tag: XXQ378NQE2
kind: definition
name: Factorization of polynomials over finite fields
msc: [11T06, "12E20", 11Y16]
defines: XNE7F0BAGE
uses: [08RTDHX1SK, EFDBS6ZME8, 99J1WXG3F7, 0AD4VS02H3]
sources:
  - url: https://en.wikipedia.org/wiki/Factorization_of_polynomials_over_finite_fields
---

## Definition

Let $\F_q$ be the [[finite field|08RTDHX1SK]] with $q$ elements and let $f \in \F_q[x]$ be a nonzero polynomial.
Factoring $f$ over $\F_q$ means computing its [[factorization into irreducibles|EFDBS6ZME8]] $f = c \, p_1^{e_1} \cdots p_k^{e_k}$ in $\F_q[x]$.
The standard algorithms do this in three stages:

1. square-free factorization: write the monic part of $f$ as $g_1 g_2^2 \cdots g_s^s$, with the $g_i$ square-free and pairwise coprime, using $\gcd(f, f')$ for the [[formal derivative|0AD4VS02H3]] $f'$;
2. distinct-degree factorization: for a square-free monic $g$, compute for each $d \ge 1$ the product $h_d$ of the monic irreducible factors of $g$ of degree $d$;
3. equal-degree factorization: split each $h_d$ into its irreducible factors of degree $d$.

## Remarks

Stage 2 uses that $x^{q^d} - x$ is the product of all monic irreducible polynomials in $\F_q[x]$ whose degree divides $d$.
So $h_1 = \gcd(g, x^q - x)$, and $h_d$ is the [[gcd|99J1WXG3F7]] of $x^{q^d} - x$ with $g$ divided by $h_1 \cdots h_{d-1}$.
In stage 1, if $f' = 0$ then $f$ is a $p$-th power, where $p$ is the characteristic, since every element of $\F_q$ is a $p$-th power.
Stage 3 is usually done with a randomised method, such as the Cantor–Zassenhaus algorithm; [[Berlekamp's algorithm|EM8MFGFAGN]] is a deterministic alternative to stages 2 and 3.
Example: over $\F_2$, $g = x^3 + 1$ is square-free, $\gcd(g, x^2 - x) = x + 1$, so $h_1 = x + 1$ and $h_2 = x^2 + x + 1$.
Non-example: $(x + 1)(x^3 + 1) = (x + 1)^2 (x^2 + x + 1)$ is not square-free, so stage 2 does not apply before stage 1.

## Explanations

### L1 human

First take out repeated factors, then sort the factors by degree, then separate factors of the same degree.
Each stage uses only greatest common divisors and powers modulo $f$.
