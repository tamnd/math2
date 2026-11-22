---
tag: Z2RTKWZZAZ
kind: statement
role: theorem
name: Normal form of nilpotent endomorphisms
aliases: [structure-of-nilpotent-endomorphisms, jordan-form-of-a-nilpotent-matrix]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
about: [063D5Z2C70, 07PH4RX0X5]
uses: [063D5Z2C70, 0PBFS92AJP, 0M0SNKZ482, 0JV30XN73Z, 096AHMB3P4, 0EWQEYRVA8]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Classification
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: Uniqueness
  - book: isbn:9780135367971
    locator: Section 7.3
---

## Statement

Every nilpotent map is a direct sum of shifts, and the lengths of the shifts form a partition of the dimension that the ranks of the powers determine.
Let $V$ be a vector space of finite dimension $n$ over a field $F$, and let $N \colon V \to V$ be a [[nilpotent endomorphism|063D5Z2C70]].

1. *Existence.* There are vectors $u_1, \dots, u_s \in V$ and integers $k_1 \ge \dots \ge k_s \ge 1$ with $N^{k_i} u_i = 0$, such that the vectors $N^j u_i$ with $1 \le i \le s$ and $0 \le j < k_i$ form a basis of $V$. In the ordered basis
$$N^{k_1 - 1} u_1, \dots, N u_1, u_1, \; \dots, \; N^{k_s - 1} u_s, \dots, N u_s, u_s$$
the matrix of $N$ is the [[block diagonal matrix|0M0SNKZ482]] $J_{k_1}(0) \oplus \dots \oplus J_{k_s}(0)$ of [[Jordan blocks|0PBFS92AJP]].
2. *Partition.* $k_1 + \dots + k_s = n$, so $(k_1, \dots, k_s)$ is an [[integer partition|0JV30XN73Z]] of $n$.
3. *Block counts.* Let $r_j = \operatorname{rank} N^j$ be the [[rank|0EWQEYRVA8]] of the $j$-th power, with $r_0 = n$. For every $j \ge 1$, the number of $i$ with $k_i \ge j$ is $r_{j-1} - r_j = \dim \ker N^j - \dim \ker N^{j-1}$, and the number of $i$ with $k_i = j$ is $r_{j-1} - 2 r_j + r_{j+1}$.
4. *Uniqueness.* The partition $(k_1, \dots, k_s)$ depends only on $N$. Two nilpotent $n \times n$ matrices over $F$ are similar if and only if they have the same partition, that is, the same ranks $r_j$ for all $j$.
5. *Young diagram.* In the [[Young diagram|096AHMB3P4]] of $(k_1, \dots, k_s)$, with row $i$ of length $k_i$, column $j$ has length $r_{j-1} - r_j$.

## Remarks

### Why each hypothesis is needed

Nilpotence is needed for the chains to end.
The identity map on $F$ is not nilpotent, and it has no nonzero vector $u$ with $N^k u = 0$, so it has no basis of chains.
Finite dimension is needed for the partition and for the ranks to be finite numbers.
On the space of all real polynomials, some power of the derivative kills each single polynomial, but no power of the derivative is zero, so the derivative is not nilpotent and has no finite list of blocks.
No hypothesis on the field is needed, since the only eigenvalue is $0$, which lies in every field.

### What it gives you

The number $s$ of blocks is $\dim \ker N$, and the size $k_1$ of the largest block is the nilpotency index, the least $k$ with $N^k = 0$.
The similarity classes of nilpotent $n \times n$ matrices correspond to the partitions of $n$, so for $n = 4$ there are exactly $5$ classes: $(4)$, $(3, 1)$, $(2, 2)$, $(2, 1, 1)$ and $(1, 1, 1, 1)$.
The [[five classes of nilpotent 4 by 4 matrices|WT7V4ACJWF]] lists them with their ranks.
Together with the [[decomposition into generalized eigenspaces|0Z3GDY89T5]], the theorem gives the [[Jordan normal form|085HQ5G5TE]]: on each generalized eigenspace, $A - \lambda I$ is nilpotent.

### A worked use

Let $N$ be nilpotent on $F^5$ with ranks $r_1 = 3$, $r_2 = 1$ and $r_3 = 0$.
The jumps of the ranks count the blocks of each size or more:
$$r_0 - r_1 = 2, \qquad r_1 - r_2 = 2, \qquad r_2 - r_3 = 1.$$
So there are $2$ blocks, both of size at least $2$, and one of them has size at least $3$.
The partition is $(3, 2)$, and $N$ is similar to $J_3(0) \oplus J_2(0)$.
Check: this matrix has $\operatorname{rank} N = 2 + 1 = 3$, $\operatorname{rank} N^2 = 1 + 0 = 1$ and $N^3 = 0$.

### Watch out

The jumps $2, 2, 1$ are the column lengths of the Young diagram, not the block sizes.
Reading them as block sizes gives $J_2(0) \oplus J_2(0) \oplus J_1(0)$, whose powers have ranks $2$ and $0$, not $3$ and $1$.
The jumps form the conjugate partition, and you must transpose the diagram to get the blocks.

### The converse

Every partition of $n$ occurs: $J_{k_1}(0) \oplus \dots \oplus J_{k_s}(0)$ is nilpotent, and its partition is $(k_1, \dots, k_s)$.

### Generalizations

The same statement holds for a finitely generated $F[x]$-module that a power of $x$ kills, since that is what a nilpotent map on a finite-dimensional space is.
More generally, a finitely generated module over a principal ideal domain that a power of a prime $p$ kills is a direct sum of cyclic modules $R/(p^{k_i})$, with a unique partition.
For a matrix $A$ with minimal polynomial $(x - \lambda)^m$, apply the theorem to $N = A - \lambda I$.

## History

The statement is the nilpotent case of the Jordan normal form, which Camille Jordan published in 1870.

## Explanations

### L1 human

A nilpotent map becomes zero after you apply it enough times.
The theorem says that you can always choose a basis made of chains, where the map pushes each vector one step down its chain and the last one to zero.
For example, a chain of length $3$ is $u \mapsto Nu \mapsto N^2 u \mapsto 0$.
The lengths of the chains are fixed by the map, and you can read them from the ranks of its powers.

### L2 human

Here is a typical computation with an explicit matrix on $\mathbb{Q}^3$:
$$N = \begin{pmatrix} 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
Its rank is $1$, and $N^2 = 0$, since the image is the line through $e_1$ and $N e_1 = 0$.
So $r_0 - r_1 = 2$ and $r_1 - r_2 = 1$: there are $2$ blocks, and one of them has size $2$.
The partition is $(2, 1)$, and a chain basis is $N e_2 = e_1$, $e_2$, together with $e_2 - e_3$, which lies in $\ker N$.
In the basis $e_1, e_2, e_2 - e_3$ the matrix of $N$ is $J_2(0) \oplus J_1(0)$.
The trap is to take $e_3$ as the third vector without checking: $N e_3 = e_1$ is not zero, so $e_3$ does not start a chain of length $1$.

### L3 human

As an $F[x]$-module with $x$ acting as $N$, the space is $V \cong \bigoplus_i F[x]/(x^{k_i})$, so the theorem is the simplest case of the structure theorem for modules over a principal ideal domain.
The jumps $\dim \ker N^j - \dim \ker N^{j-1}$ form the Weyr characteristic of $N$, which is the conjugate of the partition $(k_i)$, and the [[Weyr canonical form|9XEA4VR8WP]] is built from it.
Over $\mathbb{C}$, the nilpotent orbits under conjugation are indexed by partitions of $n$, and one orbit lies in the closure of another exactly when its partition is smaller in the dominance order.
