---
tag: ~eda9ba19
kind: statement
role: lemma
name: Product of matrix units
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
about: [~709aa34e]
uses: [~2c685e2c, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: Properties
---

## Statement

Let $R$ be a ring with identity.
Let $E_{ij}$ be an $m \times n$ [[matrix unit|~2c685e2c]] and let $E_{kl}$ be an $n \times p$ matrix unit over $R$.
Then the [[product|076JGP6R3T]] is
$$E_{ij} E_{kl} = \delta_{jk} E_{il},$$
that is, $E_{ij} E_{kl} = E_{il}$ if $j = k$, and $E_{ij} E_{kl} = 0$ if $j \neq k$.

## Remarks

### Consequences

- $E_{ii}^2 = E_{ii}$, so each $E_{ii}$ is [[idempotent|0K7TD9BV2D]].
- For $i \neq j$, $E_{ij}^2 = \delta_{ji} E_{ij} = 0$, so $E_{ij}$ is [[nilpotent|0419GJC84P]].
- $E_{12} E_{21} = E_{11}$ but $E_{21} E_{12} = E_{22}$, so matrix multiplication is [[not commutative|0P506SPZP2]] for $n \ge 2$.
- With $A = \sum a_{pq} E_{pq}$, the rule gives $E_{ij} A E_{kl} = a_{jk} E_{il}$.
- The rule and bilinearity determine every product of matrices, so they give a second proof of [[associativity|073E4XC016]].

## Explanations

### L1 human

Two matrix units multiply to a matrix unit or to zero.
The inner indices must match, and then the outer indices remain.

### L2 human

The rule is the same as the rule for composing arrows $j \to i$ and $l \to k$.
The composite exists when $k = j$, and then it is the arrow $l \to i$.
