---
tag: 9PN6QZKFCB
kind: definition
name: Mixed volume
msc: [52A39]
defines: QB3Q5FBJ08
uses: [437FSG3419, SXS6D87PHE, 2Z2QVWZ262, 2C3PAQ7H50]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_volume
---

## Definition

Let $n \ge 1$ and let $\mathcal{K}^n$ be the set of nonempty compact convex subsets of $\R^n$ (the [[convex bodies|437FSG3419]] in the broad sense).
Let $\operatorname{vol}$ be [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$.
There is a unique function $V \colon (\mathcal{K}^n)^n \to \R$ such that:

1. $V$ is symmetric in its $n$ arguments;
2. for every $r \ge 1$, all $K_1, \dots, K_r \in \mathcal{K}^n$ and all $\lambda_1, \dots, \lambda_r \ge 0$,
$$\operatorname{vol}(\lambda_1 K_1 + \cdots + \lambda_r K_r) = \sum_{i_1 = 1}^{r} \cdots \sum_{i_n = 1}^{r} V(K_{i_1}, \dots, K_{i_n}) \, \lambda_{i_1} \cdots \lambda_{i_n},$$
where the sum on the left is the [[Minkowski sum|SXS6D87PHE]].

The number $V(K_1, \dots, K_n)$ is the *mixed volume* of $K_1, \dots, K_n$.

## Remarks

The left side of clause 2 is a [[homogeneous polynomial|2C3PAQ7H50]] of degree $n$ in $\lambda_1, \dots, \lambda_r$; this is the theorem of Minkowski that makes the definition possible.
An explicit formula is
$$V(K_1, \dots, K_n) = \frac{1}{n!} \sum_{\emptyset \ne J \subseteq \set{1, \dots, n}} (-1)^{n - \abs{J}} \operatorname{vol}\Big(\sum_{j \in J} K_j\Big).$$
Mixed volumes are nonnegative, invariant under translating each argument, linear in each argument for Minkowski addition with nonnegative scalars, and monotone under inclusion.
Also $V(K, \dots, K) = \operatorname{vol}(K)$.

Example: $n = 2$, $K$ a compact convex set of area $A$ and perimeter $L$, and $D$ the closed unit disk.
The area of $K + tD$ is $A + L t + \pi t^2$, while clause 2 gives $A + 2 V(K, D)\, t + \pi t^2$.
So $V(K, D) = L / 2$.

Non-example: without clause 1 the coefficients are not unique.
For $n = 2$ one may move all of the coefficient $2 V(K_1, K_2)$ to the term $(i_1, i_2) = (1, 2)$ and put $0$ at $(2, 1)$, which still satisfies clause 2.
