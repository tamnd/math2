---
tag: V6XGZQ0GR1
kind: definition
name: Lasso
msc: [62J07, 62J05]
defines: KZ226116HW
uses: [YM708KHV2W, 0BYTQ4X1HC, 07Q7CNM5WF]
sources:
  - url: https://en.wikipedia.org/wiki/Lasso_(statistics)
---

## Definition

Let $X$ be a real $n \times p$ matrix, let $y \in \R^n$, and let $\lambda > 0$.
For $b \in \R^p$ write $\norm{b}_1 = \sum_{j=1}^p \abs{b_j}$ and let $\norm{\cdot}_2$ be the Euclidean norm.
A *lasso estimate* with parameter $\lambda$ is a minimiser over $b \in \R^p$ of
$$\frac{1}{2} \norm{y - X b}_2^2 + \lambda \norm{b}_1.$$

## Remarks

The objective is [[convex|07Q7CNM5WF]] and tends to infinity as $\norm{b}_1 \to \infty$, so a minimiser exists.
It need not be unique when the columns of $X$ are linearly dependent.
There is no closed formula in general; the estimate is computed by coordinate descent or by the LARS algorithm.
Authors scale the objective in different ways, for example with $\frac{1}{2n}$ in front of the squared norm, which only rescales $\lambda$.

Example: assume $X^T X = I_p$ and put $z = X^T y$, the [[ordinary least squares|YM708KHV2W]] estimate.
Then $\norm{y - Xb}_2^2 = \norm{z - b}_2^2 + \text{const}$, and the problem splits into the $p$ problems of minimising $\frac{1}{2}(z_j - b_j)^2 + \lambda \abs{b_j}$.
The solution is the soft thresholding $\hat\beta_j = \sgn(z_j) \max(\abs{z_j} - \lambda, 0)$.
So every $j$ with $\abs{z_j} \le \lambda$ gets $\hat\beta_j = 0$.

Non-example: with the squared norm $\norm{b}_2^2$ in place of $\norm{b}_1$, the same orthonormal case gives $\hat\beta_j = z_j / (1 + 2\lambda)$, which is never $0$ when $z_j \ne 0$; that is ridge regression, not the lasso.

Equivalent form: for each $\lambda > 0$ and each lasso estimate $\hat\beta$, the vector $\hat\beta$ minimises $\norm{y - Xb}_2^2$ under the constraint $\norm{b}_1 \le \norm{\hat\beta}_1$.
