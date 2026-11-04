---
tag: FAG05D5RT9
kind: proof
name: Proof of Lyndon's interpolation theorem
proves: BRDT1BT7WW
sources:
  - wikipedia: en:2056790@r1321826961
    locator: Craig interpolation, section Proof of Craig's interpolation theorem
    note: adopted
    mention: wikipedia://en/2056790#6M9Y
    sections: [Proof]
---

## Proof

We present here a [[constructive proof|01XM7JEKHY]] of the Craig interpolation theorem for [[propositional logic|09K9MWD2QQ]].

Since the above proof is constructive, one may extract an algorithm for computing interpolants. Using this algorithm, if *n* = |*atoms*(φ') − *atoms*(ψ)|, then the interpolant ρ has *O*(exp(*n*)) more logical connectives than φ (see Big O Notation for details regarding this assertion). Similar constructive proofs may be provided for the basic modal logic K, intuitionistic logic and μ-calculus, with similar complexity measures.

Craig interpolation can be proved by other methods as well. However, these proofs are generally non-constructive:

- model-theoretically, via Robinson's joint consistency theorem: in the presence of compactness, negation and conjunction, Robinson's joint consistency theorem and Craig interpolation are equivalent.
- proof-theoretically, via a sequent calculus. If cut elimination is possible and as a result the subformula property holds, then Craig interpolation is provable via induction over the derivations.
- algebraically, using amalgamation theorems for the variety of algebras representing the logic.
- via translation to other logics enjoying Craig interpolation.
