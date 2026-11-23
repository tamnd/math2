---
tag: TTCRX3NFNY
kind: topic
name: Proof systems for first-order logic
msc: ["03B10", "03F03"]
topics: [DYJ0KGTPMR]
---

## Summary

From "every man is mortal" and "Socrates is a man" we infer "Socrates is mortal", and a proof system for first-order logic turns such steps into precise rules that a machine can check.
Each system defines a relation $\Gamma \vdash \varphi$, "$\varphi$ has a derivation from $\Gamma$", by finite objects built with fixed rules.
The systems differ in shape.
A Hilbert-style calculus uses many axioms and one or two rules, natural deduction uses rules that introduce and remove each connective, and the sequent calculus manipulates whole sequents $\Gamma \Rightarrow \Delta$.
Tableaux and resolution search for a counterexample and prove $\varphi$ when the search fails.

The quantifiers need the most care in every system.
A rule may infer $\forall x\, \varphi$ only when $x$ is arbitrary, and a term may replace $x$ only when no quantifier captures its variables.
The generalization and deduction theorems, and the eigenvariable conditions of natural deduction and the sequent calculus, all express these two points.

The main result is that all these systems prove the same sentences, and these are exactly the logical consequences $\Gamma \models \varphi$ in the sense of [[mathematical logic|DYJ0KGTPMR]].
Equality needs its own rules in each system, and those rules decide how well a cut-free calculus or an automated prover handles it.

## Remarks

### Reading order

1. [[Hilbert-style predicate calculus|N95HV0VWSM]]: see how axioms and modus ponens give derivations, and how the variant with a rule of generalization differs.
2. [[Generalization theorem|VKSK35Y52Z]]: learn when a deduction about an arbitrary $x$ gives a deduction of $\forall x\, \varphi$.
3. [[Deduction theorem for predicate logic|8M9ZFDR4DH]]: learn to turn hypotheses into antecedents, and why the variant with generalization needs a restriction.
4. [[Natural deduction|6KT3BJZ7D1]]: write proofs with introduction and elimination rules, and check the eigenvariable conditions for the quantifiers.
5. [[Fitch-style natural deduction|2B6XC7XJA8]]: write the same proofs as nested subproofs with boxed constants.
6. [[Sequent calculus|W72CA3R9MP]]: work with Gentzen's LK and LJ, their structural rules and the cut rule.
7. [[Semantic tableaux|WGWBBVE8GX]]: refute a set of sentences with a tree, and see why systematic tableaux are sound and complete.
8. [[Hintikka set|RJNDEG07R1]]: build a model from the sentences on an open branch.
9. [[First-order resolution|DEB3CF4Z2D]]: put sentences in clause form and refute them with unification and the resolution rule.
10. [[Equivalence of proof systems|A9AAHN4BMH]]: see that the calculi derive the same sentences, exactly the logical consequences.
11. [[Rules for equality|Y90Z13AXY8]]: add equality to each calculus, from the Hilbert axioms to paramodulation.

### Prerequisites

- [[First-order languages and syntax|PSRDJXRW53]]: terms, formulas, free variables and substitution.
- [[Structures, satisfaction and truth|NJDME6F845]]: models and logical consequence.
- [[The propositional calculus|JDK63589SA]] and the propositional [[Hilbert system|1MGMQX43B8]].
- [[Proof strategies by logical form|872K5XB580]] and [[structured and hierarchical proofs|H2W8D7BMSW]]: the informal proofs that the calculi make formal.
