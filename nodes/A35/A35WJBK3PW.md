---
tag: A35WJBK3PW
kind: proof
name: Proof of the double negation law by a truth table
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
proves: 0NFAGWH84K
uses: [0ZGC7ZESYN, 029JBBF693, 0JMR2HM2N2, 05RSK4Q657]
methods: [05RSK4Q657, 0WCP0PVET6]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
  - url: https://en.wikipedia.org/wiki/Double_negation
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
---

## Proof

We compare the [[truth table|05RSK4Q657]] columns of $\neg\neg p$ and $p$.

1. By the [[principle of bivalence|~e6dead3d]], the variable $p$ is T or F, so the table has two rows.
2. Row $p = \mathrm{T}$. By the definition of [[negation|029JBBF693]], $\neg p$ is F. By the same definition applied to $\neg p$, the formula $\neg\neg p$ is T.
3. Row $p = \mathrm{F}$. By the definition of negation, $\neg p$ is T. Applied once more, the definition gives that $\neg\neg p$ is F.
4. The table is this.

| $p$ | $\neg p$ | $\neg\neg p$ |
|---|---|---|
| T | F | T |
| F | T | F |

5. By steps 2 and 3, the column of $\neg\neg p$ equals the column of $p$ in both rows.
6. The two rows cover every valuation, so $\neg\neg p$ and $p$ are [[logically equivalent|0JMR2HM2N2]]: $\neg\neg p \equiv p$. $\blacksquare$

## Idea

Negation swaps the two truth values.
Two swaps bring back the first value, so $\neg\neg p$ has the value of $p$ in every row.

## Variants

The truth-table proof treats both directions of the law at once, and it uses bivalence in step 1.
The [[natural deduction proof of the double negation law|~39d6aa0b]] proves the two directions separately.
It shows that $p \to \neg\neg p$ needs no classical rule, while $\neg\neg p \to p$ uses the [[law of excluded middle|0RYYK8PG4S]].
