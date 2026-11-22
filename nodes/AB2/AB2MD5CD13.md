---
tag: AB2MD5CD13
kind: concept
name: Matrix ring
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
specializes: [0B1261B5ED]
uses: [0CP7YY6NAG, 0BVXADM10P, 076JGP6R3T, 0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Abstract algebraic aspects and generalizations
---

## Summary

The square matrices of one size can be added and multiplied without ever leaving that size, so they form a number system of their own.
That system is the first ring most students meet in which $ab = ba$ fails, and it is the standard source of examples in [[ring theory|0B1261B5ED]].
For a ring $R$ and an integer $n \ge 1$, the *matrix ring* $M_n(R)$ is the set of $n \times n$ [[square matrices|0CP7YY6NAG]] over $R$, with [[matrix addition|0BVXADM10P]] and [[matrix multiplication|076JGP6R3T]] as its operations.
Its zero is the zero matrix $0_n$, and its identity is the identity matrix $I_n$.
The [[object page|0FHVPRAE60]] lists the ring axioms and checks them.
When $R$ is commutative, $M_n(R)$ is also an algebra over $R$, because a scalar $c$ acts as the matrix $cI_n$.

## Motivation

Why give the square matrices a name of their own?
A linear map from $F^n$ to itself can be followed by another such map, and its matrix can be added to the matrix of another such map.
So the $n \times n$ matrices carry all the algebra of these maps: we can form $A^2 + 3A - I$, ask whether $A$ has an inverse, or solve an equation such as $X^2 = A$.
The ring axioms hold because the product is [[associative|073E4XC016]] and [[distributive|0RXD6EZYBK]], so all the general theorems about rings apply at once.

The ring also shows exactly which rules of school algebra survive.
Sums behave as usual, but $AB$ can differ from $BA$, and $AB$ can be $0$ when neither factor is.
Later sub-areas return to $M_n(F)$ often: its units form the [[general linear group|0FCHE902D7]], the determinant is a map on it, and the theory of eigenvalues studies the subring of polynomials in one matrix.

## Notation

Books write $M_n(R)$, $\mathrm{M}_n(R)$, $\operatorname{Mat}_n(R)$ or $R^{n \times n}$.
When $M_n(F)$ is viewed with the bracket $[A, B] = AB - BA$ in place of the product, it is the Lie algebra $\mathfrak{gl}_n(F)$, a different structure on the same set.
In Mathlib, `Matrix (Fin n) (Fin n) R` is a `Ring` when `R` is a ring, and an `Algebra R _` when `R` is commutative; any finite type can replace `Fin n` as the index type.

## Remarks

### A first look at the ring of 2 by 2 matrices

Take $n = 2$ and $R = \mathbb{R}$.
The two [[matrix units|A4HTT7JFD1]] $E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $E_{21} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ already show the main features.
Multiply them in both orders:
$$E_{12} E_{21} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad E_{21} E_{12} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
So the ring is [[not commutative|0P506SPZP2]].
Now square $E_{12}$:
$$E_{12}^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = 0.$$
So $E_{12}$ is a [[zero divisor|0NNRDW10RZ]] and a nonzero [[nilpotent element|0ZB2JG1M9C]].
The same two matrices work for every $n \ge 2$ and every ring with $1 \ne 0$.
For $n = 1$, the [[1 by 1 matrices|WYJ95EEQFJ]] multiply like their entries, and $M_1(R)$ is a copy of $R$.

### More examples

The [[ring of 2 by 2 matrices over the field with two elements|DWKSAB7V4T]] is a finite ring with $2^4 = 16$ elements, and it already shows every feature above.
Inside $M_2(\mathbb{R})$, the matrices $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ form [[a copy of the complex numbers|GHV77C35RT]], a commutative subring that is even a field.
The ring $M_n(\mathbb{Z})$ of integer matrices is a matrix ring over a ring that is not a field, and its units are the integer matrices with determinant $1$ or $-1$.

### What it is not

The [[set of all matrices of all sizes|Q3FKC0FMXR]] is not a ring, because the sum of a $1 \times 1$ and a $2 \times 2$ matrix is not defined.
The $2 \times 3$ matrices form a group under addition, but two of them have no product, since a row of length $3$ cannot meet a column of length $2$.
Both fail the same condition: a ring needs a sum and a product for every pair of its elements, and only a fixed square size gives that.

### The center and the ideals

Which matrices commute with every matrix?
The [[center theorem|DVZ1V4A884]] answers: exactly the scalar matrices $cI$ with $c$ in the center of $R$.
So for a field $F$, the center of $M_n(F)$ is the copy $\{cI : c \in F\}$ of $F$, and the [[scalar matrix|067NKSBEWT]] page works this out.

The two-sided ideals are just as rigid.
Over a field, [[no two-sided ideal other than 0 and the whole ring exists|Z46WD9W1ZS]], so $M_n(F)$ is a [[simple ring|62M0NC3E2T]].
More generally, $M_n(R)$ is [[simple whenever R is simple|J41Y7CCE6B]].
For example, the matrices of trace $0$ are closed under addition, but they are not an ideal: $E_{12}$ has trace $0$, while $E_{21} E_{12} = E_{22}$ has trace $1$.

### The algebra structure and the units

Over a commutative ring $R$, the map $c \mapsto cI_n$ sends $R$ into the center, so $M_n(R)$ is an associative algebra over $R$.
Over a field $F$ it is an [[algebra over the field|1SENAHZW5A]] of dimension $n^2$, with the $n^2$ matrix units as a basis.
The units of the ring are the [[invertible matrices|0EB9N0S33C]], and they form the group $GL_n(R)$.

### Watch out

The ring is not commutative, so every rule that hides the order of factors needs care.
For example, $(A + B)^2 = A^2 + 2AB + B^2$ and $(AB)^2 = A^2 B^2$ both need $AB = BA$.
You cannot conclude $A = 0$ or $B = 0$ from $AB = 0$, as $E_{12} E_{12} = 0$ shows.
You also cannot conclude $A = \pm I$ from $A^2 = I$: the [[involutory matrix|NH2QE3671N]] $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has square $I$.

### History

Cayley's memoir on the theory of matrices of 1858 treated matrices as quantities that can be added and multiplied, and it observed that their product is not commutative.
Wedderburn proved in 1908 that every finite-dimensional simple algebra over a field is a matrix ring $M_n(D)$ over a division algebra $D$.

### Try it

First, find a matrix $A \ne 0$ in $M_2(\mathbb{R})$ with $A^2 = 0$, other than $E_{12}$.
One answer is $A = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$, since its square has entries $1 - 1 = 0$ in every position.

Second, show that $D = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ is not in the center of $M_2(\mathbb{R})$.
Multiplying by $E_{12}$ gives $D E_{12} = E_{12}$ but $E_{12} D = 2E_{12}$, so the two products differ.

## Explanations

### L1 human

Square matrices of one fixed size can be added and multiplied, and the answer is again a square matrix of that size.
They follow most of the rules of ordinary numbers, so you can do algebra with them.
There are two big differences.
First, $AB$ and $BA$ can be different.
Second, $AB$ can be the zero matrix even when $A$ and $B$ are not, as for $A = B = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

### L2 human

Here is a typical use: a polynomial equation for a matrix.
Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$.
Then
$$A^2 = \begin{pmatrix} 1 & 3 \\ 0 & 4 \end{pmatrix}, \qquad A^2 - 3A + 2I = \begin{pmatrix} 1 - 3 + 2 & 3 - 3 + 0 \\ 0 & 4 - 6 + 2 \end{pmatrix} = 0.$$
Since the ring has an identity and is associative, we may rearrange this as $A(3I - A) = 2I$, so $A^{-1} = \tfrac{1}{2}(3I - A) = \begin{pmatrix} 1 & -\tfrac{1}{2} \\ 0 & \tfrac{1}{2} \end{pmatrix}$.
Check: $A A^{-1}$ has first row $(1, -\tfrac{1}{2} + \tfrac{1}{2}) = (1, 0)$ and second row $(0, 1)$.
The polynomials in one matrix $A$ commute with each other, so this calculation takes place in a commutative subring of a noncommutative ring.
Watch out: the constant $2$ in the polynomial must become $2I$, not $2$ added to every entry.

### L3 human

For a commutative ring $R$, the ring $M_n(R)$ is the endomorphism ring of the free module $R^n$, and for a noncommutative $R$ the same holds with $R^n$ as a right module.
The ring $M_n(R)$ is [[Morita equivalent|JEBXXWHW8M]] to $R$, so the two rings have equivalent categories of modules, and their two-sided ideals correspond by $I \mapsto M_n(I)$.
The [[Amitsur-Levitzki theorem|YDH60KPTWT]] says that $M_n(R)$ satisfies the standard polynomial identity of degree $2n$ when $R$ is commutative.
The Wedderburn-Artin theorem makes matrix rings over division rings the building blocks of all semisimple rings, which is why they return throughout [[ring theory|0B1261B5ED]].
