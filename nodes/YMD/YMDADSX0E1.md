---
tag: YMDADSX0E1
kind: definition
name: Local asymptotic normality
msc: [62F12, "62E20"]
defines: 6DMQ97EBVG
uses: [1NTKG64F7N, 0EFDDXTVD6, 0JDAQHWA9N, 0G558GJQMW, 0QQCG3JWJ4, G1Z3WSTE8Q, CP97GRVTQ0, DQGJMP9WHC]
sources:
  - url: https://en.wikipedia.org/wiki/Local_asymptotic_normality
---

## Definition

Let $\Theta \subseteq \R^k$ be open, and for each $n$ let $\set{P_{n,\theta} : \theta \in \Theta}$ be a family of probability measures on a measurable space $(\Omega_n, \mathcal{F}_n)$.
Let $\theta \in \Theta$.
The sequence of models is *locally asymptotically normal* (LAN) at $\theta$ if the following holds.
There are random vectors $\Delta_{n,\theta}$ on $\Omega_n$ and a $k \times k$ [[positive definite matrix|0QQCG3JWJ4]] $I_\theta$ such that:

1. $\Delta_{n,\theta} \xrightarrow{d} \mathcal{N}_k(0, I_\theta)$ under $P_{n,\theta}$, in the sense of [[convergence in distribution|0JDAQHWA9N]] to a [[multivariate normal|0G558GJQMW]] law;
2. for every sequence $h_n \to h$ in $\R^k$,
$$\log \frac{dP_{n, \theta + h_n/\sqrt{n}}}{dP_{n,\theta}} = h^T \Delta_{n,\theta} - \frac{1}{2} h^T I_\theta h + o_{P_{n,\theta}}(1).$$
Here the log-likelihood ratio uses the [[Radon–Nikodym derivative|1NTKG64F7N]] of the absolutely continuous part.
The term $o_{P_{n,\theta}}(1)$ is a sequence of random variables that tends to $0$ in [[probability|0EFDDXTVD6]] under $P_{n,\theta}$.

## Remarks

Example: for i.i.d. $\mathcal{N}(\theta, 1)$ observations, $P_{n,\theta} = \mathcal{N}(\theta, 1)^{\otimes n}$, the log-likelihood ratio is exactly $h\, \Delta_n - h^2/2$ with $\Delta_n = n^{-1/2}\sum_i (X_i - \theta) \sim \mathcal{N}(0, 1)$, so the model is LAN with $I_\theta = 1$ and no remainder.

More generally, if $X_1, \dots, X_n$ are i.i.d. from a model that is differentiable in quadratic mean at $\theta$ with nonsingular [[Fisher information|G1Z3WSTE8Q]] $I_\theta$, the model is LAN at $\theta$ with $\Delta_{n,\theta} = n^{-1/2}\sum_i s(\theta; X_i)$, where $s$ is the [[score|CP97GRVTQ0]].

Non-example: for i.i.d. Uniform$(0, \theta)$ observations and $h \ne 0$, $P_{n, \theta + h/\sqrt{n}}$ and $P_{n,\theta}$ become asymptotically singular.
The reason is that the scale at which they differ is $1/n$; clause 2 fails, and the model is not LAN.

Under LAN, $P_{n,\theta + h/\sqrt{n}}$ and $P_{n,\theta}$ are mutually [[contiguous|DQGJMP9WHC]], since the limit law $\mathcal{N}(-\frac{1}{2} h^T I_\theta h, \, h^T I_\theta h)$ of the log-likelihood ratio has $E e^{L} = 1$.
