---
tag: 68VBVMFJSW
kind: proof
name: "Proof of De Morgan's laws (logic) by truth tables"
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
proves: 09PKJKA6J0
uses: [0ZGC7ZESYN, 0XR7A7RSXB, 0M28ASWG8T, 0H5GKDTB01, 06GYGS41JK, 05RSK4Q657]
methods: [05RSK4Q657, 0WCP0PVET6]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
  - url: https://en.wikipedia.org/wiki/De_Morgan's_laws
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
  - book: isbn:9780122384523
    locator: Section 1.2
---

## Proof

We find the one row where each side of a law differs from the other three rows, and we check that both sides pick the same row.
Two formulas are [[logically equivalent|06GYGS41JK]] when they agree for each of the four assignments of truth values to $p$ and $q$.

1. Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
   By the [[principle of bivalence|5DYNDW9526]], each of them is true or false, so there are four rows: TT, TF, FT and FF.
2. By the definition of [[disjunction|0H5GKDTB01]], $p \lor q$ is false only in the row FF.
   By the definition of [[negation|0XR7A7RSXB]], $\neg (p \lor q)$ is true only in the row FF.
3. By the definition of [[conjunction|0M28ASWG8T]], $\neg p \land \neg q$ is true only when $\neg p$ and $\neg q$ are both true.
   By the definition of negation, this happens only in the row FF.
4. By steps 2 and 3, both formulas are true in the row FF and false in the other three rows, so $\neg (p \lor q) \equiv \neg p \land \neg q$.
5. By the definition of conjunction, $p \land q$ is true only in the row TT, so $\neg (p \land q)$ is false only in the row TT.
6. By the definition of disjunction, $\neg p \lor \neg q$ is false only when $\neg p$ and $\neg q$ are both false.
   This happens only in the row TT.
7. By steps 5 and 6, both formulas are false in the row TT and true in the other three rows, so $\neg (p \land q) \equiv \neg p \lor \neg q$.
8. The full table shows both laws.

| $p$ | $q$ | $\neg (p \lor q)$ | $\neg p \land \neg q$ | $\neg (p \land q)$ | $\neg p \lor \neg q$ |
|---|---|---|---|---|---|
| T | T | F | F | F | F |
| T | F | F | F | T | T |
| F | T | F | F | T | T |
| F | F | T | T | T | T |

9. In each row the third column equals the fourth, and the fifth equals the sixth. $\blacksquare$

## Idea

Each side of a De Morgan law is singled out by one special row.
For the first law that row is "both false", and for the second law it is "both true".
Since the two sides pick out the same row, they agree everywhere.

## Variants

The [[proof by natural deduction|PQ22Q2DYP0]] proves each of the four directions separately.
It shows that three directions hold in [[intuitionistic logic|Q11N8X99FK]], and that $\neg(p \land q) \to \neg p \lor \neg q$ needs the [[law of excluded middle|0RYYK8PG4S]].
The truth-table proof cannot see this difference, because it is classical at step 1, where bivalence enters.
A [[Kripke model|NGHWZ9Y7ZV]] with a root and two incomparable later worlds, $p$ true at one and $q$ at the other, refutes that direction at the root.

A second classical proof derives law (2) from law (1).
Apply law (1) to $\neg p$ and $\neg q$, and use the [[double negation law|0NFAGWH84K]]:
$$\neg(\neg p \lor \neg q) \equiv \neg\neg p \land \neg\neg q \equiv p \land q.$$
Negating both sides and using the double negation law again gives $\neg p \lor \neg q \equiv \neg(p \land q)$.
