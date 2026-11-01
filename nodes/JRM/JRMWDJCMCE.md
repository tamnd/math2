---
tag: JRMWDJCMCE
kind: definition
name: Conway polynomial
msc: [11T06, "12E20"]
defines: NQQBESGPA4
uses: [08RTDHX1SK, HQ7KMZYPSQ, 0BDX4MBKT4]
sources:
  - url: https://en.wikipedia.org/wiki/Conway_polynomial_(finite_fields)
---

## Definition

Let $p$ be a prime.
Order the [[monic|0BDX4MBKT4]] polynomials of degree $n$ over $\F_p$ as follows: write such a polynomial as
$$x^n - a_{n-1} x^{n-1} + a_{n-2} x^{n-2} - \cdots + (-1)^n a_0$$
with $a_i \in \set{0, 1, \dots, p - 1}$, and compare the sequences $(a_{n-1}, a_{n-2}, \dots, a_0)$ lexicographically.
The *Conway polynomial* $C_{p,n}$ is defined by induction on $n \ge 1$.
It is the least monic polynomial $f$ of degree $n$ over $\F_p$ for this order such that:

1. $f$ is a [[primitive polynomial|HQ7KMZYPSQ]] over $\F_p$;
2. for every divisor $m$ of $n$ with $m < n$, the polynomial $f(x)$ divides $C_{p,m}\left(x^{(p^n - 1)/(p^m - 1)}\right)$.

## Remarks

Clause 2 says: if $\alpha$ is a root of $C_{p,n}$, then $\alpha^{(p^n - 1)/(p^m - 1)}$ is a root of $C_{p,m}$.
So the copies of $\F_{p^m}$ inside the models of $\F_{p^n}$ match for all $m$ dividing $n$.
Example: $C_{2,3} = x^3 + x + 1$.
The primitive cubics over $\F_2$ are $x^3 + x + 1$ and $x^3 + x^2 + 1$, with sequences $(0, 1, 1)$ and $(1, 0, 1)$.
Clause 2 holds for both, since $C_{2,1} = x + 1$ has root $1$ and every power of $1$ is $1$.
Non-example: $x^4 + x^3 + x^2 + x + 1$ is irreducible over $\F_2$ but fails clause 1, so it is not $C_{2,4}$, which is $x^4 + x + 1$.
For $p = 5$, $C_{5,1} = x - 2 = x + 3$, since $1$ is not a primitive root modulo $5$ and $2$ is.
