---
tag: VXBT9QCN22
kind: definition
name: General covariance
msc: [83C05, 53Z05]
defines: Y6JK62NNME
uses: [F45VQ47GPV, 0KZZ70ZHXP, WX302T93TW]
sources:
  - url: https://en.wikipedia.org/wiki/General_covariance
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]].
Consider a field theory whose fields are [[tensor fields|WX302T93TW]] $\psi = (\psi_1, \ldots, \psi_k)$ on $M$.
Its laws are a system of equations, and $\mathcal S$ denotes the set of its solutions $\psi$.
The theory is *generally covariant* if for every [[diffeomorphism|0KZZ70ZHXP]] $\varphi \colon M \to M$ and every solution $\psi \in \mathcal S$, the pulled-back fields $\varphi^* \psi$ also form a solution.

## Remarks

Example: the vacuum Einstein equations $\mathrm{Ric}_g = 0$ for a Lorentzian metric $g$.
For a diffeomorphism $\varphi$, $\mathrm{Ric}_{\varphi^* g} = \varphi^* \mathrm{Ric}_g$, so $\mathrm{Ric}_g = 0$ implies $\mathrm{Ric}_{\varphi^* g} = 0$.
Non-example: on $M = \R^4$ with coordinates $(t, x, y, z)$, the wave equation $-\partial_t^2 f + \partial_x^2 f + \partial_y^2 f + \partial_z^2 f = 0$ for a function $f$ alone is not generally covariant.
The diffeomorphism $(t, x, y, z) \mapsto (t, x + t^2, y, z)$ does not preserve the solutions: the solution $f = x$ is pulled back to $x + t^2$, and $-\partial_t^2 (x + t^2) = -2 \neq 0$.
It becomes generally covariant if the metric $\eta$ is treated as a field too, and the equation is written as $\eta^{\mu\nu} \nabla_\mu \nabla_\nu f = 0$.
The price is that $\eta$ is a fixed background, unlike the dynamical metric of general relativity.
For this reason some authors reserve the name for theories with no such fixed background fields, and call the weaker property diffeomorphism covariance.
