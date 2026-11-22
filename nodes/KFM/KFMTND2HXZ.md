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
We show that $Q \in SO(2)$, but $Q \neq (I - A)(I + A)^{-1}$ for every real [[skew-symmetric|03RNVFDEAN]] $2 \times 2$ matrix $A$.

1. We have $Q^{\mathsf{T}}Q = (-I)(-I) = I$ and $\det Q = (-1)^2 = 1$, so $Q \in SO(2)$.
2. Since $Qx = -x$ for every $x$, the number $-1$ is an [[eigenvalue|0ZND7NQ970]] of $Q$.
3. Every skew-symmetric $2 \times 2$ matrix is $A = \begin{pmatrix} 0 & -t \\ t & 0 \end{pmatrix}$ with $t \in \R$.
4. Then $\det(I + A) = 1 + t^2 > 0$, so $I + A$ is [[invertible|0EB9N0S33C]], and its Cayley transform is $\frac{1}{1 + t^2}\begin{pmatrix} 1 - t^2 & 2t \\ -2t & 1 - t^2 \end{pmatrix}$.
5. The entry $(1, 1)$ of this matrix is $\frac{1 - t^2}{1 + t^2} > -1$, because $1 - t^2 > -1 - t^2$. The entry $(1, 1)$ of $Q$ is $-1$.
6. So $Q$ is not a Cayley transform.
7. A second reason: $I + Q = 0$ is not invertible, so the inverse formula $(I - Q)(I + Q)^{-1}$ is not defined at $Q$.

## Remarks

The half turn is a limit of Cayley transforms but not one of them.
As $t \to \infty$, the matrix of step 4 tends to $-I_2$, because $\frac{1 - t^2}{1 + t^2} \to -1$ and $\frac{2t}{1 + t^2} \to 0$.
So the image of the Cayley transform is not closed in $SO(2)$, and the inverse formula is a chart of $SO(n)$ near $I$, not of all of $SO(n)$.

The same thing happens in every dimension.
In $\R^3$ the half turn $\operatorname{diag}(-1, -1, 1)$, and every other rotation by $\pi$, has the eigenvalue $-1$ and is missed.
Still, the half turn is a product of two Cayley transforms.
For $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ we have $C(A) = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = R(-\frac{\pi}{2})$, and $C(A)^2 = R(-\pi) = -I_2$.
Check: $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$.

## Explanations

### L1 human

The half turn sends each arrow in the plane to the opposite arrow.
The Cayley recipe can make every turn of the plane except this one.
It can come as close to the half turn as we want, but it never reaches it.

### L2 human

The worked check is in the Example above.
A typical use is the test before inverting the Cayley transform: check that $\det(I + Q) \neq 0$, which says that $-1$ is not an eigenvalue.
Watch out: the half turn has determinant $1$, so the test $\det Q = 1$ is not enough.
For the rotation $\frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$ the test gives $\det(I + Q) = \frac{16}{5}$, while for $-I_2$ it gives $0$.
