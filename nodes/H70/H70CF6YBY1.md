---
tag: H70CF6YBY1
kind: definition
name: Carleman matrix
msc: [39B12, 13F25, 15B99]
defines: 3KK7M27P8T
uses: [033WGN00BF, 0VD9ZSWWJG, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Jabotinsky_matrix
---

## Definition

Let $K$ be a field and let $f(x) = \sum_{k \ge 0} f_k x^k$ be a [[formal power series|033WGN00BF]] over $K$.
For integers $j, k \ge 0$, let $M[f]_{jk}$ be the coefficient of $x^k$ in the power $f(x)^j$, with $f(x)^0 = 1$.
The *Carleman matrix* of $f$ is the infinite [[matrix|0VD9ZSWWJG]] $M[f] = (M[f]_{jk})_{j, k \ge 0}$.
So
$$f(x)^j = \sum_{k \ge 0} M[f]_{jk} \, x^k \quad \text{for every } j \ge 0.$$

## Remarks

Example: for $f(x) = ax$ with $a \in K$, one has $f(x)^j = a^j x^j$, so $M[f]$ is diagonal with entries $1, a, a^2, \ldots$.
For $f(x) = x$ it is the identity matrix.

Non-example: the diagonal matrix with entries $1, 2, 3, \ldots$ is not a Carleman matrix.
Its row $1$ would force $f(x) = 2x$, and then row $2$ would have to list the coefficients of $4x^2$, not of $3x^2$.

If $g(0) = 0$, then $M[f \circ g] = M[f] \, M[g]$, a product of infinite matrices in which each entry is a finite sum.
Check: $f(g(x))^j = \sum_k M[f]_{jk} \, g(x)^k = \sum_k M[f]_{jk} \sum_l M[g]_{kl} x^l$, and $M[g]_{kl} = 0$ for $k > l$ because $g(x)^k$ starts at $x^k$.
In particular, if $f(0) = 0$, then $M[f^n] = M[f]^n$ for the [[iterates|AYVTR2ES5B]] of $f$, and $M[f]$ is upper triangular with diagonal entries $f_1^j$.
The transpose of $M[f]$ is the Bell matrix of $f$, which reverses the order of products.
