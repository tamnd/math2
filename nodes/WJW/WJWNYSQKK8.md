---
tag: WJWNYSQKK8
kind: concept
name: Matrix congruence
aliases: [congruent-matrices]
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
uses: [0EB9N0S33C, 09DXWYRD43, 0QK6K857HS]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
    locator: Congruence over the reals
  - book: isbn:9780135367971
    locator: Chapter 10
same_as:
  wikidata: Q377286
  wikipedia: Matrix congruence
---

## Summary

Two square matrices are congruent when they describe the same bilinear form in two different bases.
Congruence is to forms what [[similarity|0E89HQATM8]] is to linear maps: it is the relation that tells you when two matrices are "the same thing written differently".
Let $F$ be a field.
Two $n \times n$ matrices $A$ and $A'$ over $F$ are *congruent* when
$$A' = P^{\mathsf{T}} A P$$
for some [[invertible|0EB9N0S33C]] $n \times n$ matrix $P$ over $F$, where $P^{\mathsf{T}}$ is the [[transpose|09DXWYRD43]] of $P$.
The [[formal definition|NZJDNC6EP6]] states the same condition.
By the [[change of basis rule|0SPYAGE7T0]], congruent matrices are exactly the [[matrices|0QK6K857HS]] of one [[bilinear form|0SQZMXB6GP]] in two bases.

## Motivation

A bilinear form has one matrix in each basis, and these matrices can look very different.
The form $x_1 y_2 + x_2 y_1$ on $\mathbb{Q}^2$ has the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ in the standard basis and the diagonal matrix $\operatorname{diag}(2, -2)$ in the basis $(1, 1), (1, -1)$.
We want the simplest matrix of a given form, and we want to know when two matrices can never describe the same form.
Both questions are about congruence.

So the classification of bilinear forms is the classification of matrices up to congruence.
The answer depends on the field, and that is where much of the theory lives.
Over $\mathbb{R}$ it gives [[Sylvester's law of inertia|0WFED3K3DQ]], which the sub-area on quadratic forms proves, and for alternating matrices over any field it gives the [[classification of alternating forms|V8KKHKXXB3]].

## Notation

Some books write $A \cong A'$ or $A \sim_c A'$, and many use no symbol at all.
Over $\mathbb{C}$ the relation $A' = P^* A P$, with the [[conjugate transpose|0DXKE10PHF]] $P^*$, is called $*$-congruence or conjunctivity.
It is the relation for [[sesquilinear forms|054YEQ0Y8M]] written in the physics convention $h(x, y) = x^* A y$.
In the convention of these pages, $h(x, y) = x^{\mathsf{T}} M \overline{y}$, the matrix changes by $M \mapsto P^{\mathsf{T}} M \overline{P}$ instead.

## Remarks

### Three worked congruences

First, $I_2$ and $\operatorname{diag}(4, 9)$ are congruent over $\mathbb{Q}$.
Take $P = \operatorname{diag}(2, 3)$:
$$P^{\mathsf{T}} I_2 P = P^2 = \begin{pmatrix} 4 & 0 \\ 0 & 9 \end{pmatrix}.$$
Stretching the axes by $2$ and $3$ multiplies the diagonal entries by the squares $4$ and $9$.

Second, $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is congruent to $\operatorname{diag}(2, -2)$ over $\mathbb{Q}$, with $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$:
$$AP = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}, \qquad P^{\mathsf{T}} A P = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}.$$

Third, [[the matrices $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ and $\operatorname{diag}(1, -3)$ are congruent|57GZX8S4ES]] by one step of row and column reduction.
For a form that is not symmetric, [[a change of basis on $\mathbb{Q}^2$|2X09GT6SMD]] turns $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ into $\begin{pmatrix} 6 & -4 \\ 0 & 2 \end{pmatrix}$.

### What congruence keeps

[[Congruence is an equivalence relation, and it keeps the rank and the symmetry|D3E2Y85S6H]] of a matrix.
The reasons are short.
Multiplying by invertible matrices keeps the rank, and $(P^{\mathsf{T}} A P)^{\mathsf{T}} = P^{\mathsf{T}} A^{\mathsf{T}} P$, so $A^{\mathsf{T}} = \pm A$ gives $A'^{\mathsf{T}} = \pm A'$.
The property $x^{\mathsf{T}} A x = 0$ for all $x$ survives too, because $x^{\mathsf{T}} A' x = (Px)^{\mathsf{T}} A (Px)$.
The determinant is multiplied by the nonzero square $(\det P)^2$, so its square class in $F^\times / (F^\times)^2$ stays the same.

For symmetric matrices the full list of invariants depends on the field.
Over $\mathbb{C}$, the rank alone fixes the class, by the [[classification of complex quadratic forms|0CEX9BRXRZ]].
Over $\mathbb{R}$, the rank and the [[signature|07EZA80NEH]] fix it, by Sylvester's law of inertia.

### What it is not

Over $\mathbb{R}$, $I_2$ and $-I_2$ are not congruent.
For every $P$ and $x$ we have $x^{\mathsf{T}} P^{\mathsf{T}} I_2 P x = \lVert Px \rVert^2 \ge 0$, but $x^{\mathsf{T}} (-I_2) x = -\lVert x \rVert^2 < 0$ for $x \neq 0$.
Over $\mathbb{C}$ the same two matrices are congruent, with $P = iI_2$, since $(iI_2)^{\mathsf{T}} I_2 (iI_2) = i^2 I_2 = -I_2$.

Over $\mathbb{Q}$, [[$I_2$ and $\operatorname{diag}(1, 2)$ are not congruent|R4ZDJG99Q0]], since the ratio $2$ of their determinants is not a rational square.
The matrices $\operatorname{diag}(1, 0)$ and $I_2$ are not congruent over any field, since their ranks differ.
A symmetric matrix is never congruent to a matrix that is not symmetric, since congruence keeps symmetry.

### Watch out

Congruence is not similarity.
Congruent matrices can have different eigenvalues, traces and determinants.
In the second worked congruence, $A$ has eigenvalues $1$ and $-1$, but the congruent diagonal matrix has entries $2$ and $-2$.
The two relations agree only for special $P$: when $P$ is orthogonal, $P^{\mathsf{T}} = P^{-1}$, and then $P^{\mathsf{T}} A P = P^{-1} A P$.

A second trap is in characteristic $2$.
Over $\mathbb{F}_2$, the symmetric matrix $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is not congruent to any diagonal matrix.
It gives $x^{\mathsf{T}} A x = 2x_1 x_2 = 0$ for all $x$, and congruence keeps this property.
A diagonal matrix $\operatorname{diag}(a, b)$ with the same property has $a = e_1^{\mathsf{T}} D e_1 = 0$ and $b = 0$, so its rank is $0$, not $2$.

### History

Sylvester published his law of inertia in 1852.
It says that when a real quadratic form is written as a sum of positive and negative squares, the numbers of each sign do not depend on the substitution used.
In the language of matrices, together with diagonalization, it says that two real symmetric matrices are congruent exactly when they have the same rank and the same number of positive eigenvalues.

### Try it

First, show that $\operatorname{diag}(1, 1)$ and $\operatorname{diag}(1, 25)$ are congruent over $\mathbb{Q}$.
Take $P = \operatorname{diag}(1, 5)$, so $P^{\mathsf{T}} I_2 P = \operatorname{diag}(1, 25)$.

Second, are $\operatorname{diag}(1, -1)$ and $\operatorname{diag}(-1, -1)$ congruent over $\mathbb{R}$?
No: the determinants $-1$ and $1$ have different signs, while congruence over $\mathbb{R}$ multiplies the determinant by a positive number.

## Explanations

### L1 human

A bilinear form turns into a square table of numbers once we choose a basis.
If we choose another basis, the same form gives another table.
We call two such tables congruent.
For example, the identity table and the table with $4$ and $9$ on its diagonal are congruent.
To see why, stretch the first axis by $2$ and the second by $3$: each diagonal entry gets multiplied by a stretch factor twice.

### L2 human

Here is a typical problem: is $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ congruent to $I_2$ over $\mathbb{Q}$?
Look for a basis in which the form $x^{\mathsf{T}} A y$ has the identity matrix.
Completing the square on $2x_1^2 + 2x_1 x_2 + x_2^2 = x_1^2 + (x_1 + x_2)^2$ suggests the new coordinates $x_1$ and $x_1 + x_2$, so the new basis is $b'_1 = (1, -1)$ and $b'_2 = (0, 1)$.
With $P = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$ we compute
$$AP = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad P^{\mathsf{T}} A P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
So the answer is yes.
Check: $\det A = 1$ and $\det I_2 = 1$, and $\det P = 1$.
The typical use of congruence is exactly this: bring a form to a simple normal form by a change of basis.

### L3 human

Congruence is the orbit relation of the action $P \cdot A = (P^{-1})^{\mathsf{T}} A P^{-1}$ of $GL_n(F)$ on $M_n(F)$.
The stabilizer of a symmetric $A$ is the [[orthogonal group|0TKYAEJ8N7]] of its form, and the stabilizer of a nondegenerate alternating $A$ is a [[symplectic group|X12FS2JAP0]].
For symmetric matrices over a finite field of odd characteristic, the rank and the square class of the determinant of the nondegenerate part fix the class.
Over $\mathbb{Q}$ the classification needs the local invariants of the [[Hasse-Minkowski theorem|R8HCWA981S]].
