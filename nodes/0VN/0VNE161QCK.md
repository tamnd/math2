---
tag: 0VNE161QCK
kind: statement
role: proposition
name: Polynomials of degree two or three are irreducible iff they have no roots
msc: ["12E05"]
uses: [00X2A9G9W3, 00EHX6FWC0, 0K3MWA7DMC, 0T233AZ1GE]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_polynomial
    locator: Simple examples
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]] and let $f \in K[x]$ with $\deg f = 2$ or $\deg f = 3$.
Then $f$ is [[irreducible|00X2A9G9W3]] over $K$ if and only if $f$ has no [[root|00EHX6FWC0]] in $K$.

## Remarks

The proof: if $f = g h$ with $\deg g, \deg h \ge 1$, then $\deg g + \deg h \le 3$, so one factor has degree $1$. A factor $a x + b$ of degree $1$ gives the root $-b/a$. The [[factor theorem|0K3MWA7DMC]] gives the converse.
For example, $x^3 - 2$ has no root in $\mathbb{Q}$, so it is irreducible over $\mathbb{Q}$.
The statement fails in degree $4$: $(x^2 + 1)^2$ has no real root, but it is not irreducible over $\mathbb{R}$.

## Explanations

### L1 human

A factorisation of a polynomial of degree $2$ or $3$ must have a factor of degree $1$.
A factor of degree $1$ is the same as a root.
So to test irreducibility in low degree, you only look for roots.
