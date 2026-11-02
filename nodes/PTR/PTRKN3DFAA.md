---
tag: PTRKN3DFAA
kind: definition
name: Bifurcation theory
msc: [37G10, 34C23]
defines: D9TW46P19Y
uses: [BBZP1R872N, 0NT64JV96A, 0T3GK0XCBC, 0N8NGKDZDZ, D4MGFAHVMT, MAP5J6HK0T]
sources:
  - url: https://en.wikipedia.org/wiki/Bifurcation_theory
---

## Definition

Let $\Lambda \subseteq \R^k$ be an open set of parameters.
For each $\mu \in \Lambda$, let $\dot x = F(x, \mu)$ be an [[ordinary differential equation|0NT64JV96A]] on an open set of $\R^n$, with $F$ smooth in $(x, \mu)$.
Two such systems are *topologically equivalent* if a homeomorphism maps the orbits of one onto the orbits of the other.
The homeomorphism must preserve the direction of time.
A parameter value $\mu_0 \in \Lambda$ is a *bifurcation value* if the following holds.
Every neighbourhood of $\mu_0$ contains some $\mu$ whose system is not topologically equivalent to the system at $\mu_0$.
*Bifurcation theory* studies the bifurcation values of such families and the changes of the [[phase portrait|0T3GK0XCBC]] that occur at them.

## Remarks

The same definitions apply to families of maps $x \mapsto f_\mu(x)$, with topological conjugacy in place of equivalence.
Example: for $\dot x = \mu - x^2$ on $\R$, the value $\mu_0 = 0$ is a bifurcation value.
For $\mu < 0$ there is no [[equilibrium|0N8NGKDZDZ]], for $\mu = 0$ there is one, and for $\mu > 0$ there are two, at $\pm\sqrt{\mu}$.
This is a [[saddle-node bifurcation|MAP5J6HK0T]].
Non-example: $\mu_0 = 1$ is not a bifurcation value of this family.
For all $\mu$ near $1$ there are two equilibria, $\sqrt{\mu}$ attracting and $-\sqrt{\mu}$ repelling, and the phase portraits are equivalent.
A system whose topological type is unchanged by every small perturbation of the vector field, not only by changes of $\mu$, is [[structurally stable|D4MGFAHVMT]].
Local bifurcations concern a neighbourhood of an equilibrium or periodic orbit; global ones, such as homoclinic bifurcations, involve whole orbits.
