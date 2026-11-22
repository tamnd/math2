---
tag: 1QVWFSF796
kind: proof
name: Proof of the associativity of matrix multiplication
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: 073E4XC016
methods: [0NTF6DMVAP]
uses: [076JGP6R3T, 0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Associativity
  - url: https://proofwiki.org/wiki/Matrix_Multiplication_is_Associative
---

## Proof

We write one entry of each side as a double sum and show that the two double sums have the same terms.

1. Write $A = (a_{ij})$, $B = (b_{jk})$ and $C = (c_{kl})$, with $1 \le i \le m$, $1 \le j \le n$, $1 \le k \le p$ and $1 \le l \le q$.
2. By the definition of the [[matrix product|076JGP6R3T]], $AB$ is $m \times p$ and $BC$ is $n \times q$. So $(AB)C$ and $A(BC)$ are both defined, and both are $m \times q$.
3. Fix $i$ and $l$. Applying the definition twice gives
$$\bigl((AB)C\bigr)_{il} = \sum_{k=1}^{p} (AB)_{ik} \, c_{kl} = \sum_{k=1}^{p} \Bigl( \sum_{j=1}^{n} a_{ij} b_{jk} \Bigr) c_{kl}.$$
4. The right distributive law of the [[ring|0894J980RK]] $R$ moves $c_{kl}$ inside the inner sum:
$$\bigl((AB)C\bigr)_{il} = \sum_{k=1}^{p} \sum_{j=1}^{n} (a_{ij} b_{jk}) c_{kl}.$$
5. In the same way, the definition gives
$$\bigl(A(BC)\bigr)_{il} = \sum_{j=1}^{n} a_{ij} \, (BC)_{jl} = \sum_{j=1}^{n} a_{ij} \Bigl( \sum_{k=1}^{p} b_{jk} c_{kl} \Bigr).$$
6. The left distributive law moves $a_{ij}$ inside the inner sum:
$$\bigl(A(BC)\bigr)_{il} = \sum_{j=1}^{n} \sum_{k=1}^{p} a_{ij} (b_{jk} c_{kl}).$$
7. Multiplication in $R$ is associative, so $(a_{ij} b_{jk}) c_{kl} = a_{ij} (b_{jk} c_{kl})$ for every pair $(j, k)$. So the double sums of steps 4 and 6 have the same $np$ terms.
8. Addition in $R$ is associative and commutative, so a finite sum does not depend on the order of its terms. Hence the double sums of steps 4 and 6 are equal.
9. So $\bigl((AB)C\bigr)_{il} = \bigl(A(BC)\bigr)_{il}$ for all $i$ and $l$. The two matrices have the same size and the same entries, so $(AB)C = A(BC)$.

## Idea

Each side, multiplied out, is the sum of the products $a_{ij} b_{jk} c_{kl}$ over all pairs $(j, k)$.
The left side sums over $j$ first and the right side over $k$ first, which is the same finite sum taken in another order.
Think of a grid of $n$ by $p$ terms: you may add it row by row or column by column, and you get the same total.
The only ring laws used are distributivity, associativity of the product of entries, and the freedom to reorder a finite sum, so commutativity of $R$ never enters.

## Variants

The [[proof by composition|KC9SCPKS2G]] first shows $(AB)y = A(By)$ for every column $y$, and then compares the columns of the two sides.
It explains why the law holds: matrices are linear maps, and composition of maps is associative.

A third proof uses the [[matrix units|A4HTT7JFD1]].
Both sides are additive in each of $A$, $B$ and $C$, so it is enough to check the law when each factor has a single nonzero entry, $A = a E_{ij}$, $B = b E_{j'k}$ and $C = c E_{k'l}$.
Both sides are $0$ unless $j = j'$ and $k = k'$, and in that case they are $(ab)c \, E_{il}$ and $a(bc) \, E_{il}$, which agree.
