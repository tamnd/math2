---
tag: 4SNJWQBAHF
kind: definition
name: Almost convergence
msc: [40H05, 46A45]
defines: 8HTHB1QPZY
uses: [SYF2ND6J97, 0A8JNBGT2Z, 0W4CN9E2W5]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_limit
---

## Definition

Let $x = (x_n)_{n \ge 1}$ be a [[bounded sequence|0A8JNBGT2Z]] of real numbers and let $L$ be a real number.
The sequence $x$ is *almost convergent* to $L$ if $\varphi(x) = L$ for every [[Banach limit|SYF2ND6J97]] $\varphi$.

## Remarks

Example: every [[convergent sequence|0W4CN9E2W5]] with limit $L$ is almost convergent to $L$, because every Banach limit agrees with the ordinary limit on convergent sequences.

Example: $x = (1, 0, 1, 0, \dots)$ is almost convergent to $1/2$.
Let $S$ be the shift and $\mathbf{1} = (1, 1, \dots)$.
Then $x + Sx = \mathbf{1}$, so for every Banach limit $\varphi$ one has $\varphi(x) + \varphi(Sx) = 1$.
Since $\varphi(Sx) = \varphi(x)$, this gives $\varphi(x) = 1/2$.

Non-example: let $x_n = 1$ if $4^k \le n < 2 \cdot 4^k$ for some integer $k \ge 0$, and $x_n = 0$ otherwise.
This sequence has longer and longer blocks of ones and of zeros, and different Banach limits give it different values.
This follows from Lorentz's characterization, since averages over long blocks of consecutive terms can be $0$ or $1$.

The limit $L$ is unique when it exists, because Banach limits exist.
