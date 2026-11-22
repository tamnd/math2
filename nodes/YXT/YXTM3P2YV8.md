---
tag: YXTM3P2YV8
kind: example
name: A product of three reflections in the orthogonal group of space
msc: ["15B10", "51F15"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [WWK2E8BRGF]
illustrates: [0VMWGYY35Q, FEER10D15S]
uses: [025158VEYZ, 0QRBVFJ50X, 039HF58KQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan–Dieudonné_theorem
    locator: Formal statement
  - url: https://en.wikipedia.org/wiki/Householder_transformation
    locator: Properties
---

## Example

Let
$$T = \begin{pmatrix} 0 & 0 & -1 \\ -1 & 0 & 0 \\ 0 & -1 & 0 \end{pmatrix},$$
so that $T e_1 = -e_2$, $T e_2 = -e_3$ and $T e_3 = -e_1$.
For $u \ne 0$ let $s_u = I_3 - 2 \frac{u u^{\mathsf{T}}}{u^{\mathsf{T}} u}$ be the [[reflection|025158VEYZ]] in the plane $u^\perp$.
We write $T$ as a product of three reflections, following the proof of [[the theorem on reflections|FEER10D15S]], and we show that fewer are not enough.

1. The columns $-e_2$, $-e_3$ and $-e_1$ are orthonormal, so $T$ is [[orthogonal|0QRBVFJ50X]].
2. We have $T = -P$, where $P$ is [[the cyclic permutation matrix|E6SGA0X325]] with determinant $1$, so $\det T = (-1)^3 \det P = -1$.
3. The first reflection must send $e_1$ to $T e_1 = -e_2$, so we take $u_1 = e_1 - T e_1 = (1, 1, 0)$, with $u_1^{\mathsf{T}} u_1 = 2$:
$$s_{u_1} = I_3 - u_1 u_1^{\mathsf{T}} = \begin{pmatrix} 0 & -1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}.$$
4. Multiply to remove the first step:
$$S = s_{u_1} T = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}, \qquad S e_1 = e_1.$$
5. Now $S e_2 = -e_3$, so we take $u_2 = e_2 - S e_2 = (0, 1, 1)$:
$$s_{u_2} = I_3 - u_2 u_2^{\mathsf{T}} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & -1 & 0 \end{pmatrix}, \qquad s_{u_2} S = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{pmatrix} = s_{e_3}.$$
6. So $s_{u_2} s_{u_1} T = s_{e_3}$, and each reflection is its own inverse, so
$$T = s_{u_1} s_{u_2} s_{e_3}.$$
7. Check on $e_1$: $s_{e_3} e_1 = e_1$, then $s_{u_2} e_1 = e_1$, then $s_{u_1} e_1 = -e_2$, which is $T e_1$.
8. Two reflections are not enough, because a product of two reflections has determinant $1$ and $\det T = -1$.
9. One reflection is not enough, because a reflection of $\R^3$ fixes a whole plane.
But $T x = x$ means $(-x_3, -x_1, -x_2) = (x_1, x_2, x_3)$, which gives $x_1 = -x_3 = x_2 = -x_1$, so $x_1 = 0$ and then $x = 0$.

## Remarks

The example reaches the bound $n = 3$ of the [[Cartan-Dieudonné theorem|0VMWGYY35Q]] with a matrix other than $-I_3$.
Its [[characteristic polynomial|039HF58KQ5]] is
$$\det(tI_3 - T) = t^3 + 1 = (t + 1)(t^2 - t + 1),$$
so the eigenvalues are $-1$ and $e^{\pm i\pi/3}$.
Check: $t^2 - t + 1$ has roots $\frac{1 \pm i\sqrt{3}}{2} = e^{\pm i\pi/3}$.

So the [[normal form|QTY3VMFGY1]] of $T$ is a block $R(\pi/3)$ and an entry $-1$.
Geometrically, $T$ turns space by $\frac{\pi}{3}$ about the line through $(1, 1, 1)$ and then reflects in the plane perpendicular to that line.
This gives a second factorization: the turn is a product of two reflections in planes that contain the line, and the last factor is $s_{(1, 1, 1)}$.
So the three reflections are not unique.

## Explanations

### L1 human

Three mirrors can move space in a way that no single mirror can.
This move sends each coordinate axis to the next one and flips its direction.
No direction stays where it was.
One mirror always keeps a whole wall fixed, so one mirror cannot do it.
Two mirrors always give a turn, which keeps right hands right, so two mirrors cannot do it either.

### L2 human

The method is the proof of the theorem in action.
Each reflection sends one basis vector to the place where $T$ sends it, and then the remaining problem lives in one dimension less.
Here the first reflection fixed $e_1$, the second fixed $e_2$, and what was left was already a reflection.
The same steps write any orthogonal matrix as a product of Householder matrices, the reflections that the Householder QR method uses.
Watch out: a product of three reflections has determinant $-1$, so it is never a rotation.
