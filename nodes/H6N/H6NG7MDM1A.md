---
tag: H6NG7MDM1A
kind: definition
name: Spin connection
msc: ["53C27", "53C05", "83C60"]
defines: FHZETS8QTT
uses: [6VFADXR4MW, PCNPQ7YBDE, DH4P0W4V3J]
sources:
  - url: https://en.wikipedia.org/wiki/Spin_connection
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|6VFADXR4MW]] of dimension $n$, and let $\nabla$ be its [[Levi-Civita connection|PCNPQ7YBDE]].
Let $(e_1, \dots, e_n)$ be a local orthonormal [[frame|DH4P0W4V3J]] on an open set $U$, with dual coframe $(\theta^1, \dots, \theta^n)$.
Let $\eta_{ab} = g(e_a, e_b)$, a constant diagonal matrix with entries $\pm 1$.
The *spin connection* of this frame is the matrix of 1-forms $\omega^a{}_b$ on $U$ defined by
$$\nabla_X e_b = \sum_{a=1}^n \omega^a{}_b(X) \, e_a \quad \text{for every vector field } X \text{ on } U.$$

## Remarks

The forms $\omega_{ab} = \eta_{ac} \omega^c{}_b$ satisfy $\omega_{ab} = -\omega_{ba}$, because $\nabla$ preserves the metric.
Since $\nabla$ has no torsion, they satisfy the first structure equation of Cartan, $d\theta^a + \omega^a{}_b \wedge \theta^b = 0$.
These two properties determine $\omega$ uniquely from the frame.
Example: on $\R^2 \setminus \set{0}$ with polar coordinates, take $e_1 = \partial_r$ and $e_2 = r^{-1} \partial_\varphi$, so $\theta^1 = dr$ and $\theta^2 = r \, d\varphi$.
Then $\omega^2{}_1 = d\varphi$ and $\omega^1{}_2 = -d\varphi$.
Check: $d\theta^2 = dr \wedge d\varphi = -\omega^2{}_1 \wedge \theta^1$, and $d\theta^1 = 0 = -\omega^1{}_2 \wedge \theta^2$.
Non-example: for the coordinate frame $(\partial_r, \partial_\varphi)$, which is not orthonormal, the connection matrix is not antisymmetric.
Indeed $\nabla_{\partial_r} \partial_\varphi = r^{-1} \partial_\varphi$, so its diagonal entry $\omega^\varphi{}_\varphi = r^{-1} dr$ is nonzero.
On a spin manifold the matrix $\omega_{ab}$ acts on spinor fields $\psi$, and in one common convention $\nabla \psi = d\psi + \tfrac14 \omega_{ab} \gamma^a \gamma^b \psi$, where $\gamma^a$ are the Clifford generators.

## Explanations

### L1 human

The spin connection tells how an orthonormal frame turns, compared with parallel transport, as one moves in a given direction.
