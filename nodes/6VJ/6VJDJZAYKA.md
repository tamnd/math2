---
tag: 6VJDJZAYKA
kind: statement
role: theorem
name: Kolmogorov's weak-type estimate for the conjugate function
msc: [42A50]
uses: [A1H48DDW49, 2Z2QVWZ262, H4C888M5AZ, K1YKXVPVDG]
about: [A1H48DDW49]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_transform
---

## Statement

Let $\mathbb{T} = \R / 2\pi\Z$, identified with $[-\pi, \pi)$ with [[Lebesgue measure|2Z2QVWZ262]] $\abs{\cdot}$.
There is an absolute constant $C$ with the following property.
For every integrable function $f$ on $\mathbb{T}$, with [[conjugate function|A1H48DDW49]] $\tilde f$, and every $\lambda > 0$,
$$\abs{\set{\theta \in \mathbb{T} : \abs{\tilde f(\theta)} > \lambda}} \le \frac{C}{\lambda} \int_{\mathbb{T}} \abs{f(\theta)} \, d\theta.$$
That is, $f \mapsto \tilde f$ is of weak type $(1, 1)$.

## Remarks

A real-variable proof uses the [[Calderón–Zygmund lemma|K1YKXVPVDG]] at height $\lambda$ to write $f = g + b$.
The good part $g$ is bounded by $2\lambda$ and is handled by the $L^2$ bound and Chebyshev's inequality.
The bad part $b$ has mean zero on each interval $Q_k$.
So the smoothness of the kernel $\cot(t/2)$ away from $0$ makes $\tilde b$ small off the doubled intervals.
These have total length at most $C\lambda^{-1}\norm{f}_1$.

The strong bound $\norm{\tilde f}_{L^1} \le C\norm{f}_{L^1}$ fails.
For example, if $f$ is the Poisson kernel $P_r$ and $r \to 1^-$, then $\norm{P_r}_{L^1}$ stays bounded while $\tilde P_r$, the conjugate Poisson kernel, has $L^1$ norm comparable to $\log\frac{1}{1 - r}$.

So $\tilde f$ is finite almost everywhere for $f \in L^1$, and it lies in weak $L^1$, but it need not be integrable.

## Explanations

### L1 human

For an integrable function, the conjugate function can fail to be integrable, so one cannot bound its size in the $L^1$ norm.
Kolmogorov's estimate says that it is still not large on a big set: the set where it exceeds $\lambda$ has measure at most a constant times $\norm{f}_1/\lambda$.
This is the same bound that Chebyshev's inequality would give if $\tilde f$ were integrable.

### L2 human

Together with the $L^2$ bound from Parseval's identity, the Marcinkiewicz interpolation theorem turns this estimate into the $L^p$ bounds of the [[M. Riesz theorem|PJFH51Z48M]] for $1 < p \le 2$, and duality covers $2 \le p < \infty$.
It is the model for the weak type $(1, 1)$ bounds of all [[Calderón–Zygmund operators|3SCXCW4AH3]].
