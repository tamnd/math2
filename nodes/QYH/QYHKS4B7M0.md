---
tag: QYHKS4B7M0
kind: definition
name: Herman ring
msc: [37F50, 37F10]
defines: HZX6Q514X8
uses: [C0N0XGC6GK, 0XDK9CGYKJ, 0CW52NV5TC, 0YYT36R4YD, 0DZXAXEJQ9]
sources:
  - url: https://en.wikipedia.org/wiki/Herman_ring
---

## Definition

Let $f \colon \hat{\C} \to \hat{\C}$ be a [[rational function|0XDK9CGYKJ]] of degree at least $2$.
A *Herman ring* of $f$ is a component $U$ of the [[Fatou set|C0N0XGC6GK]] of $f$ with the following properties.

1. There is $p \ge 1$ with $f^p(U) = U$.
2. There are $r > 1$ and a [[conformal map|0YYT36R4YD]] $\varphi$ from $U$ onto the round [[annulus|0CW52NV5TC]] $A_r = \set{w \in \C : 1 < \abs{w} < r}$.
3. There is an [[irrational number|0DZXAXEJQ9]] $\theta$ with $\varphi(f^p(z)) = e^{2\pi i \theta} \varphi(z)$ for all $z \in U$.

## Remarks

The circles $\abs{w} = s$ with $1 < s < r$ pull back to invariant closed curves of $f^p$ in $U$.
Non-example: a polynomial $P$ has no Herman ring.
If $U$ were one, an invariant curve $\gamma$ in $U$ would bound a disc $D$, and by the maximum principle the iterates of $P$ would be bounded on $D$.
Then $D$ would lie in the Fatou set, so $U$ could not be a component of it with a hole.
Herman constructed the first examples of rational maps with Herman rings.
Shishikura later built them by quasiconformal surgery from maps with Siegel discs.
