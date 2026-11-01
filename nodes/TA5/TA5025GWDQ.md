---
tag: TA5025GWDQ
kind: definition
name: Integral quadratic form
msc: ["11E12", "11E20"]
defines: 2FQVQCTV88
uses: [0RBQS1JJCR, 0C4JS9RF5M, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
---

## Definition

Let $n \ge 1$ be an integer.
An *integral quadratic form* in $n$ variables is a [[quadratic form|0RBQS1JJCR]]
$$Q(x_1, \dots, x_n) = \sum_{1 \le i \le j \le n} a_{ij} x_i x_j$$
whose coefficients $a_{ij}$ all lie in the [[integers|0C4JS9RF5M]].
Two integral quadratic forms $Q$ and $Q'$ in $n$ variables are *equivalent* if $Q'(x) = Q(Mx)$ for some $n \times n$ integer [[matrix|0VD9ZSWWJG]] $M$ with $\det M = \pm 1$.

## Remarks

Every integral quadratic form takes integer values at integer points.
The form can be written $Q(x) = \frac12 x^T A x$ with a symmetric integer matrix $A$ whose diagonal entries $2a_{ii}$ are even.
Some authors call $Q$ integral only when $Q(x) = x^T B x$ for a symmetric integer matrix $B$.
This means that all cross coefficients $a_{ij}$ with $i < j$ are even; such forms are called classically integral.

Example: $x^2 + xy + y^2$ is integral, with $a_{11} = a_{12} = a_{22} = 1$; it is not classically integral, because the coefficient of $xy$ is odd.

Non-example: $x^2 + \frac12 xy + y^2$ is a quadratic form over $\Q$ but not integral, since the coefficient of $xy$ is not an integer; its value at $(1, 1)$ is $5/2$.
