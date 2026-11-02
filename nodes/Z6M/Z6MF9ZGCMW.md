---
tag: Z6MF9ZGCMW
kind: statement
role: theorem
name: Fisher–Neyman factorization theorem
msc: [62B05]
uses: [QNMR5F525C, JZ6R7J36K5, ECDJ8DD9RV]
about: [WP4TGXJQJG]
sources:
  - url: https://en.wikipedia.org/wiki/Sufficient_statistic
    locator: Fisher–Neyman factorization theorem
---

## Statement

Let $\set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] on a measurable space $(S, \mathcal{S})$ that is dominated by a $\sigma$-finite measure $\mu$: each $P_\theta$ has a [[density|ECDJ8DD9RV]] $f_\theta = dP_\theta/d\mu$.
Let $T \colon S \to \mathcal{T}$ be a measurable map into a measurable space $\mathcal{T}$.
Then $T$ is a [[sufficient statistic|QNMR5F525C]] for $\theta$ if and only if the following holds.
There are measurable functions $g_\theta \colon \mathcal{T} \to [0, \infty)$, for $\theta \in \Theta$, and $h \colon S \to [0, \infty)$ such that, for every $\theta \in \Theta$,
$$f_\theta(x) = g_\theta\left(T(x)\right) h(x) \quad \text{for } \mu\text{-almost every } x \in S.$$

## Remarks

In the discrete case the proof is a direct computation: if the factorization holds, then $P_\theta(X = x \mid T = t) = h(x)/\sum_{y : T(y) = t} h(y)$, which does not depend on $\theta$; conversely one takes $g_\theta(t) = P_\theta(T = t)$ and $h(x) = P(X = x \mid T = T(x))$.
The general case is due to Halmos and Savage.
It first replaces $\mu$ by a probability measure $\lambda = \sum_j c_j P_{\theta_j}$, a countable convex combination equivalent to the whole family.
It then uses Radon–Nikodym derivatives with respect to $\lambda$.
Example: for i.i.d. $\mathcal{N}(\mu, \sigma^2)$ data,
$$f_{(\mu, \sigma^2)}(x) = (2\pi\sigma^2)^{-n/2} \exp\left(-\frac{\sum_i x_i^2 - 2\mu \sum_i x_i + n\mu^2}{2\sigma^2}\right),$$
so $T(x) = \left(\sum_i x_i, \sum_i x_i^2\right)$ is sufficient for $(\mu, \sigma^2)$, with $h = 1$.
Example: for i.i.d. uniform data on $[0, \theta]$, $f_\theta(x) = \theta^{-n}\mathbf{1}\set{\max_i x_i \le \theta}\mathbf{1}\set{\min_i x_i \ge 0}$, so $\max_i x_i$ is sufficient.
The domination hypothesis is needed for the densities $f_\theta$ to exist, so without it the criterion cannot even be stated.

## Explanations

### L1 human

To check whether a summary of the data keeps all the information about a parameter, write down the likelihood.
If the parameter enters the likelihood only through the summary, the summary is sufficient, and conversely.
This turns a question about conditional distributions into simple algebra.

### L2 human

The factorization criterion is the standard way to find sufficient statistics in practice.
For an [[exponential family|EP9VPZ0S6G]] with density $h(x)\exp(\eta(\theta) \cdot T(x) - A(\theta))$, it shows at once that $T$ is sufficient.
It also shows that the likelihood function, up to a factor free of $\theta$, depends on the data only through any sufficient statistic, which links sufficiency with the [[likelihood principle|YR5RAT9HWZ]].
It is the first step towards the [[Rao–Blackwell theorem|Y3TX4J41TP]] and the [[Lehmann–Scheffé theorem|QQZPWDWS29]].
