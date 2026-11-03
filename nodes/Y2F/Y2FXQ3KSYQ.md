---
tag: Y2FXQ3KSYQ
kind: conjecture
name: MDS conjecture
msc: [94B65, "51E21", 94B05]
uses: [3H9XZA1SR5, 0ZXZ82FTX2]
about: [3H9XZA1SR5]
sources:
  - url: https://en.wikipedia.org/wiki/Singleton_bound
history:
  posed_by: Beniamino Segre
  first_stated: "1955"
---

## Statement

Let $q$ be a prime power and let $k$ be an integer with $2 \le k \le q$.
Suppose there is a linear [[MDS code|3H9XZA1SR5]] of length $n$ and dimension $k$ over the [[finite field|0ZXZ82FTX2]] $\F_q$.
If $q$ is odd, or if $k \notin \set{3, q - 1}$, then $n \le q + 1$.
If $q$ is even and $k = 3$ or $k = q - 1$, then $n \le q + 2$.

## Remarks

The bounds would be sharp.
Extended Reed–Solomon codes give MDS codes of length $q + 1$ for every $k \le q + 1$.
For even $q$ there are MDS codes of length $q + 2$ with $k = 3$ and with $k = q - 1$.
In geometric terms, the columns of a generator matrix of an MDS code form an arc in a projective space over $\F_q$.
An arc is a set of points of which any $k$ are in general position, and the question goes back to Segre's study of arcs.
The conjecture is known for $k = 2$ and $k = 3$.
Simeon Ball proved it in 2012 when $q$ is a prime.
It is open in general.

## Explanations

### L1 human

MDS codes are the best possible codes for their size, but over a field with $q$ elements they cannot be very long.
The conjecture says exactly how long they can be: one more than $q$, apart from two special cases when $q$ is even.
It is proved for prime $q$ but still open when $q$ is a power of a prime with exponent at least two.
