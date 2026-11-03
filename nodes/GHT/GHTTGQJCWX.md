---
tag: GHTTGQJCWX
kind: statement
role: theorem
name: Maximum entropy probability distributions
msc: [94A17, 62B10]
uses: [Y86E072V0V, B4PNYNYVKK, 55WNT5655E, 02MY6WZXEQ, 05AQE0QR0D, 0E99F51GVB, 0477R9PYAE, 0WQNRCNY3M, Z2ED2TA87E]
about: [Y86E072V0V, B4PNYNYVKK]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_entropy_probability_distribution
---

## Statement

Logarithms are natural, and $H$ and $h$ denote the [[Shannon entropy|Y86E072V0V]] and the [[differential entropy|B4PNYNYVKK]].

1. Let $X$ be a random variable with values in a finite set of $n$ elements. Then $H(X) \le \log n$, with equality if and only if $X$ has the [[discrete uniform distribution|02MY6WZXEQ]] on this set.
2. Let $X$ be a real random variable with a density, finite [[variance|0477R9PYAE]] $\sigma^2 > 0$, and differential entropy $h(X)$. Then $h(X) \le \frac12 \log (2 \pi e \sigma^2)$, with equality if and only if $X$ has a [[normal distribution|05AQE0QR0D]].
3. Let $X$ be a random variable with a density on $[0, \infty)$, [[mean|0WQNRCNY3M]] $\mu > 0$, and differential entropy $h(X)$. Then $h(X) \le 1 + \log \mu$, with equality if and only if $X$ has the [[exponential distribution|0E99F51GVB]] with mean $\mu$.

## Remarks

All three parts follow from [[Gibbs' inequality|55WNT5655E]] in the form $-\int f \log f \le -\int f \log g$ for a density $f$ and a reference density $g$, with equality only when $f = g$ almost everywhere.
The point is to choose $g$ with $\log g$ affine in the constrained quantities.
For part 2 take $g$ normal with the mean and variance of $X$: then $-\log g(x) = \frac12 \log (2 \pi \sigma^2) + (x - m)^2 / (2 \sigma^2)$, and its average under $f$ is $\frac12 \log (2 \pi e \sigma^2)$, the same as under $g$.
Part 3 works the same way with $g(x) = \mu^{-1} e^{-x / \mu}$, and part 1 with $g$ uniform.

Example: the uniform law on $[-a, a]$ has variance $a^2 / 3$ and entropy $\log (2a) \approx 0.693 + \log a$, below the Gaussian bound $\frac12 \log (2 \pi e a^2 / 3) \approx 0.870 + \log a$.

The constraint is needed in each part: without a bound on the variance, the uniform law on $[-a, a]$ has entropy $\log (2a)$, which is unbounded as $a \to \infty$.

## Explanations

### L1 human

Among all laws that satisfy a given constraint, the one with the largest entropy is the most spread out, the one that assumes the least.
On a finite set with no constraint, it is the uniform law.
On the real line with a fixed variance, it is the bell curve.
On the positive half-line with a fixed mean, it is the exponential law.

### L2 human

These are the basic cases of the [[principle of maximum entropy|Z2ED2TA87E]].
Under constraints $E[T_i(X)] = c_i$, the same proof shows that a density proportional to $\exp(\sum_i \lambda_i T_i(x))$ that meets the constraints is the maximizer.
Part 2 explains why Gaussian noise is the worst case for a channel with a power constraint.
It is used in the proof of the capacity formula of the [[additive white Gaussian noise channel|RYFPT7P01J]].
In $\R^n$ the same proof shows that among densities with covariance matrix $\Sigma$, the [[multivariate normal distribution|0XN3K7RSZY]] has the largest entropy, $\frac12 \log ((2 \pi e)^n \det \Sigma)$.
