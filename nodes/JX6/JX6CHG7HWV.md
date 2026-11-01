---
tag: JX6CHG7HWV
kind: definition
name: Field of rational functions
msc: [12F20, 13B30]
defines: 4V81611P9N
uses: [0QA8CHH8MG, 0Q9EZS90GY, 0VF11ZTTMD]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_function
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]] and let $K[x]$ be the [[polynomial ring|0Q9EZS90GY]] in one variable $x$ over $K$.
The field of rational functions $K(x)$ is the [[field of fractions|0VF11ZTTMD]] of $K[x]$.
Its elements are the fractions $p/q$ with $p, q \in K[x]$ and $q \ne 0$, where $p/q = p'/q'$ if and only if $p q' = p' q$.
More generally, for variables $x_1, \dots, x_n$, the field $K(x_1, \dots, x_n)$ is the field of fractions of $K[x_1, \dots, x_n]$.

## Remarks

Example: $\frac{x^2 - 1}{x - 1} = \frac{x + 1}{1}$ in $\Q(x)$, since $(x^2 - 1) \cdot 1 = (x + 1)(x - 1)$.
Non-example: no element $p/q$ of $\Q(x)$ satisfies $(p/q)^2 = x$, since $p^2 = x q^2$ would give $2 \deg p = 1 + 2 \deg q$, which is impossible.
So $K(x) \supset K$ is a field extension in which $x$ is [[transcendental|0NQMZ89X4A]] over $K$.
An element of $K(x)$ is a formal fraction, not a function on $K$: over $\F_2$, the fraction $\frac{1}{x^2 + x}$ is a nonzero element, although $x^2 + x$ vanishes at every point of $\F_2$.
Over $\R$ or $\C$, the elements correspond to [[rational functions|0WCZH4AFMT]] in the sense of analysis.

## Explanations

### L1 human

You build $K(x)$ from polynomials in the same way as you build the rational numbers from the integers.
Every nonzero fraction of polynomials has an inverse, obtained by turning it upside down.
