---
tag: 0E89HQATM8
kind: concept
name: Similar matrices
aliases: [conjugate-matrices]
msc: ["15A21"]
topics: [S6559D61BP]
audience: ug1
uses: [0VD9ZSWWJG, 0EB9N0S33C, 0YQSGNYE3K, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section4-3.xml#L1057
    locator: src/section4-3.xml:1057
  - book: isbn:9780134860244
    locator: Section 2.5
same_as:
  wikidata: Q254491
  wikipedia: Matrix similarity
---

## Summary

Two square matrices are similar when they describe the same linear map in two different bases.
Similarity is the right notion of "the same" for matrices of [[endomorphisms|0J7H0YBFDJ]], because a change of basis changes the matrix but not the map.
Precisely, two $n \times n$ [[matrices|0VD9ZSWWJG]] $A$ and $B$ over a field $F$ are *similar* when there is an [[invertible matrix|0EB9N0S33C]] $P$ over $F$ with
$$B = P^{-1} A P.$$
Equivalently, $A$ and $B$ are the [[matrices|0YQSGNYE3K]] of one endomorphism of $F^n$ in two bases, and $P$ is the change of basis matrix between them.
The [[formal definition|027KDW2K72]] states this, and similarity is an [[equivalence relation|HWKZ8DM8P0]] on $M_n(F)$.

## Motivation

An endomorphism $T$ of $V$ has one matrix for each basis of $V$, and the [[change of basis formula|0MQXVZEBMT]] says that these matrices are $P^{-1}[T]_B P$.
So a property of the map $T$ itself must be a property that all these matrices share.
This turns a question about maps into a question about matrices: which numbers stay the same under $A \mapsto P^{-1}AP$?
The rank, the trace, the determinant and the characteristic and minimal polynomials do, as the [[theorem on similarity invariants|191HBJ7PVZ]] shows.

The second question is how to choose a basis that makes the matrix simple.
A diagonal matrix is the best case, and finding $P$ with $P^{-1}AP$ diagonal is the problem of diagonalization in the sub-area on [[eigenvalues|6R1D6QPY3S]].
When no diagonal matrix is similar to $A$, the Jordan and rational canonical forms give the next best choice.
Similar matrices are also easier to compute with: if $A = PDP^{-1}$ with $D$ diagonal, then $A^k = PD^kP^{-1}$.

## Notation

We write $A \sim B$ when the meaning is clear, but the same symbol also stands for row equivalence in some books.
Some books write $B = PAP^{-1}$ in place of $B = P^{-1}AP$.
The two forms define the same relation, since one becomes the other when $P$ is replaced by $P^{-1}$.
The set of matrices similar to $A$ is the *similarity class*, or conjugacy class, of $A$.

## Remarks

### A first example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ and $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, so that $P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$.
Multiply out, first on the right and then on the left:
$$AP = \begin{pmatrix} 1 & 2 \\ 0 & 2 \end{pmatrix}, \qquad P^{-1}AP = \begin{pmatrix} 1 - 0 & 2 - 2 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}.$$
So $A$ is [[similar to a diagonal matrix|X1CZSG8JEC]].
The reason is visible in the columns of $P$: $A(1, 0) = (1, 0)$ and $A(1, 1) = (2, 2)$, so in the basis $(1, 0)$, $(1, 1)$ the map only stretches by $1$ and by $2$.
Check: $\operatorname{tr} A = 3 = 1 + 2$ and $\det A = 2 = 1 \cdot 2$, as the invariants require.

### Two matrices that look different

The rotations $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ and $S = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ turn the plane a quarter turn in opposite directions.
With the reflection $P = \operatorname{diag}(1, -1)$, which is its own inverse, a short product gives $P^{-1}RP = S$.
So the [[two quarter turns are similar|XPAX5P9NNC]]: a quarter turn to the left looks like a quarter turn to the right in a mirror.
A scalar matrix is the other extreme, since $P^{-1}(cI)P = cI$ for every invertible $P$, so $cI$ is similar only to itself.

### What it is not

The [[Jordan block and the identity|62XEH0NYE1]] share the trace $2$, the determinant $1$ and the characteristic polynomial $(x - 1)^2$.
They are not similar, because only $I_2$ is similar to $I_2$.
Even rank, trace, determinant and both polynomials together do not decide similarity, as [[two 4 by 4 matrices built from Jordan blocks|J4Q3B9ZNHF]] show.
The relation $B = QAP$ with two unrelated invertible matrices is matrix equivalence, which is weaker: the [[equivalent matrices that are not similar|6CKAMR5WK9]] share only the rank.
Matrices of different sizes are never similar, since $P^{-1}AP$ needs one size $n$.

### The rules you can use

Similarity is reflexive, symmetric and transitive, by the [[theorem on the equivalence relation|HWKZ8DM8P0]].
Similarity respects the algebra of one matrix: if $B = P^{-1}AP$, then $B^2 = P^{-1}APP^{-1}AP = P^{-1}A^2P$, and by induction $B^k = P^{-1}A^kP$.
Adding these gives $q(B) = P^{-1}q(A)P$ for every polynomial $q$, so $q(A) = 0$ exactly when $q(B) = 0$.
If $A$ is invertible, then so is $B$, and $B^{-1} = P^{-1}A^{-1}P$.

### Watch out

The most common error is to believe that equal invariants make two matrices similar.
The Jordan block $J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $I_2$ fail this, as above; the extra invariant that separates them is the rank of $J - I$, which is $1$ for $J$ and $0$ for $I_2$.
A second error is to use $P^{-1}AQ$ with $Q \ne P$, which is equivalence and not similarity.
A third is to mix $P^{-1}AP$ and $PAP^{-1}$ in one computation, which applies the change of basis in opposite directions.

### History

Camille Jordan described the normal form that now bears his name in his treatise on substitutions of 1870.
The normal form picks one simple matrix from each similarity class over the complex numbers.

### Try it

First, show that $\operatorname{diag}(2, 3)$ and $\operatorname{diag}(3, 2)$ are similar.
Take $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, which is its own inverse; then $P \operatorname{diag}(2, 3) P$ swaps both the rows and the columns and gives $\operatorname{diag}(3, 2)$.

Second, are $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $\begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$ similar?
No: both have trace $2$, but the determinants are $1$ and $0$, and similar matrices have the same determinant.

## Explanations

### L1 human

Two matrices are similar when one turns into the other by a change of basis.
They describe the same motion of space, written down from two points of view.
For example, the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ looks complicated, but along the directions $(1, 0)$ and $(1, 1)$ it only stretches by $1$ and by $2$.
So it is similar to the diagonal matrix with entries $1$ and $2$.
Similar matrices share every number that belongs to the motion itself, such as the trace and the determinant.

### L2 human

Here is a typical use: compute every power of $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$.
From the first example, $A = PDP^{-1}$ with $D = \operatorname{diag}(1, 2)$, so $A^k = PD^kP^{-1}$, because the inner factors $P^{-1}P$ cancel.
Multiply out:
$$A^k = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 2^k \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2^k \\ 0 & 2^k \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2^k - 1 \\ 0 & 2^k \end{pmatrix}.$$
Check with $k = 2$: directly $A^2 = \begin{pmatrix} 1 & 3 \\ 0 & 4 \end{pmatrix}$, and the formula gives the same.
So a similar diagonal matrix turns a hard computation into powers of numbers.
Watch out: the factor order matters, and $P^{-1}D^kP$ gives a different and wrong matrix.

### L3 human

The group $GL_n(F)$ acts on $M_n(F)$ by conjugation, and the similarity classes are the orbits of this action.
Over any field, two matrices are similar exactly when they have the same rational canonical form, or equivalently the same invariant factors.
Over an algebraically closed field, the Jordan normal form gives a representative of each class.
A consequence of the rational form is that similarity does not change under a field extension: two matrices over $F$ that are similar over a larger field are already similar over $F$.
In group theory the same relation is conjugacy, and for linear maps $S \colon V \to V$ and $T \colon W \to W$ it becomes $T = \phi S \phi^{-1}$ for an isomorphism $\phi \colon V \to W$.
