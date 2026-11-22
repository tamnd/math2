---
tag: S3ZGYKVBRR
kind: example
name: Eigenvalues of a shear are not its singular values
msc: [15A18]
topics: [SS4EVPKT3A]
audience: ug1
not_instance_of:
  - target: 09VMDSRXWJ
    note: the eigenvalue 1 of the shear is not one of its singular values, which are the golden ratio and its inverse
illustrates: [0K2TX12X58]
uses: [0K2TX12X58, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value
    locator: Basic properties
---

## Example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the shear that slides each point sideways by its height.
We compute its eigenvalues and its singular values and see that they differ.

1. The matrix $A$ is upper triangular with diagonal entries $1$ and $1$, so its only [[eigenvalue|0ZND7NQ970]] is $1$, with algebraic multiplicity $2$.
2. Multiply $A$ by its transpose on the left:
$$A^{\mathsf{T}} A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}.$$
3. This matrix has trace $3$ and determinant $2 - 1 = 1$, so its eigenvalues are the roots of $t^2 - 3t + 1$, namely $\tfrac{3 \pm \sqrt5}{2}$.
4. Square the candidates $\tfrac{\sqrt5 \pm 1}{2}$:
$$\left(\frac{\sqrt5 \pm 1}{2}\right)^2 = \frac{5 \pm 2\sqrt5 + 1}{4} = \frac{3 \pm \sqrt5}{2}.$$
So the [[singular values|0K2TX12X58]] are $\sigma_1 = \tfrac{\sqrt5 + 1}{2} \approx 1.618$ and $\sigma_2 = \tfrac{\sqrt5 - 1}{2} \approx 0.618$.
5. Neither singular value equals $1$, so the list $1, 1$ of absolute values of eigenvalues is not the list $\sigma_1, \sigma_2$.

## Remarks

The two lists do share their product.
Here $\sigma_1 \sigma_2 = \tfrac{5 - 1}{4} = 1 = \abs{\det A}$, and this holds for every square matrix, because both products equal $\abs{\det A}$.
The individual values are what differ.

The singular values describe stretching, and the eigenvalues do not.
The unit vector $(0, 1)$ goes to $(1, 1)$, of length $\sqrt2 \approx 1.414$, so $A$ stretches some vectors by more than its eigenvalue $1$.
The largest stretch is $\sigma_1 \approx 1.618$, the golden ratio, and the smallest is its inverse.

The difference comes from the fact that the shear is not normal.
Its other product is $A A^{\mathsf{T}} = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, which is not $A^{\mathsf{T}} A$.
For a [[normal matrix|0MR0BYF0K2]] the singular values are exactly the absolute values of the eigenvalues.
If we change the corner entry $1$ to $0$, the shear becomes $I$, which is normal, and both lists become $1, 1$.
If we change it to $c$, then $A^{\mathsf{T}} A$ has trace $2 + c^2$ and determinant $1$, so $\sigma_1$ grows without bound as $c$ grows, while the eigenvalues stay $1, 1$.

## Explanations

### L1 human

A shear slides the top of a square sideways and keeps the bottom fixed.
Its eigenvalues are $1$ and $1$, because the bottom edge does not move and the area does not change.
Still, it stretches some arrows: the arrow $(0, 1)$ becomes $(1, 1)$, which is longer.
The singular values $1.618$ and $0.618$ measure the real amount of stretching.

### L2 human

Eigenvalues tell how $A$ acts on its own eigenvectors, and singular values tell how $A$ changes lengths.
For a matrix that is not normal these are two different questions, with two different answers.
Watch out for a second mistake on the same example: the eigenvalues of $A^{\mathsf{T}} A$ are $\sigma_i^2 \approx 2.618$ and $0.382$, not the singular values themselves.
