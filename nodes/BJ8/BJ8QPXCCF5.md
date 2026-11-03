---
tag: BJ8QPXCCF5
kind: statement
role: theorem
name: Rushbrooke inequality
msc: [82B27, 82B30]
uses: [SQ41AZGZ2P]
about: [SQ41AZGZ2P]
sources:
  - url: https://en.wikipedia.org/wiki/Rushbrooke_inequality
same_as:
  wikidata: Q7380772
  wikipedia: Rushbrooke inequality
---

## Statement

Consider a magnetic system with magnetization $M(T, H)$, isothermal susceptibility $\chi_T = (\partial M / \partial H)_T > 0$, and specific heats $C_H$ and $C_M \ge 0$ at fixed field and at fixed magnetization.
Let $T_c$ be its critical temperature and $t = (T - T_c)/T_c$.
Assume that, as $t \to 0^-$ at $H = 0$, the [[critical exponents|SQ41AZGZ2P]] $\alpha'$, $\beta$, $\gamma'$ exist with
$$C_H \sim (-t)^{-\alpha'}, \qquad M \sim (-t)^{\beta}, \qquad \Big(\frac{\partial M}{\partial T}\Big)_H \sim (-t)^{\beta - 1}, \qquad \chi_T \sim (-t)^{-\gamma'}.$$
Then
$$\alpha' + 2\beta + \gamma' \ge 2.$$

## Remarks

Proof: thermodynamics gives the identity $\chi_T (C_H - C_M) = T \, (\partial M / \partial T)_H^2$.
Since $C_M \ge 0$, this gives $C_H \ge T (\partial M / \partial T)_H^2 / \chi_T$.
The right side behaves like $(-t)^{2\beta - 2 + \gamma'}$ and the left like $(-t)^{-\alpha'}$.
As $-t \to 0^+$, the inequality between the powers forces $-\alpha' \le 2\beta - 2 + \gamma'$.

Example: mean-field theory gives $\alpha' = 0$, $\beta = 1/2$ and $\gamma' = 1$, and $0 + 1 + 1 = 2$, so equality holds.
The two-dimensional Ising model gives $0 + 1/4 + 7/4 = 2$, also with equality.

Rushbrooke proved the inequality in 1963.
Under the Widom scaling hypothesis it becomes the equality $\alpha' + 2\beta + \gamma' = 2$.

## Explanations

### L1 human

The specific heat, the magnetization and the susceptibility are linked by an exact law of thermodynamics.
Near the critical point this law becomes a constraint on how fast they can blow up or vanish.
The Rushbrooke inequality says that their three exponents, added in the right way, are at least $2$.

### L2 human

The inequality is one of several rigorous inequalities among critical exponents that use only convexity and stability, such as the positivity of the specific heat.
It is a check on any proposed set of exponents.
Experiments and exactly solved models show equality, and the [[scaling relations|Z6W0AXDN9G]] explain why: under scaling the inequality becomes the Rushbrooke relation.
