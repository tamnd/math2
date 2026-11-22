---
tag: PFZF3KRBBB
kind: counterexample
name: A real matrix with no real Jordan normal form
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
uses: [085HQ5G5TE, 027KDW2K72, 0PBFS92AJP, 0VSSPAFM2C, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: Real matrices
---

## Counterexample

The rotation of the plane by a quarter turn shows that the [[Jordan normal form|085HQ5G5TE]] needs the characteristic polynomial to split.
Let
$$A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in M_2(\mathbb{R}).$$
We claim that $A$ is not [[similar|027KDW2K72]] over $\mathbb{R}$ to any real matrix of [[Jordan blocks|0PBFS92AJP]].

1. The [[characteristic polynomial|0VSSPAFM2C]] is $\det(xI - A) = x \cdot x - (-1)(1) = x^2 + 1$.
2. For every real $x$ we have $x^2 + 1 \ge 1 > 0$, so $A$ has no real [[eigenvalue|0BQAA2BK3Q]], and $\chi_A$ does not split over $\mathbb{R}$.
3. A real Jordan matrix of size $2$ is $J_2(\lambda)$ or $J_1(\lambda) \oplus J_1(\mu)$ with $\lambda, \mu \in \mathbb{R}$. It is upper triangular, so its characteristic polynomial is $(x - \lambda)^2$ or $(x - \lambda)(x - \mu)$, which has a real root.
4. Similar matrices have the same characteristic polynomial, and $x^2 + 1$ has no real root. So $A$ is similar to no real Jordan matrix.
5. Over $\mathbb{C}$ the polynomial splits as $(x - i)(x + i)$, and the eigenvectors are $(1, -i)$ and $(1, i)$:
$$A \begin{pmatrix} 1 \\ -i \end{pmatrix} = \begin{pmatrix} i \\ 1 \end{pmatrix} = i \begin{pmatrix} 1 \\ -i \end{pmatrix}, \qquad A \begin{pmatrix} 1 \\ i \end{pmatrix} = \begin{pmatrix} -i \\ 1 \end{pmatrix} = -i \begin{pmatrix} 1 \\ i \end{pmatrix}.$$
6. With $P = \begin{pmatrix} 1 & 1 \\ -i & i \end{pmatrix}$ we get
$$AP = \begin{pmatrix} i & -i \\ 1 & 1 \end{pmatrix} = P \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix},$$
so the complex Jordan form is $J_1(i) \oplus J_1(-i)$.

## Remarks

So the hypothesis "the characteristic polynomial splits" in the Jordan normal form cannot be dropped, even for a $2 \times 2$ matrix with integer entries.
Two normal forms survive over $\mathbb{R}$.
The matrix $A$ is already in [[real Jordan form|MPFT45RFGV]], as the rotation-scaling block $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a = 0$ and $b = 1$.
It is also its own [[rational canonical form|042JWAR3Q0]], the companion matrix $C(x^2 + 1)$ in the column version.

What changes with the field?
Over $\mathbb{F}_2$ the same matrix has $\chi = x^2 + 1 = (x + 1)^2$, which splits, and $A - I = A + I = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ has rank $1$.
So over $\mathbb{F}_2$ the Jordan form exists and is $J_2(1)$.

## Explanations

### L1 human

A quarter turn of the plane moves every line through the origin to a different line.
So no arrow is just stretched, and the turn has no real eigenvector.
A Jordan form over the reals would need at least one such arrow, so it cannot exist.
With complex numbers the turn becomes diagonal, with $i$ and $-i$ on the diagonal.

### L2 human

The test is the characteristic polynomial.
Every real Jordan matrix has real numbers on its diagonal, and they are the roots of its characteristic polynomial.
Here $\chi_A = x^2 + 1$ has no real root, so $A$ and a real Jordan matrix can never be similar over $\mathbb{R}$.
The trap is to conclude that $A$ has no normal form at all: over $\mathbb{R}$ the real Jordan form and the rational canonical form both exist.
