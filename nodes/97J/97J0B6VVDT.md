---
tag: 97J0B6VVDT
kind: definition
name: Compact operator
msc: [47B07]
defines: M2NEP1K5AE
uses: [03J5RAKB30, 0RJF668P1T, 0R6EWFKRCF, 0QEAJB91GZ]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_operator
---

## Definition

Let $X$ and $Y$ be [[normed spaces|03J5RAKB30]] over $\R$ or $\C$ and let $T \colon X \to Y$ be a [[linear map|0RJF668P1T]].
Let $B_X = \set{x \in X : \norm{x} \le 1}$ be the closed unit ball of $X$.
The map $T$ is *compact* when the [[closure|0QEAJB91GZ]] of $T(B_X)$ is a [[compact subset|0R6EWFKRCF]] of $Y$.

## Remarks

Equivalent form: $T$ is compact if and only if for every bounded sequence $(x_n)$ in $X$, the sequence $(Tx_n)$ has a convergent subsequence in $Y$.
A compact operator is bounded, since a compact set is bounded.

Example: on $\ell^2$ let $T$ be the diagonal operator $T(x_1, x_2, \ldots) = (x_1, x_2/2, x_3/3, \ldots)$.
The finite-rank operators $T_N$ that keep the first $N$ entries of $Tx$ and set the rest to $0$ satisfy $\norm{T - T_N} \le 1/(N+1)$.
A norm limit of finite-rank operators into a Banach space is compact, because the image of the unit ball is then totally bounded; so $T$ is compact.

Non-example: the identity of $\ell^2$ is not compact.
The basis vectors $e_n$ lie in the unit ball, and $\norm{e_n - e_m} = \sqrt{2}$ for $n \ne m$, so $(e_n)$ has no convergent subsequence.

The set of compact operators on a Banach space is a closed two-sided ideal of the algebra of bounded operators, the [[ideal of compact operators|2WAZF1RV2Y]] in the Hilbert space case.
