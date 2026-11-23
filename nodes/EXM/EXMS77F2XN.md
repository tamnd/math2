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

The lemma says that in the G3 calculi most rules can be run backwards: whenever the conclusion is derivable, so are the premises, by derivations that are no higher.

Use the calculi G3cp and G3ip of the [[definition of contraction-free sequent calculi|KP5KA51FC4]].
Write $\vdash_n S$ when the sequent $S$ has a derivation of height at most $n$.
A rule is *height-preserving invertible* when, for every instance and every $n$, if its conclusion satisfies $\vdash_n$, then each of its premises does.
A premise of a rule is *invertible* when the conclusion of an instance is derivable only if that premise is.

1. **G3cp.** Every rule of G3cp is height-preserving invertible.
2. **G3ip, the invertible rules.** In G3ip, the rules L${\wedge}$, R${\wedge}$, L${\vee}$ and R${\to}$ are height-preserving invertible.
   Moreover, if $\vdash_n A \to B, \Gamma \Rightarrow C$, then $\vdash_n B, \Gamma \Rightarrow C$.
3. **G3ip, the other rules.** The rule R${\vee}$ is not invertible, and the left premise of L${\to}$ is not invertible.

## Remarks

### Proof search without backtracking

We look for a derivation of $\Rightarrow (p \to q) \vee (q \to p)$ in G3cp, building it from the bottom.

1. R${\vee}$ backwards gives $\Rightarrow p \to q, q \to p$.
2. R${\to}$ backwards gives $p \Rightarrow q, q \to p$.
3. R${\to}$ backwards gives $q, p \Rightarrow q, p$, which is an axiom.

At each step we picked a rule without looking ahead, and part 1 says this was safe: had the sequent been derivable and our first move been different, our premises would still be derivable.
In G3ip the same search fails at the first step.
There R${\vee}$ must keep only one disjunct, and neither $\Rightarrow p \to q$ nor $\Rightarrow q \to p$ is derivable, which is what part 3 warns about.

### Why each hypothesis is needed

The axioms must be atomic.
If $A \wedge B, \Gamma \Rightarrow \Delta, A \wedge B$ were an axiom, then the inverse of L${\wedge}$ would need a derivation of $A, B, \Gamma \Rightarrow \Delta, A \wedge B$ of height $0$.
That sequent is in general not an axiom, so height preservation would fail.

The premises must keep all the information of the conclusion.
In LK, the rule ${\vee}$R of [[Gentzen's calculus|PZX9J3VEMT]] infers $\Gamma \Rightarrow \Delta, A \vee B$ from $\Gamma \Rightarrow \Delta, A$, and it loses $B$.
It is not invertible: $\Rightarrow p \vee \neg p$ is derivable, but neither $\Rightarrow p$ nor $\Rightarrow \neg p$ is.
G3cp avoids this by keeping both disjuncts in one premise, and the single succedent of G3ip makes that impossible.

### What it gives you

The lemma gives a decision procedure for G3cp.
Apply rules backwards in any order; each premise has fewer connectives than its conclusion, so the search ends with sequents of propositional variables and $\bot$.
By part 1, the sequent is derivable if and only if every final sequent is an axiom, whatever order we chose.

It also gives completeness of G3cp.
A sequent of variables and $\bot$ that is not an axiom is falsified by the valuation that makes its antecedent variables true and the others false.
Each rule of G3cp has a valid conclusion exactly when all premises are valid, so a valid sequent leads only to valid final sequents, which are axioms.

Finally, height-preserving invertibility is the main lemma in the proof that contraction is height-preserving admissible in G3cp and G3ip.

### The converse

The converse of invertibility is the rule itself: if all premises are derivable, so is the conclusion.
So in G3cp, the conclusion of a rule is derivable exactly when all its premises are.
In G3ip this equivalence fails for R${\vee}$ and for L${\to}$, by part 3.

### Generalizations

The first-order calculus G3c has the same property for all its rules, where the premise of L${\forall}$ and R${\exists}$ keeps the principal formula.
Height-preserving inversion also holds for all rules of the G3-style [[labelled calculi|F46GV42XCE]] for modal logics.
In [[focused calculi|AMMKNENT3R]], the invertible rules form the asynchronous phase, which is applied eagerly.

### Watch out

Invertible is not the same as admissible.
An invertible rule is a rule of the calculus that can also be read upward, while an admissible rule is one that may be added without new derivable sequents.
The inverse of R${\wedge}$, from $\Gamma \Rightarrow \Delta, A \wedge B$ to $\Gamma \Rightarrow \Delta, A$, is admissible in G3cp by part 1, and it is not a rule of the calculus.

## History

Oiva Ketonen gave a classical sequent calculus with invertible propositional rules in his thesis of 1944.
Kleene introduced the calculi G3 in his *Introduction to Metamathematics* of 1952.
The height-preserving form of the lemma is standard in the books *Basic Proof Theory* of Troelstra and Schwichtenberg and *Structural Proof Theory* of Negri and von Plato.

## Explanations

### L1 human

A rule of a proof system says: if these statements hold, then that statement holds.
A rule is invertible if we can also go back: whenever the conclusion holds, every premise holds.
For such a rule, using it in a search for a proof never leads into a dead end.

### L2 human

Here is inversion on a small derivation in G3cp.
The sequent $p \wedge q \Rightarrow q \wedge p$ has a derivation of height $2$: R${\wedge}$ from $p \wedge q \Rightarrow q$ and $p \wedge q \Rightarrow p$, each by L${\wedge}$ from an axiom.
Inverting L${\wedge}$ asks for $p, q \Rightarrow q \wedge p$ with height at most $2$.
The proof of the lemma removes $p \wedge q$ in both premises, which gives the axioms $p, q \Rightarrow q$ and $p, q \Rightarrow p$, and then repeats R${\wedge}$, for height $1$.
The typical use is in a proof by induction on height, where a principal formula must be taken apart one level up.
A trap is to expect inversion for every rule of G3ip, which fails for R${\vee}$ and for the left premise of L${\to}$.

### L3 human

Invertibility is the proof-theoretic form of the fact that a rule is an equivalence, not only an implication.
The height-preserving form gives contraction and cut admissibility by simple inductions on height.
The split between invertible and non-invertible rules is the base of [[focusing|AMMKNENT3R]] and of goal-directed proof search.
In intuitionistic logic the non-invertible rules are where the search must branch, and propositional provability there is PSPACE-complete, while classical validity is coNP-complete.
