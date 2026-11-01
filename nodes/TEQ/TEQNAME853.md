---
tag: TEQNAME853
kind: definition
name: Lagrange polynomial
msc: [41A05, 65D05, 26C05]
defines: Y7KSGE97GK
uses: [0Q9EZS90GY, 0DPF6WRZW6, SS1YMS2NPC]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_polynomial
---

## Definition

Let $n \ge 0$, let $x_0, x_1, \dots, x_n$ be pairwise distinct real numbers, and let $y_0, y_1, \dots, y_n$ be real numbers.
For $j = 0, \dots, n$, the *Lagrange basis polynomial* is
$$\ell_j(x) = \prod_{\substack{0 \le m \le n \\ m \ne j}} \frac{x - x_m}{x_j - x_m}.$$
The *Lagrange polynomial* of the data $(x_j, y_j)$ is
$$L(x) = \sum_{j=0}^{n} y_j \, \ell_j(x).$$

## Remarks

Each $\ell_j$ has [[degree|0DPF6WRZW6]] $n$, with $\ell_j(x_j) = 1$ and $\ell_j(x_k) = 0$ for $k \ne j$.
So $L$ lies in the [[polynomial ring|0Q9EZS90GY]] $\R[x]$, has degree at most $n$, and satisfies $L(x_k) = y_k$ for all $k$.
It is the unique polynomial with these properties: the difference of two of them has degree at most $n$ and $n + 1$ roots, so it is $0$.
The same formula works over any field; this solves [[polynomial interpolation|SS1YMS2NPC]].

Example: nodes $0, 1, 2$ with values $1, 3, 7$.
Here $\ell_0 = \frac{(x - 1)(x - 2)}{2}$, $\ell_1 = -x(x - 2)$ and $\ell_2 = \frac{x(x - 1)}{2}$.
Then $L = \ell_0 + 3 \ell_1 + 7 \ell_2 = x^2 + x + 1$, and indeed $L(0) = 1$, $L(1) = 3$, $L(2) = 7$.

Non-example: if two nodes coincide, say $x_0 = x_1$, the factor $\frac{x - x_1}{x_0 - x_1}$ in $\ell_0$ has denominator $0$, so the formula is not defined.
