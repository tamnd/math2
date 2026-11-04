---
tag: SWH5EJP8PS
kind: proof
name: Proof that an implication is equivalent to its contrapositive by a truth table
msc: [03B05]
proves: 04T1CT7212
uses: [0ZGC7ZESYN, 0XR7A7RSXB, 0ZNX6DQ3EJ, 06GYGS41JK, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: Proof by contrapositive
---

## Proof

We compare the [[truth tables|05RSK4Q657]] of $p \to q$ and $\neg q \to \neg p$.

1. Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]]. In classical logic, each of them is true or false, so there are four rows: TT, TF, FT and FF.
2. By the definition of [[implication|0ZNX6DQ3EJ]], $p \to q$ is false exactly when $p$ is true and $q$ is false, that is, only in the row TF.
3. Again by the definition of implication, $\neg q \to \neg p$ is false exactly when $\neg q$ is true and $\neg p$ is false.
4. By the definition of [[negation|0XR7A7RSXB]], $\neg q$ is true exactly when $q$ is false, and $\neg p$ is false exactly when $p$ is true.
5. By steps 3 and 4, $\neg q \to \neg p$ is false exactly when $p$ is true and $q$ is false, that is, only in the row TF.
6. The table is this.

| $p$ | $q$ | $\neg q$ | $\neg p$ | $p \to q$ | $\neg q \to \neg p$ |
|---|---|---|---|---|---|
| T | T | F | F | T | T |
| T | F | T | F | F | F |
| F | T | F | T | T | T |
| F | F | T | T | T | T |

7. By steps 2 and 5, the two implications have the same truth value in each row. So they are [[logically equivalent|06GYGS41JK]]: $p \to q \equiv \neg q \to \neg p$.

## Idea

An implication fails in only one situation: a true hypothesis with a false conclusion. For $\neg q \to \neg p$ this situation is "$q$ false and $p$ true". This is the very same situation in which $p \to q$ fails.
