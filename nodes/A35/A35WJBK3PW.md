---
tag: A35WJBK3PW
kind: proof
name: Proof of the double negation law by a truth table
msc: [03B05]
proves: 0NFAGWH84K
uses: [0ZGC7ZESYN, 0XR7A7RSXB, 06GYGS41JK, 05RSK4Q657]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
---

## Proof

We compare the [[truth tables|05RSK4Q657]] of $\neg \neg p$ and $p$.

1. Let $p$ be a [[proposition|0ZGC7ZESYN]]. In classical logic, $p$ is either true or false.
2. Suppose $p$ is true. By the definition of [[negation|0XR7A7RSXB]], $\neg p$ is false. Applying the definition again, $\neg \neg p$ is true.
3. Suppose $p$ is false. By the definition of negation, $\neg p$ is true. Applying the definition again, $\neg \neg p$ is false.
4. The truth table is this.

| $p$ | $\neg p$ | $\neg \neg p$ |
|---|---|---|
| T | F | T |
| F | T | F |

5. By steps 1, 2 and 3, $\neg \neg p$ and $p$ have the same truth value for each truth value of $p$.
6. So $\neg \neg p$ and $p$ are [[logically equivalent|06GYGS41JK]], that is, $\neg \neg p \equiv p$.

## Idea

Negation swaps true and false. Swapping twice gives back the original truth value, so $\neg \neg p$ always agrees with $p$.
