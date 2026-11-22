---
tag: XGRN8RY29P
kind: example
name: A real matrix with complex eigenvalues
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
instance_of: [0VSSPAFM2C, 7JJE96MZQY]
illustrates: [053QVHF6N7, 0NMXDCNNKR, 0C2F40MEBC]
uses: [039HF58KQ5, 0ZND7NQ970, 0B5H4208Z9, 053QVHF6N7, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Eigenvalues and characteristic polynomial
  - book: isbn:9780321982384
---

## Example

Let
$$A = \begin{pmatrix} 3 & -2 \\ 4 & -1 \end{pmatrix},$$
a matrix with real entries.
We find its eigenvalues and eigenvectors, first over $\mathbb{R}$ and then over $\mathbb{C}$.

1. By the [[definition of the characteristic polynomial|039HF58KQ5]],
$$p_A(t) = \det \begin{pmatrix} t - 3 & 2 \\ -4 & t + 1 \end{pmatrix} = (t - 3)(t + 1) + 8 = t^2 - 2t + 5.$$
2. Check with the trace and the determinant: $\operatorname{tr} A = 3 - 1 = 2$ and $\det A = -3 + 8 = 5$, which give the same polynomial.
3. The discriminant is $(-2)^2 - 4 \cdot 5 = -16 < 0$, so $p_A$ has no real root.
   By the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], $A$ has no eigenvalue over $\mathbb{R}$.
4. Over $\mathbb{C}$ the roots are $\lambda = 1 + 2i$ and $\bar\lambda = 1 - 2i$, so these are the [[eigenvalues|0ZND7NQ970]] of $A$ over $\mathbb{C}$.
5. For $\lambda = 1 + 2i$, the first row of $A - \lambda I$ is $(2 - 2i, -2)$.
   The equation $(2 - 2i) x_1 - 2 x_2 = 0$ gives $x_2 = (1 - i) x_1$, so $v = (1, 1 - i)$ is an [[eigenvector|0B5H4208Z9]].
6. Check: multiply out both sides:
$$Av = \big(3 - 2(1 - i),\ 4 - (1 - i)\big) = (1 + 2i,\ 3 + i),$$
$$\lambda v = \big(1 + 2i,\ (1 + 2i)(1 - i)\big) = (1 + 2i,\ 1 - i + 2i + 2) = (1 + 2i,\ 3 + i).$$
7. The entries of $A$ are real, so taking the [[complex conjugate|0FTH2E9TAS]] of $Av = \lambda v$ gives $A \bar v = \bar\lambda \bar v$.
   So $\bar v = (1, 1 + i)$ is an eigenvector for $\bar\lambda = 1 - 2i$.

## Remarks

The example shows that the field matters.
The same matrix has no eigenvalue over $\mathbb{R}$ and two over $\mathbb{C}$, and the nonreal eigenvalues of a real matrix always come in conjugate pairs, with conjugate eigenvectors.
The trace and determinant rules still hold over $\mathbb{C}$: $\lambda + \bar\lambda = 2 = \operatorname{tr} A$ and $\lambda \bar\lambda = 1 + 4 = 5 = \det A$.

The complex eigenvector also explains what $A$ does to the real plane.
Split $v = a + i b$ with $a = (1, 1)$ and $b = (0, -1)$.
Comparing real and imaginary parts of $Av = \lambda v$ gives $Aa = a - 2b$ and $Ab = 2a + b$, so in the real basis $a, b$ the matrix of $A$ is
$$\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix} = \sqrt{5} \begin{pmatrix} \cos\varphi & \sin\varphi \\ -\sin\varphi & \cos\varphi \end{pmatrix}, \qquad \cos\varphi = \tfrac{1}{\sqrt 5}.$$
That is a rotation combined with a stretch by $\sqrt{5} = \lvert \lambda \rvert$.

Change one entry and the picture changes.
If the entry $-2$ becomes $2$, the trace is still $2$ but the determinant is $-3 - 8 = -11$, so $p(t) = t^2 - 2t - 11$ has the real roots $1 \pm 2\sqrt{3}$.

## Explanations

### L1 human

Some real matrices turn every arrow of the plane, so no arrow stays on its own line.
Such a matrix has no real eigenvalue.
This matrix turns the plane and also stretches it by about $2.24$, the square root of $5$.
If we allow complex numbers, it does have eigenvalues, namely $1 + 2i$ and $1 - 2i$, and the size of each one is that stretch factor.

### L2 human

The method for complex eigenvalues is the same as for real ones: roots of $p_A$ first, then a linear system for each root.
Since the matrix is $2 \times 2$ and $A - \lambda I$ is singular, one row of it is enough to find the eigenvector, as in step 5.
For a real matrix you need only one of the two systems, because the other eigenvector is the conjugate.
Watch out: when you check $Av = \lambda v$, remember that $i^2 = -1$, which turned $-2i^2$ into $+2$ in step 6.
