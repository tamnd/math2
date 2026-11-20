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

Let $V$ be a vector space of dimension $n$ over a field $F$, and let $N \colon V \to V$ be a [[nilpotent endomorphism|063D5Z2C70]].

1. *Existence.* There are vectors $u_1, \dots, u_s \in V$ and integers $k_1 \ge \cdots \ge k_s \ge 1$ with $N^{k_i} u_i = 0$, such that the vectors $N^j u_i$ with $1 \le i \le s$ and $0 \le j < k_i$ form a basis of $V$. In the basis
$$N^{k_1 - 1} u_1, \dots, N u_1, u_1, \; \dots, \; N^{k_s - 1} u_s, \dots, N u_s, u_s$$
the matrix of $N$ is the [[block diagonal matrix|0M0SNKZ482]] $J_{k_1}(0) \oplus \cdots \oplus J_{k_s}(0)$ of [[Jordan blocks|0PBFS92AJP]].
2. *Partition.* $k_1 + \cdots + k_s = n$, so $(k_1, \dots, k_s)$ is an [[integer partition|0JV30XN73Z]] of $n$.
3. *Block counts.* Let $r_j = \operatorname{rank} N^j$ be the [[rank|0EWQEYRVA8]], with $r_0 = n$. For every $j \ge 1$, the number of $i$ with $k_i \ge j$ is $r_{j-1} - r_j = \dim \ker N^j - \dim \ker N^{j-1}$. The number of $i$ with $k_i = j$ is $r_{j-1} - 2 r_j + r_{j+1}$.
4. *Uniqueness.* The partition $(k_1, \dots, k_s)$ depends only on $N$. Two nilpotent matrices are similar if and only if they have the same partition, that is, the same ranks $r_j$ for all $j$.
5. *Young diagram.* In the [[Young diagram|096AHMB3P4]] of $(k_1, \dots, k_s)$, with row $i$ of length $k_i$, column $j$ has length $r_{j-1} - r_j$. So the column lengths are the jumps $\dim \ker N^j - \dim \ker N^{j-1}$.

## Remarks

### Why each hypothesis is needed

Nilpotence is needed: $N = (1)$ on $F$ has no nonzero vector $u$ with $N^k u = 0$, so no chain basis exists.
Finite dimension is used in the proof, through induction on $\dim V$ and the rank-nullity theorem, and in the block counts of part 3.
No hypothesis on the field is needed, because $0$ is the only eigenvalue and it lies in every field.

### Consequences

The number of blocks $s$ is $\dim \ker N$.
The size $k_1$ of the largest block is the nilpotency index, the least $k$ with $N^k = 0$.
The similarity classes of nilpotent $n \times n$ matrices are in bijection with the partitions of $n$; for $n = 4$ there are $5$ classes.
Together with the decomposition into generalized eigenspaces, the theorem gives the [[Jordan normal form|085HQ5G5TE]].

### Converse

Every partition of $n$ occurs: $J_{k_1}(0) \oplus \cdots \oplus J_{k_s}(0)$ is nilpotent with partition $(k_1, \dots, k_s)$.

### Generalizations

The same statement holds for a finitely generated torsion module over $F[x]$ that is killed by a power of $x$.
More generally, it holds for a torsion module over a principal ideal domain killed by a power of a prime element.
For a field $F$ and a matrix $A$ with minimal polynomial $(x - \lambda)^m$, apply the theorem to $N = A - \lambda I$.

## Explanations

### L1 human

A nilpotent map becomes zero after you apply it enough times.
This theorem says that you can always find a basis made of chains: each chain is pushed one step at a time toward zero.
The lengths of the chains are fixed by the map, and you can read them from the ranks of its powers.

### L2 human

Take a nilpotent $N$ on $F^5$ with $r_1 = 2$, $r_2 = 1$, $r_3 = 0$.

1. The jumps $r_0 - r_1 = 3$, $r_1 - r_2 = 1$, $r_2 - r_3 = 1$ are the column lengths of the Young diagram.
2. So there are $3$ blocks, at least $1$ block of size $\ge 2$, and at least $1$ block of size $\ge 3$.
3. The partition is $(3, 1, 1)$, and $N$ is similar to $J_3(0) \oplus J_1(0) \oplus J_1(0)$.
4. Check: the ranks of the powers of this matrix are $2 + 0 + 0$, $1$ and $0$.

The trap is to read the kernel dimensions $3, 4, 5$ as block sizes; only their differences count blocks.

### L3 human

As an $F[x]$-module with $x$ acting as $N$, $V \cong \bigoplus_i F[x]/(x^{k_i})$, and the theorem is the structure theorem for modules over a PID in its simplest case.
The numbers $\dim \ker N^j$ define the Weyr characteristic, the conjugate partition of $(k_i)$.
Over $\mathbb{C}$, the nilpotent orbits under conjugation are indexed by partitions, and the closure order on orbits is the dominance order on partitions.
