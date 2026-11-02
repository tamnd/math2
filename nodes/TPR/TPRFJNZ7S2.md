---
tag: TPRFJNZ7S2
kind: statement
role: proposition
name: Barycentric interpolation formula
msc: [65D05, 41A05]
uses: [DA3CQJ5MJ6, Y7KSGE97GK, SS1YMS2NPC, 04C5ZBG1WT]
about: [Y7KSGE97GK]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_polynomial
---

## Statement

Let $K$ be a [[field|04C5ZBG1WT]], let $n \ge 0$, let $x_0, \dots, x_n \in K$ be pairwise distinct, and let $y_0, \dots, y_n \in K$.
Let $p$ be the [[interpolation polynomial|SS1YMS2NPC]] of degree at most $n$ with $p(x_j) = y_j$ for all $j$.
Define the *barycentric weights* $w_j = \prod_{k \ne j} (x_j - x_k)^{-1}$ and let $\ell(x) = \prod_{k=0}^{n} (x - x_k)$.
Then for every $x \in K$ that is not a node:

1. (first form) $\displaystyle p(x) = \ell(x) \sum_{j=0}^{n} \frac{w_j}{x - x_j} \, y_j$;
2. (second form) $\displaystyle p(x) = \frac{\sum_{j=0}^{n} \frac{w_j}{x - x_j} \, y_j}{\sum_{j=0}^{n} \frac{w_j}{x - x_j}}$.

## Remarks

The [[Lagrange basis polynomials|DA3CQJ5MJ6]] satisfy $\ell_j(x) = \ell(x) \, w_j / (x - x_j)$, so the first form is the [[Lagrange formula|Y7KSGE97GK]] $p = \sum_j y_j \ell_j$ rewritten.
Applying the first form to the constant data $y_j = 1$, whose interpolant is $1$, gives $1 = \ell(x) \sum_j w_j / (x - x_j)$.
Dividing the first form by this identity gives the second form.

Example: nodes $0, 1$ have weights $w_0 = -1$ and $w_1 = 1$.
The second form gives $p(x) = \dfrac{-y_0/x + y_1/(x - 1)}{-1/x + 1/(x - 1)} = y_0 (1 - x) + y_1 x$, the line through the data.

Once the weights are computed, in $O(n^2)$ operations, each evaluation costs $O(n)$ operations, and adding a new node updates the weights in $O(n)$ operations.
The weights do not depend on the data, so the same weights serve for many data sets.

## Explanations

### L1 human

The Lagrange formula is clear but slow to evaluate, because each basis polynomial is a long product.
The barycentric formula moves the common product out and keeps only simple fractions $w_j / (x - x_j)$.
In the second form the value $p(x)$ is a weighted average of the data, with weights that depend on $x$.

### L2 human

The second form is the standard way to evaluate an interpolation polynomial in floating point arithmetic.
For good node families, such as [[Chebyshev nodes|HYK8J56PSH]], the weights have simple closed forms and the evaluation is numerically stable.
Unlike the [[Newton form|9W77FPTM9E]], it needs no ordering of the nodes and no table of [[divided differences|N5ZHV4HWDC]].
