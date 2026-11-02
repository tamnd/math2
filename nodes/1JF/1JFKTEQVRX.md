---
tag: 1JFKTEQVRX
kind: statement
role: theorem
name: Cramér–Rao bound
msc: [62F10, 62B10]
uses: [G1Z3WSTE8Q, CP97GRVTQ0, 0Q5CG2NEQ8, 0SSS6ERQ0S, 0BWGTN92FG, 0477R9PYAE, 03PGHKAJG3]
about: [G1Z3WSTE8Q, 0SSS6ERQ0S]
sources:
  - url: https://en.wikipedia.org/wiki/Cramér–Rao_bound
same_as:
  wikidata: Q1138810
  wikipedia: Cramér–Rao bound
---

## Statement

Let $\set{f(\cdot\,; \theta) : \theta \in \Theta}$ be a family of densities with respect to a fixed measure $\mu$, where $\Theta \subseteq \R$ is an open interval.
Assume the following regularity conditions.

1. The set $\set{x : f(x; \theta) > 0}$ does not depend on $\theta$.
2. For every such $x$, the map $\theta \mapsto f(x; \theta)$ is differentiable.
3. The [[Fisher information|G1Z3WSTE8Q]] $I(\theta)$ satisfies $0 < I(\theta) < \infty$ for every $\theta$.

Let $X$ have density $f(\cdot\,; \theta)$, and let $T = T(X)$ be a [[statistic|0Q5CG2NEQ8]] with $E_\theta[T^2] < \infty$ for every $\theta$.
Put $\psi(\theta) = E_\theta[T]$.
Assume that differentiation in $\theta$ may be taken under the integral sign in $\int f(x; \theta) \, \mu(dx) = 1$ and in $\int T(x) f(x; \theta) \, \mu(dx) = \psi(\theta)$.
Then $\psi$ is differentiable, and for every $\theta \in \Theta$,
$$\operatorname{Var}_\theta(T) \ge \frac{\psi'(\theta)^2}{I(\theta)}.$$
In particular, if $T$ is an [[unbiased|0BWGTN92FG]] [[estimator|0SSS6ERQ0S]] of $\theta$, then $\operatorname{Var}_\theta(T) \ge 1/I(\theta)$.

## Remarks

Let $s$ be the [[score|CP97GRVTQ0]].
Differentiating the two integrals gives $E_\theta[s] = 0$ and $E_\theta[T s] = \psi'(\theta)$, so $\operatorname{Cov}_\theta(T, s) = \psi'(\theta)$.
The [[Cauchy–Schwarz inequality|03PGHKAJG3]] then gives $\psi'(\theta)^2 \le \operatorname{Var}_\theta(T) \operatorname{Var}_\theta(s) = \operatorname{Var}_\theta(T) \, I(\theta)$.
For $n$ independent observations the information is $n I(\theta)$, so the bound becomes $\psi'(\theta)^2 / (n I(\theta))$.
In dimension $d$, the bound reads $\operatorname{Cov}_\theta(T) \succeq D \, I(\theta)^{-1} D^{\mathsf T}$, with $D$ the Jacobian matrix of $\psi$.

Example: for $n$ independent normal observations with mean $\theta$ and known variance $\sigma^2$, one has $I(\theta) = 1/\sigma^2$.
The sample mean is unbiased with variance $\sigma^2/n = 1/(n I(\theta))$, so it attains the bound.

The fixed support is necessary.
For $n$ independent uniform observations on $(0, \theta)$, the unbiased estimator $\frac{n+1}{n} \max_i X_i$ has variance $\theta^2 / (n(n+2))$.
This is smaller than $\theta^2/n$, the value of the formal bound with $E_\theta[s^2] = 1/\theta^2$.

## Explanations

### L1 human

No unbiased estimate can be more precise than a limit fixed by the model itself.
The limit is one over the Fisher information, so models whose data carry much information allow precise estimates.
An estimator that reaches the limit cannot be improved among unbiased estimators.

### L2 human

The bound is the benchmark for the efficiency of estimators: the ratio of the bound to the actual variance measures how much information an estimator wastes.
It is attained exactly only in special cases, essentially for exponential families and the natural statistic.
Asymptotically, under regularity conditions, the maximum likelihood estimator has variance close to $1/(n I(\theta))$ and so reaches the bound in the limit.
The regularity conditions matter: models with a moving support, such as the uniform family, can be estimated faster than the bound allows.
