---
tag: PAJVDWFC9Q
kind: example
name: Spectral decomposition of I + J with a repeated eigenvalue
msc: ["15A18", "15B57"]
topics: [3YM9EK6VMB]
audience: ug1
instance_of: [0NEGN5CRSC]
illustrates: [D5KVBA1K9R, 06J4PXRG22]
uses: [0N28QN4CYA, 0Q8HZTJC7G, 0AYEPBQMAW]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theorem
    locator: Hermitian maps and Hermitian matrices
  - book: isbn:9780134860244
    locator: Section 6.6
---

## Example

Let $J$ be the $3 \times 3$ matrix with every entry $1$, and let
$$A = I + J = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$$
act on $\mathbb{R}^3$ with the dot product.
The matrix is [[symmetric|0N28QN4CYA]], and one of its eigenvalues is repeated.
We write $A$ as a sum of eigenvalues times orthogonal projections.

1. The line. $J (1, 1, 1) = (3, 3, 3)$, so $A (1, 1, 1) = (1, 1, 1) + (3, 3, 3) = 4 \cdot (1, 1, 1)$. Let $L$ be the line spanned by $(1, 1, 1)$.
2. The plane. If $x_1 + x_2 + x_3 = 0$, then every entry of $Jx$ is $x_1 + x_2 + x_3 = 0$, so $Ax = x$. So the plane $H$ given by $x_1 + x_2 + x_3 = 0$ lies in the [[eigenspace|0AYEPBQMAW]] of $1$.
3. The eigenvalues. The line and the plane together span $\mathbb{R}^3$, so the eigenvalues are $4$ and $1$, the eigenspace of $4$ is $L$, and the eigenspace of $1$ is $H$, of dimension $2$. Check: $4 + 1 + 1 = 6$ is the trace $2 + 2 + 2$.
4. The projection onto the line. The [[orthogonal projection|0Q8HZTJC7G]] onto $L$ is
$$P_L x = \frac{x \cdot (1, 1, 1)}{3} (1, 1, 1) = \frac{x_1 + x_2 + x_3}{3} (1, 1, 1), \qquad \text{so} \qquad P_L = \frac{1}{3} J.$$
5. The projection onto the plane. The plane $H$ is the orthogonal complement of $L$, so $P_H = I - P_L = I - \tfrac{1}{3} J$.
6. The resolution of the identity. From $J^2 = 3J$ we get $P_L^2 = \tfrac{1}{9} \cdot 3J = P_L$ and $P_L P_H = \tfrac{1}{3} J - \tfrac{1}{9} \cdot 3J = 0$, and $P_L + P_H = I$ by step 5.
7. The decomposition. Now
$$4 P_L + 1 \cdot P_H = \frac{4}{3} J + I - \frac{1}{3} J = I + J = A.$$

## Remarks

The example shows the spectral decomposition when an eigenvalue is repeated.
The sum in the [[spectral decomposition|D5KVBA1K9R]] runs over the two distinct eigenvalues $4$ and $1$, not over three eigenvectors.
The eigenvalue $1$ gets one projection $P_H$ of rank $2$, and $P_H$ does not depend on a choice of basis in $H$.
For example, with the orthonormal basis $u = \tfrac{1}{\sqrt{2}}(1, -1, 0)$ and $u' = \tfrac{1}{\sqrt{6}}(1, 1, -2)$ of $H$, the sum $u u^{\mathsf{T}} + u' u'^{\mathsf{T}}$ has the diagonal entries $\tfrac{1}{2} + \tfrac{1}{6} = \tfrac{2}{3}$, as $I - \tfrac{1}{3} J$ does.

The product formula for the projections gives the same answer without any eigenvectors:
$$P_L = \frac{A - 1 \cdot I}{4 - 1} = \frac{1}{3} J, \qquad P_H = \frac{A - 4I}{1 - 4} = \frac{3I - J}{3} = I - \frac{1}{3} J.$$

Functions of $A$ act on the two eigenvalues.
The inverse is $A^{-1} = \tfrac{1}{4} P_L + P_H = I - \tfrac{1}{4} J$.
Check: $(I + J)(I - \tfrac{1}{4} J) = I + J - \tfrac{1}{4} J - \tfrac{1}{4} \cdot 3J = I$.
The positive square root is $\sqrt{A} = 2 P_L + P_H = I + \tfrac{1}{3} J$.
Check: $(I + \tfrac{1}{3} J)^2 = I + \tfrac{2}{3} J + \tfrac{1}{9} \cdot 3J = I + J$.
The same method works for $I + cJ$ with any real $c$: the eigenvalues are $1 + 3c$ and $1$, and the projections stay the same.

## Explanations

### L1 human

This matrix stretches the diagonal direction $(1, 1, 1)$ by a factor of $4$.
It leaves every vector in the perpendicular plane where it is.
So the matrix acts as $4$ times the shadow on the line plus $1$ times the shadow on the plane.

### L2 human

To find a spectral decomposition, first find the distinct eigenvalues and their eigenspaces.
Then find the orthogonal projection onto each eigenspace; here the plane is the complement of the line, so $P_H = I - P_L$ needs no new work.
Write $A = \sum_i \lambda_i P_i$, and compute a function of $A$ as $\sum_i f(\lambda_i) P_i$, as we did for $A^{-1}$ and $\sqrt{A}$.
Watch out: the eigenvectors $(1, -1, 0)$ and $(1, 0, -1)$ both lie in $H$, but their dot product is $1$, so they are not an orthonormal basis of $H$.
If you build $P_H$ from eigenvectors, apply the Gram-Schmidt process to them first.
