---
tag: H1Z2TKY3EQ
kind: definition
name: Convergence of an infinite product
msc: [40A20]
defines: PCYRWA7SYB
uses: [RZ0Z2BTMT4, 0AZ3R52593]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_product
---

## Definition

Let $(a_n)_{n \ge 1}$ be a sequence of complex numbers, and consider the [[infinite product|RZ0Z2BTMT4]] $\prod_{n=1}^{\infty} a_n$.
The product converges if there is an index $m$ such that:

1. $a_n \ne 0$ for all $n \ge m$;
2. the partial products $q_N = \prod_{n=m}^{N} a_n$ [[converge|0AZ3R52593]] to a limit $q$ as $N \to \infty$;
3. $q \ne 0$.

The value of the product is then $\prod_{n=1}^{\infty} a_n = a_1 \cdots a_{m-1} \, q$.
A product that does not converge diverges.

## Remarks

The value does not depend on the choice of $m$.
If the product converges, then $a_n \to 1$, since $a_n = q_n / q_{n-1}$ for $n > m$.
Example: $\prod_{n=2}^{\infty} (1 - 1/n^2)$ converges with value $\tfrac12$.
With $m = 2$, the partial products are $\prod_{n=2}^{N} \frac{(n-1)(n+1)}{n^2} = \frac{N+1}{2N}$, which tend to $\tfrac12 \ne 0$.
Non-example: $\prod_{n=2}^{\infty} (1 - 1/n)$ has partial products $1/N \to 0$, so it fails clause 3 for every $m$ and diverges.
The product $0 \cdot 2 \cdot 2 \cdot 2 \cdots$ also diverges, because its tail products are growing powers of $2$ with no limit.

## Explanations

### L1 human

A convergent product may contain a few zero factors, but the rest must multiply to a nonzero limit.
