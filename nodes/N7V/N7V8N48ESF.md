---
tag: N7V8N48ESF
kind: example
name: A cyclic vector for diag(1, 2)
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
instance_of: [42MMQBTP0M]
illustrates: [RK1QVMYW7H, 5VYBJYPYMW]
uses: [42MMQBTP0M, 5VYBJYPYMW, 0KCQ9Y3QKA, 0VH1TC1PWF]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Examples
---

## Example

Let $F$ be any field and let $T$ be the map of $A = \operatorname{diag}(1, 2) = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ on $F^2$.
We show that $v = (1, 1)$ is a [[cyclic vector|42MMQBTP0M]], and that $e_1$ is not.

1. $Av = (1, 2)$.
2. The matrix with columns $v$ and $Av$ is $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, with determinant $2 - 1 = 1 \ne 0$. So $v, Av$ is a [[basis|0KCQ9Y3QKA]] of $F^2$, and $Z(v; T) = F^2$.
3. $A^2 v = (1, 4)$, and $3 Av - 2 v = (3 - 2, 6 - 2) = (1, 4)$. So $A^2 v - 3 A v + 2 v = 0$.
4. By step 2, no polynomial of degree $1$ kills $v$. So the $T$-annihilator is $m_v = x^2 - 3x + 2 = (x - 1)(x - 2)$.
5. In the basis $v, Av$, the matrix of $T$ is the [[companion matrix|0VH1TC1PWF]] $C(x^2 - 3x + 2) = \begin{pmatrix} 0 & -2 \\ 1 & 3 \end{pmatrix}$, as the [[lemma on cyclic subspaces|5VYBJYPYMW]] predicts.
6. For $e_1$: $A e_1 = e_1$. So $Z(e_1; T) = F e_1$, of dimension $1$, and $m_{e_1} = x - 1$. So $e_1$ is not a cyclic vector.

## Remarks

The example shows that a cyclic map can have vectors that are not cyclic.
A vector $(a, b)$ is cyclic exactly when $\det \begin{pmatrix} a & a \\ b & 2b \end{pmatrix} = ab \ne 0$, that is, when it is not on an eigenline.
If $2$ is replaced by $1$, the matrix becomes $I_2$, and no vector is cyclic.
In characteristic $2$ the matrix is $\operatorname{diag}(1, 0)$, and the computation is the same.

## Explanations

### L1 human

The map keeps the first coordinate of a point and doubles the second.
Start at the point one, one.
The map sends it to the point one, two.
These two points do not lie on one line through the origin, so they reach every point of the plane.
The point one, zero only reaches its own line, since the map does not move it.

### L2 human

1. Take $v = (3, -1)$. Then $Av = (3, -2)$.
2. $\det \begin{pmatrix} 3 & 3 \\ -1 & -2 \end{pmatrix} = -6 + 3 = -3 \ne 0$ over $\mathbb{Q}$, so $v$ is also a cyclic vector.
3. Over $\mathbb{F}_3$ the same determinant is $0$, and indeed $A = \operatorname{diag}(1, 2)$ and $v = (0, -1) = (0, 2)$ there, an eigenvector.

The typical use is to find a basis in which $T$ has its companion matrix.
The trap is to test a single vector, find that it is not cyclic, and conclude that $T$ is not cyclic.
