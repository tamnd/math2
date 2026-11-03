---
tag: 5SYY633TJE
kind: definition
name: Force-free magnetic field
msc: [78A30, 76W05]
defines: AHEEC3Y5JF
uses: [XRED3C547P, S3RZRCH0T5, HK2E8BX09G, 0NF6GQNXMY, 0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Force-free_magnetic_field
---

## Definition

Let $U \subseteq \R^3$ be open, and let $B \colon U \to \R^3$ be a $C^1$ [[magnetic field|XRED3C547P]] with $\nabla \cdot B = 0$.
Then $B$ is *force-free* if
$$(\nabla \times B) \times B = 0 \quad \text{on } U,$$
where $\nabla \times$ is the [[curl|0NF6GQNXMY]] and $\times$ the [[cross product|0N5N15HWZ7]].
Equivalently, on the set where $B \neq 0$ there is a function $\alpha$ with $\nabla \times B = \alpha B$.
The field is *linear force-free* if $\alpha$ is a constant on $U$.

## Remarks

By [[Ampère's circuital law|HK2E8BX09G]] in magnetostatics, $\nabla \times B = \mu_0 J$, so the condition says that the [[Lorentz force|S3RZRCH0T5]] density $J \times B$ vanishes.
Taking the divergence of $\nabla \times B = \alpha B$ and using $\nabla \cdot B = 0$ gives $B \cdot \nabla \alpha = 0$ where $\alpha$ is $C^1$, so $\alpha$ is constant along each field line.
Curl-free fields, with $\alpha = 0$, are force-free; they are called potential fields.

Example: $B = (\sin z, \cos z, 0)$ on $\R^3$ has $\nabla \cdot B = 0$ and $\nabla \times B = (\sin z, \cos z, 0) = B$.
So it is linear force-free with $\alpha = 1$; its field lines are horizontal and turn steadily with height.

Non-example: $B = (-y, x, 0)$ has $\nabla \times B = (0, 0, 2)$, and $(\nabla \times B) \times B = (-2x, -2y, 0)$, which is nonzero away from the $z$-axis.
