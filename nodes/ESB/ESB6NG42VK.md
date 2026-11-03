---
tag: ESB6NG42VK
kind: definition
name: Normed division algebra
msc: [17A35, 17A75]
defines: DZ18QZHAMS
uses: [1SENAHZW5A, 0V2WP9B1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(composition_algebras)
---

## Definition

Let $A$ be an [[algebra|1SENAHZW5A]] over $\R$ with a unit $1 \neq 0$.
Let $\norm{\cdot}$ be a [[norm|0V2WP9B1MF]] on the real vector space $A$.
The pair is a *normed division algebra* if
$$\norm{xy} = \norm{x} \norm{y} \quad \text{for all } x, y \in A.$$

## Remarks

If $xy = 0$, then $\norm{x}\norm{y} = 0$, so $x = 0$ or $y = 0$.
Hence a finite-dimensional normed division algebra is a [[division algebra|8H3JKHAAHE]].
Example: $\C$ with $\norm{z} = \abs{z}$, since $\abs{zw} = \abs{z}\abs{w}$.
Non-example: the $2 \times 2$ real matrices with the operator norm satisfy only $\norm{xy} \le \norm{x}\norm{y}$; equality fails for $x = y = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, where $xy = 0$ but $\norm{x}\norm{y} = 1$.
In finite dimension the norm comes from an inner product, and the algebra is $\R$, $\C$, the quaternions or the octonions, by [[Hurwitz's theorem|WZ81H3S4KK]].
