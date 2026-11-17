---
tag: EXMS77F2XN
kind: statement
role: lemma
name: Inversion lemma
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
uses: [KP5KA51FC4, W72CA3R9MP]
about: [BZ59F5GBRR]
proofs: [APDYXQKZNV]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Structural rules
---

## Statement

Use the calculi G3cp and G3ip of the [[definition of contraction-free sequent calculi|KP5KA51FC4]].
Write $\vdash_n S$ when the sequent $S$ has a derivation of height at most $n$.
A rule is *height-preserving invertible* when, for every instance and every $n$, if its conclusion satisfies $\vdash_n$, then each of its premises does.
A premise of a rule is *invertible* when the conclusion of an instance is derivable only if that premise is.

1. **G3cp.** Every rule of G3cp is height-preserving invertible.
2. **G3ip, the invertible rules.** In G3ip, the rules L${\wedge}$, R${\wedge}$, L${\vee}$ and R${\to}$ are height-preserving invertible. If $\vdash_n A \to B, \Gamma \Rightarrow C$, then $\vdash_n B, \Gamma \Rightarrow C$.
3. **G3ip, the other rules.** The rule R${\vee}$ is not invertible, and the left premise of L${\to}$ is not invertible.

## Remarks

### Why each hypothesis is needed

The axioms must be atomic.
If $A \wedge B, \Gamma \Rightarrow \Delta, A \wedge B$ were an axiom, then the inverse of L${\wedge}$ would need a derivation of $A, B, \Gamma \Rightarrow \Delta, A \wedge B$ of height $0$.
This sequent is not an axiom, so height preservation would fail.
The premises must keep all the information of the conclusion.
In LK, the rule ${\vee}$R of [[Gentzen's calculus|PZX9J3VEMT]] infers $\Gamma \Rightarrow \Delta, A \vee B$ from $\Gamma \Rightarrow \Delta, A$, and it loses $B$.
It is not invertible: $\Rightarrow p \vee \neg p$ is derivable, but neither $\Rightarrow p$ nor $\Rightarrow \neg p$ is.
In G3ip, the single succedent forces a choice in R${\vee}$, and part 3 shows that this choice cannot be undone.

### Consequences

- **A decision procedure for G3cp.** Apply rules backwards in any order. Each premise has fewer connectives than the conclusion, so the search ends with sequents of propositional variables and $\bot$.
- By part 1, the sequent is derivable if and only if every final sequent is an axiom, and the order of the rules does not matter.
- **Completeness of G3cp.** A sequent of variables and $\bot$ that is not an axiom is falsified by the valuation that makes its antecedent variables true and the others false.
- Each rule of G3cp has a valid conclusion exactly when all premises are valid. So a valid sequent leads only to valid final sequents, which are axioms.
- **Admissibility of contraction.** Height-preserving invertibility is the main lemma in the proof that contraction is height-preserving admissible in G3cp and G3ip.

### Converse

The converse of invertibility is the rule itself: if all premises are derivable, so is the conclusion.
So in G3cp, the conclusion of a rule is derivable exactly when all premises are.
In G3ip this equivalence fails for R${\vee}$ and for L${\to}$, by part 3.

### Generalizations

The first-order calculus G3c has the same property for all its rules, where the premise of L${\forall}$ and R${\exists}$ keeps the principal formula.
Height-preserving inversion also holds for all rules of the G3-style [[labelled calculi|F46GV42XCE]] for modal logics.
In [[focused calculi|AMMKNENT3R]], the invertible rules form the asynchronous phase, which is applied eagerly.

## History

Kleene introduced the calculi G3 in his *Introduction to Metamathematics* of 1952.
The height-preserving form of the lemma is standard in the books *Basic Proof Theory* of Troelstra and Schwichtenberg and *Structural Proof Theory* of Negri and von Plato.

## Explanations

### L1 human

A rule of a proof system says: if these statements hold, then that statement holds.
A rule is invertible if we can also go back: whenever the conclusion holds, every premise holds.
For such a rule, using it in a search for a proof never leads into a dead end.

### L2 human

We decide $\Rightarrow (p \to q) \vee (q \to p)$ in G3cp.

1. R${\vee}$ backwards gives $\Rightarrow p \to q, q \to p$.
2. R${\to}$ backwards gives $p \Rightarrow q, q \to p$.
3. R${\to}$ backwards gives $q, p \Rightarrow q, p$, which is an axiom.

So the sequent is derivable, and by part 1 no other order of rules could fail.
A trap is to use the same search in G3ip: there R${\vee}$ must choose $p \to q$ or $q \to p$, and neither is derivable.

### L3 human

Invertibility is the proof-theoretic form of the fact that a rule is an equivalence, not only an implication.
The height-preserving form gives contraction and cut admissibility by simple inductions on height.
The split between invertible and non-invertible rules is the base of [[focusing|AMMKNENT3R]] and of goal-directed proof search.
In intuitionistic logic, the non-invertible rules are where the search must branch, which explains the higher complexity of the decision problem.
