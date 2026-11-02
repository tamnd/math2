---
tag: PZR6RC79ED
kind: statement
role: theorem
name: Quintuple product identity
msc: [11F27, 33D15]
uses: [RZ0Z2BTMT4]
about: [2F5CYQJVAF]
sources:
  - url: https://en.wikipedia.org/wiki/Quintuple_product_identity
same_as:
  wikidata: Q7272511
  wikipedia: Quintuple product identity
---

## Statement

Let $s, t \in \C$ with $\abs{s} < 1$ and $t \ne 0$.
Then
$$\prod_{n=1}^{\infty} \left(1 - s^n\right) \left(1 - s^n t\right) \left(1 - s^{n-1} t^{-1}\right) \left(1 - s^{2n-1} t^2\right) \left(1 - s^{2n-1} t^{-2}\right) = \sum_{n=-\infty}^{\infty} s^{(3n^2 + n)/2} \left( t^{3n} - t^{-3n-1} \right).$$

## Remarks

Both sides are holomorphic in $t$ on $\C \setminus \set{0}$, and the [[infinite product|RZ0Z2BTMT4]] converges because $\abs{s} < 1$.
Proof idea: as for the [[Jacobi triple product|JFP2DGMNXT]], one checks that both sides $F$ satisfy $F(st) = s^{-2} t^{-3} F(t)$.
This relation links the Laurent coefficients of index $k$ and $k + 3$, so it fixes them from three of them, and these are compared directly.
Example: at $t = 1$ the factor $1 - s^0 t^{-1}$ of index $n = 1$ vanishes, so the left side is $0$.
On the right the terms $s^{(3n^2+n)/2}(1 - 1)$ also vanish, so both sides agree.
The exponents $(3n^2 + n)/2$ are the generalized pentagonal numbers, as in [[Euler's pentagonal number theorem|R587SR9GNV]].

## Explanations

### L1 human

Like the triple product identity, this identity turns an infinite product into a sum, but now each step of the product has five factors.
The sum on the right is very sparse: only exponents of the form $(3n^2 + n)/2$ appear.
It is used to prove identities for partitions and for theta functions.

### L2 human

The identity has been rediscovered many times, and there are many equivalent forms obtained by changes of variables.
It can be derived from the [[Jacobi triple product|JFP2DGMNXT]], and it is a source of identities for theta functions and for the [[Dedekind eta function|MX3CVYMNDV]].
