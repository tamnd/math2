---
tag: 01DSNP0B4R
kind: definition
name: Periodic orbit
aliases: [closed-orbit, cycle]
msc: [34C25, 37C27]
defines: 0AA97XA70K
uses: [07BNRFQ0PJ, 0BVT6VSB3S, 04SW7WECS8]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_point
    locator: Dynamical system
  - url: https://en.wikipedia.org/wiki/Limit_cycle
    locator: Definition
---

## Definition

Let $U$ be an open subset of $\mathbb{R}^n$, let $f : U \to \mathbb{R}^n$ be locally Lipschitz, and consider the [[autonomous system|07BNRFQ0PJ]] $x' = f(x)$.
A [[solution|04SW7WECS8]] $\gamma : \mathbb{R} \to U$ is periodic if it is not constant and there is a real number $T > 0$ with $\gamma(t + T) = \gamma(t)$ for each $t \in \mathbb{R}$.
The smallest such $T$ is the period of $\gamma$.
A periodic orbit, or closed orbit, is the [[trajectory|0BVT6VSB3S]] $\gamma(\mathbb{R})$ of a periodic solution $\gamma$.

## Remarks

A non-constant periodic solution has a smallest period $T > 0$, because $\gamma$ is continuous and not constant.
A periodic orbit is a simple closed curve in $U$.
Let a maximal solution $\gamma$ that is not constant satisfy $\gamma(t_1 + T) = \gamma(t_1)$ for one $t_1$ and one $T > 0$. Then, by [[uniqueness|025PKW8AMR]], $\gamma$ is defined on $\mathbb{R}$ and is periodic.
For the [[harmonic oscillator|0YG0ZJPTWG]] $x' = y$, $y' = -x$, each circle $x^2 + y^2 = r^2$ with $r > 0$ is a periodic orbit of period $2\pi$.

## Explanations

### L1 human

A periodic orbit is a motion that repeats itself exactly after a fixed time.
In the phase space it is a closed loop that the state goes around again and again.
