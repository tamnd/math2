---
tag: HC5NDQ3DTS
kind: statement
role: theorem
name: Capelli's theorem
msc: ["12E05", 12F05]
uses: [0QA8CHH8MG, 00X2A9G9W3]
about: [00X2A9G9W3]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_polynomial
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]], let $a \in K$ and let $n \ge 2$ be an integer.
The polynomial $x^n - a$ is [[irreducible|00X2A9G9W3]] in $K[x]$ if and only if both of the following hold:

1. for every prime $p$ dividing $n$, $a$ is not of the form $b^p$ with $b \in K$;
2. if $4$ divides $n$, then $a$ is not of the form $-4 c^4$ with $c \in K$.

## Remarks

The conditions are necessary: if $a = b^p$ with $p \mid n$, then $y^p - b^p$ has the factor $y - b$, and $y = x^{n/p}$ gives a factor of $x^n - a$.
If $a = -4c^4$ and $4 \mid n$, the identity $y^4 + 4c^4 = (y^2 + 2cy + 2c^2)(y^2 - 2cy + 2c^2)$ with $y = x^{n/4}$ gives a factorisation.
The proof of sufficiency first treats $n$ prime with a norm argument, then prime powers, and combines them with the multiplicativity of degrees in towers of extensions.
Example: $x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2)$ over $\Q$, although $-4$ is not a square in $\Q$; this is the case $c = 1$ of clause 2.
Example: $x^n - 2$ is irreducible over $\Q$ for every $n \ge 1$.
For $n$ odd, clause 2 is empty and the test reduces to $p$-th powers for the primes $p \mid n$.

## Explanations

### L1 human

The polynomial $x^n - a$ factors in two obvious ways: when $a$ is a perfect $p$-th power for a prime $p$ dividing $n$, and in one special case built from $x^4 + 4$.
Capelli's theorem says that there are no other ways.

### L2 human

The theorem is the basic tool to study binomial equations $x^n = a$ and the radical extensions $K(\sqrt[n]{a})$.
It gives the degree $[K(\sqrt[n]{a}) : K] = n$ when the two clauses hold.
This is used in the theory of [[radical extensions|V74WMGQQ9D]] and of Kummer extensions.
