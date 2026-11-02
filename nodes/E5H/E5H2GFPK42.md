---
tag: E5H2GFPK42
kind: statement
role: theorem
name: Hájek–Le Cam convolution theorem
msc: [62F12, "62E20"]
uses: [6DMQ97EBVG, 0JDAQHWA9N, 0G558GJQMW, 07CHJ5YX28, 0TTNRP5PFQ, G1Z3WSTE8Q]
about: [6DMQ97EBVG]
sources:
  - url: https://en.wikipedia.org/wiki/Local_asymptotic_normality
---

## Statement

Let $\Theta \subseteq \R^k$ be open and let the models $\set{P_{n,\theta} : \theta \in \Theta}$ be [[locally asymptotically normal|6DMQ97EBVG]] at $\theta$, with nonsingular information matrix $I_\theta$.
Let $T_n$ be [[estimators|0TTNRP5PFQ]] of $\theta$ that are *regular* at $\theta$.
This means that there is a probability measure $L_\theta$ on $\R^k$ such that, for every $h \in \R^k$,
$$\sqrt{n}\,\Big(T_n - \big(\theta + \tfrac{h}{\sqrt{n}}\big)\Big) \xrightarrow{d} L_\theta \quad \text{under } P_{n, \theta + h/\sqrt{n}},$$
where $\xrightarrow{d}$ is [[convergence in distribution|0JDAQHWA9N]].
Then there is a probability measure $M_\theta$ on $\R^k$ such that
$$L_\theta = \mathcal{N}_k\big(0, I_\theta^{-1}\big) * M_\theta,$$
the [[convolution|07CHJ5YX28]] of the [[multivariate normal distribution|0G558GJQMW]] $\mathcal{N}_k(0, I_\theta^{-1})$ with $M_\theta$.

## Remarks

Idea of proof: by LAN, the pair $\big(\sqrt{n}(T_n - \theta), \Delta_{n,\theta}\big)$ has a joint limit along subsequences, and Le Cam's third lemma gives its limit under the local alternatives.
Regularity says that this limit does not change with $h$; comparing characteristic functions then shows that the limit of $\sqrt{n}(T_n - \theta) - I_\theta^{-1}\Delta_{n,\theta}$ is independent of the limit of $I_\theta^{-1}\Delta_{n,\theta}$, which is $\mathcal{N}_k(0, I_\theta^{-1})$.

Consequence: if $L_\theta$ has covariance $\Sigma$, then $\Sigma - I_\theta^{-1}$ is positive semidefinite, so $I_\theta^{-1}$ is the best possible asymptotic covariance for regular estimators.
An estimator with $L_\theta = \mathcal{N}_k(0, I_\theta^{-1})$, such as the maximum likelihood estimator in smooth models, is called asymptotically efficient.

The regularity hypothesis is necessary: there exist superefficient estimators that beat $I_\theta^{-1}$ at single points, but they are not regular there.

## Explanations

### L1 human

Any well-behaved estimator, in large samples, behaves like the best possible estimator plus some independent extra noise.
The best possible error is normal with covariance equal to the inverse Fisher information.
So no well-behaved estimator can beat that, and the best ones add no extra noise at all.

### L2 human

The theorem is the asymptotic counterpart of the Cramér–Rao bound, but it needs no unbiasedness and it describes the whole limit law, not just its variance.
"Regular" rules out estimators that are tuned to one parameter value, which could otherwise do better there.
Together with the local asymptotic minimax theorem, it makes precise in what sense maximum likelihood estimators are asymptotically optimal in LAN models.
