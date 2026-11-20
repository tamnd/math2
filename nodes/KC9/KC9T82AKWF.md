---
tag: KC9T82AKWF
kind: proof
name: Proof of the product rule for matrix units
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: E66YRYVWQ3
methods: [0WCP0PVET6]
uses: [4H93XF4RVH, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: Properties
---

## Proof

Let $E_{ij}$ be $m \times n$ and $E_{kl}$ be $n \times p$, and fix a place $(a, b)$ with $1 \le a \le m$ and $1 \le b \le p$.

1. By the [[definition of the product|076JGP6R3T]], $(E_{ij} E_{kl})_{ab} = \sum_{c = 1}^{n} (E_{ij})_{ac} (E_{kl})_{cb}$.
2. By the [[definition of matrix units|4H93XF4RVH]], $(E_{ij})_{ac} = \delta_{ia} \delta_{jc}$ and $(E_{kl})_{cb} = \delta_{kc} \delta_{lb}$.
3. So $(E_{ij} E_{kl})_{ab} = \delta_{ia} \delta_{lb} \sum_{c = 1}^{n} \delta_{jc} \delta_{kc}$, because the factors $\delta_{ia}$ and $\delta_{lb}$ do not depend on $c$.
4. Case $j = k$: the term $c = j$ of the sum is $1$, and every other term is $0$. So the sum is $1 = \delta_{jk}$.
5. Case $j \neq k$: no $c$ is equal to both $j$ and $k$, so every term is $0$. So the sum is $0 = \delta_{jk}$.
6. By steps 3 to 5, $(E_{ij} E_{kl})_{ab} = \delta_{jk} \delta_{ia} \delta_{lb} = \delta_{jk} (E_{il})_{ab}$, by the definition of $E_{il}$.
7. Step 6 holds for every place $(a, b)$, so $E_{ij} E_{kl} = \delta_{jk} E_{il}$.

## Idea

Row $i$ of $E_{ij}$ has its $1$ in column $j$, and column $l$ of $E_{kl}$ has its $1$ in row $k$.
Their dot product is $1$ exactly when the two places meet, that is, when $j = k$.

## Variants

- As linear maps, $E_{ij} e_q = \delta_{jq} e_i$. Then $E_{ij} E_{kl} e_q = \delta_{lq} E_{ij} e_k = \delta_{lq} \delta_{jk} e_i = \delta_{jk} E_{il} e_q$ for each standard basis vector $e_q$.
