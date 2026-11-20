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

Let $F$ be a field.
By the [[normal form of nilpotent endomorphisms|Z2RTKWZZAZ]], a nilpotent $N \in M_4(F)$ is similar to exactly one sum of nilpotent [[Jordan blocks|0PBFS92AJP]] $J_{k_1}(0) \oplus \cdots \oplus J_{k_s}(0)$ with $k_1 \ge \cdots \ge k_s$ and $k_1 + \cdots + k_s = 4$.
The [[partitions|0JV30XN73Z]] of $4$ are $(4)$, $(3, 1)$, $(2, 2)$, $(2, 1, 1)$ and $(1, 1, 1, 1)$, so there are five classes.

1. $\operatorname{rank} J_k(0)^j = \max(k - j, 0)$, and ranks add over a block diagonal matrix.
2. So the ranks of $N, N^2, N^3$ for the five classes are:

| partition | $\operatorname{rank} N$ | $\operatorname{rank} N^2$ | $\operatorname{rank} N^3$ | invariant factors | minimal polynomial |
|---|---|---|---|---|---|
| $(4)$ | $3$ | $2$ | $1$ | $x^4$ | $x^4$ |
| $(3, 1)$ | $2$ | $1$ | $0$ | $x, x^3$ | $x^3$ |
| $(2, 2)$ | $2$ | $0$ | $0$ | $x^2, x^2$ | $x^2$ |
| $(2, 1, 1)$ | $1$ | $0$ | $0$ | $x, x, x^2$ | $x^2$ |
| $(1, 1, 1, 1)$ | $0$ | $0$ | $0$ | $x, x, x, x$ | $x$ |

3. The five rank triples are different, so the ranks of the powers separate the five classes.
4. The [[invariant factors|F7GJPMVBXA]] of $J_{k_1}(0) \oplus \cdots \oplus J_{k_s}(0)$ are the $x^{k_i}$, in increasing order of degree. They also separate the five classes.
5. The characteristic polynomial is $x^4$ in all five cases. The [[minimal polynomial|03NDVCSHSB]] is the same for $(2, 2)$ and $(2, 1, 1)$, so it does not separate these two classes, but the rank of $N$ does.

## Remarks

Over every field the number of similarity classes of nilpotent $n \times n$ matrices is the number of partitions of $n$, and it does not depend on the field.
For $n = 1, 2, 3, 4, 5$ this number is $1, 2, 3, 5, 7$.

## Explanations

### L1 human

There are five kinds of nilpotent $4 \times 4$ matrices up to change of basis.
Each kind is a way to write $4$ as a sum of block sizes.

### L2 human

To find the class of a given nilpotent $N$, compute the ranks of $N$, $N^2$ and $N^3$ and find the row of the table.
The number of blocks of size at least $j$ is $\operatorname{rank} N^{j-1} - \operatorname{rank} N^j$, with $\operatorname{rank} N^0 = 4$.
For the row $(3, 1)$ this gives $4 - 2 = 2$ blocks, $2 - 1 = 1$ block of size at least $2$, and $1 - 0 = 1$ block of size at least $3$.
