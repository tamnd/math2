---
tag: SWH5EJP8PS
kind: proof
name: Proof that an implication is equivalent to its contrapositive by a truth table
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
proves: 04T1CT7212
uses: [0ZGC7ZESYN, 0XR7A7RSXB, 0ZNX6DQ3EJ, 06GYGS41JK, 05RSK4Q657]
methods: [05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Proof

We show that $\varphi \to \psi$ and $\neg \psi \to \neg \varphi$ are false in exactly the same row of the [[truth table|05RSK4Q657]].
The truth value of each formula depends only on the truth values of $\varphi$ and $\psi$, so we may treat them as two propositional variables $p$ and $q$.

1. By the principle of [[bivalence|5DYNDW9526]], each of $p$ and $q$ is true or false, so there are four rows: TT, TF, FT and FF.
2. By the definition of [[implication|0ZNX6DQ3EJ]], $p \to q$ is false exactly when $p$ is true and $q$ is false, that is, only in the row TF.
3. By the same definition applied to $\neg q$ and $\neg p$, the formula $\neg q \to \neg p$ is false exactly when $\neg q$ is true and $\neg p$ is false.
4. By the definition of [[negation|0XR7A7RSXB]], $\neg q$ is true exactly when $q$ is false, and $\neg p$ is false exactly when $p$ is true.
5. By steps 3 and 4, $\neg q \to \neg p$ is false exactly when $p$ is true and $q$ is false, that is, only in the row TF.
6. The complete table is this.

| $p$ | $q$ | $\neg q$ | $\neg p$ | $p \to q$ | $\neg q \to \neg p$ |
|---|---|---|---|---|---|
| T | T | F | F | T | T |
| T | F | T | F | F | F |
| F | T | F | T | T | T |
| F | F | T | T | T | T |

7. By steps 2 and 5, the last two columns agree in each row.
8. So $p \to q$ and $\neg q \to \neg p$ have the same truth value under every valuation, and by definition they are [[logically equivalent|06GYGS41JK]].
9. In particular, $(p \to q) \leftrightarrow (\neg q \to \neg p)$ is T in every row, so it is a tautology, and both directions (a) and (b) hold. $\blacksquare$

## Idea

An implication fails in only one situation: a true antecedent with a false consequent.
For $\neg q \to \neg p$ this situation is "$\neg q$ true and $\neg p$ false", that is, "$q$ false and $p$ true".
This is the same situation in which $p \to q$ fails, so the two formulas fail together and hold together.
The proof uses bivalence in step 1, so it is a classical proof, and it cannot show which direction holds intuitionistically.

## Variants

The [[proof by rules of inference|QB99VRZQ4Y]] treats the two directions separately.
It shows that direction (a) needs only [[modus ponens|0Y0MQYST0M]] and the rules for negation, and that direction (b) needs the [[law of excluded middle|0RYYK8PG4S]].

An algebraic variant rewrites both sides with $p \to q \equiv \neg p \lor q$.
Then $\neg q \to \neg p \equiv \neg\neg q \lor \neg p \equiv q \lor \neg p$, which equals $\neg p \lor q$ by commutativity of $\lor$.
This variant uses the double negation law $\neg\neg q \equiv q$, which is again a classical step.
