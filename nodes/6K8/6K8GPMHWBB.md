---
tag: 6K8GPMHWBB
kind: statement
role: theorem
name: Evans potential theorem
msc: [31A15, 31B15]
uses: [0R6EWFKRCF, 059TJN0NZ1, C95QJ7YH5T, 46NHWJHW44, W9N1TR1X8P]
about: [C95QJ7YH5T]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_set_(potential_theory)
---

## Statement

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$ of logarithmic [[capacity zero|W9N1TR1X8P]], or equivalently a compact [[polar set|C95QJ7YH5T]].
Then there is a Borel [[probability measure|059TJN0NZ1]] $\mu$ on $K$ whose [[logarithmic potential|46NHWJHW44]]
$$U^\mu(z) = \int_K \log \frac{1}{\abs{z - w}} \, d\mu(w)$$
satisfies $U^\mu(z) = +\infty$ for every $z \in K$.

## Remarks

The potential $U^\mu$ is harmonic on $\C \setminus K$ and superharmonic on $\C$, so $u = -U^\mu$ is a subharmonic function equal to $-\infty$ exactly on $K$.
Such a potential is called an Evans potential of $K$.

Proof idea: let $K_k = \set{z : \operatorname{dist}(z, K) \le 1/k}$.
Since $K$ has capacity zero, the capacities of the compact sets $K_k$ tend to $0$, so their Robin constants $V(K_k)$ tend to $+\infty$.
By Frostman's theorem, the potential of the equilibrium measure of $K_k$ equals $V(K_k)$ on $K$.
One combines these equilibrium measures with suitable weights and passes to a limit measure carried by $K$.
The delicate step is to keep the potential infinite at every point of $K$ in the limit.

Example: for $K = \set{0}$, the measure $\mu = \delta_0$ has $U^\mu(z) = \log(1/\abs{z})$, which is $+\infty$ exactly at $0$.

The theorem is false without polarity.
If $K$ is compact and not polar, then for every probability measure $\mu$ on $K$ the set where $U^\mu = +\infty$ is polar, so it cannot contain $K$.
The analogous statement in $\R^n$, $n \ge 3$, holds with the Newtonian potential $\int \abs{x - y}^{2-n} \, d\mu(y)$.

## Explanations

### L1 human

A polar set is one where some subharmonic function equals $-\infty$.
The theorem says that for a compact polar set one can choose this function very concretely: as minus the potential of a charge placed on the set itself.
It also says that the infinite values can be made to occur exactly on the set and nowhere else.

### L2 human

Evans potentials are a key tool in the study of exceptional sets.
They are used to show that compact polar sets are removable for bounded harmonic functions and to build harmonic functions with prescribed singular behaviour.
They also show that the definition of polar sets by subharmonic functions agrees with the definition by capacity for compact sets.
