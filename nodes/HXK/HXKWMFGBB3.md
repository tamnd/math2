---
tag: HXKWMFGBB3
kind: statement
role: theorem
name: Lorentz reciprocity theorem
msc: [78A25, 78A40]
uses: [9BWWD4QK8Y, F768YN0P2V, 5MJQ5J5H8Z, HSPJC4VVQ8]
about: [9BWWD4QK8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Reciprocity_(electromagnetism)
---

## Statement

Fix an angular frequency $\omega > 0$ and the time factor $e^{-i\omega t}$.
Let $\varepsilon(\mathbf{x})$ and $\mu(\mathbf{x})$ be $3 \times 3$ complex matrix fields, the [[permittivity|F768YN0P2V]] and [[permeability|5MJQ5J5H8Z]], that are symmetric ($\varepsilon^T = \varepsilon$, $\mu^T = \mu$) at every point.
Assume that outside some bounded region they equal the constants $\varepsilon_0 I$ and $\mu_0 I$ of vacuum.
For $j = 1, 2$, let $\mathbf{J}_j$ be a current density with bounded support.
Let $(\mathbf{E}_j, \mathbf{H}_j)$ solve the time-harmonic [[Maxwell's equations|9BWWD4QK8Y]]
$$\nabla \times \mathbf{E}_j = i\omega \mu \mathbf{H}_j, \qquad \nabla \times \mathbf{H}_j = -i\omega \varepsilon \mathbf{E}_j + \mathbf{J}_j$$
that satisfies the [[Silver–Müller radiation condition|HSPJC4VVQ8]].
Then
$$\nabla \cdot (\mathbf{E}_1 \times \mathbf{H}_2 - \mathbf{E}_2 \times \mathbf{H}_1) = \mathbf{J}_1 \cdot \mathbf{E}_2 - \mathbf{J}_2 \cdot \mathbf{E}_1,$$
and
$$\int_{\R^3} \mathbf{J}_1 \cdot \mathbf{E}_2 \, dV = \int_{\R^3} \mathbf{J}_2 \cdot \mathbf{E}_1 \, dV.$$

## Remarks

The local identity follows from $\nabla \cdot (\mathbf{a} \times \mathbf{b}) = \mathbf{b} \cdot (\nabla \times \mathbf{a}) - \mathbf{a} \cdot (\nabla \times \mathbf{b})$ and the two curl equations; the terms $i\omega\, \mathbf{H}_2 \cdot \mu \mathbf{H}_1$ and $i\omega\, \mathbf{E}_1 \cdot \varepsilon \mathbf{E}_2$ cancel against their partners exactly because $\mu$ and $\varepsilon$ are symmetric.
Integrating over a large ball and using the divergence theorem leaves a surface integral.
It tends to $0$ by the radiation condition, since far away both fields are outgoing waves with $\mathbf{H}_j \approx \eta_0^{-1}\, \hat{\mathbf{r}} \times \mathbf{E}_j$.
Note that the products are bilinear, without complex conjugates; this is not an energy statement.
Example: for two antennas, it implies that the transmitting and receiving patterns of one antenna are the same.
It also implies that the transfer impedance from antenna $1$ to antenna $2$ equals that from $2$ to $1$.
The symmetry hypothesis is necessary.
In a magnetized plasma or a ferrite, $\varepsilon$ or $\mu$ is not symmetric, and devices such as Faraday isolators transmit in one direction only.
Losses do not break reciprocity, as long as the matrices stay symmetric.

## Explanations

### L1 human

Put a source at point A and measure the signal at point B.
Move the same source to B, and the signal at A is the same.
This holds even in complicated surroundings with mirrors, lenses and absorbers, as long as the materials behave the same way in both directions.
It is why an antenna receives best from the same directions in which it transmits best.

### L2 human

Reciprocity is a symmetry of the Green's function of the Maxwell operator: $G(\mathbf{x}, \mathbf{y}) = G(\mathbf{y}, \mathbf{x})^T$ for symmetric media.
It is used to compute received signals from transmitted fields, to derive the symmetry of scattering matrices, and to simplify integral equations in the method of moments.
It is the electromagnetic analogue of the symmetry of Green's functions for self-adjoint boundary value problems, and of Green's reciprocity theorem in electrostatics.
Non-reciprocal media, with non-symmetric $\varepsilon$ or $\mu$, are exactly those needed to build isolators and circulators.
