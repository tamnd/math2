---
tag: NZBYY2NE8T
kind: definition
name: Parametric oscillator
msc: [70J40, 34C25, 70K28]
defines: HF4K06Q6XX
uses: [0YG0ZJPTWG, 0NT64JV96A, BJVZXPB297, FPS7YFGX32, 2DDZXF5EBY]
sources:
  - url: https://en.wikipedia.org/wiki/Parametric_oscillator
---

## Definition

Let $T > 0$ and let $\beta, q \colon \R \to \R$ be continuous functions with period $T$, not both constant.
A *parametric oscillator* is the linear [[ordinary differential equation|0NT64JV96A]]
$$x''(t) + \beta(t) \, x'(t) + q(t) \, x(t) = 0$$
for a real function $x$ of the time $t$.
Here $\beta$ is the damping coefficient and $q$ plays the role of the squared frequency.

## Remarks

One speaks of *parametric resonance* when the periodic variation of the coefficients produces solutions that grow without bound.

The *Mathieu equation* $x'' + \omega_0^2 (1 + h \cos \gamma t) \, x = 0$ with $\omega_0 > 0$, $\gamma > 0$ and $h \neq 0$ satisfies the definition, with $\beta = 0$ and $q(t) = \omega_0^2 (1 + h \cos \gamma t)$, which has period $2 \pi / \gamma$.
Its solutions are expressed with [[Mathieu functions|2DDZXF5EBY]].
For small $\abs{h}$, parametric resonance occurs for $\gamma$ near the values $2 \omega_0 / n$ with $n = 1, 2, 3, \ldots$, and the instability is strongest near $\gamma = 2 \omega_0$.

A non-example is the [[harmonic oscillator|0YG0ZJPTWG]] $x'' + \omega_0^2 x = 0$: both coefficients are constant, so it fails the first clause.
A forced oscillator $x'' + \omega_0^2 x = F \cos \gamma t$ is also not parametric, because the time dependence enters as a separate term and not through a coefficient.

By [[Floquet theory|BJVZXPB297]], the stability of the oscillator is decided by its two [[Floquet multipliers|FPS7YFGX32]], the eigenvalues of the monodromy matrix over one period.
With $\beta = 0$ their product is $1$, so the zero solution is unstable as soon as the trace of the monodromy matrix has absolute value larger than $2$.

## Explanations

### L1 human

An ordinary oscillator has a fixed spring and a fixed mass.
In a parametric oscillator the spring constant, or another coefficient, is wiggled periodically in time.
Wiggling it at the right rhythm feeds energy into the motion, so even a tiny oscillation can grow without bound.
