---
tag: TEZ3YS5VTB
kind: example
name: The Cayley transform of a three by three skew-symmetric matrix
msc: ["15B10", "15A16"]
topics: [AZS5BPF5H3]
audience: grad
instance_of: [6WBVP2PB1Y]
illustrates: [HKQ5YY027B, R9Z3W1CFPP]
uses: [03RNVFDEAN, 0EB9N0S33C, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Matrix map
---

## Example

Let $A = \frac{1}{3}\begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix}$, a [[skew-symmetric matrix|03RNVFDEAN]] built from the three free numbers $\frac{1}{3}$, $-\frac{1}{3}$ and $\frac{1}{3}$ above the diagonal.
We compute its [[Cayley transform|HKQ5YY027B]] $Q = (I - A)(I + A)^{-1}$ and check that $Q \in SO(3)$.

1. We have $I + A = \frac{1}{3}\begin{pmatrix} 3 & 1 & -1 \\ -1 & 3 & 1 \\ 1 & -1 & 3 \end{pmatrix}$.
2. The integer matrix has [[determinant|0C3CFHDN6R]] $3(9 + 1) - 1(-3 - 1) - 1(1 - 3) = 30 + 4 + 2 = 36$. So $\det(I + A) = \frac{36}{27} = \frac{4}{3}$, and $I + A$ is [[invertible|0EB9N0S33C]].
3. The adjugate of the integer matrix is $\begin{pmatrix} 10 & -2 & 4 \\ 4 & 10 & -2 \\ -2 & 4 & 10 \end{pmatrix}$. So $(I + A)^{-1} = 3 \cdot \frac{1}{36}\begin{pmatrix} 10 & -2 & 4 \\ 4 & 10 & -2 \\ -2 & 4 & 10 \end{pmatrix} = \frac{1}{6}\begin{pmatrix} 5 & -1 & 2 \\ 2 & 5 & -1 \\ -1 & 2 & 5 \end{pmatrix}$.
4. We have $I - A = \frac{1}{3}\begin{pmatrix} 3 & -1 & 1 \\ 1 & 3 & -1 \\ -1 & 1 & 3 \end{pmatrix}$.
5. The first row of $(I - A)(I + A)^{-1}$ is $\frac{1}{18}(15 - 2 - 1, \ -3 - 5 + 2, \ 6 + 1 + 5) = \frac{1}{18}(12, -6, 12)$. The second row is $\frac{1}{18}(5 + 6 + 1, \ -1 + 15 - 2, \ 2 - 3 - 5) = \frac{1}{18}(12, 12, -6)$, and the third is $\frac{1}{18}(-5 + 2 - 3, \ 1 + 5 + 6, \ -2 - 1 + 15) = \frac{1}{18}(-6, 12, 12)$.
6. So
$$Q = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}.$$
7. Each column of $3Q$ has squared length $4 + 4 + 1 = 9$, and the dot products of the columns are $-2 + 4 - 2 = 0$, $4 - 2 - 2 = 0$ and $-2 - 2 + 4 = 0$. So $Q^{\mathsf{T}}Q = I$.
8. The determinant of $3Q$ is $2(4 + 2) + 1(4 - 1) + 2(4 + 2) = 12 + 3 + 12 = 27$, so $\det Q = 1$ and $Q \in SO(3)$.

## Remarks

Write $A = -[w]_\times$, where $[w]_\times x = w \times x$ and $w = \frac{1}{3}(1, 1, 1)$.
The axis of $Q$ is the line through $w$: each row of $3Q$ has sum $3$, so $Q(1, 1, 1) = (1, 1, 1)$.
The angle $\theta$ satisfies $\tan\frac{\theta}{2} = \norm{w} = \frac{1}{\sqrt{3}}$, so $\theta = \frac{\pi}{3}$.
Check: $\tr Q = \frac{6}{3} = 2 = 1 + 2\cos\frac{\pi}{3}$, as the trace rule for rotations requires.
So $Q$ is the [[rotation by sixty degrees|TFWTJ9K6K7]] about the line through $(1, 1, 1)$.

The [[Cayley transform theorem|R9Z3W1CFPP]] gives $A = (I - Q)(I + Q)^{-1}$, so $A$ can be recovered from $Q$.
Here $I + Q = 2(I + A)^{-1}$, which is the matrix of step 3 times $2$.
Replacing $w$ by $sw$ for $s > 0$ keeps the axis and changes the angle to the $\theta$ with $\tan\frac{\theta}{2} = \frac{s}{\sqrt{3}}$, so every angle in $(0, \pi)$ about this axis appears, but the half turn does not.

## Explanations

### L1 human

Three free numbers, here all of size $\frac{1}{3}$, go into a skew-symmetric table.
The recipe turns the table into a turn of space.
The turn has its axis along the direction $(1, 1, 1)$ that the three numbers point in.
The size of the numbers fixes the angle of the turn, here a sixth of a full turn.

### L2 human

The worked computation is in the Example above.
A typical use is to build a rotation of space with a given axis $w$ and rational entries: put $A = -[w]_\times$ and compute $C(A)$.
Watch out: the angle is not $\norm{w}$, but the angle $\theta$ with $\tan\frac{\theta}{2} = \norm{w}$.
Here $\norm{w} = \frac{1}{\sqrt{3}} \approx 0.58$, while $\theta = \frac{\pi}{3} \approx 1.05$.
