---
tag: E66YRYVWQ3
kind: statement
role: lemma
name: Product of matrix units
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [A4HTT7JFD1]
uses: [4H93XF4RVH, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: Properties
---

## Statement

Let $R$ be a ring with identity.
Let $E_{ij}$ be an $m \times n$ [[matrix unit|4H93XF4RVH]] and let $E_{kl}$ be an $n \times p$ matrix unit over $R$.
Then the [[product|076JGP6R3T]] is
$$E_{ij} E_{kl} = \delta_{jk} E_{il},$$
that is, $E_{ij} E_{kl} = E_{il}$ if $j = k$, and $E_{ij} E_{kl} = 0$ if $j \ne k$.

## Remarks

### Reading the rule

The product of two matrix units is again a matrix unit or zero.
The inner indices $j$ and $k$ decide which, and when they agree, the outer indices $i$ and $l$ name the result.
For example, with $3 \times 3$ matrix units, $E_{23} E_{31} = E_{21}$ and $E_{23} E_{13} = 0$.
The [[proof|KC9T82AKWF]] computes one entry of the product at a time.

### Consequences

For square matrix units, $E_{ii}^2 = E_{ii}$, so each $E_{ii}$ is [[idempotent|0K7TD9BV2D]], and for $i \ne j$, $E_{ij}^2 = \delta_{ji} E_{ij} = 0$, so $E_{ij}$ is [[nilpotent|0419GJC84P]].
Since $E_{12} E_{21} = E_{11}$ but $E_{21} E_{12} = E_{22}$, matrix multiplication is [[not commutative|0P506SPZP2]] for $n \ge 2$.
Writing $A = \sum a_{pq} E_{pq}$ and applying the rule twice gives
$$E_{ij} A E_{kl} = \sum_{p, q} a_{pq} \, \delta_{jp} \delta_{qk} E_{il} = a_{jk} E_{il}.$$
The rule and bilinearity determine every product of matrices, so they give a second proof of [[associativity|073E4XC016]]: both $(E_{ij} E_{kl}) E_{rs}$ and $E_{ij} (E_{kl} E_{rs})$ equal $\delta_{jk} \delta_{lr} E_{is}$.

## History

The rule appears wherever matrices are studied through a basis of the matrix space, and it is the defining relation of a system of matrix units in ring theory.

## Explanations

### L1 human

Two matrix units multiply to a matrix unit or to zero.
The inner indices must match, and then the outer indices remain: $E_{12} E_{21} = E_{11}$, while $E_{12} E_{12} = 0$.

### L2 human

Think of $E_{ij}$ as an arrow from $j$ to $i$, since it sends the basis vector $e_j$ to $e_i$.
The product $E_{ij} E_{kl}$ means following the arrow $l \to k$ and then the arrow $j \to i$.
The two arrows connect when $k = j$, and then the composite is the arrow $l \to i$, which is $E_{il}$.
Watch out: the order of the factors matters, because the right factor acts first.
