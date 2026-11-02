---
tag: HS5ZEM7TWA
kind: definition
name: Bifurcation diagram
msc: [37G35, 37G10]
defines: 2XDRZV3GSA
uses: [D9TW46P19Y, 0N8NGKDZDZ, 7FWX24X5MW, P88X34MSVV, QN9X9BNKTX]
sources:
  - url: https://en.wikipedia.org/wiki/Bifurcation_diagram
---

## Definition

Let $I \subseteq \R$ be an interval of parameters and $X$ a state space.
Let $(\phi_\mu)_{\mu \in I}$ be a one-parameter family of dynamical systems on $X$, flows or maps.
For each $\mu$, let $A_\mu \subseteq X$ be a chosen invariant set of $\phi_\mu$.
Typical choices are the set of [[equilibria|0N8NGKDZDZ]] and periodic points, or the [[attractor|7FWX24X5MW]] reached from a fixed initial point.
The *bifurcation diagram* of the family for this choice is the set
$$\set{(\mu, x) \in I \times X : x \in A_\mu}.$$

## Remarks

Example: for $\dot x = \mu x - x^3$ on $\R$, take $A_\mu$ to be the set of equilibria.
The equilibria solve $x(\mu - x^2) = 0$, so the diagram is the line $x = 0$ together with the parabola $\mu = x^2$.
The branches meet at $(0, 0)$, the [[pitchfork bifurcation|P88X34MSVV]] of [[bifurcation theory|D9TW46P19Y]].
Usually stable branches are drawn solid and unstable ones dashed.
For the [[logistic map|QN9X9BNKTX]], one takes for $A_\mu$ the limit points of the orbit of a typical initial point.
Non-example: a plot of a single orbit $x_n$ against the time $n$, at one parameter value, is a time series, not a bifurcation diagram.
