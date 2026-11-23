---
tag: F46GV42XCE
kind: concept
name: Labeled sequent calculus
msc: ["03F05", "03B45"]
topics: [R10RMQCJQX]
audience: research
uses: [W72CA3R9MP, C3RZY20ETK, NGHWZ9Y7ZV, XBCYFDPS2F]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Dov_Gabbay
    locator: Work
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: References
---

## Summary

A labeled sequent calculus writes the world next to each formula, so a sequent becomes a small piece of a Kripke model.
For example, the sequent $x : \Box p, x R y \Rightarrow y : p$ reads "if $\Box p$ holds at $x$ and $y$ is reachable from $x$, then $p$ holds at $y$".
Exactly, a *labeled sequent calculus* for a [[modal logic|C3RZY20ETK]] is a [[sequent calculus|W72CA3R9MP]] whose sequents contain labeled formulas $x : A$ and relational atoms $x R y$.
Its rules for $\Box$ and $\Diamond$ follow the clauses of [[Kripke semantics|NGHWZ9Y7ZV]], with a fresh label for each new world.
Each frame condition becomes a rule that acts on relational atoms only.
The [[definition|VW8XP95XCB]] gives Negri's calculus G3K and its extensions by geometric frame rules.
For every frame class defined by geometric implications, this method gives a calculus in which weakening, contraction and cut are admissible.

## Motivation

Many modal logics have no cut-free ordinary sequent calculus, and each known calculus needs its own cut-elimination proof.
Kripke semantics, by contrast, treats all normal modal logics in one way: a logic is fixed by a condition on the [[accessibility relation|XBCYFDPS2F]].
A labeled calculus brings the semantics into the syntax.
The truth clause for $\Box A$ at $x$ quantifies over the worlds $y$ with $x R y$, and the labeled rules for $\Box$ say exactly this.
A frame condition such as reflexivity then becomes a structural rule on relational atoms, so the logical rules stay the same for all logics.
This makes one cut-elimination proof work for a large class of modal logics.

## Notation

Negri writes $x : A$ and $x R y$, and names the calculi G3K, G3KT, G3S4 and so on.
Other authors write $x \Vdash A$, $A^x$ or $(x, A)$ for labeled formulas.
In some systems relational atoms may appear in the succedent, and some systems use natural deduction instead of sequents.

## Remarks

### A first derivation

The calculus G3KT adds to G3K the rule Ref, which infers $\Gamma \Rightarrow \Delta$ from $x R x, \Gamma \Rightarrow \Delta$.
Read upward, Ref creates the atom $x R x$.
The rule ${\Box}$L can then use $x$ itself as a world reachable from $x$:
$$x : p, x : \Box p, x R x \Rightarrow x : p.$$
That sequent is initial, and ${\Box}$L, Ref and ${\to}$R turn it into $\Rightarrow x : \Box p \to p$, the axiom T.
The [[example of the axiom T|HDWFDRR42X]] gives each step and a countermodel that shows G3K alone does not derive T.

### A derivation with two new worlds

The calculus G3K4 adds the rule Trans, which infers $x R y, y R z, \Gamma \Rightarrow \Delta$ from $x R z, x R y, y R z, \Gamma \Rightarrow \Delta$.
To prove $x : \Box\Box p$, the rule ${\Box}$R is applied twice, with a fresh world $y$ and then a fresh world $z$.
That leaves the goal $x : \Box p, x R y, y R z \Rightarrow z : p$.
Trans adds $x R z$, and ${\Box}$L sends $x : \Box p$ to $z$, which closes the branch.
The [[example of the axiom 4|2N9E5E8HRX]] gives the derivation of $\Box p \to \Box\Box p$ and checks both eigenvariable conditions.

### Symmetry and seriality

The calculus G3KB adds the rule Sym, which infers $x R y, \Gamma \Rightarrow \Delta$ from $y R x, x R y, \Gamma \Rightarrow \Delta$.
It derives $p \to \Box\Diamond p$.
After ${\to}$R and ${\Box}$R with a fresh $y$, the goal is $x R y, x : p \Rightarrow y : \Diamond p$.
Sym adds $y R x$, and ${\Diamond}$R with that atom adds $x : p$ to the succedent:
$$y R x, x R y, x : p \Rightarrow y : \Diamond p, x : p.$$
This sequent is initial.

The calculus G3KD adds the rule Ser, which infers $\Gamma \Rightarrow \Delta$ from $x R y, \Gamma \Rightarrow \Delta$ with $y$ fresh.
It derives $\Box p \to \Diamond p$.
After ${\to}$R, Ser adds $x R y$, then ${\Box}$L adds $y : p$ on the left and ${\Diamond}$R adds $y : p$ on the right.

### What it is not

Provability logic GL is the logic of transitive frames with no infinite ascending $R$-chain.
That frame condition is not first-order, so it is not a geometric implication and gives no frame rule.
The [[non-example|QKATP0KQH2]] proves this with the compactness theorem.
GL still has a labeled calculus, but it changes the rule ${\Box}$R instead of adding a frame rule.

An ordinary modal sequent calculus, such as the calculus for K with the rule from $\Gamma \Rightarrow A$ to $\Box\Gamma \Rightarrow \Box A$, has no labels.
Its rules do not mention worlds, so a frame condition cannot be added to it as a rule on relational atoms.

### Why cut elimination is uniform

Each rule is sound for the frames that satisfy the conditions of the calculus.
Frame rules act only on relational atoms, which never occur in the succedent, so a cut formula is never principal in a frame rule.
A cut therefore moves above every frame rule without a new case for each logic.
For a set of geometric frame rules with the closure condition, weakening, contraction and label substitution are height-preserving admissible, and every rule is height-preserving invertible.
Cut is admissible, by Negri's theorem in the [[definition|VW8XP95XCB]].
A cut-free derivation has the subformula property for labeled formulas.
When backward proof search fails, the open sequent often describes a Kripke countermodel, because its atoms already list worlds and accessibility.

### Watch out

The eigenvariable condition matters.
In ${\Box}$R and ${\Diamond}$L the new label must not occur in the conclusion, and without that condition ${\Box}$R would derive $x : p \Rightarrow x : \Box p$ from $x R x, x : p \Rightarrow x : p$.

The rule ${\Box}$L keeps its principal formula $x : \Box A$ in the premise.
Without that copy, the rule cannot be used again for another world, and contraction is no longer admissible.

The closure condition matters too.
Without the contracted instance of Eucl, which infers $x R y, \Gamma \Rightarrow \Delta$ from $y R y, x R y, \Gamma \Rightarrow \Delta$, contraction of relational atoms is not admissible.

### History

Dov Gabbay developed a general theory of labeled deductive systems.
Sara Negri proved cut elimination for labeled calculi with geometric frame rules in her 2005 paper "Proof analysis in modal logic", which also gives the calculus for GL.
Her calculi extend the G3 calculi of the 2001 textbook "Structural proof theory" by Negri and Jan von Plato.

### Try it

Which atom does ${\Box}$L need in order to turn $x : \Box p, x R y \Rightarrow y : p$ into an initial sequent?
It needs $x R y$, which is already there, and it adds $y : p$ to the antecedent.

Derive $x : \Box(p \wedge q) \Rightarrow x : \Box p$ in G3K.
${\Box}$R with a fresh $y$ gives the goal $x R y, x : \Box(p \wedge q) \Rightarrow y : p$.
${\Box}$L adds $y : p \wedge q$, ${\wedge}$L splits it into $y : p, y : q$, and the sequent is initial.

## Explanations

### L1 human

A modal statement such as "necessarily $A$" says that $A$ holds in every world that can be reached from here.
A labeled calculus gives each world a name, like $x$ or $y$, and writes "$x : A$" for "$A$ holds at $x$".
It also writes "$x R y$" for "$y$ can be reached from $x$".
The proof rules then follow this meaning directly.
To prove "necessarily $A$" at $x$, we take a new world $y$ reachable from $x$ and prove $A$ at $y$.

### L2 human

We try to derive $\Box p \to p$ in G3K, without the rule Ref, and read a countermodel off the failure.
Backward ${\to}$R gives the goal $x : \Box p \Rightarrow x : p$.
The sequent is not initial, and no rule applies: ${\Box}$L needs an atom $x R y$, and there is none.
So the search fails.
The open sequent describes a model: one world $x$, nothing reachable from $x$, and $p$ false at $x$.
In that model $\Box p$ holds at $x$ and $p$ fails, so $\Box p \to p$ is not valid in all frames.
The typical use of this reading is to find countermodels during proof search.
Watch out: the countermodel takes only the atoms that the search produced, so a frame rule such as Ref would add $x R x$ and change it.

### L3 human

Labeled calculi make the semantics part of the syntax, and that gives a uniform proof theory for all logics with geometric frame conditions.
The same idea gives labeled calculi for intuitionistic and intermediate logics, where the relation is the order of a Kripke model.
Compared with [[hypersequent calculi|73J7F0FN4A]] and [[display calculi|2Q62W689SC]], labeled calculi cover many frame conditions directly, but their derivations use symbols that are not formulas of the logic.
