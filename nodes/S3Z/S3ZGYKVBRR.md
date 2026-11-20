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

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, a shear.

1. $A$ is triangular with diagonal $1, 1$, so its only [[eigenvalue|0ZND7NQ970]] is $1$, with algebraic multiplicity $2$.
2. $A^T A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$.
3. Its trace is $3$ and its determinant is $1$, so its eigenvalues are the roots of $t^2 - 3t + 1$, namely $\tfrac{3 \pm \sqrt5}{2}$.
4. Since $\left(\tfrac{\sqrt5 \pm 1}{2}\right)^2 = \tfrac{6 \pm 2\sqrt5}{4} = \tfrac{3 \pm \sqrt5}{2}$, the [[singular values|0K2TX12X58]] are $\sigma_1 = \tfrac{\sqrt5 + 1}{2} \approx 1.618$ and $\sigma_2 = \tfrac{\sqrt5 - 1}{2} \approx 0.618$.
5. So the eigenvalue $1$ is not a singular value of $A$: the pair $1, 1$ is not the pair $\sigma_1, \sigma_2$.

## Remarks

- $\sigma_1 \sigma_2 = \tfrac{5 - 1}{4} = 1 = \abs{\det A}$. The product of the singular values and the absolute product of the eigenvalues always agree for square matrices; the single values do not.
- $\norm{A (0, 1)} = \norm{(1, 1)} = \sqrt2 > 1$, so $A$ stretches some vectors by more than its eigenvalue. The largest stretch is $\sigma_1 \approx 1.618$, the golden ratio.
- For [[normal matrices|0MR0BYF0K2]] the singular values are the absolute values of the eigenvalues. The shear is not normal, since $A^T A \ne A A^T$.

## Explanations

### L1 human

A shear slides the top of a square sideways.
Its eigenvalues are $1$ and $1$, but it still stretches some vectors.
The singular values $1.618$ and $0.618$ measure the stretch.

### L2 human

Eigenvalues tell how $A$ acts on its own eigenvectors, and singular values tell how $A$ changes lengths.
For a matrix that is not normal these two things differ.
A trap: the eigenvalues of $A^T A$ are $\sigma_i^2$, not $\sigma_i$; here they are $2.618$ and $0.382$.
