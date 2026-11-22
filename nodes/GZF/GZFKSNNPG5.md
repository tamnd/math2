---
tag: GZFKSNNPG5
kind: proof
name: Proof that a matrix commuting with all matrix units is scalar
msc: ["15A27"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: TX4J5JR205
methods: [0NTF6DMVAP]
uses: [4H93XF4RVH, 076JGP6R3T, 0FRM62SG7D]
sources:
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
    locator: Properties
---

## Proof

Let $A = (a_{kl})$ commute with every matrix unit.
The plan is to compute both products $E_{ij} A$ and $A E_{ij}$ entry by entry, and to compare one row of them.

1. By the [[definition of matrix units|4H93XF4RVH]], $(E_{ij})_{pq} = \delta_{ip}\delta_{jq}$, where $\delta$ is $1$ for equal indices and $0$ otherwise.
2. By the [[product rule|076JGP6R3T]],
$$(E_{ij} A)_{kl} = \sum_{p=1}^{n} \delta_{ik}\delta_{jp}\, a_{pl} = \delta_{ik}\, a_{jl}.$$
So $E_{ij} A$ has row $j$ of $A$ in row $i$, and zeros elsewhere.
3. In the same way,
$$(A E_{ij})_{kl} = \sum_{p=1}^{n} a_{kp}\, \delta_{ip}\delta_{jl} = a_{ki}\, \delta_{jl}.$$
So $A E_{ij}$ has column $i$ of $A$ in column $j$, and zeros elsewhere.
4. By hypothesis, $E_{ij} A = A E_{ij}$. Compare the entries in position $(i, l)$: step 2 gives $a_{jl}$, and step 3 gives $a_{ii}\,\delta_{jl}$. So $a_{jl} = a_{ii}\,\delta_{jl}$ for all $i, j, l$.
5. Take $l \ne j$. Then $\delta_{jl} = 0$, and step 4 gives $a_{jl} = 0$. Since $j$ and $l$ are arbitrary, every off-diagonal entry of $A$ is $0$.
6. Take $l = j$. Then step 4 gives $a_{jj} = a_{ii}$. With $i = 1$, every diagonal entry equals $c = a_{11}$.
7. By steps 5 and 6, $A = cI_n$, a [[scalar matrix|0FRM62SG7D]].
8. If $A$ commutes with every $n \times n$ matrix, then it commutes in particular with every $E_{ij}$, so $A$ is scalar by step 7.

## Idea

Each matrix unit moves a single row or a single column of $A$ and erases the rest.
So commuting with $E_{ij}$ compares row $j$ of $A$ with column $i$ of $A$, placed in the same spot.
These comparisons pin down every entry: the off-diagonal entries are forced to vanish, and the diagonal entries are forced to agree.

## Variants

Steps 4 to 6 use only the units with $i = 1$.
So a matrix that commutes with the $n$ units $E_{11}, E_{12}, \dots, E_{1n}$ of the first row is already scalar, since step 4 then reads $a_{jl} = a_{11}\,\delta_{jl}$ for all $j$ and $l$.

Over a field there is a proof without indices.
A linear map $T$ that commutes with every linear map commutes with each projection onto a line $Fv$, so $Tv \in Fv$ for every $v$.
A linear map that sends every vector to a multiple of itself is a multiple of the identity, because the factors for $v$, $w$ and $v + w$ must agree when $v$ and $w$ are independent.
