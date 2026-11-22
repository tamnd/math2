---
tag: H3E52HTEZ2
kind: concept
name: Classification of matrices up to similarity
aliases: [classification-of-matrices-up-to-similarity, similarity-problem]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
uses: [027KDW2K72, F7GJPMVBXA, 042JWAR3Q0, R5X8SNHBGG, TXMV0YDACG, 92VZF0QRM8, 085HQ5G5TE, RE9YFFS3TS, TXVWFWP6VQ]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_similarity
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Wild_problem
    locator: Mathematics
  - url: https://en.wikipedia.org/wiki/Frobenius_normal_form
  - book: isbn:9780471433347
    locator: Section 12.2
---

## Summary

When do two square matrices describe the same linear map in different bases?
Over a field this question has a complete answer: a short list of polynomials, the invariant factors, decides it, and each class has one standard matrix.
The same question for two matrices at once has no such answer, and it is the standard example of a hopeless classification problem.

Let $F$ be a field.
Two matrices $A, B \in M_n(F)$ are [[similar|027KDW2K72]] when $B = P^{-1} A P$ for some invertible $P \in M_n(F)$.
The *similarity problem* asks for invariants that decide similarity and for one normal form in each class.
Over a field it is solved by the theorem
$$A \sim B \iff A \text{ and } B \text{ have the same invariant factors},$$
and each class contains exactly one [[rational canonical form|042JWAR3Q0]], a block diagonal matrix of companion matrices.

## Motivation

A linear map $T \colon V \to V$ has a different matrix in each basis of $V$, and two matrices of $T$ are always similar.
So the similarity class of a matrix is exactly the information in $T$ that does not depend on a basis.
To classify matrices up to similarity is to know which properties of a linear map can be read from one standard matrix.

The answer over a field is one of the first great uses of module theory.
A matrix makes $F^n$ into a module over the polynomial ring $F[x]$, and modules over this ring have a structure theorem.
The same method fails for pairs of matrices, and that failure marks where classification by normal forms stops being possible.

The answer is used across the sub-area.
The [[Jordan normal form|085HQ5G5TE]] is the version for split characteristic polynomials, the [[centralizer theorem|GXZGWZSJ2J]] measures the size of a class, and the [[conjugacy classes of GL_n over a finite field|4FV9TDGWWH]] are counted with it.

## Notation

We write $A \sim B$ for similarity.
The group $GL_n(F)$ acts on $M_n(F)$ by $P \cdot A = P A P^{-1}$, and the similarity classes are the orbits of this action.
For pairs, $(A, B) \sim (A', B')$ means that one matrix $P$ gives both $A' = P A P^{-1}$ and $B' = P B P^{-1}$; this is *simultaneous similarity*.

## Remarks

### Why invariant factors solve it

Make $F^n$ into an $F[x]$-module $F^n_A$, with $x$ acting as $A$.
By the [[module form of similarity|R5X8SNHBGG]], $A \sim B$ holds exactly when $F^n_A \cong F^n_B$ as modules.
The ring $F[x]$ is a principal ideal domain, so the [[structure theorem|TXMV0YDACG]] writes each such module as $F[x]/(d_1) \oplus \cdots \oplus F[x]/(d_r)$ with $d_1 \mid \cdots \mid d_r$ monic and nonconstant, and the list of the $d_i$ is unique.
These $d_i$ are the [[invariant factors|F7GJPMVBXA]] of $A$, and the companion matrices of the $d_i$, placed on the diagonal, give the rational canonical form.

The invariants are computable.
They are the nonconstant diagonal entries of the [[Smith normal form of xI − A|92VZF0QRM8]], and they are quotients of gcds of minors of $xI - A$.
Since gcds of polynomials do not change when the field grows, the answer [[does not depend on the field|5PVFX89NM7]].

### Small cases worked out

For $2 \times 2$ matrices the answer is short, as the [[similarity classes of 2 × 2 matrices|H6R274A93F]] show.
A scalar matrix is alone in its class, and two nonscalar matrices are similar exactly when they have the same trace and determinant.
For example, $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ has trace $5$ and determinant $-2$, so it is similar to the companion matrix $\begin{pmatrix} 0 & 2 \\ 1 & 5 \end{pmatrix}$, which has the same trace and determinant.

For nilpotent matrices the classes match partitions.
The [[five similarity classes of nilpotent 4 × 4 matrices|WT7V4ACJWF]] belong to the five partitions $(4)$, $(3, 1)$, $(2, 2)$, $(2, 1, 1)$ and $(1, 1, 1, 1)$, and the ranks of $N, N^2, N^3$ separate them.
Over a finite field $\mathbb{F}_q$, the classes of invertible matrices can be counted, and $GL_2(\mathbb{F}_q)$ has $q^2 - 1$ of them by the [[class count for GL_n|4FV9TDGWWH]].

### Invariants that are not enough

Many numbers are preserved by similarity: the characteristic polynomial, the minimal polynomial, the rank, the trace and the determinant.
None of these, alone or together, decides similarity in general.
The [[two nilpotent 7 × 7 matrices|PQR08Q9529]] $J_3(0) \oplus J_3(0) \oplus J_1(0)$ and $J_3(0) \oplus J_2(0) \oplus J_2(0)$ agree in characteristic polynomial, minimal polynomial and rank, but their squares have ranks $2$ and $1$.

In size at most $3$ the two polynomials do decide similarity, because the invariant factors $d_1 \mid \cdots \mid d_r$ have $d_r = \mu_A$ and product $\chi_A$, and in size $3$ this leaves only one choice.
In size $4$ they already fail: $J_2(0) \oplus J_2(0)$ and $J_2(0) \oplus J_1(0) \oplus J_1(0)$ both have $\chi = x^4$ and $\mu = x^2$, but their invariant factors are $x^2, x^2$ and $x, x, x^2$.
[[Invariant factors separate two such matrices|1K0AP4D1S2]] in general.

### Neighbors of similarity

*Equivalence*, $A \mapsto QAP$ with two independent invertible matrices, is a coarser relation.
Its classes are decided by the rank alone, by the [[rank normal form|T2H2QV0M06]], so for example $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ are equivalent but not similar.

Simultaneous similarity of pairs is much finer, and it is not decided by the invariant factors of each matrix.
With the matrix units of $M_2(F)$, we have $E_{11} \sim E_{11}$ and $E_{11} \sim E_{22}$.
But $(E_{11}, E_{11}) \not\sim (E_{11}, E_{22})$, because $PAP^{-1} \cdot PBP^{-1} = P(AB)P^{-1}$, and $E_{11} E_{11} = E_{11} \ne 0$ while $E_{11} E_{22} = 0$.

### Tame and wild problems

A single matrix up to similarity is a [[representation|TXVWFWP6VQ]] of the [[quiver|RE9YFFS3TS]] with one vertex and one loop.
Over an algebraically closed field its indecomposable representations are the Jordan blocks $J_k(\lambda)$, one family with a single parameter $\lambda$ for each size $k$, and such a problem is called *tame*.
A pair of matrices up to simultaneous similarity is a representation of the quiver with one vertex and two loops.
A classification problem is called *wild* when it contains the problem of pairs, and the problem of pairs is wild in this sense.
Over an algebraically closed field, the representation problem of a connected quiver is wild exactly when the quiver is neither of Dynkin nor of Euclidean type, and the two-loop quiver is of this kind.

### Watch out

The first trap is to decide similarity from the characteristic and minimal polynomials, which fails from size $4$ on, as above.
The second trap is to use the Jordan form over a field where $\chi_A$ does not split.
The quarter turn $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has $\chi = x^2 + 1$ and [[no real Jordan form|PFZF3KRBBB]], while its rational canonical form over $\mathbb{R}$ is the companion matrix of $x^2 + 1$.
The third trap is to treat a pair $(A, B)$ as two separate problems, as the matrix units above show.

### History

Camille Jordan published his normal form in 1870.
Eduard Weyr found a different normal form for the split case, now called the [[Weyr form|9XEA4VR8WP]], in 1885.

### Try it

First, decide whether $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ and $\begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}$ are similar.
Both are nonscalar with trace $4$ and determinant $4$, so they are similar.

Second, decide whether $2 I_2$ and $\begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ are similar.
They have the same trace and determinant, but a scalar matrix is similar only to itself, so they are not.

## Explanations

### L1 human

Two square matrices are similar when they describe the same move of space, written in two different coordinate systems.
For one matrix at a time, a short list of polynomials decides the question completely.
For $2 \times 2$ matrices it is even simpler: apart from multiples of the identity, two matrices are similar exactly when their traces agree and their determinants agree.
So $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, with trace $5$ and determinant $-2$, is similar to every other non-scalar matrix with those two numbers.
For two matrices at the same time, no such list is known, and the problem is called wild.

### L2 human

Here is a typical use: are $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ similar over $\mathbb{Q}$?
Both have $\chi = (x - 1)^3$.
The matrices $A - I = E_{12}$ and $B - I = E_{13}$ both have rank $1$ and square $0$, so both minimal polynomials are $(x - 1)^2$.
In size $3$ the invariant factors are then fixed: $d_2 = \mu = (x - 1)^2$ and $d_1 = \chi / \mu = x - 1$.
So $A$ and $B$ have the same invariant factors $x - 1, (x - 1)^2$, and they are similar; the permutation matrix that swaps $e_2$ and $e_3$ conjugates one into the other.
The method is the same in every size: compute the invariant factors, for example from the Smith normal form of $xI - A$, and compare the lists.
The trap is to stop at the characteristic polynomial, which is only the product $d_1 \cdots d_r$.

### L3 human

The similarity problem over a field is the classification of finitely generated torsion modules over the principal ideal domain $F[x]$.
A pair of matrices gives a module over the free algebra $F\langle x, y \rangle$, which is not a principal ideal domain, and no structure theorem of the same kind applies.
In representation theory, one loop gives a tame problem and two loops give a wild one.
The [[structure theorem over a principal ideal domain|TXMV0YDACG]] and the representation theory of [[quivers|RE9YFFS3TS]] treat these ideas in full.
