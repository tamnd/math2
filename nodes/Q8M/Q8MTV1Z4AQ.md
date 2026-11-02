---
tag: Q8MTV1Z4AQ
kind: definition
name: Elastic net
msc: [62J07, 62J05]
defines: TKQPE0Q05Y
uses: [KZ226116HW, 3KZW2930V2, 07Q7CNM5WF]
sources:
  - url: https://en.wikipedia.org/wiki/Elastic_net_regularization
---

## Definition

Let $X$ be a real $n \times p$ matrix, let $y \in \R^n$, and let $\lambda_1 \ge 0$ and $\lambda_2 \ge 0$.
For $b \in \R^p$ write $\norm{b}_1 = \sum_{j=1}^p \abs{b_j}$ and let $\norm{\cdot}_2$ be the Euclidean norm.
An *elastic net estimate* with parameters $\lambda_1, \lambda_2$ is a minimiser over $b \in \R^p$ of
$$\norm{y - X b}_2^2 + \lambda_1 \norm{b}_1 + \lambda_2 \norm{b}_2^2.$$

## Remarks

If $\lambda_2 > 0$, the objective is strictly [[convex|07Q7CNM5WF]] and tends to infinity with $\norm{b}_2$, so the estimate exists and is unique.
With $\lambda_2 = 0$ it is a [[lasso|KZ226116HW]] estimate, and with $\lambda_1 = 0$ it is the [[ridge regression|3KZW2930V2]] estimate.
A common parametrisation uses one level $\lambda$ and a mixing weight $\alpha \in [0, 1]$, with penalty $\lambda \big( \alpha \norm{b}_1 + \frac{1 - \alpha}{2} \norm{b}_2^2 \big)$.
Some authors multiply the estimate defined above by $1 + \lambda_2$ to undo part of the double shrinkage.

Example: assume $X^T X = I_p$ and put $z = X^T y$.
Then $\norm{y - Xb}_2^2 = \norm{z - b}_2^2 + \text{const}$, and the problem splits into coordinates.
Minimising $(z_j - b_j)^2 + \lambda_1 \abs{b_j} + \lambda_2 b_j^2$ gives
$$\hat\beta_j = \frac{\sgn(z_j) \max(\abs{z_j} - \lambda_1/2, \, 0)}{1 + \lambda_2}.$$
So coefficients with $\abs{z_j} \le \lambda_1 / 2$ are exactly zero, and the others are shrunk by both penalties.

Non-example: if $\lambda_1 = 0$ and $\lambda_2 > 0$, no coefficient is set to zero unless $z_j = 0$, so no selection takes place; that is ridge regression.
