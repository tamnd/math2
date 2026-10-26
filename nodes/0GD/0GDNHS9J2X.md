---
tag: 0GDNHS9J2X
kind: definition
name: Curl
msc: [26B12]
defines: 0NF6GQNXMY
uses: [0N67NBKQ5T, 05AXG3QRKR]
sources:
  - url: https://en.wikipedia.org/wiki/Curl_(mathematics)
    locator: In Cartesian coordinate systems
  - url: https://en.wikipedia.org/wiki/Curl_(mathematics)
    locator: Examples
---

## Definition

Let $U \subseteq \mathbb{R}^3$ be open, and let $F = (P, Q, R) \colon U \to \mathbb{R}^3$ be a [[vector field|0N67NBKQ5T]] whose first [[partial derivatives|05AXG3QRKR]] exist on $U$.
The curl of $F$ is the vector field $\operatorname{curl} F \colon U \to \mathbb{R}^3$,
$$\operatorname{curl} F = \nabla \times F = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \ \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \ \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right).$$
A field with $\operatorname{curl} F = 0$ on $U$ is irrotational, or curl-free.

## Remarks

As a mnemonic, $\nabla \times F$ is the formal determinant of the matrix with rows $(\mathbf{i}, \mathbf{j}, \mathbf{k})$, $(\partial_x, \partial_y, \partial_z)$ and $(P, Q, R)$.
For $F(x, y, z) = (-y, x, 0)$, $\operatorname{curl} F = (0, 0, 2)$. For $F(x, y, z) = (x, y, z)$, $\operatorname{curl} F = 0$.
For a plane field $(P, Q)$, one uses the scalar curl $\partial Q / \partial x - \partial P / \partial y$, the third component of the curl of $(P, Q, 0)$. It appears in [[Green's theorem|0HR3N02317]].
Take small loops orthogonal to a unit vector $n$. The component of $\operatorname{curl} F$ along $n$ is the limit of the circulation of $F$ around these loops, divided by the enclosed area. This follows from [[Stokes' theorem|0AKRKVHW94]].

## Explanations

### L1 human

Put a tiny paddle wheel into a fluid with velocity field $F$.
If it spins, the curl is not zero there. The curl points along the axis about which the wheel spins fastest.
