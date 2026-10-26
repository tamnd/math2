---
tag: 0BFDHF2H7N
kind: statement
role: theorem
name: Weak law of large numbers
aliases: [khinchin-law, bernoulli-law-of-large-numbers]
msc: [60F05]
uses: [0AJN7WHBJZ, 0EFDDXTVD6, 02HZ1BK3MW, 0V0778DCW9, 0ZVEAYVRC3]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_large_numbers
    locator: Weak law
---

## Statement

Let $X_1, X_2, \dots$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with $E[|X_1|] < \infty$ and $\mu = E[X_1]$. Let $\bar{X}_n = (X_1 + \dots + X_n)/n$.
Then $\bar{X}_n \to \mu$ [[in probability|0EFDDXTVD6]]: for each $\varepsilon > 0$,
$$\lim_{n \to \infty} P\left(\left|\bar{X}_n - \mu\right| > \varepsilon\right) = 0.$$

## Remarks

If $\sigma^2 = \operatorname{Var}(X_1) < \infty$, there is a short proof. By the [[variance of a sum|0V0778DCW9]], $\operatorname{Var}(\bar{X}_n) = \sigma^2/n$.
Then [[Chebyshev's inequality|02HZ1BK3MW]] gives $P(|\bar{X}_n - \mu| > \varepsilon) \le \sigma^2 / (n \varepsilon^2) \to 0$.
The general case uses truncation, or characteristic functions: $\varphi_{\bar{X}_n}(t) = \varphi_{X_1}(t/n)^n \to e^{i\mu t}$.
The finite-variance proof needs only that the $X_i$ are pairwise uncorrelated with the same mean and bounded variances.

## History

Jacob Bernoulli proved the first version, for Bernoulli trials. It appeared after his death in Ars Conjectandi in 1713.

## Explanations

### L1 human

The weak law says that for a large number $n$ of trials, the sample mean is very likely to be close to the true mean.
For example, in $10000$ tosses of a fair coin, the fraction of heads is very likely to be between $0.49$ and $0.51$.
