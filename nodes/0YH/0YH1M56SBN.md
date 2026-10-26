---
tag: 0YH1M56SBN
kind: statement
role: proposition
name: Sum of independent Poisson random variables
msc: ["60E05"]
uses: [0VEFSSKX18, 0REMT01N36, 0XCE070V8B]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_distribution
    locator: Sums of Poisson-distributed random variables
---

## Statement

Let $X_1, \dots, X_n$ be [[independent|0XCE070V8B]] random variables with $X_i \sim \operatorname{Poisson}(\lambda_i)$ and $\lambda_i > 0$. Then
$$X_1 + \dots + X_n \sim \operatorname{Poisson}(\lambda_1 + \dots + \lambda_n).$$

## Remarks

Proof with [[generating functions|0REMT01N36]]: $G_{X_i}(z) = e^{\lambda_i (z - 1)}$, so the sum has $G(z) = e^{(\lambda_1 + \dots + \lambda_n)(z - 1)}$. This is the generating function of $\operatorname{Poisson}(\lambda_1 + \dots + \lambda_n)$.
A direct proof for $n = 2$ uses the binomial theorem: $\sum_{k=0}^{m} e^{-\lambda_1} \frac{\lambda_1^k}{k!} e^{-\lambda_2} \frac{\lambda_2^{m-k}}{(m-k)!} = e^{-(\lambda_1 + \lambda_2)} \frac{(\lambda_1 + \lambda_2)^m}{m!}$.
Conversely, given $X_1 + X_2 = m$, the conditional law of $X_1$ is $\operatorname{Bin}(m, \lambda_1 / (\lambda_1 + \lambda_2))$.

## Explanations

### L1 human

If calls come to two help desks as independent Poisson counts, the total number of calls is again a Poisson count. Its mean is the sum of the two means.
