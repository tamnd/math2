---
tag: 0QWR8WTZEW
kind: statement
role: proposition
name: Every element of a finite field of order q satisfies x^q = x
msc: ["12E20"]
uses: [08RTDHX1SK, 05THZKR9AN]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Multiplicative structure
---

## Statement

Let $F$ be a [[finite field|08RTDHX1SK]] of order $q$.
Then $a^q = a$ for every $a \in F$, and
$$x^q - x = \prod_{a \in F} (x - a) \quad \text{in } F[x].$$

## Remarks

The proof: the [[group of units|05THZKR9AN]] $F^\times$ has order $q - 1$, so $a^{q-1} = 1$ for $a \neq 0$, by [[Lagrange's theorem|3C53TD]]. Then $a^q = a$ for all $a$, also for $a = 0$.
So the $q$ elements of $F$ are $q$ distinct roots of $x^q - x$, which has degree $q$. This gives the factorisation.
For $q = p$ prime, $a^p = a$ in $\mathbb{Z}/p\mathbb{Z}$ is Fermat's little theorem.

## Explanations

### L1 human

In a field with $q$ elements, raising to the power $q$ changes nothing.
So the polynomial $x^q - x$ has every element of the field as a root.
