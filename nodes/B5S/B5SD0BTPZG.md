---
tag: B5SD0BTPZG
kind: example
name: A matrix with orthogonal columns that is not orthogonal
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: ug1
not_instance_of:
  - target: 0W02QESPJQ
    note: the columns are orthogonal but have length the square root of 2, so the product of the transpose with the matrix is 2I
uses: [0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: lead section
---

## Example

Let
$$A = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}.$$
We test the condition $A^TA = I$ of an [[orthogonal matrix|0QRBVFJ50X]] and find that it fails.

1. The columns are $a_1 = (1, -1)$ and $a_2 = (1, 1)$.
2. Their dot product is $1 \cdot 1 + (-1) \cdot 1 = 0$, so the columns are orthogonal.
3. Their squared lengths are $1 + 1 = 2$, so they are not unit vectors.
4. So $A^TA = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2I \ne I$, and $A$ is not orthogonal.
5. The determinant gives a second sign: $\det A = 1 \cdot 1 - 1 \cdot (-1) = 2$, which is not $\pm 1$.

## Remarks

The example is the main trap of the topic.
The name "orthogonal matrix" sounds as if orthogonal columns were enough, but the definition asks for orthonormal columns.
For this $A$, the inverse is $\frac{1}{2}A^T$ and not $A^T$.

Fix the lengths and the trap disappears.
Dividing each column by its length $\sqrt 2$ gives $\frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$, which is orthogonal: it is the rotation $R(-\pi/4)$, with $\cos(-\pi/4) = \frac{1}{\sqrt 2}$ and $\sin(-\pi/4) = -\frac{1}{\sqrt 2}$.
So $x \mapsto Ax$ is the rotation by $-\pi/4$ followed by scaling by $\sqrt{2}$.
It keeps angles, but it multiplies every length by $\sqrt{2}$.

## Explanations

### L1 human

The two columns of this matrix are arrows that meet at a right angle.
But each arrow has length about $1.41$, not $1$.
So the matrix stretches the plane, and it is not orthogonal.

### L2 human

One vector is enough to rule $A$ out.
Take $x = (1, 0)$, of length $1$.
Then $Ax = (1, -1)$, and its length is
$$\sqrt{1^2 + (-1)^2} = \sqrt 2 \ne 1.$$
A length changed, so $A$ is not orthogonal.
Watch out: a test of the dot products of the columns alone would pass, so always test the lengths too.
