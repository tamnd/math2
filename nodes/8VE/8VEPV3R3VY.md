---
tag: 8VEPV3R3VY
kind: definition
name: McKendrick–von Foerster equation
msc: [92D25, 35Q92, 35L04]
defines: SV5Q8A9GNA
uses: [1YEMFQ1H32, GC5BDZ6QBC, PVD7VZJZ9B]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Foerster_equation
---

## Definition

Let $\mu \colon [0, \infty) \to [0, \infty)$ be the age-specific death rate and $\beta \colon [0, \infty) \to [0, \infty)$ the age-specific birth rate.
Let $n_0 \colon [0, \infty) \to [0, \infty)$ be an initial age density.
The *McKendrick–von Foerster equation* is the problem of finding the density $n(a, t) \ge 0$ of individuals of age $a \ge 0$ at time $t \ge 0$ such that:

1. $\dfrac{\partial n}{\partial t}(a, t) + \dfrac{\partial n}{\partial a}(a, t) = -\mu(a) \, n(a, t)$ for $a > 0$, $t > 0$;
2. $n(0, t) = \displaystyle\int_0^\infty \beta(a) \, n(a, t) \, da$ for $t > 0$;
3. $n(a, 0) = n_0(a)$ for $a \ge 0$.

The number of individuals with age between $a_1$ and $a_2$ at time $t$ is $\int_{a_1}^{a_2} n(a, t) \, da$.

## Remarks

Clause 1 is a [[transport equation|PVD7VZJZ9B]] with speed $1$ and a loss term; clause 2 is the renewal condition that counts the newborns.
Along a characteristic $a - t = \text{const}$ the density satisfies $\frac{d}{dt} n = -\mu n$, so for $a > t$ the solution is $n(a, t) = n_0(a - t) \exp\left(-\int_{a - t}^{a} \mu(s) \, ds\right)$.
Example: with $\mu \equiv m$ and $\beta \equiv b$ constant, the function $n(a, t) = C e^{(b - m) t} e^{-b a}$ satisfies clause 1, since $\partial_t n + \partial_a n = (b - m - b) n = -m n$, and clause 2, since $\int_0^\infty b \, C e^{(b - m)t} e^{-ba} \, da = C e^{(b - m) t}$.
Non-example: the ordinary differential equation $N' = (b - m) N$ for the total number $N$ is not of this form, since it has no age variable.
