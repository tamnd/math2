---
tag: 5VK9NZM0R7
kind: definition
name: Indefinite sum
msc: [39A12, 39A70]
defines: SMAQN2N739
uses: [TXTR68V4R1]
sources:
  - url: https://en.wikipedia.org/wiki/Indefinite_sum
---

## Definition

Let $f \colon \R \to \R$ be a function, and let $\Delta$ be the [[forward difference operator|TXTR68V4R1]] with step $1$.
An *indefinite sum* of $f$ is a function $F \colon \R \to \R$ with $\Delta F = f$, that is,
$$F(x + 1) - F(x) = f(x) \quad \text{for all } x \in \R.$$
Another name is *antidifference*.
The same definition applies to functions $f \colon \Z \to \R$, with $F \colon \Z \to \R$.

## Remarks

Common notations are $\Delta^{-1} f$ and $\sum_x f(x)$.
Example: $F(x) = 2^x$ is an indefinite sum of $f(x) = 2^x$, since $2^{x+1} - 2^x = 2^x$.
Non-example: $F(x) = x^2/2$ is not an indefinite sum of $f(x) = x$, since $F(x + 1) - F(x) = x + \tfrac{1}{2}$.
Indefinite sums are not unique.
On $\Z$, two indefinite sums of $f$ differ by a constant.
On $\R$, two indefinite sums of $f$ differ by a function $C$ with $C(x + 1) = C(x)$ for all $x$, such as $\sin(2\pi x)$.
