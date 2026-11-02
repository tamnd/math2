---
tag: W4MT7K2QTF
kind: definition
name: Monte Carlo method
msc: [65C05, 11K45]
defines: HWP11G3HTN
uses: [0PNRKMRC55, 0WQNRCNY3M, 00MRN0FARV]
sources:
  - url: https://en.wikipedia.org/wiki/Monte_Carlo_method
---

## Definition

Let $q$ be a real number to be computed.
A *(plain) Monte Carlo method* for $q$ consists of the following data:

1. a [[random variable|0PNRKMRC55]] $Y$ with $\mathbb E\abs{Y} < \infty$ and [[expected value|0WQNRCNY3M]] $\mathbb E Y = q$;
2. a procedure that produces [[independent and identically distributed|00MRN0FARV]] random variables $Y_1, Y_2, \ldots$ with the distribution of $Y$;
3. for each sample size $n \ge 1$, the estimate
$$\hat q_n = \frac{1}{n} \sum_{i=1}^{n} Y_i.$$

More generally, a *Monte Carlo method* is any algorithm whose output is a random variable used to approximate a deterministic quantity.

## Remarks

Example: $q = \pi/4$ is the probability that a point $(U, V)$ uniform on $[0, 1]^2$ satisfies $U^2 + V^2 \le 1$.
So $Y = 1$ if $U^2 + V^2 \le 1$ and $Y = 0$ otherwise satisfies clause 1, since $Y$ is bounded and $\mathbb E Y = \pi/4$, and independent uniform points give clause 2.
Non-example: $Y = 1/U$ with $U$ uniform on $(0, 1)$ has $\mathbb E\abs{Y} = \int_0^1 u^{-1}\, du = \infty$, so clause 1 fails and the averages $\hat q_n$ tend to $+\infty$ almost surely.
The estimate $\hat q_n$ is unbiased, $\mathbb E \hat q_n = q$, and if $\operatorname{Var} Y = \sigma^2 < \infty$ its standard deviation is $\sigma/\sqrt{n}$.
In practice clause 2 is realised with a pseudorandom number generator, so the samples are only imitations of independent random variables.
Methods based on Markov chains, such as Markov chain Monte Carlo, fit the general sense but not the plain one, since their samples are dependent.
