---
tag: HGGYPYA9XB
kind: example
name: The quarter-turn rotation of the plane
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [0J7H0YBFDJ]
uses: [0PTF1PTJK0, 0RJF668P1T, 0HFREYRSZP]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Examples in two dimensions
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
---

## Example

A quarter turn sends the plane to itself, so it can be repeated, and four quarter turns bring every vector back.
Let $R \colon \R^2 \to \R^2$ be the [[rotation|0HFREYRSZP]] by $90°$ counterclockwise,
$$R(x, y) = (-y, \; x), \qquad A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$

1. The map $R$ is [[linear|0RJF668P1T]], since $R(v) = Av$ for each $v \in \R^2$.
2. The source and the target of $R$ are both $\R^2$, so $R$ is an [[endomorphism|0PTF1PTJK0]] of $\R^2$.
3. We have $R^2(x, y) = R(-y, x) = (-x, \; -y)$, so $R^2 = -\id$.
4. Then $R^4 = (R^2)^2 = (-\id)^2 = \id$.
5. So $R \circ R^3 = R^3 \circ R = \id$, and $R$ is an automorphism with inverse $R^3$, the rotation by $-90°$.

Check: $R(1, 0) = (0, 1)$, $R(0, 1) = (-1, 0)$, $R(-1, 0) = (0, -1)$ and $R(0, -1) = (1, 0)$, so four steps return $(1, 0)$ to itself.

## Remarks

The map $R$ has no real eigenvalue.
If $R(v) = \lambda v$ with $v \ne 0$, then $-v = R^2(v) = \lambda^2 v$, so $\lambda^2 = -1$, which has no real solution.
Over $\C$, the same matrix has the eigenvalues $i$ and $-i$.

If we change the angle to $\theta$, the rotation has matrix $\begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$.
It satisfies $R_\theta^k = \id$ for some $k \ge 1$ exactly when $\theta / 2\pi$ is rational.

## Explanations

### L1 human

Turn the plane by a quarter turn about the origin.
This sends the plane to itself, so it is an endomorphism.
Four quarter turns bring each vector back, so the turn can be undone.

### L2 human

Because $R$ maps $\R^2$ to itself, its powers make sense: $R^2$ is the half turn $-\id$, and $R^4 = \id$.
The equation $R^4 = \id$ shows directly that $R$ is invertible, with inverse $R^3$.
Watch out: there is no real eigenvector, since no line through the origin is sent to itself by a quarter turn.
