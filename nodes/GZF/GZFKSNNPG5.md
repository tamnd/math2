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

Let $A = (a_{kl})$ commute with every matrix unit, and fix indices $i$ and $j$.

1. By the [[definition|4H93XF4RVH]], $(E_{ij})_{pq} = \delta_{ip}\delta_{jq}$.
2. By the [[product rule|076JGP6R3T]], $(E_{ij} A)_{kl} = \sum_p \delta_{ik}\delta_{jp} a_{pl} = \delta_{ik}\, a_{jl}$. So $E_{ij} A$ has row $j$ of $A$ in row $i$, and zeros elsewhere.
3. In the same way, $(A E_{ij})_{kl} = \sum_p a_{kp} \delta_{ip}\delta_{jl} = a_{ki}\, \delta_{jl}$. So $A E_{ij}$ has column $i$ of $A$ in column $j$, and zeros elsewhere.
4. By hypothesis $E_{ij} A = A E_{ij}$. Compare the entries $(i, l)$: step 2 gives $a_{jl}$, and step 3 gives $a_{ii}\,\delta_{jl}$.
5. For $l \neq j$, step 4 gives $a_{jl} = 0$. Since $j$ is arbitrary, every off-diagonal entry of $A$ is $0$.
6. For $l = j$, step 4 gives $a_{jj} = a_{ii}$. Since $i$ and $j$ are arbitrary, all diagonal entries equal $c = a_{11}$.
7. By steps 5 and 6, $A = cI_n$, a [[scalar matrix|0FRM62SG7D]].
8. If $A$ commutes with every $n \times n$ matrix, it commutes in particular with every $E_{ij}$, so $A$ is scalar by step 7.

## Idea

Each matrix unit moves a single row or a single column.
Commutation with it compares one row of $A$ with one column of $A$, and these comparisons pin down every entry.

## Variants

- With the units $E_{1j}$ and $E_{j1}$ alone, $j = 1, \dots, n$, the same computation already gives $A = cI$.
- For a linear map $T$ on a vector space $V$ that commutes with all operators: $T$ commutes with each projection onto a line $Fv$, so $Tv \in Fv$ for all $v$, and then $T$ is scalar.
