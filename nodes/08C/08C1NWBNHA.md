---
tag: 08C1NWBNHA
kind: statement
role: theorem
name: Product of primitive polynomials is primitive
msc: [13F20]
uses: [0SP14DZN0G, 06YMXJMXYS, 0MNHXBSX3M]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_lemma_(polynomials)
    locator: Statements for unique factorization domains
---

## Statement

Let $R$ be a [[unique factorisation domain|06YMXJMXYS]] and let $f, g \in R[x]$ be [[primitive polynomials|0SP14DZN0G]].
Then $f g$ is primitive.

## Remarks

The proof: suppose an irreducible $p$ divides all the coefficients of $f g$. Since $p$ is [[prime|0MNHXBSX3M]], $R/(p)$ is an integral domain. The images of $f$ and $g$ in $(R/(p))[x]$ are nonzero, but their product is zero, which is a contradiction.
Many texts call this statement Gauss's lemma. The node [[Gauss's lemma|0QFV5Y1Z5X]] states the form about irreducibility.
Over $\mathbb{Z}$: $2x + 1$ and $3x + 2$ are primitive, and so is $6x^2 + 7x + 2$.

## Explanations

### L1 human

Suppose that no prime divides all the coefficients of $f$, and no prime divides all the coefficients of $g$.
Then no prime divides all the coefficients of $f g$.
The proof reduces the coefficients modulo a prime and uses that the result is an integral domain.
