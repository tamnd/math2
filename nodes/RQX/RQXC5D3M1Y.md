---
tag: RQXC5D3M1Y
kind: concept
name: Injective tensor product
msc: [46B28, 46M05]
specializes: [0BF2DE2SYK]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_tensor_product
same_as:
  wikidata: Q1663619
  wikipedia: Injective tensor product
---

## Summary

Let $X$ and $Y$ be Banach spaces.
Their injective tensor product is the completion of the algebraic [[tensor product|0BF2DE2SYK]] $X \otimes Y$ for the smallest reasonable norm on it.
This norm sees a tensor only through its values on pairs of functionals of norm at most $1$.
It describes spaces of continuous vector-valued functions: $C(K)$ with the injective tensor product by $X$ is the space of continuous functions from $K$ to $X$.
With the [[projective tensor product|685ZV73JJ8]] it is one of the two extreme tensor norms of Grothendieck's theory.

## Explanations

### L1 human

A tensor $u = \sum_i x_i \otimes y_i$ gives a number $\sum_i f(x_i) g(y_i)$ for each pair of functionals $f$ and $g$.
The injective norm is the largest such number when $f$ and $g$ have norm at most $1$.
If $X$ and $Y$ are spaces of continuous functions on compact spaces $K$ and $L$, the tensor becomes the function $(s, t) \mapsto \sum_i x_i(s) y_i(t)$ on $K \times L$.
Then the injective norm is just the maximum of its absolute value.
