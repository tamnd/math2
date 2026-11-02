---
tag: 1PKZW82H0C
kind: definition
name: Efficiency of an estimator
msc: [62F10, 62F12]
defines: 8VDNRZG3R1
uses: [0TTNRP5PFQ, 01BD2TFFP4, 007QED3E0Y, G1Z3WSTE8Q, 1JFKTEQVRX, 0QNRBHWV35]
sources:
  - url: https://en.wikipedia.org/wiki/Efficiency_(statistics)
---

## Definition

Let $\set{f(\cdot; \theta) : \theta \in \Theta}$ be a parametric family of densities with $\Theta \subseteq \R$ an open interval, regular enough for the [[Cramér–Rao bound|1JFKTEQVRX]] to hold.
Let $X = (X_1, \dots, X_n)$ be the data, and let $I_n(\theta)$ be the [[Fisher information|G1Z3WSTE8Q]] of $X$, assumed finite and positive.
Let $T$ be an unbiased [[estimator|0TTNRP5PFQ]] of $\theta$ (its [[bias|01BD2TFFP4]] is $0$) with finite positive [[variance|007QED3E0Y]].

1. The *efficiency* of $T$ at $\theta$ is $e(T, \theta) = \dfrac{1/I_n(\theta)}{\operatorname{Var}_\theta(T)}$.
2. $T$ is *efficient* if $e(T, \theta) = 1$ for every $\theta \in \Theta$.
3. For two unbiased estimators $T_1, T_2$ of $\theta$, the *relative efficiency* of $T_1$ with respect to $T_2$ is $\operatorname{Var}_\theta(T_2)/\operatorname{Var}_\theta(T_1)$.

## Remarks

By the Cramér–Rao bound, $0 < e(T, \theta) \le 1$.

Example: for i.i.d. $X_i \sim \mathcal{N}(\mu, \sigma^2)$ with $\sigma^2$ known, $I_n(\mu) = n/\sigma^2$ and the [[sample mean|0QNRBHWV35]] has variance $\sigma^2/n$, so $e(\bar{X}, \mu) = 1$ and $\bar{X}$ is efficient.

Non-example: in the same model, $T = X_1$ is unbiased with variance $\sigma^2$, so $e(T, \mu) = 1/n$, and $T$ is not efficient when $n \ge 2$.

The *asymptotic relative efficiency* compares two estimators $T_{1,n}, T_{2,n}$ with $\sqrt{n}(T_{j,n} - \theta) \xrightarrow{d} \mathcal{N}(0, v_j(\theta))$ by the ratio $v_2(\theta)/v_1(\theta)$.
For normal data, the asymptotic relative efficiency of the sample median with respect to the sample mean is $2/\pi \approx 0.64$.
