---
tag: NVW7KDY7PN
kind: proof
name: Proof that the center of a matrix ring is the set of scalar matrices
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

We prove the two inclusions: every $cI$ with $c \in Z(R)$ is central, and every central matrix has this form.

1. Let $c \in Z(R)$ and $B = (b_{ij}) \in M_n(R)$. By the product rule, the $(i, j)$ entry of $(cI)B$ is $c\,b_{ij}$, and the $(i, j)$ entry of $B(cI)$ is $b_{ij}\,c$.
2. Since $c$ lies in the [[center|MVT64B3B6H]] of $R$, $c\,b_{ij} = b_{ij}\,c$ for all $i, j$. So $(cI)B = B(cI)$ for every $B$, and $cI \in Z(M_n(R))$.
3. Conversely, let $A \in Z(M_n(R))$. Then $A$ commutes with every matrix, in particular with every [[matrix unit|4H93XF4RVH]] $E_{ij}$.
4. By the [[lemma on matrix units|TX4J5JR205]], $A = cI$ with $c = a_{11} \in R$.
5. Let $b \in R$. The matrix $A$ also commutes with the scalar matrix $bI$. The $(1, 1)$ entry of $A(bI)$ is $cb$, and the $(1, 1)$ entry of $(bI)A$ is $bc$.
6. So $cb = bc$ for every $b \in R$, which means $c \in Z(R)$.
7. By steps 2 and 6, $Z(M_n(R)) = \{ cI : c \in Z(R) \}$.
8. If $R$ is commutative, then $Z(R) = R$, and the center of $M_n(R)$ is the set of all [[scalar matrices|0FRM62SG7D]].

## Idea

Two kinds of test matrices do the work.
The matrix units have a single entry $1$, and commuting with them forces the shape $cI$.
The scalar matrices $bI$ carry the elements of $R$, and commuting with them forces $c$ to commute with each $b$.
When $R$ is commutative the second test is automatic, and only the first one matters.

## Variants

Over a field $F$ there is a proof with linear maps.
A linear map $T$ of $F^n$ that commutes with a projection $P$ maps the image of $P$ into itself, since $T(Px) = P(Tx)$.
Taking $P$ to be a projection onto a line $Fv$ shows that $Tv$ is a multiple of $v$ for every $v$.
A linear map that sends every vector to a multiple of itself is a multiple of the identity, because $v$, $w$ and $v + w$ must all be scaled by the same factor when $v$ and $w$ are independent.
