---
tag: NE0BW8Q2PX
kind: definition
name: Exponential family
msc: [62B05, "60E05"]
defines: EP9VPZ0S6G
uses: [MSC0MR8VMH, WEBBT18D4X, 1NTKG64F7N, 0386Y0Z7Y7]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_family
---

## Definition

Let $(\mathcal{X}, \mathcal{F})$ be a measurable space with a [[σ-finite measure|WEBBT18D4X]] $\mu$, and let $\set{P_\theta : \theta \in \Theta}$ be a [[parametric family|MSC0MR8VMH]] of probability measures on it.
The family is a *$k$-parameter exponential family* if there are

1. a measurable function $h \colon \mathcal{X} \to [0, \infty)$,
2. measurable functions $T_1, \dots, T_k \colon \mathcal{X} \to \R$,
3. functions $\eta_1, \dots, \eta_k, A \colon \Theta \to \R$,

such that each $P_\theta$ has a [[density|1NTKG64F7N]] with respect to $\mu$ of the form
$$p_\theta(x) = h(x) \exp\Big( \sum_{i=1}^{k} \eta_i(\theta) T_i(x) - A(\theta) \Big), \qquad x \in \mathcal{X}.$$

## Remarks

The function $A$ is fixed by normalization: $A(\theta) = \log \int h(x) \exp\big(\sum_i \eta_i(\theta) T_i(x)\big) \, \mu(dx)$.
The numbers $\eta_i = \eta_i(\theta)$ are the *natural parameters*, and writing the density in terms of $\eta$ gives the *canonical form*.

Example: the [[Bernoulli distribution|0386Y0Z7Y7]] with parameter $p \in (0, 1)$, with $\mu$ the counting measure on $\set{0, 1}$.
Its density is $p^x (1-p)^{1-x} = \exp\big(x \log \tfrac{p}{1-p} + \log(1-p)\big)$.
So it is a $1$-parameter exponential family with $h = 1$, $T(x) = x$, $\eta(p) = \log \frac{p}{1-p}$ and $A(p) = -\log(1-p)$.

Non-example: the uniform distributions on $[0, \theta]$ for $\theta > 0$.
In an exponential family the set $\set{x : p_\theta(x) > 0} = \set{x : h(x) > 0}$ does not depend on $\theta$, up to a $\mu$-null set, because the exponential factor is positive.
For the uniform family this set is $[0, \theta]$, which moves with $\theta$, so no choice of $h$, $T_i$, $\eta_i$, $A$ works.
