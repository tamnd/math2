---
tag: 4NQ2GAJ8MH
kind: definition
name: Hicksian demand function
msc: [91B42, 91B16]
defines: ZFX4T69SST
uses: [Y0M5J89V2Q, GZZS4MTDG9, EQPEPJ7QQZ]
sources:
  - url: https://en.wikipedia.org/wiki/Hicksian_demand_function
---

## Definition

Let $u \colon \R^n_{\ge 0} \to \R$ be a continuous [[utility function|GZZS4MTDG9]] and let $U$ be the set of utility levels $\bar{u} > u(0)$ that $u$ reaches.
Assume that, for every price vector $p \in \R^n$ with all entries positive and every $\bar{u} \in U$, the [[expenditure minimization problem|Y0M5J89V2Q]]
$$\min \set{p \cdot x : x \in \R^n_{\ge 0},\ u(x) \ge \bar{u}}$$
has exactly one solution.
The *Hicksian demand function* of $u$ is the map $(p, \bar{u}) \mapsto h(p, \bar{u})$ that sends $(p, \bar{u})$ to this solution.
The minimal value $e(p, \bar{u}) = p \cdot h(p, \bar{u})$ is the *expenditure function*.

## Remarks

For $u(x_1, x_2) = \sqrt{x_1 x_2}$, the demand is $h(p, \bar{u}) = (\bar{u}\sqrt{p_2/p_1}, \bar{u}\sqrt{p_1/p_2})$.
Check: $u(h) = \bar{u}$, and on the curve $x_1 x_2 = \bar{u}^2$ the cost $p_1 x_1 + p_2 \bar{u}^2 / x_1$ has its only minimum where $p_1 = p_2 \bar{u}^2 / x_1^2$, that is, $x_1 = \bar{u}\sqrt{p_2/p_1}$.
For $u(x_1, x_2) = x_1 + x_2$ and $p_1 = p_2$, every bundle with $x_1 + x_2 = \bar{u}$ is cheapest, so the solution is not unique and there is no Hicksian demand function.
The demand is homogeneous of degree zero in $p$: $h(t p, \bar{u}) = h(p, \bar{u})$ for $t > 0$.
The law of compensated demand holds: $(p' - p) \cdot (h(p', \bar{u}) - h(p, \bar{u})) \le 0$, so the own-price effect is never positive.
Under local nonsatiation it is linked to the [[Marshallian demand|EQPEPJ7QQZ]] by $h(p, \bar{u}) = x(p, e(p, \bar{u}))$.
