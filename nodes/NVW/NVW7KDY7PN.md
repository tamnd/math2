---
tag: NVW7KDY7PN
kind: proof
name: Proof that the centre of a matrix ring is the set of scalar matrices
msc: ["15A27", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug2
proves: DVZ1V4A884
methods: [0NTF6DMVAP]
uses: [TX4J5JR205, 4H93XF4RVH, 0FRM62SG7D, MVT64B3B6H]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: Properties
---

## Proof

We prove the two inclusions.

1. Let $c \in Z(R)$ and $B \in M_n(R)$. The entries of $(cI)B$ are $c\,b_{ij}$, and the entries of $B(cI)$ are $b_{ij}\,c$, by the product rule.
2. Since $c$ is central in $R$, $c\,b_{ij} = b_{ij}\,c$. So $cI$ commutes with $B$, and $cI \in Z(M_n(R))$.
3. Conversely, let $A \in Z(M_n(R))$. Then $A$ commutes with every [[matrix unit|4H93XF4RVH]] $E_{ij}$.
4. By the [[lemma on matrix units|TX4J5JR205]], $A = cI$ for $c = a_{11} \in R$.
5. For $b \in R$, the matrix $A$ also commutes with $bI$. The entry $(1, 1)$ of $A(bI)$ is $cb$, and that of $(bI)A$ is $bc$.
6. So $cb = bc$ for every $b \in R$, that is, $c \in Z(R)$.
7. By steps 2 and 6, $Z(M_n(R)) = \{cI : c \in Z(R)\}$.
8. If $R$ is commutative, $Z(R) = R$, and the centre is the set of all [[scalar matrices|0FRM62SG7D]].

## Idea

Commuting with the matrix units forces the shape $cI$.
Commuting with the scalar matrices forces $c$ to be central.

## Variants

- Over a field one can use the linear map point of view: a map commuting with all projections onto lines $Fv$ keeps every line, so it is a scalar multiple of the identity.
