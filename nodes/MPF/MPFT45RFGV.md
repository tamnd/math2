---
tag: MPFT45RFGV
kind: statement
role: theorem
name: Real Jordan form
aliases: [real-jordan-form, real-jordan-canonical-form]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
about: [0E89HQATM8, 07PH4RX0X5]
uses: [085HQ5G5TE, 0PBFS92AJP, 027KDW2K72, 0M0SNKZ482, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: Real matrices
  - book: isbn:9780521839402
    locator: Chapter 3
---

## Statement

Every real square matrix has a normal form over $\mathbb{R}$ in which each pair of complex conjugate eigenvalues $a \pm ib$ is replaced by $2 \times 2$ blocks that rotate and scale.
For real $a$ and $b$, let
$$R(a, b) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}.$$
For $k \ge 1$ and $b > 0$, let $C_k(a, b)$ be the real $2k \times 2k$ matrix with $k$ diagonal blocks $R(a, b)$, the identity $I_2$ in each block position $(s, s + 1)$, and $0$ elsewhere:
$$C_k(a, b) = \begin{pmatrix} R(a,b) & I_2 & & \\ & R(a,b) & \ddots & \\ & & \ddots & I_2 \\ & & & R(a,b) \end{pmatrix}.$$
Let $A \in M_n(\mathbb{R})$.

1. *Existence.* $A$ is [[similar|027KDW2K72]] over $\mathbb{R}$ to a [[block diagonal matrix|0M0SNKZ482]] whose blocks are [[Jordan blocks|0PBFS92AJP]] $J_k(\lambda)$ with $\lambda \in \mathbb{R}$ and blocks $C_k(a, b)$ with $a \in \mathbb{R}$ and $b > 0$.
2. *Correspondence.* Each block $C_k(a, b)$ is similar over $\mathbb{C}$ to $J_k(a + ib) \oplus J_k(a - ib)$. So the blocks $J_k(\lambda)$ of the real form are the blocks of the complex [[Jordan normal form|085HQ5G5TE]] with a real eigenvalue, and the blocks $C_k(a, b)$ match the pairs of [[complex conjugate|0FTH2E9TAS]] blocks $J_k(a \pm ib)$.
3. *Uniqueness.* The real Jordan form of $A$ is unique up to the order of the blocks.

## Remarks

### Why each hypothesis is needed

The condition $b > 0$ makes the form unique.
The matrix $R(a, -b)$ is similar to $R(a, b)$ by the swap of the two basis vectors, and in the same way $C_k(a, -b)$ is similar to $C_k(a, b)$, so one sign of $b$ must be fixed.
The matrix must be real.
For a complex matrix the nonreal eigenvalues need not come in conjugate pairs, for example $\operatorname{diag}(i, 0)$, and then the ordinary Jordan form over $\mathbb{C}$ is the right form.

### What it gives you

Every real matrix is similar over $\mathbb{R}$ to a block upper triangular matrix with diagonal blocks of size $1$ and $2$.
For a $2 \times 2$ real matrix with nonreal eigenvalues $a \pm ib$, the real form is the single block $R(a, b)$, which is the [[rotation-scaling form|KKJAZTB1EB]]: a rotation by the argument of $a + ib$ times a scaling by $\sqrt{a^2 + b^2}$.
The real solutions of a [[linear system of differential equations|037ZNY7NAG]] $y' = Ay$ come from the real form and the [[matrix exponential|020M04FN1H]].
A block $J_k(\lambda)$ gives the terms $t^j e^{\lambda t}$, and a block $C_k(a, b)$ gives $t^j e^{at} \cos bt$ and $t^j e^{at} \sin bt$, with $j < k$ in both cases.
Two real matrices are similar over $\mathbb{R}$ if and only if they are similar over $\mathbb{C}$, which is a case of the theorem that [[similarity does not depend on the field|5PVFX89NM7]].

### A worked use

Take $A = \begin{pmatrix} 1 & -2 \\ 1 & 3 \end{pmatrix}$, with $\chi_A = x^2 - 4x + 5$ and eigenvalues $2 \pm i$.
An eigenvector for $\mu = 2 + i$ is $z = (-1 + i, 1)$, since the first row gives $(1 - 2 - i)(-1 + i) - 2 = 2 - 2 = 0$.
Its imaginary part is $y = (1, 0)$ and its real part is $x = (-1, 1)$.
With $P = (y \mid x)$ and $R = R(2, 1)$ we get
$$AP = \begin{pmatrix} 1 & -2 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -3 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ 1 & 2 \end{pmatrix} = PR.$$
So $A$ is similar over $\mathbb{R}$ to $R(2, 1)$.
Watch out for the order: with $P = (x \mid y)$ the block becomes $R(2, -1)$, which is not in the normal form.

### Generalizations

Over any field $F$ the primary rational canonical form plays the same part: each irreducible factor $p$ of $\chi_A$ contributes blocks built from $p$.
Over $\mathbb{R}$ the irreducible factors have degree $1$ or $2$, and $C_k(a, b)$ is similar over $\mathbb{R}$ to the companion matrix of $((x - a)^2 + b^2)^k$, since both are cyclic with this characteristic polynomial.
So the real Jordan form is the primary rational form written in bases adapted to the rotation-scaling blocks.

## History

The theorem is the real version of the normal form that Camille Jordan published in 1870.

## Explanations

### L1 human

A real matrix can have complex eigenvalues, and then its Jordan form has complex entries.
The real Jordan form keeps everything real.
Each pair of complex eigenvalues $a \pm ib$ becomes a small $2 \times 2$ block that rotates the plane and stretches it.
For example, the quarter turn $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has eigenvalues $\pm i$, and it is already the block $R(0, 1)$.

### L2 human

Here is how the form of a $4 \times 4$ matrix with eigenvalues $1 \pm 2i$, each of multiplicity $2$, can look.
If each eigenvalue has only one Jordan block over $\mathbb{C}$, then the complex form is $J_2(1 + 2i) \oplus J_2(1 - 2i)$, and the real form is
$$C_2(1, 2) = \begin{pmatrix} 1 & -2 & 1 & 0 \\ 2 & 1 & 0 & 1 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 2 & 1 \end{pmatrix}.$$
If each has two blocks over $\mathbb{C}$, the real form is $R(1, 2) \oplus R(1, 2)$ instead.
The solutions of $y' = Ay$ in the first case contain $t e^{t} \cos 2t$ and $t e^{t} \sin 2t$, and in the second case they do not.
The trap is to forget the identity blocks $I_2$ above the diagonal: they are the real shadow of the ones in $J_2(1 \pm 2i)$.

### L3 human

The theorem is a case of Galois descent along $\mathbb{C} / \mathbb{R}$.
Complex conjugation maps the generalized eigenspace of $\mu$ onto that of $\bar\mu$, so Jordan chains can be chosen in conjugate pairs.
The real and imaginary parts of a chain for $\mu$ then span a real invariant subspace whose complexification is the sum of the two conjugate pieces, as the [[proof from complex chains|TJ75DCK774]] shows.
For other fields the [[rational canonical form|042JWAR3Q0]] is the general answer.
