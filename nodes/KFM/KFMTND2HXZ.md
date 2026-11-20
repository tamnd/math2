---
tag: KFMTND2HXZ
kind: example
name: The half turn of the plane is not a Cayley transform
msc: ["15B10", "15A16"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [6WBVP2PB1Y]
not_instance_of:
  - target: HKQ5YY027B
    note: the half turn has the eigenvalue minus one, so it is not the Cayley transform of a skew-symmetric matrix
uses: [03RNVFDEAN, 0ZND7NQ970, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Matrix map
---

## Example

Let $Q = -I_2 = R(\pi)$, the half turn of the plane.
We show that $Q \in SO(2)$, but $Q \neq (I - A)(I + A)^{-1}$ for each real [[skew-symmetric|03RNVFDEAN]] $2 \times 2$ matrix $A$.

1. $Q^TQ = (-I)(-I) = I$, and $\det Q = (-1)^2 = 1$. So $Q \in SO(2)$.
2. $Qx = -x$ for each $x$, so $-1$ is an [[eigenvalue|0ZND7NQ970]] of $Q$.
3. Each skew-symmetric $2 \times 2$ matrix is $A = \begin{pmatrix} 0 & -t \\ t & 0 \end{pmatrix}$ with $t \in \R$.
4. $\det(I + A) = 1 + t^2 > 0$, so $I + A$ is [[invertible|0EB9N0S33C]], and its Cayley transform is $\frac{1}{1 + t^2}\begin{pmatrix} 1 - t^2 & 2t \\ -2t & 1 - t^2 \end{pmatrix}$.
5. The entry $(1, 1)$ is $\frac{1 - t^2}{1 + t^2} > -1$, because $1 - t^2 > -1 - t^2$. The entry $(1, 1)$ of $Q$ is $-1$.
6. So $Q$ is not a Cayley transform.
7. A second reason: $I + Q = 0$ is not invertible. So the inverse formula $(I - Q)(I + Q)^{-1}$ is not defined at $Q$.

## Remarks

- The example shows that the Cayley transform misses part of $SO(n)$, so the inverse formula is not a chart of all of $SO(n)$.
- As $t \to \infty$, the transform tends to $-I_2$. So the half turn is a limit of Cayley transforms, but not one of them.
- In $\R^3$, the half turns $\operatorname{diag}(-1, -1, 1)$, and all rotations by $\pi$, are missed in the same way.
- The half turn is $C(A)^2$ for $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, because $C(A) = R(-\frac{\pi}{2})$. So it is a product of two Cayley transforms.

## Explanations

### L1 human

The half turn sends each arrow in the plane to the opposite arrow.
The Cayley recipe can make every turn of the plane except this one.
It can come as close to the half turn as we want, but it never reaches it.

### L2 human

The worked check is in the Example.
The typical use: before inverting the Cayley transform, check that $-1$ is not an eigenvalue, or that $\det(I + Q) \neq 0$.
A trap: the half turn has determinant $1$, so the test $\det Q = 1$ is not enough.
