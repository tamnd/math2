---
tag: KCBFS516DE
kind: definition
name: Multivariate formal power series
msc: [13F25, 13J05]
defines: 3E8ZG3NJYZ
uses: [0310REJJY8, 033WGN00BF, 07GNX8GCYP, 0XVEZDE9J8]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_power_series
    locator: Power series in several variables
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $n \ge 1$.
For $\alpha = (\alpha_1, \dots, \alpha_n) \in \N^n$ write $X^\alpha = X_1^{\alpha_1} \cdots X_n^{\alpha_n}$.
A *formal power series* in $X_1, \dots, X_n$ over $R$ is a family $(a_\alpha)_{\alpha \in \N^n}$ of elements of $R$, written $\sum_{\alpha} a_\alpha X^\alpha$.
The set $R[\![X_1, \dots, X_n]\!]$ of these series is a commutative ring with
$$\sum_\alpha a_\alpha X^\alpha + \sum_\alpha b_\alpha X^\alpha = \sum_\alpha (a_\alpha + b_\alpha) X^\alpha, \qquad \Big(\sum_\alpha a_\alpha X^\alpha\Big)\Big(\sum_\alpha b_\alpha X^\alpha\Big) = \sum_\alpha \Big(\sum_{\beta + \gamma = \alpha} a_\beta b_\gamma\Big) X^\alpha.$$

## Remarks

The inner sum in the product is finite, since each $\alpha$ has finitely many decompositions $\alpha = \beta + \gamma$ in $\N^n$.
For $n = 1$ this is the ring of [[formal power series|033WGN00BF]] in one variable, and $R[\![X_1, \dots, X_n]\!] \cong R[\![X_1, \dots, X_{n-1}]\!][\![X_n]\!]$.
Example: in $\Z[\![X, Y]\!]$ the series $f = \sum_{k \ge 0} (X + Y)^k$ satisfies $(1 - X - Y) f = 1$, because the coefficient of each monomial of degree $k \ge 1$ cancels between $(X + Y)^k$ and $(X + Y)(X + Y)^{k-1}$.
Non-example: $\sum_{k \ge 0} X^{-k} Y^k$ is not a formal power series in $X, Y$, since the exponents must lie in $\N^n$.
A series is a [[unit|0XVEZDE9J8]] if and only if its constant coefficient $a_{(0, \dots, 0)}$ is a unit of $R$.
