---
tag: TTCRX3NFNY
kind: topic
name: Proof systems for first-order logic
msc: ["03B10", "03F03"]
topics: [DYJ0KGTPMR]
---

## Summary

This topic is a part of [[mathematical logic|DYJ0KGTPMR]].
It covers the standard deductive calculi for first-order logic, their rules for quantifiers and equality, and the proofs that the calculi are equivalent.
Each calculus defines a relation $\Gamma \vdash \varphi$ by finite derivations, and the topic proves that these relations agree with logical consequence $\Gamma \models \varphi$.

## Remarks

### Reading order

1. [[Hilbert-style predicate calculus|~4ea8b834]]: axioms, modus ponens, and the variant with a rule of generalization.
2. [[Generalization theorem|~380337c7]]: a deduction about an arbitrary $x$ gives a deduction of $\forall x\, \varphi$.
3. [[Deduction theorem for predicate logic|8M9ZFDR4DH]]: hypotheses become antecedents, and the restriction in the variant with generalization.
4. [[Natural deduction|6KT3BJZ7D1]]: introduction and elimination rules, with eigenvariable conditions for the quantifiers.
5. [[Fitch-style natural deduction|~1528beb9]]: natural deduction written as nested subproofs with boxed constants.
6. [[Sequent calculus|W72CA3R9MP]]: Gentzen's LK and LJ, structural rules and cut.
7. [[Semantic tableaux|~78632a29]]: refutation trees, with soundness and completeness of systematic tableaux.
8. [[Hintikka set|~03b04954]]: the sets of sentences that an open branch gives, and their models.
9. [[First-order resolution|~787204b5]]: clause form, unification and the resolution rule.
10. [[Equivalence of proof systems|~c9d242a1]]: the four calculi derive the same sentences, exactly the logical consequences.
11. [[Rules for equality|~65701c23]]: the equality axioms and rules in each calculus.

### Prerequisites

- [[First-order languages and syntax|PSRDJXRW53]]: terms, formulas, free variables and substitution.
- [[Structures, satisfaction and truth|NJDME6F845]]: models and logical consequence.
- [[The propositional calculus|JDK63589SA]] and the propositional [[Hilbert system|1MGMQX43B8]].
- [[Proof strategies by logical form|872K5XB580]] and [[structured and hierarchical proofs|H2W8D7BMSW]]: the informal proofs that the calculi make formal.
