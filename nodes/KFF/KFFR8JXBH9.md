---
tag: KFFR8JXBH9
kind: example
name: A rational matrix with no Jordan form over the rationals
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
not_instance_of:
  - target: 7M1W0ZA49Q
    note: the characteristic polynomial x² − 2 does not split over Q, so the method stops at its first step
illustrates: [085HQ5G5TE]
uses: [7M1W0ZA49Q, 0VH1TC1PWF, 0VSSPAFM2C]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: Matrices with entries in a field
---

## Example

Let $A$ be the [[companion matrix|0VH1TC1PWF]] of $x^2 - 2$ over $\mathbb{Q}$, in the column version:
$$A = C(x^2 - 2) = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}.$$
We show that the [[method for computing the Jordan form|7M1W0ZA49Q]] cannot start over $\mathbb{Q}$, and that it works over $\mathbb{R}$.

1. For a $2 \times 2$ matrix the [[characteristic polynomial|0VSSPAFM2C]] is $x^2 - (\operatorname{tr} A)\, x + \det A$, and here $\operatorname{tr} A = 0$ and $\det A = -2$. So $\chi_A = x^2 - 2$.
2. The roots of $x^2 - 2$ are $\pm \sqrt 2$, which are irrational. So $\chi_A$ does not split over $\mathbb{Q}$, and $A$ has no eigenvalue in $\mathbb{Q}$.
3. A Jordan matrix over $\mathbb{Q}$ is triangular with rational diagonal entries, so its characteristic polynomial has only rational roots. Similar matrices have the same characteristic polynomial, so $A$ is similar over $\mathbb{Q}$ to no Jordan matrix.
4. Over $\mathbb{R}$ the polynomial factors as $(x - \sqrt 2)(x + \sqrt 2)$. The eigenvectors are found from $A (a, b)^{\mathsf T} = (2b, a)^{\mathsf T}$:
$$A \begin{pmatrix} \sqrt 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ \sqrt 2 \end{pmatrix} = \sqrt 2 \begin{pmatrix} \sqrt 2 \\ 1 \end{pmatrix}, \qquad A \begin{pmatrix} -\sqrt 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 \\ -\sqrt 2 \end{pmatrix} = -\sqrt 2 \begin{pmatrix} -\sqrt 2 \\ 1 \end{pmatrix}.$$
5. These two eigenvectors for different eigenvalues are independent, so over $\mathbb{R}$ the Jordan form is $J_1(\sqrt 2) \oplus J_1(-\sqrt 2)$.

## Remarks

Over $\mathbb{Q}$ the matrix $A$ is already in [[rational canonical form|042JWAR3Q0]], with the single invariant factor $x^2 - 2$.
So when the characteristic polynomial does not split, the rational canonical form is the normal form to use, and the Jordan form needs a larger field.
The field matters only for the existence of the form: by the theorem that [[similarity does not depend on the field|5PVFX89NM7]], two rational matrices that are similar over $\mathbb{R}$ are already similar over $\mathbb{Q}$.

Change the entry $2$ to $4$.
Then $\chi = x^2 - 4 = (x - 2)(x + 2)$ splits over $\mathbb{Q}$, the eigenvectors are $(2, 1)$ and $(-2, 1)$, and the Jordan form over $\mathbb{Q}$ is $\operatorname{diag}(2, -2)$.

## Explanations

### L1 human

The eigenvalues of this matrix are the two square roots of $2$, and they are not fractions.
A Jordan form shows the eigenvalues on its diagonal, so with fractions only you cannot write it.
With real numbers you can, and the form is the diagonal matrix with $\sqrt 2$ and $-\sqrt 2$.

### L2 human

The first step of the method is to factor the characteristic polynomial over the field.
Here $x^2 - 2$ has no rational root, so the method stops at once over $\mathbb{Q}$.
Over $\mathbb{R}$ the check $A v = \lambda v$ in step 4 shows that the two eigenvectors exist, and the form is diagonal.
The trap is to think that $A$ is "not diagonalizable" in an absolute sense: whether it is diagonalizable depends on the field.
