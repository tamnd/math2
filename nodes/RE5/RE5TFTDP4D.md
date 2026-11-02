---
tag: RE5TFTDP4D
kind: definition
name: Quantifier elimination
msc: [03C10]
defines: 7FDDXV3JK7
uses: [92SWXST1ZM, HYJ10AF6RT, WDVVEYD6AT, FSJ9NGRRPA]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]] and let $T$ be an $L$-[[theory|92SWXST1ZM]].
The theory $T$ *has quantifier elimination* if, for every $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$, there is a quantifier-free $L$-formula $\psi(x_1, \dots, x_n)$ such that
$$T \models \forall x_1 \cdots \forall x_n \, \bigl(\varphi(x_1, \dots, x_n) \leftrightarrow \psi(x_1, \dots, x_n)\bigr).$$

## Remarks

For sentences ($n = 0$) one allows the quantifier-free sentences $\top$ and $\bot$ when $L$ has no constant symbols.
It suffices to treat formulas of the form $\exists y \, \chi(x_1, \dots, x_n, y)$ with $\chi$ a conjunction of atomic and negated atomic formulas.

Example: the theory of dense linear orders without endpoints, in the signature $\set{<}$, has quantifier elimination.
For instance, $\exists y \, (x_1 < y \wedge y < x_2)$ is equivalent to $x_1 < x_2$ by density, and $\exists y \, (x_1 < y)$ is equivalent to $x_1 = x_1$ since there is no greatest element.

Non-example: the theory of $(\R, +, \cdot, 0, 1)$, without the order symbol, does not have quantifier elimination.
The formula $\exists y \, (x = y \cdot y)$ defines $[0, \infty)$, which is infinite and co-infinite.
A quantifier-free formula in $x$ is a Boolean combination of polynomial equations $p(x) = 0$, so it defines a finite or cofinite subset of $\R$.
With the order symbol added, the theory has quantifier elimination; this is [[Tarski's theorem|FSJ9NGRRPA]].
