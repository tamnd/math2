---
tag: ZCVB4ZQ0SA
kind: definition
name: Lagrange basis polynomials
msc: [41A05, 65D05]
defines: DA3CQJ5MJ6
uses: [04C5ZBG1WT, 0SDC934R52, 0P4JRMSWNH, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_polynomial
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]], let $n \ge 0$, and let $x_0, \dots, x_n \in K$ be pairwise distinct.
For $j = 0, \dots, n$, the *Lagrange basis polynomial* $\ell_j$ is the polynomial in the [[polynomial ring|0SDC934R52]] $K[x]$ given by
$$\ell_j(x) = \prod_{\substack{0 \le k \le n \\ k \ne j}} \frac{x - x_k}{x_j - x_k}.$$

## Remarks

Each $\ell_j$ has [[degree|0P4JRMSWNH]] $n$, and $\ell_j(x_i) = 1$ if $i = j$ and $\ell_j(x_i) = 0$ if $i \ne j$.
The $\ell_j$ form a [[basis|0KCQ9Y3QKA]] of the space of polynomials of degree at most $n$, and every such $p$ satisfies $p = \sum_{j} p(x_j) \, \ell_j$.
They also satisfy $\sum_j \ell_j = 1$, the case $p = 1$.
With $\ell(x) = \prod_{k=0}^{n} (x - x_k)$, one has $\ell_j(x) = \dfrac{\ell(x)}{(x - x_j) \, \ell'(x_j)}$.

Example: for the nodes $0, 1, 2$ in $\R$, $\ell_1(x) = \frac{(x - 0)(x - 2)}{(1 - 0)(1 - 2)} = -x(x - 2)$.
Check: $\ell_1(0) = 0$, $\ell_1(1) = 1$ and $\ell_1(2) = 0$.

Non-example: for the nodes $0, 0, 1$, the nodes are not distinct, and the factor $\frac{x - x_1}{x_0 - x_1}$ in $\ell_0$ has denominator $0$, so $\ell_0$ is not defined.
