---
tag: XS5H42KEP5
kind: example
name: Rotation of the plane by a right angle
msc: ["15A04", "15A20"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [08VRX3Q4PB]
not_instance_of:
  - target: 0ACX5QT8TE
    note: the line spanned by e1 is not invariant under the rotation, and no line through 0 is invariant over the real numbers
  - target: 07SQCNV233
    note: the rotation matrix has no real eigenvalue, so it is not diagonalizable over the real numbers, although it is diagonalizable over the complex numbers
uses: [0EP59ESQ94, 0Y17PEKF24, 0QS8P74F2Z, 039HF58KQ5, 053QVHF6N7]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Examples
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Example

Let
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},$$
the [[rotation|0B9QNFGTHM]] of $\R^2$ by a right angle, counterclockwise.
We find its invariant subspaces over $\R$, and then diagonalize it over $\C$.

1. The line $\R e_1$ is not [[invariant|0ACX5QT8TE]], since $R e_1 = e_2$ is not a multiple of $e_1$.
2. The [[characteristic polynomial|0VSSPAFM2C]] is
$$p_R(t) = \det \begin{pmatrix} t & 1 \\ -1 & t \end{pmatrix} = t^2 + 1,$$
   which has no real root, so $R$ has no real [[eigenvalue|0BQAA2BK3Q]] by the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
3. A line $\R v$ with $v \ne 0$ is invariant exactly when $R v = \lambda v$ for some real $\lambda$.
   By step 2 there is no such $\lambda$, so the only invariant subspaces of $\R^2$ are $0$ and $\R^2$.
4. With no real eigenvector, there is no basis of eigenvectors, so $R$ is not [[diagonalizable|07SQCNV233]] over $\R$.
5. Over $\C$ the roots of $t^2 + 1$ are $i$ and $-i$, and we check two eigenvectors:
$$R \begin{pmatrix} 1 \\ -i \end{pmatrix} = \begin{pmatrix} i \\ 1 \end{pmatrix} = i \begin{pmatrix} 1 \\ -i \end{pmatrix}, \qquad R \begin{pmatrix} 1 \\ i \end{pmatrix} = \begin{pmatrix} -i \\ 1 \end{pmatrix} = -i \begin{pmatrix} 1 \\ i \end{pmatrix}.$$
6. Put the eigenvectors in the columns of $P$.
   Then $\det P = i - (-i) = 2i$, and
$$P = \begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix}, \qquad P^{-1} = \frac{1}{2} \begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix}.$$
7. Multiply back with $D = \operatorname{diag}(i, -i)$:
$$P D = \begin{pmatrix} i & -i \\ 1 & 1 \end{pmatrix}, \qquad P D P^{-1} = \frac{1}{2} \begin{pmatrix} i - i & -1 - 1 \\ 1 + 1 & i - i \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = R.$$
   So $R$ is diagonalizable over $\C$.
8. By step 3 the only invariant subspaces over $\R$ are $0$ and $\R^2$, and each is an invariant complement of the other.
   So $R$ is [[semisimple|08VRX3Q4PB]] over $\R$.

## Remarks

The example shows that diagonalizability depends on the field, while semisimplicity does not need the eigenvalues to exist in the field.
The minimal polynomial of $R$ is $t^2 + 1$, a single irreducible factor over $\R$, which is the minimal polynomial test for semisimplicity.

Change the angle to $\theta$.
If $\theta$ is not a multiple of $\pi$, the same steps work with the complex eigenvalues $\cos \theta \pm i \sin \theta$, and no real line is invariant.
If $\theta = \pi$, the rotation is $-I$, every line is invariant, and the matrix is already diagonal.
The matrix $R$ also satisfies $R^4 = I$, and every complex matrix of finite order is diagonalizable over $\C$, which agrees with step 7.

## Explanations

### L1 human

A quarter turn of the plane moves every line through the center to a different line.
So no direction is only stretched, and a real diagonal matrix, which only stretches along the axes, cannot describe the turn.
With complex numbers there are two special directions, and on them the turn acts as multiplication by $i$ and by $-i$.

### L2 human

Here is how to find the complex eigenvectors of step 5.

1. For $\lambda = i$, the matrix $R - iI = \begin{pmatrix} -i & -1 \\ 1 & -i \end{pmatrix}$ has determinant $(-i)^2 + 1 = 0$, so it has rank $1$.
2. Its first row gives $-ix - y = 0$, so $y = -ix$, and $x = 1$ gives $v = (1, -i)$.
3. For $\lambda = -i$, the same work with $R + iI$ gives $y = ix$ and $v = (1, i)$.
4. These vectors are the columns of $P$, and $P^{-1} R P = \operatorname{diag}(i, -i)$.

The trap is to say that $R$ "is not diagonalizable" without naming the field: the statement is true over $\R$ and false over $\C$.
