---
tag: 57PTMS2ADY
kind: definition
name: Ordinal analysis
msc: ["03F15", "03F05"]
defines: C5E5TG8PGP
uses: [C19Z3B6V4P, C72RBH0CDR, 0QFT7Z76N5, KT50SMH3EC, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
---

## Definition

Let $T$ be a recursively axiomatized theory that contains elementary arithmetic.
An *ordinal analysis* of $T$ is the determination of its [[proof-theoretic ordinal|C19Z3B6V4P]] $\abs{T}$.
It consists of three parts.

1. A computable notation system: a computable well-order $\prec$ on a set of codes in $\N$, whose order type is an ordinal $\alpha$.
2. A lower bound: for each $\beta < \alpha$, a proof in $T$ of [[transfinite induction|0ZHQMQ2C1N]] along the initial segment of $\prec$ of order type $\beta$.
3. An upper bound: a proof that $T$ does not prove transfinite induction along $\prec$ itself. More precisely, each computable well-order that $T$ proves well-founded has order type below $\alpha$.

Then $\abs{T} = \alpha$.

## Remarks

Example: Gentzen's analysis of [[Peano arithmetic|0QFT7Z76N5]] uses the Cantor normal forms below [[epsilon nought|KT50SMH3EC]] as notation system, and gives $\abs{\mathrm{PA}} = \varepsilon_0$.
The upper bound comes from a cut-elimination argument for PA, together with transfinite induction up to $\varepsilon_0$.
Non-example: a proof that $T$ is consistent, by itself, is not an ordinal analysis, because it gives no ordinal.
The upper bound is usually proved in a weak base theory together with transfinite induction along $\prec$.
This also gives a proof of the consistency of $T$ in that base theory.
