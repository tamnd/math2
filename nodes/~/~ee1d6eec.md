---
tag: ~ee1d6eec
kind: concept
name: Weyr canonical form
aliases: [weyr-canonical-form, weyr-form, weyr-matrix]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: research
uses: [085HQ5G5TE, ~29b2bf0c, 0JV30XN73Z, 096AHMB3P4, 8G3X8MPG7E]
sources:
  - url: https://en.wikipedia.org/wiki/Weyr_canonical_form
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Weyr_canonical_form
    locator: Relation between Weyr and Jordan forms
  - url: https://en.wikipedia.org/wiki/Weyr_canonical_form
    locator: The Weyr form is canonical
  - book: isbn:9780199793730
---

## Summary

Let $F$ be a field and $\lambda \in F$.
Let $n_1 \ge \cdots \ge n_r \ge 1$ with $n_1 + \cdots + n_r = n$.
Cut an $n \times n$ matrix $W$ into an $r \times r$ block matrix $(W_{ij})$ with $W_{ij}$ of size $n_i \times n_j$.
Then $W$ is a *basic Weyr matrix* with eigenvalue $\lambda$ and *Weyr structure* $(n_1, \dots, n_r)$ if it has these three features:

1. $W_{ii} = \lambda I_{n_i}$ for $i = 1, \dots, r$;
2. $W_{i, i+1} = \begin{pmatrix} I_{n_{i+1}} \\ 0 \end{pmatrix}$, the $n_i \times n_{i+1}$ matrix with the identity on top and zero rows below, for $i = 1, \dots, r - 1$;
3. $W_{ij} = 0$ for $j \ne i, i + 1$.

A *Weyr matrix* is a block diagonal matrix $W_1 \oplus \cdots \oplus W_k$ of basic Weyr matrices with distinct eigenvalues.
If the characteristic polynomial of $A$ splits, $A$ is similar to a Weyr matrix, unique up to the order of the basic blocks: the *Weyr form* of $A$.
For each eigenvalue, the Weyr structure is the conjugate of the partition of [[Jordan block|07PH4RX0X5]] sizes, and $n_j = \dim \ker (A - \lambda I)^j - \dim \ker (A - \lambda I)^{j-1}$.

## Motivation

The Jordan form is good for powers and functions of one matrix, but it is bad for the matrices that commute with it.
For $J = J_3(0) \oplus J_1(0)$, the matrix $E_{43}$, with a single $1$ in position $(4, 3)$, commutes with $J$, and it lies below the diagonal.
In the Weyr form the [[commuting matrices|8G3X8MPG7E]] are block upper triangular, with the block sizes of the Weyr structure.
This makes the Weyr form the natural tool for problems about several commuting matrices.
The Jordan and Weyr forms carry the same information, and they differ by a permutation of the basis.

## Notation

The Weyr structure of $\lambda$ is also called the *Weyr characteristic* of $A$ at $\lambda$.
Write $\omega_j(A, \lambda) = \dim \ker (A - \lambda I)^j - \dim \ker (A - \lambda I)^{j-1}$, so the Weyr structure is $(\omega_1, \omega_2, \dots, \omega_r)$.
In the [[Young diagram|096AHMB3P4]] of the Jordan block sizes, with rows of the block sizes, the $\omega_j$ are the column lengths.
So the Jordan partition and the Weyr partition are conjugate [[integer partitions|0JV30XN73Z]], by part 5 of the [[normal form of nilpotent endomorphisms|~29b2bf0c]].

## Remarks

### Examples

- The [[basic Weyr matrix of structure $(2, 1, 1)$|~ee8d26ce]] is $E_{13} + E_{34}$, with Jordan form $J_3(0) \oplus J_1(0)$ and a block upper triangular centralizer of dimension $6$.
- The [[basic Weyr matrix of structure $(2, 2)$|~22d1f891]] is $\begin{pmatrix} 0 & I_2 \\ 0 & 0 \end{pmatrix}$, with Jordan form $J_2(0) \oplus J_2(0)$; its centralizer is the set of $\begin{pmatrix} X & Y \\ 0 & X \end{pmatrix}$.
- A Jordan block $J_n(\lambda)$ is a basic Weyr matrix of structure $(1, 1, \dots, 1)$; for a single Jordan block the two forms agree.
- A scalar matrix $\lambda I_n$ is a basic Weyr matrix of structure $(n)$.

### Non-examples

- The [[Jordan matrix $J_2(0) \oplus J_2(0)$|~f756a308]] is not a Weyr matrix: its Weyr structure is $(2, 2)$, but its upper left $2 \times 2$ block is $J_2(0)$, not $0 \cdot I_2$.
- $E_{12} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ is not a Weyr matrix. Its Weyr structure is $(2, 1)$, so its upper left $2 \times 2$ block would have to be $0$, but it has the entry $1$ in position $(1, 2)$. Its Weyr form is $E_{13}$.

### Basic properties

- *Existence and uniqueness.* Over an algebraically closed field, every square matrix is similar to a Weyr matrix, unique up to the order of the basic blocks. The same holds over any field when the characteristic polynomial splits, because the proof reduces to the Jordan form.
- *Relation to the Jordan form.* A permutation of the basis turns the Jordan form into the Weyr form. In a basic block, take the first basis vector of each Weyr subblock, from the last subblock to the first. These vectors form the longest Jordan chain. Remove them and repeat to get the next chain.
- *Centralizers.* If $W$ is a basic Weyr matrix of structure $(n_1, \dots, n_r)$, every matrix that commutes with $W$ is block upper triangular for the same block sizes. More precisely, its diagonal blocks are determined by the first one, and its block $(i, j)$ is $0$ for $i > j$.
- The dimension of the centralizer is $\sum_j \omega_j^2$, the sum of the squares of the Weyr structure, for a single eigenvalue.

### History

The Weyr form was found by the Czech mathematician Eduard Weyr in 1885.
O'Meara, Clark and Vinsonhaler wrote a book on the form and its uses for commuting matrices, published by Oxford University Press in 2011.

### Common errors

- Confusing the Weyr structure with the Jordan partition. For $J_3 \oplus J_1$ the Jordan partition is $(3, 1)$ and the Weyr structure is $(2, 1, 1)$.
- Placing the identity of $W_{i, i+1}$ at the bottom of the block; it is at the top, with zero rows below.
- Expecting the centralizer of a Jordan matrix to be block upper triangular in the Jordan basis; this holds in the Weyr basis.

## Explanations

### L1 human

The Weyr form is another way to write a matrix in a simple standard shape.
It has the same information as the Jordan form, but the basis vectors are put in a different order.
With this order, all the matrices that commute with the given one have a simple triangular shape.

### L2 human

Take $N = J_3(0) \oplus J_1(0)$, with kernel dimensions $2, 3, 4$ of its powers.

1. The jumps are $2, 1, 1$, so the Weyr structure is $(2, 1, 1)$.
2. The Jordan chains are $e_3 \mapsto e_2 \mapsto e_1 \mapsto 0$ and $e_4 \mapsto 0$.
3. Order the basis by height: first the eigenvectors $e_1, e_4$, then $e_2$, then $e_3$.
4. In the basis $e_1, e_4, e_2, e_3$ the matrix of $N$ is $E_{13} + E_{34}$, the basic Weyr matrix of structure $(2, 1, 1)$.

The trap is the order inside the first group: the eigenvector of the longest chain comes first.

### L3 human

The Weyr basis orders the vectors by their height in the filtration $\ker N \subseteq \ker N^2 \subseteq \cdots$.
This is why centralizers become block upper triangular: a matrix that commutes with $N$ preserves each $\ker N^j$.
Uses include Gerstenhaber's theorem that two commuting $n \times n$ matrices generate an algebra of dimension at most $n$, approximate simultaneous diagonalization, and the irreducibility of varieties of commuting tuples.
