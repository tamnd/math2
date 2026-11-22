---
tag: 1CF483TZZA
kind: example
name: Unitary diagonalization of the rotation by a right angle
msc: ["15A18", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
instance_of: [0C8BR8XRTR]
not_instance_of:
  - target: 0NEGN5CRSC
    note: the rotation matrix R satisfies R^* = -R, which differs from R, and its eigenvalues i and -i are not real
illustrates: [04CW1P44VD, G6T1FNE3JC, EMW3QTE3H9]
uses: [0ENZN5G4CV, 0D6RMJ10M9, XS5H42KEP5, 0XYKE8BE7X]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_matrix
    locator: Special cases
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Example

Let $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, [[the rotation by a right angle|XS5H42KEP5]], act on $\mathbb{C}^2$ with the standard inner product $\ip{x}{y} = x_1 \overline{y_1} + x_2 \overline{y_2}$.
We check that $R$ is normal and find a unitary matrix that makes it diagonal.

1. The entries of $R$ are real, so the conjugate transpose is the transpose: $R^* = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = -R$.
2. Then $R^* R = -R^2$ and $R R^* = -R^2$, and $R^2 = -I$, so both products are $I$. Hence $R$ is [[normal|0ENZN5G4CV]], and it is also [[unitary|0D6RMJ10M9]].
3. The characteristic polynomial is $t^2 + 1$, with the roots $i$ and $-i$.
4. For $i$: $R(1, -i) = (i, 1) = i(1, -i)$. For $-i$: $R(1, i) = (-i, 1) = -i(1, i)$.
5. The two eigenvectors are orthogonal for the complex inner product:
$$\ip{(1, -i)}{(1, i)} = 1 \cdot \overline{1} + (-i) \cdot \overline{i} = 1 + (-i)(-i) = 1 - 1 = 0.$$
6. Each eigenvector has length $\sqrt{1 + 1} = \sqrt{2}$. So $U = \tfrac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix}$, with the unit eigenvectors as columns, is unitary, and
$$U^* R U = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}.$$

Check: $R U = \tfrac{1}{\sqrt{2}} \begin{pmatrix} i & -i \\ 1 & 1 \end{pmatrix}$, and $U \operatorname{diag}(i, -i) = \tfrac{1}{\sqrt{2}} \begin{pmatrix} i & -i \\ 1 & 1 \end{pmatrix}$ too.

## Remarks

The rotation is the [[complex spectral theorem|04CW1P44VD]] at work on a normal matrix that is not Hermitian.
Its eigenvalues $\pm i$ are not real, so $R$ is not self-adjoint, and they have absolute value $1$, as the eigenvalues of every unitary matrix do.
[[The norm criterion|EMW3QTE3H9]] is visible too: $\norm{Rv} = \norm{R^* v} = \norm{v}$ for every $v$, because $R$ and $R^* = -R$ both keep lengths.

Over $\mathbb{R}$ the picture changes completely.
The polynomial $t^2 + 1$ has no real root, so $R$ has no real eigenvector, and no real orthonormal basis makes $R$ diagonal.
The best real form is the matrix itself, which already has the shape $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a = 0$ and $b = 1$ of [[the real normal form|G6T1FNE3JC]].
If you replace the right angle by an angle $\theta$, the same eigenvectors work for every $\theta$, with the eigenvalues $\cos \theta \pm i \sin \theta = e^{\pm i\theta}$.

## Explanations

### L1 human

A quarter turn of the plane keeps no real direction fixed.
With complex numbers, two special directions appear, and the turn multiplies them by $i$ and by $-i$.
These two complex directions are perpendicular.
So even a rotation becomes a diagonal matrix in a suitable orthonormal complex basis.

### L2 human

The recipe for a normal matrix is the same as for a Hermitian matrix, with one change: the eigenvalues need not be real.
First check $R^* R = R R^*$, and here both products are $I$.
Next find the eigenvalues, here $\pm i$, and a unit eigenvector for each.
Then check orthogonality with the complex inner product, which conjugates the second vector.
Last put the unit eigenvectors as the columns of $U$, and $U^* R U$ is diagonal.
Watch out: without the conjugation, the product of $(1, -i)$ and $(1, i)$ would be $1 + 1 = 2$, and the eigenvectors would wrongly look not orthogonal.
