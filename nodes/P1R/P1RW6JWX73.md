---
tag: P1RW6JWX73
kind: problem
name: Hilbert's program
msc: [03A05, 03F25, 03F30]
uses: [46JCQ6KDA4, 0QFT7Z76N5]
about: [EFFRJFW67Y]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert's_program
same_as:
  wikidata: Q968548
  wikipedia: Hilbert's program
history:
  posed_by: "David Hilbert"
  first_stated: "1922"
---

## Problem

Write all of classical mathematics as a formal system with finitely describable axioms and rules of inference.
Then prove, by finitary means only, that this formal system is consistent.
Here a proof is finitary when it reasons only about finite strings of symbols in a concrete, checkable way.
Consistency means that no formula $\varphi$ is derivable together with its negation $\neg \varphi$.

## Remarks

The program is the main form of [[formalism|46JCQ6KDA4]].
It also asked for a proof of completeness: every statement of the system should be provable or refutable.
Gödel's [[incompleteness theorems|X9WYNYE29C]] of 1931 showed that the program cannot be carried out as first intended.
A consistent, effectively axiomatized system that contains enough arithmetic is incomplete.
Such a system also cannot prove its own consistency.
In 1936 Gerhard Gentzen proved the consistency of the [[Peano axioms|0QFT7Z76N5]] of first-order arithmetic, see [[Gentzen's consistency proof|QPV0HNP22S]].
His proof uses transfinite induction up to the ordinal $\varepsilon_0$, which goes beyond the finitary means of the original program.
Partial versions of the program are studied in [[proof theory|N4EDJNMTEF]] and in [[reverse mathematics|7SQS69T17R]].

## Explanations

### L1 human

Hilbert wanted to put all of mathematics on a safe base.
First, write every theorem as the result of fixed rules applied to fixed axioms, like moves in a game.
Second, show with simple, finite reasoning that the game can never produce a contradiction such as $0 = 1$.
Gödel showed that the second step is impossible in the strong form that Hilbert hoped for.
