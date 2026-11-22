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

Let $A = \begin{pmatrix} 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 \end{pmatrix}$, the [[skew-symmetric matrix|03RNVFDEAN]] $\begin{pmatrix} 0 & -t \\ t & 0 \end{pmatrix}$ with $t = \frac{1}{2}$.
We compute its [[Cayley transform|HKQ5YY027B]] $Q = (I - A)(I + A)^{-1}$, and we check that $Q \in SO(2)$.

1. We have $I + A = \begin{pmatrix} 1 & -\frac{1}{2} \\ \frac{1}{2} & 1 \end{pmatrix}$, with determinant $1 + \frac{1}{4} = \frac{5}{4}$. So $I + A$ is [[invertible|0EB9N0S33C]].
2. By the formula for the inverse of a $2 \times 2$ matrix, $(I + A)^{-1} = \frac{4}{5}\begin{pmatrix} 1 & \frac{1}{2} \\ -\frac{1}{2} & 1 \end{pmatrix}$.
3. We have $I - A = \begin{pmatrix} 1 & \frac{1}{2} \\ -\frac{1}{2} & 1 \end{pmatrix}$, the same matrix as in step 2 without the factor $\frac{4}{5}$.
4. Multiplying out,
$$(I - A)(I + A)^{-1} = \frac{4}{5}\begin{pmatrix} 1 - \frac{1}{4} & \frac{1}{2} + \frac{1}{2} \\ -\frac{1}{2} - \frac{1}{2} & -\frac{1}{4} + 1 \end{pmatrix} = \frac{4}{5}\begin{pmatrix} \frac{3}{4} & 1 \\ -1 & \frac{3}{4} \end{pmatrix}.$$
5. So $Q = \frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$.
6. We have $Q^{\mathsf{T}}Q = \frac{1}{25}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix} = \frac{1}{25}\begin{pmatrix} 25 & 0 \\ 0 & 25 \end{pmatrix} = I$, so $Q$ is [[orthogonal|0QRBVFJ50X]].
7. Also $\det Q = \frac{9 + 16}{25} = 1$, so $Q \in SO(2)$.
8. Finally $Q = R(-\theta)$ with $\cos\theta = \frac{3}{5}$ and $\sin\theta = \frac{4}{5}$. Then $\tan\frac{\theta}{2} = \frac{\sin\theta}{1 + \cos\theta} = \frac{4/5}{8/5} = \frac{1}{2}$, which is $t$.

## Remarks

The example is one point of the rational parametrization of the circle.
The first column of $Q$ is the point $(\frac{3}{5}, -\frac{4}{5})$ of the unit circle, and the numbers $3$, $4$, $5$ form a [[Pythagorean triple|0M7ARED5Q7]].
For any rational $t = \frac{a}{b}$ the same computation gives the first column $\frac{1}{a^2 + b^2}(b^2 - a^2, -2ab)$, and so the triple $b^2 - a^2$, $2ab$, $a^2 + b^2$.
For $t = \frac{2}{3}$ this is the triple $5$, $12$, $13$.

The formula also runs backward.
We have $I + Q = \frac{1}{5}\begin{pmatrix} 8 & 4 \\ -4 & 8 \end{pmatrix}$ and $I - Q = \frac{1}{5}\begin{pmatrix} 2 & -4 \\ 4 & 2 \end{pmatrix}$, and $(I - Q)(I + Q)^{-1} = A$.
Check: $(I + Q)^{-1} = \frac{1}{16}\begin{pmatrix} 8 & -4 \\ 4 & 8 \end{pmatrix}$, and the entry $(1, 2)$ of the product is $\frac{1}{80}(-8 - 32) = -\frac{1}{2}$.
Replacing $t$ by $-t$ replaces $A$ by $A^{\mathsf{T}}$ and $Q$ by $Q^{\mathsf{T}} = Q^{-1}$, the rotation by the opposite angle.

## Explanations

### L1 human

We start from a small table with the numbers $\frac{1}{2}$ and $-\frac{1}{2}$, and the recipe turns it into a turn of the plane.
The turn has the numbers $\frac{3}{5}$ and $\frac{4}{5}$ in it.
These come from the right triangle with sides $3$, $4$ and $5$.

### L2 human

The worked computation is in the Example above.
A typical use is to get a rotation with rational entries: choose a rational $t$ and compute $C(A)$.
Watch out: the matrix $I + A$ must be inverted, not $I - A$.
The other choice gives $(I + A)(I - A)^{-1} = \frac{1}{5}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$, which is $Q^{\mathsf{T}}$ instead of $Q$.
