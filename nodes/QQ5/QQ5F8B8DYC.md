---
tag: QQ5F8B8DYC
kind: definition
name: Differential operator between vector bundles
msc: [58J99, 47F05, 35A99]
defines: CGBX1N9V8H
uses: [F45VQ47GPV, P4DZM975BV, WWX7H5W1RP, 6DZETZ5T9G, 0ZHSTAG8ZY]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_operator
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, and let $\mathbb{K}$ be $\R$ or $\C$.
Let $E$ and $F$ be smooth [[vector bundles|P4DZM975BV]] over $M$ with fibres $\mathbb{K}^r$ and $\mathbb{K}^s$.
Write $\Gamma(E)$ for the space of smooth [[sections|WWX7H5W1RP]] of $E$.
Let $m \ge 0$ be an integer.
Consider a linear map $P \colon \Gamma(E) \to \Gamma(F)$.
It is a *differential operator of order at most $m$* if the following holds.
Let $(U, x_1, \ldots, x_n)$ be any chart of $M$ over which $E$ and $F$ are trivial.
In the trivialisations, there are smooth $A_\alpha \colon U \to \mathbb{K}^{s \times r}$ for $\abs{\alpha} \le m$ with
$$(P u)(x) = \sum_{\abs{\alpha} \le m} A_\alpha(x) \, \partial^\alpha u(x) \quad \text{for all } u \in \Gamma(E) \text{ and } x \in U,$$
where $u$ is written on $U$ as a function $U \to \mathbb{K}^r$.
The operator has *order $m$* if moreover some $A_\alpha$ with $\abs{\alpha} = m$ is not identically zero.

## Remarks

The condition does not depend on the charts and trivialisations.
A change of coordinates or of trivialisation turns a sum of this form into another one of the same order.
A differential operator is local: the value of $Pu$ near a point depends only on $u$ near that point.
By the Peetre theorem, linear local operators are, locally, differential operators.

Example: the [[exterior derivative|0ZHSTAG8ZY]] $d \colon \Gamma(\Lambda^k T^* M) \to \Gamma(\Lambda^{k+1} T^* M)$ is a differential operator of order $1$.
In a chart, $d(\sum_I f_I \, dx_I) = \sum_I \sum_{j} \partial_j f_I \, dx_j \wedge dx_I$, whose coefficients are constant matrices.

Non-example: on the circle $S^1 = \R / 2\pi\Z$, the map $u \mapsto \bigl(\int_0^{2\pi} u(t) \, dt\bigr) \cdot 1$ on functions is linear but not a differential operator.
It is not local: changing $u$ on a small interval changes $Pu$ everywhere.

## Explanations

### L1 human

A differential operator between bundles is, in every coordinate patch, a matrix of partial derivatives with smooth coefficients.
