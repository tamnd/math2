---
tag: GQM8GPBRYN
kind: definition
name: General linear model
msc: [62J05, 62J10, 62H12]
defines: A06SGFCSCE
uses: [41FVC4P5JB, 0V7G6WMFK0, 0WQNRCNY3M, 0XN3K7RSZY]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_model
---

## Definition

Let $n, p, m \ge 1$.
A *general linear model* is a statistical model for a random $n \times m$ response matrix $Y$ of the form
$$Y = X B + U,$$
where:

1. $X$ is a known real $n \times p$ matrix, the *design matrix*;
2. $B$ is an unknown real $p \times m$ matrix of coefficients;
3. $U$ is a random $n \times m$ error matrix whose rows are independent with [[expected value|0WQNRCNY3M]] $0$ and a common [[covariance matrix|0V7G6WMFK0]] $\Sigma$.

Often the rows of $U$ are assumed to follow the [[multivariate normal distribution|0XN3K7RSZY]] $N_m(0, \Sigma)$.

## Remarks

With $m = 1$, the model is $y = X\beta + \varepsilon$, multiple [[linear regression|41FVC4P5JB]], and $\Sigma = \sigma^2$ is a single variance.

Example: the comparison of two group means.
Let observations $1, \dots, n_1$ belong to group $1$ and the others to group $2$, and let $X$ have two columns: the indicator of group $1$ and the indicator of group $2$.
Then $\beta = (\mu_1, \mu_2)^T$, and the model says that $y_i$ has mean $\mu_1$ or $\mu_2$ according to its group, with a common error variance.
This is the model of the two-sample $t$-test.

Non-example: the model $E[y_i] = \exp(x_i^T \beta)$ is not a general linear model.
Its mean is not a linear function of $\beta$, so it cannot be written as the $i$-th entry of $X B$.

When $X$ has rank $p$, the least squares estimate is $\hat B = (X^T X)^{-1} X^T Y$, computed column by column.
