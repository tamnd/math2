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

Let $F$ be a field.
Two matrices $A, B \in M_n(F)$ are [[similar|027KDW2K72]] if $B = P^{-1} A P$ for some invertible $P \in M_n(F)$.
The similarity problem asks for a list of invariants that decides similarity, and for one normal form in each class.
Over a field this problem is solved: $A$ and $B$ are similar if and only if they have the same [[invariant factors|F7GJPMVBXA]].
Each class contains exactly one [[rational canonical form|042JWAR3Q0]], a block diagonal matrix of companion matrices.
The invariant factors are computable with gcds of polynomials, and they do not change when the field is enlarged.
The problem for pairs of matrices up to simultaneous similarity is of a different nature.
It is the standard *wild* problem, and no comparable list of normal forms is known.

## Motivation

Similar matrices describe the same linear map $T \colon V \to V$ in two bases.
So the similarity class of a matrix is exactly the information in the map $T$ that does not depend on a basis.
A solution of the similarity problem tells which properties of $T$ can be read from one standard matrix.
The solution over a field is one of the main successes of the module theory of principal ideal domains.
The failure of the same method for pairs of matrices shows where this success ends.

## Notation

Write $A \sim B$ for similarity.
The group $GL_n(F)$ acts on $M_n(F)$ by $P \cdot A = P A P^{-1}$, and the similarity classes are the orbits of this action.
For a pair, $(A, B) \sim (A', B')$ means that one $P$ gives both $A' = P A P^{-1}$ and $B' = P B P^{-1}$.

## Remarks

### Examples

- The [[similarity classes of $2 \times 2$ matrices|H6R274A93F]]. Each class contains one scalar matrix or one companion matrix $C(x^2 + bx + c)$. Nonscalar matrices are similar exactly when they have the same trace and determinant.
- The [[five similarity classes of nilpotent $4 \times 4$ matrices|WT7V4ACJWF]] correspond to the five partitions of $4$, and the ranks of $N, N^2, N^3$ separate them.
- [[Invariant factors separate two matrices with the same characteristic and minimal polynomials|1K0AP4D1S2]].
- Over a finite field $\mathbb{F}_q$, the classes in $GL_n(\mathbb{F}_q)$ correspond to rational canonical forms, and there are [[$q^2 - 1$ classes in $GL_2(\mathbb{F}_q)$|4FV9TDGWWH]].

### Non-examples

- The [[characteristic polynomial, minimal polynomial and rank|PQR08Q9529]] do not classify: $J_3(0) \oplus J_3(0) \oplus J_1(0)$ and $J_3(0) \oplus J_2(0) \oplus J_2(0)$ agree in all three and are not similar.
- Equivalence $A \mapsto Q A P$ with two independent invertible matrices is a different and coarser relation. Its classes are decided by the rank alone, by the [[rank normal form|T2H2QV0M06]].
- Simultaneous similarity of pairs is not solved by invariant factors of each matrix separately. With $E_{ij}$ the matrix units in $M_2(F)$, $E_{11} \sim E_{11}$ and $E_{11} \sim E_{22}$, but $(E_{11}, E_{11}) \not\sim (E_{11}, E_{22})$, because $P A P^{-1} \cdot P B P^{-1} = P (AB) P^{-1}$ and $E_{11} E_{11} \ne 0 = E_{11} E_{22}$.

### Basic properties

- *Why invariant factors solve it.* Make $F^n$ an $F[x]$-module $F^n_A$ with $x$ acting as $A$. Then $A \sim B$ if and only if $F^n_A \cong F^n_B$, by the [[module form of similarity|R5X8SNHBGG]]. Since $F[x]$ is a principal ideal domain, the [[structure theorem|TXMV0YDACG]] classifies these torsion modules by their invariant factors.
- *Computation.* The invariant factors are the nonconstant diagonal entries of the [[Smith normal form of $xI - A$|92VZF0QRM8]]. They are quotients of gcds of minors, so they lie in $F[x]$ and [[do not depend on the field|5PVFX89NM7]].
- *Jordan form.* When $\chi_A$ splits over $F$, the [[Jordan normal form|085HQ5G5TE]] is a second normal form. Its data are the numbers $\dim \ker (A - \lambda I)^k$ for all eigenvalues $\lambda$ and all $k$.
- *Transpose.* Every matrix is [[similar to its transpose|C708QKZPE6]], so the classification does not distinguish $A$ from $A^{\mathsf T}$.
- *Pairs and quivers.* A pair $(A, B)$ up to simultaneous similarity is a [[representation|TXVWFWP6VQ]] of the [[quiver|RE9YFFS3TS]] with one vertex and two loops. A single matrix up to similarity is a representation of the quiver with one vertex and one loop. Over an algebraically closed field the indecomposable representations of the one-loop quiver are the Jordan blocks $J_k(\lambda)$.
- *Wild problems.* A classification problem is called wild if it contains the problem of pairs of matrices up to simultaneous similarity. Classifying the indecomposable representations of a quiver that is neither Dynkin nor Euclidean is wild. The two-loop quiver is of this kind.

### History

Camille Jordan published his normal form in 1870.
Eduard Weyr found a dual normal form, now called the [[Weyr form|9XEA4VR8WP]], in 1885.

### Common errors

- Deciding similarity from the characteristic polynomial and the minimal polynomial. For $n \le 3$ they decide it, but for $n \ge 4$ they do not, as $J_2(0) \oplus J_2(0)$ and $J_2(0) \oplus J_1(0) \oplus J_1(0)$ show.
- Using the Jordan form over a field where $\chi_A$ does not split. A [[real matrix can have no real Jordan form|PFZF3KRBBB]]; the rational canonical form works over every field.
- Treating a pair $(A, B)$ as two separate similarity problems, as in the third non-example.

## Explanations

### L1 human

Two square matrices are similar when they describe the same linear map in two different bases.
For one matrix at a time, a short list of polynomials, the invariant factors, decides this question completely.
For two matrices at the same time, no such list is known, and the problem is called wild.

### L2 human

To decide whether $A$ and $B$ are similar, compute the invariant factors of both.

1. Find the Smith normal form of $xI - A$ and of $xI - B$, or the gcds of their $k \times k$ minors.
2. Read off the nonconstant diagonal entries $d_1 \mid \cdots \mid d_r$.
3. $A \sim B$ if and only if the two lists are equal.

The trap is to stop at the characteristic polynomial, which is only the product $d_1 \cdots d_r$.

### L3 human

The similarity problem is the classification of finitely generated torsion modules over the principal ideal domain $F[x]$.
A pair of matrices gives a module over the free algebra $F\langle x, y \rangle$, which is not a principal ideal domain, and no structure theorem applies.
In the language of representation theory, one loop gives a tame problem, with a one-parameter family $J_k(\lambda)$ of indecomposables for each $k$.
Two loops give a wild problem.
The other areas cover the module theory of principal ideal domains, the Smith normal form, and the representation theory of quivers in full.
