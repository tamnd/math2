---
tag: SKG7KA5GZ8
kind: definition
name: Quantum vortex
msc: [76Y05, 82D50, 76B47]
defines: V4KQ2RVR7E
uses: [4PZBRJ78X4, BTHH4Y71QR, 0NQSV2EWDR, F5EAWFMC8A]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_vortex
---

## Definition

Let a [[superfluid|4PZBRJ78X4]] of particles of mass $m$ be described by a smooth wave function $\psi = \sqrt{n} \, e^{i \theta}$ on a region $\Omega \subseteq \R^3$.
Where $n > 0$, its superfluid velocity is $\mathbf{v}_s = (\hbar / m) \nabla \theta$.
A *quantum vortex* is a curve $\Gamma \subset \Omega$ such that:

1. $\psi = 0$ on $\Gamma$, and $\psi \ne 0$ near $\Gamma$ off $\Gamma$;
2. along a small loop $C$ around $\Gamma$, the phase $\theta$ changes by $2\pi q$ for a nonzero integer $q$, the [[winding number|0NQSV2EWDR]] of $\psi$ along $C$.

The integer $q$ is the *charge* of the vortex.
In two dimensions, a quantum vortex is an isolated zero of $\psi$ with nonzero winding number.

## Remarks

The [[circulation|BTHH4Y71QR]] around the vortex is quantised:
$$\oint_C \mathbf{v}_s \cdot d\mathbf{l} = \frac{\hbar}{m} \oint_C \nabla \theta \cdot d\mathbf{l} = q \, \frac{h}{m}.$$
Example: in the plane, the [[Gross–Pitaevskii|F5EAWFMC8A]] equation has solutions $\psi = f(r) e^{i q \varphi}$ in polar coordinates $(r, \varphi)$, with $f(0) = 0$ and $f(r) \to \sqrt{n_\infty}$ as $r \to \infty$.
There $\mathbf{v}_s = q \hbar / (m r) \, \mathbf{e}_\varphi$, and the circulation around any circle centred at $0$ equals $2\pi r \cdot q\hbar/(m r) = q h / m$.
Non-example: a classical [[Rankine vortex|1JP90A94FR]] can have any circulation, and its core rotates as a solid body with nonzero vorticity.
Away from its core, the flow of a quantum vortex is irrotational, like a point vortex in an ideal fluid.
