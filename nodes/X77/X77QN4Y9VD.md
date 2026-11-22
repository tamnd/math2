---
tag: X77QN4Y9VD
kind: example
name: The point reflection of space is not a rotation
msc: ["15B10", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
not_instance_of:
  - target: 6WBVP2PB1Y
    note: the matrix minus the identity of size 3 is orthogonal with determinant minus one
instance_of: [WWK2E8BRGF]
uses: [GPWRS6HSNR, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: Special orthogonal group
---

## Example

Let $Q = -I_3 = \operatorname{diag}(-1, -1, -1)$, the map $x \mapsto -x$ of $\R^3$ that sends each point to the opposite point through the origin.
We show that $Q$ is in the [[orthogonal group|WWK2E8BRGF]] $O(3)$ but not in the [[special orthogonal group|6WBVP2PB1Y]] $SO(3)$.

1. The matrix is symmetric, so $Q^{\mathsf{T}} Q = Q^2 = (-1)^2 I_3 = I_3$, and $Q$ is orthogonal.
2. The [[determinant|0C3CFHDN6R]] of a diagonal matrix is the product of its diagonal entries, so $\det Q = (-1)^3 = -1$.
3. A rotation has determinant $1$, so $Q \notin SO(3)$.
4. We can split $Q$ into two familiar pieces:
$$\operatorname{diag}(-1, -1, -1) = \operatorname{diag}(-1, -1, 1) \cdot \operatorname{diag}(1, 1, -1).$$
5. The first factor has determinant $1$, and it is the half turn about the $z$-axis.
6. The second factor is the reflection in the $xy$-plane, with determinant $-1$.
7. So $Q$ is a half turn followed by a reflection in the plane perpendicular to the axis of the turn.

## Remarks

The answer depends on the dimension, because $\det(-I_n) = (-1)^n$.
So $-I_n$ is a rotation exactly when $n$ is even, and for $n = 2$ it is the half turn $R(\pi)$ of the plane.
In physics, $-I_3$ is the parity transformation, and it changes a right-handed frame into a left-handed frame.

The matrix $-I_3$ commutes with every $3 \times 3$ matrix, and its determinant is $-1$.
So every element of $O(3)$ is either a rotation $R$ or a product $-R$, and $O(3)$ is the direct product of $SO(3)$ and $\{ I_3, -I_3 \}$.
In even dimension this splitting fails, because $-I_n$ then lies inside $SO(n)$.

## Explanations

### L1 human

The map $x \mapsto -x$ sends each point of space to the point on the opposite side of the origin at the same distance.
It keeps all distances, so it is in the orthogonal group.
But it turns a right glove into a left glove.
A rotation never does that, so the map is not a rotation.

### L2 human

The typical test of whether an orthogonal matrix is a rotation is its determinant, and here it is one line: $(-1)^3 = -1$.
The factorization in step 4 says more, since it names the move as a half turn and a mirror.
Watch out: the same formula $x \mapsto -x$ in the plane is a rotation, because there
$$\det \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = 1 \quad \text{and} \quad -I_2 = R(\pi).$$
So "turn every vector around" is a rotation or not, depending on whether the dimension is even or odd.
