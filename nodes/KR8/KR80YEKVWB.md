---
tag: KR80YEKVWB
kind: statement
role: theorem
name: Independence of sample mean and sample variance for normal samples
msc: ["62E15"]
uses: [HSBWJSBH0D, 0QNRBHWV35, 0JN9P4A944, 07RXBVTVZB, 0AJN7WHBJZ, 0RFMMBHFTV, 0E9502NT92, 0NQ5798SB1]
about: [0QNRBHWV35, 0JN9P4A944]
sources:
  - url: https://en.wikipedia.org/wiki/Cochran%27s_theorem
---

## Statement

Let $n \ge 2$, and let $X_1, \dots, X_n$ be [[independent and identically distributed|0AJN7WHBJZ]] with the [[normal distribution|07RXBVTVZB]] $\mathcal{N}(\mu, \sigma^2)$, where $\sigma > 0$.
Let $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ be the [[sample mean|0QNRBHWV35]] and $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ the [[sample variance|0JN9P4A944]].
Then:

1. $\bar{X}$ and $S^2$ are [[independent|0E9502NT92]];
2. $\bar{X} \sim \mathcal{N}(\mu, \sigma^2/n)$;
3. $(n - 1) S^2/\sigma^2$ has the [[chi-squared distribution|0RFMMBHFTV]] with $n - 1$ degrees of freedom.

## Remarks

Put $Z_i = (X_i - \mu)/\sigma$, which are independent standard normal.
[[Cochran's theorem|HSBWJSBH0D]] with $A_1 = \frac{1}{n} J$ and $A_2 = I_n - \frac{1}{n} J$, where $J$ is the matrix of ones, shows that $n \bar{Z}^2$ and $\sum_i (Z_i - \bar{Z})^2 = (n-1)S^2/\sigma^2$ are independent, with $\chi^2$ laws with $1$ and $n - 1$ degrees of freedom.
Independence of $\bar{X}$ itself follows because $\bar{Z}$ is a function of the projection $A_1 Z$, which is independent of $A_2 Z$.
Another proof uses an orthogonal matrix whose first row is $(1, \dots, 1)/\sqrt{n}$.

At work: the statistic $T = \sqrt{n}(\bar{X} - \mu)/S$ is a standard normal variable divided by $\sqrt{V/(n-1)}$, with $V \sim \chi^2_{n-1}$ independent of it.
So $T$ has the [[Student t-distribution|0NQ5798SB1]] with $n - 1$ degrees of freedom.
This gives the one-sample $t$-test and the $t$ confidence interval for $\mu$.

The normality hypothesis is necessary: for i.i.d. samples from a nondegenerate distribution with finite variance and $n \ge 2$, independence of $\bar{X}$ and $S^2$ holds only if the distribution is normal.
For example, for Bernoulli variables, $\bar{X} = 0$ forces $S^2 = 0$, while $S^2 > 0$ is possible when $0 < \bar{X} < 1$.

## Explanations

### L1 human

For normal data, knowing the average of the sample tells you nothing about how spread out the sample is.
This is special to the normal distribution.
It is the reason why the $t$ statistic has a simple exact distribution.

### L2 human

The result is the case of two pieces of Cochran's theorem.
It underlies the exact $t$-test, the $\chi^2$ confidence interval for $\sigma^2$, and through them much of classical small-sample inference.
The analogous result for multivariate normal samples says that the sample mean vector and the sample covariance matrix are independent, the latter with a Wishart distribution.
