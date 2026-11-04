---
tag: ZNQN1JW1V3
kind: proof
name: Proof of the law of excluded middle by a truth table
msc: [03B05]
proves: 0RYYK8PG4S
uses: [0ZGC7ZESYN, 0XR7A7RSXB, 0H5GKDTB01, 05RSK4Q657]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
---

## Proof

We compute the [[truth table|05RSK4Q657]] of $p \lor \neg p$.

1. Let $p$ be a [[proposition|0ZGC7ZESYN]]. In classical logic, $p$ has exactly one of the two truth values, true or false.
2. Suppose $p$ is true. By the definition of [[disjunction|0H5GKDTB01]], $p \lor \neg p$ is true, since its first part is true.
3. Suppose $p$ is false. By the definition of [[negation|0XR7A7RSXB]], $\neg p$ is true.
4. In the case of step 3, $p \lor \neg p$ is true by the definition of disjunction, since its second part is true.
5. The two rows of the truth table are these.

| $p$ | $\neg p$ | $p \lor \neg p$ |
|---|---|---|
| T | F | T |
| F | T | T |

6. By step 1, steps 2 and 4 cover every possible truth value of $p$. In each case $p \lor \neg p$ is true. So $p \lor \neg p$ is true for each proposition $p$.

## Idea

In classical logic a proposition has only two possible truth values. If $p$ is true, the first part of $p \lor \neg p$ is true. If $p$ is false, the second part is true. Either way the disjunction is true.
