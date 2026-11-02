---
tag: 3X4YMR25ST
kind: definition
name: Type and cotype
msc: [46B07, 46B09]
defines: BF9XR5SVPV
uses: [06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Type_and_cotype_of_a_Banach_space
---

## Definition

Let $X$ be a real or complex [[Banach space|06GZ956657]].
For vectors $x_1, \dots, x_n$ in $X$, write
$$R(x_1, \dots, x_n) = \Big( \frac{1}{2^n} \sum_{\varepsilon \in \set{-1, 1}^n} \Big\| \sum_{i=1}^n \varepsilon_i x_i \Big\|^2 \Big)^{1/2},$$
the quadratic mean of the norm over all choices of signs.

1. Let $1 \le p \le 2$. The space $X$ has *type* $p$ if there is a constant $C$ with $R(x_1, \dots, x_n) \le C \big( \sum_{i=1}^n \norm{x_i}^p \big)^{1/p}$ for all $n$ and all $x_1, \dots, x_n \in X$.
2. Let $2 \le q < \infty$. The space $X$ has *cotype* $q$ if there is a constant $C$ with $\big( \sum_{i=1}^n \norm{x_i}^q \big)^{1/q} \le C \, R(x_1, \dots, x_n)$ for all $n$ and all $x_1, \dots, x_n \in X$.

## Remarks

Example: a Hilbert space $H$ has type $2$ and cotype $2$ with $C = 1$.
Expanding the squares, the cross terms $\pm 2 \operatorname{Re} \ip{x_i}{x_j}$ cancel in the average over signs.
So $R(x_1, \dots, x_n)^2 = \sum_i \norm{x_i}^2$ exactly.

Non-example: $\ell^1$ has no type $p > 1$.
For the unit vectors $e_1, \dots, e_n$, every sign sum has norm $n$, so $R = n$.
The right side of the type inequality is $C n^{1/p}$, and $n \le C n^{1/p}$ fails for large $n$.

Every Banach space has type $1$, by the triangle inequality.
Type $p$ implies type $p'$ for $p' < p$, and cotype $q$ implies cotype $q'$ for $q' > q$.
By the Kahane inequality, the quadratic mean in $R$ can be replaced by the plain mean of the norm, with other constants.
For $1 \le p < \infty$, the space $L^p$ has type $\min(p, 2)$ and cotype $\max(p, 2)$.
