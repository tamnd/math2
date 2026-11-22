---
tag: WT7V4ACJWF
kind: example
name: The five similarity classes of nilpotent 4 × 4 matrices
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
instance_of: [H3E52HTEZ2]
illustrates: [Z2RTKWZZAZ]
uses: [Z2RTKWZZAZ, 0PBFS92AJP, 0JV30XN73Z, F7GJPMVBXA, 03NDVCSHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Classification
---

## Example

Let $F$ be any field.
By the [[normal form of nilpotent endomorphisms|Z2RTKWZZAZ]], a nilpotent $N \in M_4(F)$ is similar to exactly one sum of nilpotent [[Jordan blocks|0PBFS92AJP]]
$$J_{k_1}(0) \oplus \cdots \oplus J_{k_s}(0), \qquad k_1 \ge \cdots \ge k_s \ge 1, \quad k_1 + \cdots + k_s = 4.$$
The [[partitions|0JV30XN73Z]] of $4$ are $(4)$, $(3, 1)$, $(2, 2)$, $(2, 1, 1)$ and $(1, 1, 1, 1)$, so there are exactly five classes.
We find invariants that tell them apart.

1. The block $J_k(0)$ sends $e_k \mapsto e_{k-1} \mapsto \cdots \mapsto e_1 \mapsto 0$, so its $j$-th power has rank $\max(k - j, 0)$. Ranks add over a block diagonal matrix.
2. This gives the ranks of $N$, $N^2$ and $N^3$ for each class, shown in the table with the [[invariant factors|F7GJPMVBXA]] $x^{k_s}, \dots, x^{k_1}$ and the [[minimal polynomial|03NDVCSHSB]] $x^{k_1}$.

| partition | $\operatorname{rank} N$ | $\operatorname{rank} N^2$ | $\operatorname{rank} N^3$ | invariant factors | minimal polynomial |
|---|---|---|---|---|---|
| $(4)$ | $3$ | $2$ | $1$ | $x^4$ | $x^4$ |
| $(3, 1)$ | $2$ | $1$ | $0$ | $x, x^3$ | $x^3$ |
| $(2, 2)$ | $2$ | $0$ | $0$ | $x^2, x^2$ | $x^2$ |
| $(2, 1, 1)$ | $1$ | $0$ | $0$ | $x, x, x^2$ | $x^2$ |
| $(1, 1, 1, 1)$ | $0$ | $0$ | $0$ | $x, x, x, x$ | $x$ |

3. The five rank triples are different, so the ranks of the powers separate the five classes.
4. The five lists of invariant factors are also different, as the theorem on invariant factors predicts.
5. The characteristic polynomial is $x^4$ in all five cases. The minimal polynomial is $x^2$ for both $(2, 2)$ and $(2, 1, 1)$, so it does not separate these two classes, but the rank of $N$ does.

## Remarks

The ranks determine the partition, and here is how to read it back.
The number of blocks of size at least $j$ is $\operatorname{rank} N^{j-1} - \operatorname{rank} N^j$, with $\operatorname{rank} N^0 = 4$.
For the row $(3, 1)$ this gives $4 - 2 = 2$ blocks in all, $2 - 1 = 1$ block of size at least $2$, and $1 - 0 = 1$ block of size at least $3$, which is the partition $(3, 1)$.

Over every field the number of similarity classes of nilpotent $n \times n$ matrices is the number of partitions of $n$, so it does not depend on the field.
For $n = 1, 2, 3, 4, 5$ this number is $1, 2, 3, 5, 7$.
The pair $(2, 2)$ and $(2, 1, 1)$ is the smallest case where the characteristic and minimal polynomials agree on two different classes.

## Explanations

### L1 human

Up to a change of basis, there are five kinds of nilpotent $4 \times 4$ matrices.
Each kind is a way to cut $4$ into block sizes: $4$, $3 + 1$, $2 + 2$, $2 + 1 + 1$ or $1 + 1 + 1 + 1$.
Think of each block as a ladder whose rungs step down to zero.
Counting how many rungs survive after one, two and three steps tells you which kind you have.

### L2 human

To find the class of a given nilpotent $N$, compute the ranks of $N$, $N^2$ and $N^3$ and find the row of the table.
For example, let $N = E_{12} + E_{34} + E_{23}$, which sends $e_4 \mapsto e_3 \mapsto e_2 \mapsto e_1 \mapsto 0$.
Its powers have ranks $3, 2, 1$, so $N$ is in the class $(4)$, a single block.
If we drop the term $E_{23}$, the matrix $E_{12} + E_{34}$ has rank $2$ and square $0$, so it is in the class $(2, 2)$.
Watch out: two matrices with the same rank of $N$ need not be similar, since $(3, 1)$ and $(2, 2)$ both have rank $2$.
