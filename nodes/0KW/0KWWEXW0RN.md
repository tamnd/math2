---
tag: 0KWWEXW0RN
kind: statement
role: theorem
name: Reduction modulo p test for irreducibility
msc: ["12E05"]
uses: [00X2A9G9W3, 0BDX4MBKT4, 0QFV5Y1Z5X]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_polynomial
    locator: Over the integers and finite fields
---

## Statement

Let $f \in \mathbb{Z}[x]$ be a [[monic polynomial|0BDX4MBKT4]] and let $p$ be a prime number.
Let $\bar{f} \in \mathbb{F}_p[x]$ be the polynomial whose coefficients are those of $f$ modulo $p$.
If $\bar{f}$ is [[irreducible|00X2A9G9W3]] in $\mathbb{F}_p[x]$, then $f$ is irreducible in $\mathbb{Z}[x]$ and in $\mathbb{Q}[x]$.

## Remarks

The proof: a factorisation $f = g h$ into monic factors of positive degree gives $\bar{f} = \bar{g} \bar{h}$, with $\deg \bar{g} = \deg g$ and $\deg \bar{h} = \deg h$.
Irreducibility in $\mathbb{Q}[x]$ then follows by [[Gauss's lemma|0QFV5Y1Z5X]].
The converse is false: $x^4 + 1$ is irreducible over $\mathbb{Q}$, but it is reducible modulo every prime.
Example: $x^3 + x + 1$ has no root in $\mathbb{F}_2$, so it is irreducible over $\mathbb{F}_2$, and so over $\mathbb{Q}$.

## Explanations

### L1 human

A factorisation over the integers stays a factorisation after reduction modulo $p$.
So if the reduced polynomial does not factor, the original one does not factor either.
Over a small finite field, you can check irreducibility by a finite search.
