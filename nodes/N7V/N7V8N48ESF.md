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

Let $F$ be any field and let $T$ be the map $v \mapsto Av$ on $F^2$, where
$$A = \operatorname{diag}(1, 2) = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}.$$
We show that $v = (1, 1)$ is a [[cyclic vector|42MMQBTP0M]] for $T$, find its annihilator, and show that $e_1$ is not a cyclic vector.

1. Apply $A$ to $v$: $Av = (1, 2)$.
2. Put $v$ and $Av$ side by side as columns; the determinant is $\det \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = 2 - 1 = 1$, which is nonzero in every field.
3. So $v, Av$ is a [[basis|0KCQ9Y3QKA]] of $F^2$, and $Z(v; T) = F^2$.
4. Apply $A$ again: $A^2 v = (1, 4)$, and $3 Av - 2v = (3 - 2, 6 - 2) = (1, 4)$, so $A^2 v - 3 Av + 2v = 0$.
5. By step 3, no polynomial of degree $1$ kills $v$, so the $T$-annihilator is $m_v = x^2 - 3x + 2 = (x - 1)(x - 2)$.
6. In the basis $v, Av$ the map sends the first vector to the second, and the second to $-2 v + 3 Av$. So its matrix is the [[companion matrix|0VH1TC1PWF]] $C(x^2 - 3x + 2) = \begin{pmatrix} 0 & -2 \\ 1 & 3 \end{pmatrix}$, as the [[lemma on cyclic subspaces|5VYBJYPYMW]] predicts.
7. For $e_1$ we get $A e_1 = e_1$, so $Z(e_1; T) = F e_1$ has dimension $1$ and $m_{e_1} = x - 1$; hence $e_1$ is not a cyclic vector.

## Remarks

The example shows that a cyclic map can have vectors that are not cyclic.
For a general vector $(a, b)$ we have $A(a, b) = (a, 2b)$, and the test determinant is
$$\det \begin{pmatrix} a & a \\ b & 2b \end{pmatrix} = 2ab - ab = ab.$$
So $(a, b)$ is cyclic exactly when $ab \ne 0$, that is, when the vector lies on neither eigenline.

If you change the entry $2$ to $1$, the matrix becomes $I_2$, and then no vector is cyclic.
In characteristic $2$ the matrix is $\operatorname{diag}(1, 0)$, and the same computation works, with $m_v = x^2 + x = x(x + 1)$.

## Explanations

### L1 human

The map keeps the first coordinate of a point and doubles the second.
Start at the point $(1, 1)$, and the map sends it to $(1, 2)$.
These two points do not lie on one line through the origin, so together they reach every point of the plane.
The point $(1, 0)$ is not moved at all, so it only reaches its own line.

### L2 human

Here is the same test for another vector, and a warning about the field.
Take $v = (3, -1)$ over $\mathbb{Q}$, so that $Av = (3, -2)$.
The test determinant is
$$\det \begin{pmatrix} 3 & 3 \\ -1 & -2 \end{pmatrix} = -6 + 3 = -3,$$
which is nonzero, so $v$ is also a cyclic vector over $\mathbb{Q}$.
Over $\mathbb{F}_3$ the same determinant is $0$, and indeed $v = (3, -1) = (0, 2)$ there, which lies on the eigenline of $e_2$.
So whether a given vector is cyclic can depend on the field, even when the matrix has integer entries.
