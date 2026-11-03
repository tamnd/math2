---
tag: ZGSAEYV8FX
kind: example
name: Symplectic Lie algebra
msc: [17B20, "22E60"]
instance_of: [5JJYBJ6A8K]
uses: [G8FEGYDSNE, 09DXWYRD43, X12FS2JAP0]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_group
---

## Example

Let $k$ be a field and $n \ge 1$.
Let $J$ be the $2n \times 2n$ matrix
$$J = \begin{pmatrix} 0 & I_n \\ -I_n & 0 \end{pmatrix},$$
where $I_n$ is the $n \times n$ identity matrix.
The *symplectic Lie algebra* is
$$\mathfrak{sp}_{2n}(k) = \set{X \in \mathfrak{gl}_{2n}(k) : X^T J + J X = 0},$$
where $X^T$ is the [[transpose|09DXWYRD43]], with the bracket $[X, Y] = XY - YX$ of the [[general linear Lie algebra|G8FEGYDSNE]].

Check that it is closed under brackets: if $X^T J = -JX$ and $Y^T J = -JY$, then
$$[X, Y]^T J = Y^T X^T J - X^T Y^T J = Y^T(-JX) - X^T(-JY) = JYX - JXY = -J[X, Y].$$

Write $X = \begin{pmatrix} A & B \\ C & D \end{pmatrix}$ with $n \times n$ blocks.
The condition says $D = -A^T$, $B = B^T$ and $C = C^T$.
So $\dim \mathfrak{sp}_{2n}(k) = n^2 + n(n+1) = n(2n+1)$.

## Remarks

For $n = 1$ the condition reduces to $\tr X = 0$, so $\mathfrak{sp}_2(k) = \mathfrak{sl}_2(k)$.
For $k = \R$ or $\C$, $\mathfrak{sp}_{2n}(k)$ is the Lie algebra of the [[symplectic group|X12FS2JAP0]] $Sp_{2n}(k)$, the group of matrices $A$ with $A^T J A = J$.
Over $\C$ it is the simple Lie algebra of type $C_n$.
Some authors write $\mathfrak{sp}_n$ instead of $\mathfrak{sp}_{2n}$.

## Explanations

### L1 human

The symplectic group preserves the area form $\omega(u, v) = u^T J v$, which pairs positions with momenta in mechanics.
Its Lie algebra consists of the infinitesimal linear maps that preserve this form.
In block form these are matrices whose off-diagonal blocks are symmetric and whose diagonal blocks are $A$ and $-A^T$.
They correspond to linear Hamiltonian systems, whose flows preserve phase space area.
