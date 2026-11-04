---
tag: 68VBVMFJSW
kind: proof
name: Proof of De Morgan's laws by truth tables
msc: [03B05]
proves: 09PKJKA6J0
uses: [0ZGC7ZESYN, 0XR7A7RSXB, 0M28ASWG8T, 0H5GKDTB01, 06GYGS41JK, 05RSK4Q657]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
---

## Proof

We compare [[truth tables|05RSK4Q657]]. Two formulas are [[logically equivalent|06GYGS41JK]] when they agree for each of the four assignments of truth values to $p$ and $q$.

1. Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]]. In classical logic, each of them is true or false, so there are four rows: TT, TF, FT and FF.
2. We compute $\neg (p \lor q)$. By the definition of [[disjunction|0H5GKDTB01]], $p \lor q$ is false only in the row FF. By the definition of [[negation|0XR7A7RSXB]], $\neg (p \lor q)$ is true only in the row FF.
3. We compute $\neg p \land \neg q$. By the definition of [[conjunction|0M28ASWG8T]], it is true only when $\neg p$ and $\neg q$ are both true. By the definition of negation, this happens only in the row FF.
4. By steps 2 and 3, both formulas are true in the row FF and false in the other three rows. So $\neg (p \lor q) \equiv \neg p \land \neg q$.
5. We compute $\neg (p \land q)$. By the definition of conjunction, $p \land q$ is true only in the row TT. So $\neg (p \land q)$ is false only in the row TT.
6. We compute $\neg p \lor \neg q$. By the definition of disjunction, it is false only when $\neg p$ and $\neg q$ are both false. This happens only in the row TT.
7. By steps 5 and 6, both formulas are false in the row TT and true in the other three rows. So $\neg (p \land q) \equiv \neg p \lor \neg q$.
8. The full table shows both laws.

| $p$ | $q$ | $\neg (p \lor q)$ | $\neg p \land \neg q$ | $\neg (p \land q)$ | $\neg p \lor \neg q$ |
|---|---|---|---|---|---|
| T | T | F | F | F | F |
| T | F | F | F | T | T |
| F | T | F | F | T | T |
| F | F | T | T | T | T |

## Idea

Each side of a De Morgan law is singled out by one special row. For the first law that row is "both false", and for the second law it is "both true". Since the two sides pick out the same row, they agree everywhere.
