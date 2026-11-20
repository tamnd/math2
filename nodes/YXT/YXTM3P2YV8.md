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

Let $T = \begin{pmatrix} 0 & 0 & -1 \\ -1 & 0 & 0 \\ 0 & -1 & 0 \end{pmatrix}$, so $Te_1 = -e_2$, $Te_2 = -e_3$ and $Te_3 = -e_1$.
For $u \neq 0$, let $s_u = I_3 - 2\frac{uu^T}{u^Tu}$, the [[reflection|025158VEYZ]] in the plane $u^\perp$.
We write $T$ as a product of three reflections, and we show that fewer reflections are not enough.

1. The columns $-e_2$, $-e_3$, $-e_1$ are orthonormal, so $T$ is [[orthogonal|0QRBVFJ50X]].
2. $T = -R$, where $R$ is [[the cyclic permutation matrix|E6SGA0X325]]. So $\det T = (-1)^3\det R = -1$.
3. First reflection: $u_1 = Te_1 - e_1 = -(1, 1, 0)$. By part 5 of [[the reflection theorem|FEER10D15S]], $s_{(1, 1, 0)}$ swaps $e_1$ and $-e_2$.
4. $s_{(1, 1, 0)} = \begin{pmatrix} 0 & -1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, and $S = s_{(1, 1, 0)}T = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$. So $Se_1 = e_1$.
5. Second reflection: $Se_2 = -e_3$, so $u_2 = Se_2 - e_2 = -(0, 1, 1)$. Then $s_{(0, 1, 1)} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & -1 & 0 \end{pmatrix}$.
6. $s_{(0, 1, 1)}S = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{pmatrix} = s_{(0, 0, 1)}$.
7. Each reflection is its own inverse. So $T = s_{(1, 1, 0)}s_{(0, 1, 1)}s_{(0, 0, 1)}$, a product of three reflections.
8. Check: the product sends $e_1 \mapsto e_1 \mapsto e_1 \mapsto -e_2$, as $T$ does.
9. Fewer reflections are not enough. $\det T = -1$, so the number of reflections is odd. One reflection fixes a plane pointwise.
10. $T$ fixes no vector $x \neq 0$: $Tx = x$ gives $x_1 = -x_3$, $x_2 = -x_1$ and $x_3 = -x_2$, so $x_1 = -x_1$ and $x = 0$. So $T$ is not one reflection, and it needs three.

## Remarks

- The example shows that the bound $n = 3$ of the [[Cartan-Dieudonné theorem|0VMWGYY35Q]] is reached by a matrix other than $-I_3$.
- The [[characteristic polynomial|039HF58KQ5]] of $T$ is $t^3 + 1 = (t + 1)(t^2 - t + 1)$. The eigenvalues are $-1$ and $e^{\pm i\pi/3}$.
- So the [[normal form|QTY3VMFGY1]] of $T$ is $\operatorname{diag}(R(\pi/3), -1)$. $T$ is a rotation by $\frac{\pi}{3}$ about the line through $(1, 1, 1)$, followed by the reflection in the plane orthogonal to this line.
- The decomposition is not unique. $T = s_{(1, 1, 1)}R'$, where $R'$ is the rotation by $\frac{\pi}{3}$ about the same line. Two reflections in planes through this line give $R'$, and so a second decomposition.

## Explanations

### L1 human

Three mirrors can move space in a way that no single mirror can.
This move sends each coordinate axis to the next axis, and it flips the direction.
No direction stays fixed under this move.
One mirror always keeps a whole wall fixed, so one mirror is not enough.
Two mirrors give a turn, which keeps the orientation, so two mirrors are not enough.

### L2 human

The worked computation is in the Example.
The method follows the proof of the theorem: each reflection moves one basis vector to its image, and then the problem has one dimension less.
The typical use: write an orthogonal matrix as a product of Householder matrices.
A trap: a product of three reflections has determinant $-1$, so it is never a rotation.
