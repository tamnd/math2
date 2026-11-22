---
tag: 9XEA4VR8WP
kind: concept
name: Weyr canonical form
aliases: [weyr-canonical-form, weyr-form, weyr-matrix]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: research
uses: [085HQ5G5TE, Z2RTKWZZAZ, 0JV30XN73Z, 096AHMB3P4, 8G3X8MPG7E]
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

The Weyr form is the Jordan form with its basis vectors put in a different order.
The Jordan form keeps each chain of vectors together, and the Weyr form groups the vectors by their height instead: first all the eigenvectors, then all the vectors one step above them, and so on.
The two forms carry the same information, but in the Weyr order every matrix that commutes with the given one becomes block upper triangular.

Here is the exact definition.
Let $F$ be a field, let $\lambda \in F$, and let $n_1 \ge n_2 \ge \cdots \ge n_r \ge 1$ be integers with $n_1 + \cdots + n_r = n$.
Cut an $n \times n$ matrix $W$ into an $r \times r$ block matrix $(W_{ij})$, where $W_{ij}$ has size $n_i \times n_j$.
Then $W$ is a *basic Weyr matrix* with eigenvalue $\lambda$ and *Weyr structure* $(n_1, \dots, n_r)$ when it has these three features:

1. $W_{ii} = \lambda I_{n_i}$ for $i = 1, \dots, r$.
2. $W_{i, i+1} = \begin{pmatrix} I_{n_{i+1}} \\ 0 \end{pmatrix}$ for $i = 1, \dots, r - 1$, the $n_i \times n_{i+1}$ matrix with the identity on top and zero rows below.
3. $W_{ij} = 0$ for every other pair $(i, j)$.

A *Weyr matrix* is a block diagonal matrix $W_1 \oplus \cdots \oplus W_k$ of basic Weyr matrices with distinct eigenvalues.
When the characteristic polynomial of $A \in M_n(F)$ splits over $F$, the matrix $A$ is similar to a Weyr matrix, unique up to the order of the basic blocks, and this matrix is the *Weyr form* of $A$.
For each eigenvalue $\lambda$ of $A$ the Weyr structure is read from kernels:
$$n_j = \dim \ker (A - \lambda I)^j - \dim \ker (A - \lambda I)^{j-1}.$$

## Motivation

The [[Jordan normal form|085HQ5G5TE]] is the right tool for powers and functions of one matrix.
It is a poor tool for the [[matrices that commute with it|8G3X8MPG7E]].
Take $J = J_3(0) \oplus J_1(0) = E_{12} + E_{23}$, where $E_{ij}$ is the matrix with a single $1$ in position $(i, j)$.
The matrix $E_{43}$ commutes with $J$, because both products vanish:
$$J E_{43} = E_{12} E_{43} + E_{23} E_{43} = 0, \qquad E_{43} J = E_{43} E_{12} + E_{43} E_{23} = 0.$$
So the centralizer of a Jordan matrix can have entries below the diagonal, and its shape is hard to describe.

After the Weyr reordering of the basis, every commuting matrix is block upper triangular, with the block sizes of the Weyr structure.
Problems about several commuting matrices, such as finding a basis that makes them all nearly triangular, become problems about such block matrices.
This is why the Weyr form is the main tool in the study of commuting matrices, while the Jordan form remains the standard one for a single matrix.

## Notation

The Weyr structure at $\lambda$ is also called the *Weyr characteristic* of $A$ at $\lambda$, and some books write it as $\omega_j(A, \lambda) = \dim \ker (A - \lambda I)^j - \dim \ker (A - \lambda I)^{j-1}$.
Draw the [[Young diagram|096AHMB3P4]] of the Jordan block sizes at $\lambda$, with one row for each block.
Then the $\omega_j$ are the lengths of the columns of that diagram.
So the Jordan partition and the Weyr partition are conjugate [[integer partitions|0JV30XN73Z]], by the [[normal form of nilpotent endomorphisms|Z2RTKWZZAZ]].

## Remarks

### From Jordan to Weyr on one matrix

Start with $N = J_3(0) \oplus J_1(0)$ on $F^4$.
Its powers have kernels of dimension $2, 3, 4$, so the jumps are $2, 1, 1$ and the Weyr structure is $(2, 1, 1)$.
The Jordan partition is $(3, 1)$, and its conjugate is indeed $(2, 1, 1)$.

The Jordan chains are $e_3 \mapsto e_2 \mapsto e_1 \mapsto 0$ and $e_4 \mapsto 0$.
Order the basis by height: first the eigenvectors $e_1, e_4$, then $e_2$, then $e_3$.
In the new basis $f_1 = e_1$, $f_2 = e_4$, $f_3 = e_2$, $f_4 = e_3$ we get
$$N f_1 = 0, \quad N f_2 = 0, \quad N f_3 = f_1, \quad N f_4 = f_3,$$
so the matrix of $N$ is $E_{13} + E_{34}$.
This is the [[basic Weyr matrix of structure (2, 1, 1)|H568T13KR4]].
Check: its block $W_{12}$ in rows $1, 2$ and column $3$ is $(1, 0)^{\mathsf T}$, the identity on top and a zero row below.

### More examples

The [[basic Weyr matrix of structure (2, 2)|1MN49GY0GV]] is $\begin{pmatrix} 0 & I_2 \\ 0 & 0 \end{pmatrix}$, and its Jordan form is $J_2(0) \oplus J_2(0)$.
Its centralizer is the set of block matrices $\begin{pmatrix} X & Y \\ 0 & X \end{pmatrix}$.

Two families are Jordan and Weyr matrices at once.
A single Jordan block $J_n(\lambda)$ has Weyr structure $(1, 1, \dots, 1)$, and it is its own Weyr form.
A scalar matrix $\lambda I_n$ has Weyr structure $(n)$, and it is a basic Weyr matrix with one block.

### What is not a Weyr matrix

The [[Jordan matrix J₂(0) ⊕ J₂(0)|Y64E6EXGY5]] has Weyr structure $(2, 2)$.
A Weyr matrix of that structure has the zero block in rows and columns $1, 2$, but here that block is $J_2(0) \ne 0$, so the matrix is not in Weyr form.

In the same way, the $3 \times 3$ matrix $E_{12}$ has rank $1$, so its kernels have dimension $2, 3$ and its Weyr structure is $(2, 1)$.
Its upper left $2 \times 2$ block contains the entry $1$ in position $(1, 2)$, so it is not a Weyr matrix.
Its Weyr form is $E_{13}$, which has the column $(1, 0)^{\mathsf T}$ in rows $1, 2$ of column $3$.

### The rules you can use

Existence and uniqueness come from the Jordan form.
When the characteristic polynomial splits, a permutation of a Jordan basis gives a Weyr basis, and the Weyr structure is fixed by the kernel dimensions, so the Weyr form is unique up to the order of the basic blocks.

The permutation also runs backwards.
In a basic Weyr block, take the first basis vector of each group, from the last group to the first.
The matrix $W - \lambda I$ sends each of these vectors to the one before, so they form the longest Jordan chain.
Remove them and repeat with the second vectors of the groups that have one.

For centralizers, let $W$ be a basic Weyr matrix of structure $(n_1, \dots, n_r)$ and let $X$ commute with $W$.
Then $X$ is block upper triangular for the same block sizes, and each diagonal block $X_{i+1, i+1}$ is the upper left $n_{i+1} \times n_{i+1}$ corner of $X_{ii}$.
The dimension of the centralizer of $W$ is $n_1^2 + \cdots + n_r^2$, which agrees with the general [[centralizer dimension formula|GXZGWZSJ2J]].
For the structure $(2, 1, 1)$ this gives $4 + 1 + 1 = 6$.

### Watch out

The first trap is to confuse the two partitions.
For $J_3(0) \oplus J_1(0)$ the Jordan partition is $(3, 1)$ but the Weyr structure is $(2, 1, 1)$, so a Weyr matrix with blocks of sizes $3, 1$ would be wrong.

The second trap is the order of the vectors inside the first group.
In the example above, the order $e_4, e_1, e_2, e_3$ gives the matrix $E_{23} + E_{34}$, whose block $W_{12}$ is $(0, 1)^{\mathsf T}$.
The identity must sit on top, so the eigenvector at the bottom of the longest chain comes first.

The third trap is to expect a triangular centralizer in the Jordan basis.
The matrix $E_{43}$ of the Motivation shows that this fails.

### History

The Czech mathematician Eduard Weyr found the form in 1885.
O'Meara, Clark and Vinsonhaler wrote a book, published in 2011, that develops the form and uses it for problems about commuting matrices.

### Try it

First, find the Weyr structure of $J_3(0) \oplus J_2(0)$.
The kernels of its powers have dimensions $2, 4, 5$, so the jumps give $(2, 2, 1)$, the conjugate of $(3, 2)$.

Second, find the Weyr form of $J_2(0) \oplus J_1(0) \oplus J_1(0)$.
The Weyr structure is $(3, 1)$, so the Weyr form is the $4 \times 4$ matrix $E_{14}$, with the column $(1, 0, 0)^{\mathsf T}$ in rows $1$ to $3$ of column $4$.

Third, find the dimension of the centralizer of $J_4(0)$.
Its Weyr structure is $(1, 1, 1, 1)$, so the dimension is $1 + 1 + 1 + 1 = 4$, which fits the fact that $J_4(0)$ is cyclic.

## Explanations

### L1 human

Think of a nilpotent matrix as a set of ladders: each basis vector steps down to the next one, and the bottom one steps to zero.
The Jordan form lists the rungs ladder by ladder.
The Weyr form lists them floor by floor: first all the bottom rungs, then all the rungs one floor up, and so on.
For ladders of heights $3$ and $1$, the floors hold $2$, $1$ and $1$ rungs.
Both lists describe the same ladders, but the floor-by-floor list makes the matrices that commute with the given one look like staircases.

### L2 human

Here is a typical computation: find the Weyr form of $N = J_2(0) \oplus J_2(0)$ and the matrices that commute with it.
The kernels of $N$ and $N^2$ have dimensions $2$ and $4$, so the Weyr structure is $(2, 2)$.
The chains are $e_2 \mapsto e_1$ and $e_4 \mapsto e_3$, so the Weyr basis is $e_1, e_3, e_2, e_4$.
In that basis $N$ becomes $W = \begin{pmatrix} 0 & I_2 \\ 0 & 0 \end{pmatrix}$.
For $X = \begin{pmatrix} P & Q \\ R & S \end{pmatrix}$ in $2 \times 2$ blocks, multiply both ways:
$$W X = \begin{pmatrix} R & S \\ 0 & 0 \end{pmatrix}, \qquad X W = \begin{pmatrix} 0 & P \\ 0 & R \end{pmatrix}.$$
So $X$ commutes with $W$ exactly when $R = 0$ and $S = P$, and the centralizer is block upper triangular of dimension $8 = 2^2 + 2^2$.
The same computation in the Jordan basis gives matrices with entries below the diagonal, which is the reason to change the order.

### L3 human

The Weyr basis is adapted to the filtration $\ker N \subseteq \ker N^2 \subseteq \cdots$ of a nilpotent $N$.
A matrix that commutes with $N$ preserves each $\ker N^j$, and this is why its matrix in an adapted basis is block upper triangular.
In this sense the Weyr form is the normal form that respects the flag of kernels, while the Jordan form respects the decomposition into cyclic pieces.
Problems on commuting matrices use it, for instance around the theorem of Gerstenhaber that two commuting $n \times n$ matrices over a field generate an algebra of dimension at most $n$.
The [[centralizer theorem|GXZGWZSJ2J]] gives the dimension of the commuting matrices from the invariant factors, and the Weyr form shows their shape.
