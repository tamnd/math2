---
tag: ZNQN1JW1V3
kind: proof
name: Proof of the law of excluded middle by a truth table
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
proves: 0RYYK8PG4S
uses: [0ZGC7ZESYN, 029JBBF693, 0F72FK8EKB, 05RSK4Q657, 05006AJ7DZ]
methods: [05RSK4Q657, 0WCP0PVET6]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
  - url: https://en.wikipedia.org/wiki/Law_of_excluded_middle
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 1.2
---

## Proof

We compute the [[truth table|05RSK4Q657]] of $p \lor \neg p$ and check that its column contains only T.

1. By the [[principle of bivalence|~e6dead3d]], the variable $p$ takes exactly one of the two truth values T and F. So the truth table has two rows.
2. Row $p = \mathrm{T}$. By the definition of [[disjunction|0F72FK8EKB]], a disjunction with a true part is true. The first part $p$ is true, so $p \lor \neg p$ is T.
3. Row $p = \mathrm{F}$. By the definition of [[negation|029JBBF693]], $\neg p$ is T.
4. In the same row, the second part $\neg p$ of the disjunction is true, so $p \lor \neg p$ is T by the definition of disjunction.
5. The two rows give this table.

| $p$ | $\neg p$ | $p \lor \neg p$ |
|---|---|---|
| T | F | T |
| F | T | T |

6. By step 1, the two rows cover every valuation. By steps 2 and 4, the formula is true in both rows.
7. So $p \lor \neg p$ is true under every valuation, that is, it is a [[tautology|05006AJ7DZ]]. $\blacksquare$

## Idea

Under classical two-valued semantics a variable has only two possible values.
If $p$ is true, the first part of $p \lor \neg p$ is true.
If $p$ is false, the second part is true.
In both cases the disjunction is true.

## Variants

In a proof system the law is either an axiom or a derived formula.
In [[natural deduction|6KT3BJZ7D1]], the formula $\neg\neg(p \lor \neg p)$ has a proof without any classical rule, as in the [[natural deduction proof of the double negation law|~39d6aa0b]].
With the classical rule of double negation elimination, this formula gives $p \lor \neg p$.
No proof of $p \lor \neg p$ exists in [[intuitionistic logic|Q11N8X99FK]]: a [[Kripke model|NGHWZ9Y7ZV]] with two worlds refutes it, as on the page of the [[law of excluded middle|0RYYK8PG4S]].
The truth-table proof is classical at step 1, where bivalence enters.
