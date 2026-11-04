---
tag: 1Q8PDAHQVC
kind: proof
name: Proof of the formula for the variance of a sum
msc: [60A05]
proves: 0D86GJEZ39
uses: [0DCT0QZVQ1, 007QED3E0Y, 0DJ8W3HP2D, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Variance
    locator: Sum of correlated variables
---

## Proof

We expand the square of the centred sum and use linearity of expectation.

1. Let $X_1, \dots, X_n$ be real random variables on one probability space with $E[X_i^2] < \infty$ for each $i$. Let $S = X_1 + \dots + X_n$.
2. For each real $x$, $\abs{x} \le (1 + x^2)/2$, because $(\abs{x} - 1)^2 \ge 0$.
3. The integral of nonnegative functions is monotone. So by step 2, $E[\abs{X_i}] \le (1 + E[X_i^2])/2 < \infty$, and each $X_i$ is integrable, with [[expected value|0DCT0QZVQ1]] $m_i = E[X_i]$.
4. Let $Y_i = X_i - m_i$. Since $(x - m)^2 \le 2x^2 + 2m^2$ for real $x$ and $m$, we get $E[Y_i^2] \le 2E[X_i^2] + 2m_i^2 < \infty$.
5. For real $u$ and $v$, $\abs{uv} \le (u^2 + v^2)/2$. So $\abs{Y_i Y_j} \le (Y_i^2 + Y_j^2)/2$, and each product $Y_i Y_j$ is integrable.
6. By [[linearity of expectation|0P7PTC8DDE]], $S$ is integrable and $E[S] = m_1 + \dots + m_n$. So $S - E[S] = Y_1 + \dots + Y_n$.
7. Expanding the square of a finite sum gives, pointwise,
$$(S - E[S])^2 = \sum_{i=1}^n Y_i^2 + 2 \sum_{1 \le i < j \le n} Y_i Y_j.$$
8. All terms on the right are integrable by steps 4 and 5. By linearity of expectation,
$$E[(S - E[S])^2] = \sum_{i=1}^n E[Y_i^2] + 2 \sum_{1 \le i < j \le n} E[Y_i Y_j].$$
9. By the definition of the [[variance|007QED3E0Y]], the left side is $\operatorname{Var}(S)$ and $E[Y_i^2] = \operatorname{Var}(X_i)$.
10. By the definition of the [[covariance|0DJ8W3HP2D]], $E[Y_i Y_j] = E[(X_i - m_i)(X_j - m_j)] = \operatorname{Cov}(X_i, X_j)$.
11. Steps 8 to 10 give
$$\operatorname{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \operatorname{Var}(X_i) + 2 \sum_{1 \le i < j \le n} \operatorname{Cov}(X_i, X_j).$$
12. For $n = 2$ with $X_1 = X$ and $X_2 = Y$, the only pair is $(1, 2)$. So $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2 \operatorname{Cov}(X, Y)$.

## Idea

The deviation of the sum from its mean is the sum of the deviations of the terms. Squaring a sum gives the squares plus twice the cross products. Their expectations are the variances and the covariances.
