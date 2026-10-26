---
tag: 0DFWHQ839T
kind: statement
role: theorem
name: Strong law of large numbers
aliases: [kolmogorov-strong-law]
msc: [60F15]
uses: [0AJN7WHBJZ, 04P7D63W8P, 0BFDHF2H7N, 0ZVEAYVRC3]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_large_numbers
    locator: Strong law
---

## Statement

Let $X_1, X_2, \dots$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with $E[|X_1|] < \infty$ and $\mu = E[X_1]$. Let $\bar{X}_n = (X_1 + \dots + X_n)/n$.
Then $\bar{X}_n \to \mu$ [[almost surely|04P7D63W8P]]:
$$P\left(\lim_{n \to \infty} \bar{X}_n = \mu\right) = 1.$$

## Remarks

The strong law implies the [[weak law|0BFDHF2H7N]], because almost sure convergence implies convergence in probability.
A short proof exists if $E[X_1^4] < \infty$: then $E[(\bar{X}_n - \mu)^4] \le C/n^2$, and the first Borel–Cantelli lemma applies.
Etemadi proved that the result holds when the $X_i$ are only pairwise independent and identically distributed.
Conversely, if $E[|X_1|] = \infty$, then almost surely $\bar{X}_n$ does not converge to a finite limit.

## Explanations

### L1 human

The strong law says more than the weak law. Almost every infinite sequence of trials has sample means that converge to the true mean.
So, with probability $1$, the fraction of heads in an infinite sequence of fair coin tosses tends to $1/2$.
