---
tag: QFJZBPVV00
kind: example
name: The Cayley transform of a two by two skew-symmetric matrix
msc: ["15B10", "15A16"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [6WBVP2PB1Y]
illustrates: [HKQ5YY027B, R9Z3W1CFPP]
uses: [03RNVFDEAN, 0EB9N0S33C, 0QRBVFJ50X, 0M7ARED5Q7]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Matrix map
---

## Example

Let $A = \begin{pmatrix} 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 \end{pmatrix}$, a [[skew-symmetric matrix|03RNVFDEAN]].
We compute its [[Cayley transform|HKQ5YY027B]] $Q = (I - A)(I + A)^{-1}$, and we check that $Q \in SO(2)$.

1. $I + A = \begin{pmatrix} 1 & -\frac{1}{2} \\ \frac{1}{2} & 1 \end{pmatrix}$, with determinant $1 + \frac{1}{4} = \frac{5}{4}$. So $I + A$ is [[invertible|0EB9N0S33C]].
2. By the formula for the inverse of a $2 \times 2$ matrix, $(I + A)^{-1} = \frac{4}{5}\begin{pmatrix} 1 & \frac{1}{2} \\ -\frac{1}{2} & 1 \end{pmatrix}$.
3. $I - A = \begin{pmatrix} 1 & \frac{1}{2} \\ -\frac{1}{2} & 1 \end{pmatrix}$.
4. $(I - A)(I + A)^{-1} = \frac{4}{5}\begin{pmatrix} 1 - \frac{1}{4} & \frac{1}{2} + \frac{1}{2} \\ -\frac{1}{2} - \frac{1}{2} & -\frac{1}{4} + 1 \end{pmatrix} = \frac{4}{5}\begin{pmatrix} \frac{3}{4} & 1 \\ -1 & \frac{3}{4} \end{pmatrix}$.
5. So $Q = \frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$.
6. $Q^TQ = \frac{1}{25}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix} = \frac{1}{25}\begin{pmatrix} 25 & 0 \\ 0 & 25 \end{pmatrix} = I$. So $Q$ is [[orthogonal|0QRBVFJ50X]].
7. $\det Q = \frac{9 + 16}{25} = 1$. So $Q \in SO(2)$.
8. $Q = R(-\theta)$ with $\cos\theta = \frac{3}{5}$ and $\sin\theta = \frac{4}{5}$. Then $\tan\frac{\theta}{2} = \frac{\sin\theta}{1 + \cos\theta} = \frac{4/5}{8/5} = \frac{1}{2}$, the entry $t$ of $A$.

## Remarks

- The example shows the rational parametrization of the circle: the entry $t = \frac{1}{2}$ gives the point $(\frac{3}{5}, -\frac{4}{5})$.
- The numbers $3$, $4$, $5$ form a [[Pythagorean triple|0M7ARED5Q7]]. Each rational $t$ gives the triple $1 - t^2$, $2t$, $1 + t^2$ after clearing denominators.
- Applying the formula to $Q$ gives $A$ back: $I + Q = \frac{1}{5}\begin{pmatrix} 8 & 4 \\ -4 & 8 \end{pmatrix}$, $I - Q = \frac{1}{5}\begin{pmatrix} 2 & -4 \\ 4 & 2 \end{pmatrix}$, and $(I - Q)(I + Q)^{-1} = A$.
- With $t$ replaced by $-t$, the transform gives $Q^T = Q^{-1}$.

## Explanations

### L1 human

We start from a simple table with $\frac{1}{2}$ and $-\frac{1}{2}$, and the recipe gives a turn of the plane.
The turn has the numbers $\frac{3}{5}$ and $\frac{4}{5}$ in it.
These come from the right triangle with sides $3$, $4$ and $5$.

### L2 human

The worked computation is in the Example.
The typical use: to get a rotation with rational entries, choose a rational $t$.
A trap: the matrix $I + A$ must be inverted, not $I - A$, or the result is $Q^T$ instead of $Q$.
