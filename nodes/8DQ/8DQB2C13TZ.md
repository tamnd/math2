---
about:
- 05XT5AVJBK
- TKZAV3KR86
kind: statement
msc:
- 44A10
name: Uniqueness of the Laplace transform for continuous functions of exponential order
role: theorem
sources:
- url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-laplace.tex#L331
  locator: ch-laplace.tex:331
tag: 8DQB2C13TZ
uses:
- 05XT5AVJBK
- TKZAV3KR86
---

## Statement

Let $f$ and $g$ be continuous functions on $[0, \infty)$. Assume that both are [[functions of exponential order|TKZAV3KR86]].
Let $F$ and $G$ be their [[Laplace transforms|05XT5AVJBK]].
Suppose there is a real constant $C$ such that $F(s) = G(s)$ for every $s > C$.
Then $f(t) = g(t)$ for every $t \geq 0$.

## Remarks

So a continuous function of exponential order is determined by its transform on any right half-line.
The continuity is needed for equality at every point. Changing a function at a single point does not change its transform.
