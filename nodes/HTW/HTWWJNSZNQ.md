---
tag: HTWWJNSZNQ
kind: example
name: Dyadic transformation
msc: ["37E05", 37A05, 37A25]
instance_of: [556WBDAHNP, S3RJQ9CX2P]
uses: [2Z2QVWZ262, D33JK3AXRZ, X1D1C7VH6P]
sources:
  - url: https://en.wikipedia.org/wiki/Dyadic_transformation
same_as:
  wikidata: Q826704
  wikipedia: Dyadic transformation
---

## Example

The *dyadic transformation*, or *doubling map*, is
$$T \colon [0, 1) \to [0, 1), \qquad T(x) = 2x \bmod 1.$$

It is a [[measure-preserving transformation|556WBDAHNP]] for [[Lebesgue measure|2Z2QVWZ262]] $\lambda$.
Check on an interval $[a, b) \subseteq [0, 1)$:
$$T^{-1}[a, b) = \Big[\frac{a}{2}, \frac{b}{2}\Big) \cup \Big[\frac{a+1}{2}, \frac{b+1}{2}\Big),$$
a disjoint union of two intervals of length $(b - a)/2$, so $\lambda(T^{-1}[a, b)) = b - a$.

Write $x = \sum_{n \ge 1} x_n 2^{-n}$ in binary, with digits $x_n \in \set{0, 1}$ not eventually all equal to $1$.
Then $T$ deletes the first digit: $T(x) = \sum_{n \ge 1} x_{n+1} 2^{-n}$.
Under $\lambda$ the digits are independent fair coin tosses.
So the binary expansion is an isomorphism, up to null sets, from $T$ to the one-sided [[Bernoulli scheme|D33JK3AXRZ]] $B(1/2, 1/2)$.
Hence $T$ is [[mixing|S3RJQ9CX2P]], and its [[Kolmogorov–Sinai entropy|X1D1C7VH6P]] is $\log 2$.

The map is not invertible: each point has two preimages.

## Explanations

### L1 human

Double the number and throw away the whole part.
In binary, this is the same as shifting the digits one step to the left and forgetting the first digit.
So the future of a point is written in its digits, and for a typical number these digits look like fair coin tosses.
That is why such a simple formula gives a fully random system.
