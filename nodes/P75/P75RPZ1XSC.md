---
tag: P75RPZ1XSC
kind: definition
name: Contact geometry of thermodynamics
msc: [80A10, 53D10, 53B50]
defines: ZTH9SSWCDG
uses: [WNSAZD8EZC, RTAVY44P4Z, 41NHDR6MH6, F6JVQ12X43, SPY89W0RJ7, HKPHRSN3ER]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_geometry
---

## Definition

Fix $n \ge 1$.
The *thermodynamic phase space* is $\mathcal{T} = \R^{2n+1}$ with coordinates $(\Phi, E^1, \dots, E^n, I_1, \dots, I_n)$ and the $1$-form
$$\Theta = d\Phi - \sum_{a=1}^{n} I_a \, dE^a.$$
Here $\Phi$ stands for a thermodynamic potential, the $E^a$ for extensive variables and the $I_a$ for the conjugate intensive variables.
Since $\Theta \wedge (d\Theta)^n \ne 0$ everywhere, $(\mathcal{T}, \Theta)$ is a [[contact manifold|WNSAZD8EZC]].
A thermodynamic system with fundamental relation $\Phi = f(E^1, \dots, E^n)$, for a differentiable $f$, is represented by its *equilibrium manifold*
$$\mathcal{E} = \set{ (f(E), E, \partial f / \partial E^1, \dots, \partial f / \partial E^n) : E \in D },$$
for an open domain $D \subseteq \R^n$.
It is an $n$-dimensional [[Legendrian submanifold|RTAVY44P4Z]]: the pull-back of $\Theta$ to $\mathcal{E}$ is $0$.

## Remarks

Example: a simple one-component system with fixed amount of matter has $n = 2$, $\Phi = U$, $(E^1, E^2) = (S, V)$ and $(I_1, I_2) = (T, -p)$.
Then $\Theta = dU - T\,dS + p\,dV$, and $\Theta = 0$ on $\mathcal{E}$ is exactly the [[fundamental thermodynamic relation|41NHDR6MH6]] $dU = T\,dS - p\,dV$ for the [[internal energy|F6JVQ12X43]] $U(S, V)$ and the [[entropy|SPY89W0RJ7]] $S$.

Non-example: for $n = 2$ take the surface on which $U = S + V$, $T = 2$ and $p = 0$, parametrised by $(S, V)$.
On it $\Theta = d(S + V) - 2\,dS = dV - dS \ne 0$, so it is not Legendrian and is not the equilibrium manifold of any system.

The [[Legendre transformation|HKPHRSN3ER]] that sends $(\Phi, E^1, I_1)$ to $(\Phi - I_1 E^1, I_1, -E^1)$ and fixes the other coordinates preserves $\Theta$ exactly.
For $\Phi = U$ and $E^1 = S$ it maps the equilibrium manifold of $U(S, V)$ to that of the Helmholtz free energy $U - TS$ as a function of $(T, V)$.
