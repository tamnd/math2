---
tag: VA6BNNY2YC
kind: statement
role: theorem
name: Church's theorem on undecidability of first-order logic
msc: [03B25, 03D35, 03B10]
uses: [086QKPF0A6, DKFGQTRYZE, PPGD5KW8JC, 758EYCN27B, Z7TN2B35B0, WQ1ZE255SF]
about: [086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Entscheidungsproblem
---

## Statement

There is a finite signature $L$ with the following property.
The set of valid first-order [[sentences|DKFGQTRYZE]] of $L$, that is, of the $L$-sentences true in every $L$-structure, is not a [[computable set|PPGD5KW8JC]].
Equivalently, no algorithm decides, for an arbitrary $L$-sentence, whether it is valid in [[first-order logic|086QKPF0A6]].

## Remarks

Church proved the result in 1936 with the lambda calculus, and Turing proved it independently with [[Turing machines|758EYCN27B]].
In Turing's approach, one builds from each Turing machine $M$ a sentence $\varphi_M$ that is valid exactly when $M$ halts on the empty input.
A decision procedure for validity would then solve the [[halting problem|Z7TN2B35B0]], which is impossible.

The theorem gives a negative answer to Hilbert's Entscheidungsproblem.
It holds for every signature that contains a binary relation symbol.
It fails for signatures with only unary relation symbols: monadic first-order logic is decidable.

By [[Gödel's completeness theorem|WQ1ZE255SF]], the valid sentences are exactly the provable ones, so they form a computably enumerable set.
So validity is semi-decidable but not decidable.

## Explanations

### L1 human

The theorem says that there is no general mechanical method to decide whether a first-order sentence is logically true.
A computer can list all proofs and so confirm every valid sentence eventually, but it cannot always confirm that a sentence is not valid.

### L2 human

Church's theorem is the first-order counterpart of the undecidability of the halting problem.
It is the reason why automated theorem provers can only search for proofs, and may run forever.
Decidable fragments, such as monadic logic, and decidable theories, such as [[Presburger arithmetic|B66JYY3K58]], are therefore valuable in computer science.
