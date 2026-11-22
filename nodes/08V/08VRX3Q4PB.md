---
tag: 08VRX3Q4PB
kind: concept
name: Semisimple endomorphism
msc: ["15A04", "15A20"]
topics: [Z6S6PWMJPH]
audience: grad
specializes: [0J7H0YBFDJ]
uses: [0J7H0YBFDJ, 0ACX5QT8TE, 03NDVCSHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Semisimple_operator
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition
    locator: Decomposition of a linear operator
  - book: isbn:9780135367971
    locator: Section 6.8
same_as:
  wikidata: Q3299281
  wikipedia: Semisimple operator
---

## Summary

A semisimple map is a linear map with no shearing part: every piece of the space that it keeps in place has a partner piece that it also keeps in place.
It is the right replacement for "diagonalizable" over a field where the eigenvalues may be missing, such as $\R$.
Exactly, an [[endomorphism|0J7H0YBFDJ]] $T$ of a finite-dimensional vector space $V$ over a field $F$ is [[semisimple|0QS8P74F2Z]] when every $T$-[[invariant subspace|0ACX5QT8TE]] $W$ has a $T$-invariant complement $W'$, so that $V = W \oplus W'$.
An equivalent test uses the [[minimal polynomial|03NDVCSHSB]]:
$$T \text{ is semisimple} \iff m_T = p_1 p_2 \cdots p_k \text{ with distinct monic irreducible } p_i \in F[t].$$
When the characteristic polynomial of $T$ splits over $F$, semisimple means the same as [[diagonalizable|07SQCNV233]].

## Motivation

The rotation of $\R^2$ by a right angle is not diagonalizable over $\R$, because it has no real eigenvalue.
Yet it has nothing in common with a shear, which is not diagonalizable for a different reason: it has an eigenvalue whose eigenvectors are too few.
Over $\C$ the rotation becomes diagonal and the shear does not.
We want a word for maps like the rotation that we can use without leaving the field $F$, and "semisimple" is that word.

The notion is needed for the [[Jordan-Chevalley decomposition|011K11VPJN]] $T = S + N$ over fields that are not algebraically closed, where $S$ is semisimple and $N$ is nilpotent.
It returns in the sub-area on canonical forms, where the elementary divisors of a semisimple map are irreducible polynomials, and in Lie theory, where semisimple elements of a Lie algebra play the role of diagonal matrices.

## Notation

There is no special symbol.
In Mathlib, `Module.End.IsSemisimple T` says that $V$ is a semisimple module over $F[t]$, with $t$ acting as $T$.
This agrees with the definition above, because the $F[t]$-submodules of $V$ are exactly the $T$-invariant subspaces.
Watch out for the word in older books: some authors call a map semisimple only when it is diagonalizable over an algebraic closure of $F$, and outside characteristic $0$ the two meanings differ.

## Remarks

### Diagonalizable maps are semisimple

Take $A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ over $\R$, which has the eigenvalues $5$ and $2$ with eigenvectors $(1, 1)$ and $(1, -2)$, as in [[diagonalizing a 2 × 2 matrix|306FBDECMB]].
An invariant line must be spanned by an eigenvector, so the invariant subspaces are $0$, the two eigenlines and $\R^2$.
Each eigenline has the other eigenline as an invariant complement, and $0$ and $\R^2$ are complements of each other.
So $A$ is semisimple.

The same works for every diagonalizable $T$.
An invariant subspace $W$ is the sum of its pieces $W \cap E_\lambda$ in the eigenspaces, because the projections onto the eigenspaces are polynomials in $T$ and so map $W$ into $W$.
Choose a complement of $W \cap E_\lambda$ inside each $E_\lambda$; every subspace of an eigenspace is invariant, and the sum of these choices is an invariant complement of $W$.

### Semisimple without eigenvalues

The [[rotation by a right angle|XS5H42KEP5]] $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has $p_R(t) = t^2 + 1$ and no real eigenvalue.
So no line through $0$ is invariant, and the only invariant subspaces of $\R^2$ are $0$ and $\R^2$.
Each is a complement of the other, so $R$ is semisimple over $\R$ while it is not diagonalizable over $\R$.

For a larger case, put $R$ and the number $2$ in one block diagonal matrix:
$$B = \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 2 \end{pmatrix}, \qquad m_B(t) = (t^2 + 1)(t - 2).$$
Check: $B^2 + I$ is zero on the first two coordinates and $B - 2I$ is zero on the third, so the product kills all of $\R^3$.
The two factors are distinct and irreducible over $\R$, so $B$ is semisimple over $\R$.

### What it is not

The [[shear|SBDF8APDF7]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ is not semisimple.
The line $F e_1$ is invariant, and an invariant complement would be a second invariant line, so a second eigenline.
The only eigenvalue is $1$ and its eigenspace is $F e_1$ itself, so no complement exists.
In the same way, a nonzero [[nilpotent|063D5Z2C70]] map is never semisimple, since its minimal polynomial $t^k$ with $k \ge 2$ repeats the factor $t$.
The [[Jordan block of size 3|1YGY396SAS]] fails for the same reason, with $m = (t - 2)^3$.

### The rules you can use

The minimal polynomial test comes from the [[primary decomposition theorem|49ZHBMYKVE]].
When $m_T = p_1 \cdots p_k$ with distinct irreducible $p_i$, the space splits as $\bigoplus_i \ker p_i(T)$, and each piece is a vector space over the field $F[t]/(p_i)$, where invariant subspaces always have complements.
Three rules follow at once.
The restriction of a semisimple map to an invariant subspace is semisimple, because its minimal polynomial divides $m_T$.
A map that is both semisimple and nilpotent is $0$, because a squarefree power of $t$ is $t$ itself.
If $p_T$ splits, a squarefree $m_T$ has simple roots, so semisimple means diagonalizable by the [[minimal polynomial criterion|0MPAJRB23T]].

### Watch out

Do not read "semisimple" as "diagonalizable over the algebraic closure" without checking the field.
If $T$ is diagonalizable over an algebraic closure $\bar F$, then $m_T$ has simple roots in $\bar F$, so it is squarefree over $F$ and $T$ is semisimple; this direction holds over every field.
The other direction needs a [[perfect field|VWBVKT794W]], such as a field of characteristic $0$ or a finite field, where irreducible polynomials have simple roots in $\bar F$.
Over the imperfect field $\mathbb{F}_2(s)$, the [[companion matrix of x² + s|C720K6S84D]] is semisimple, but over $\bar F$ it has the single eigenvalue $\sqrt{s}$ and is not diagonal.

### History

The name comes from module theory.
A module is semisimple when it is a direct sum of simple modules, and $T$ is semisimple exactly when $V$ is a semisimple module over $F[t]$.

### Try it

First, is $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ semisimple over $\R$?
No: its minimal polynomial is $(t - 2)^2$, which repeats the factor $t - 2$.

Second, let $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which is diagonalizable over $\mathbb{Q}$ with eigenvalues $1$ and $-1$.
Is it semisimple over the field $\mathbb{F}_2$?
No: $A^2 = I$ and $A \ne I$, so $m_A = t^2 - 1$, and over $\mathbb{F}_2$ this is $t^2 + 1 = (t + 1)^2$.

## Explanations

### L1 human

Think of a map that stretches the plane by $5$ along one line and by $2$ along another.
Each of the two lines stays in place, and together they fill the plane.
A quarter turn keeps no line in place, so no line needs a partner, and it is semisimple too.
A shear keeps the horizontal line in place, but it tilts every other line toward it, so the horizontal line has no partner.
Semisimple maps are the stretches and turns, and the shear is the typical map that is not semisimple.

### L2 human

Let us decide whether $A = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ is semisimple over $\R$.
The trace is $2$ and the determinant is $1 + 1 = 2$, so
$$p_A(t) = t^2 - 2t + 2.$$
Its discriminant is $4 - 8 = -4 < 0$, so $p_A$ has no real root and is irreducible over $\R$.
The minimal polynomial divides $p_A$ and has degree at least $1$, and an irreducible polynomial has no other monic factor of positive degree, so $m_A = p_A$.
This is a single irreducible factor, so $A$ is semisimple over $\R$.
Over $\C$ the roots are $1 + i$ and $1 - i$, which are distinct, so $A$ is diagonalizable over $\C$.
The example shows the usual test: factor $m_T$ over $F$ and look for a repeated irreducible factor.
It also shows the trap: a matrix with no real eigenvalue can still be semisimple over $\R$.

### L3 human

Semisimplicity is a statement about the $F[t]$-module $V$: it is a direct sum of simple modules $F[t]/(p)$ with $p$ irreducible.
The same definition works for any family of commuting maps, using the algebra that they generate, and for an element of a finite-dimensional algebra acting on itself.
Over a perfect field, every element $g$ of a linear algebraic group has a multiplicative Jordan decomposition $g = g_s g_u$ with $g_s$ semisimple, $g_u$ unipotent and $g_s g_u = g_u g_s$.
In a semisimple Lie algebra, the abstract Jordan decomposition uses the semisimple and nilpotent parts of the adjoint map; this belongs to Lie theory.
In the sub-area on canonical forms, a semisimple map is the one whose elementary divisors are all irreducible polynomials, so its primary rational form is block diagonal with companion matrices of irreducible polynomials.
