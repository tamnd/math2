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

Let $Q = -I_3 = \operatorname{diag}(-1, -1, -1)$, the map $x \mapsto -x$ of $\R^3$.
We check that $Q$ is in the [[orthogonal group|WWK2E8BRGF]] $O(3)$, but not in the [[special orthogonal group|6WBVP2PB1Y]] $SO(3)$.

1. $Q^T = Q$ and $Q^TQ = (-1)^2 I_3 = I_3$. So $Q$ is orthogonal.
2. The [[determinant|0C3CFHDN6R]] of a diagonal matrix is the product of its diagonal entries. So $\det Q = (-1)^3 = -1$.
3. So $Q \notin SO(3)$, and $x \mapsto -x$ is not a rotation of space.
4. Write $Q = \operatorname{diag}(-1, -1, 1) \cdot \operatorname{diag}(1, 1, -1)$.
5. The first factor has determinant $1$. It is the rotation by $\pi$ about the $z$-axis.
6. The second factor is the reflection in the $xy$-plane. So $Q$ is a half turn followed by a reflection.

## Remarks

- The determinant of $-I_n$ is $(-1)^n$. So $-I_n \in SO(n)$ exactly when $n$ is even.
- For $n = 2$, $-I_2 = R(\pi)$ is the half turn of the plane, a rotation.
- In physics, $-I_3$ is the parity transformation. It changes a right-handed frame into a left-handed frame.
- $-I_3$ commutes with every matrix, and $O(3) = SO(3) \times \set{I_3, -I_3}$.

## Explanations

### L1 human

The map $x \mapsto -x$ sends each point of space to the opposite point through the origin.
It keeps all distances, so it is in the orthogonal group.
But it turns a right hand into a left hand.
A rotation never does this, so the map is not a rotation.

### L2 human

The worked check is in the Example.
The typical use: to test whether an orthogonal matrix is a rotation, compute its determinant.
A trap: the same map in the plane, $x \mapsto -x$, is a rotation by $\pi$.
The answer depends on whether the dimension is even or odd.
