---
tag: ~fddc9de5
kind: concept
name: Labelled sequent calculus
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

A *labelled sequent calculus* for a [[modal logic|C3RZY20ETK]] is a [[sequent calculus|W72CA3R9MP]] whose sequents contain labelled formulas $x : A$, read "$A$ holds at world $x$", and relational atoms $x R y$, read "$y$ is accessible from $x$".
Its rules for $\Box$ and $\Diamond$ follow the clauses of [[Kripke semantics|NGHWZ9Y7ZV]], with a fresh label for a new world, and each frame condition becomes a rule that acts on relational atoms.
The [[definition|~aff1be18]] gives Negri's calculus G3K and its extensions by geometric frame rules.
For every frame class defined by geometric implications, this method gives a calculus in which weakening, contraction and cut are admissible.

## Motivation

Many modal logics have no cut-free ordinary sequent calculus, and each known calculus needs its own cut-elimination proof.
Kripke semantics, by contrast, treats all normal modal logics in one way: a logic is fixed by a condition on the [[accessibility relation|XBCYFDPS2F]].
A labelled calculus brings the semantics into the syntax.
The truth clause for $\Box A$ at $x$ quantifies over the worlds $y$ with $x R y$, and the labelled rules for $\Box$ say exactly this.
A frame condition such as reflexivity then becomes a structural rule on relational atoms, so the logical rules stay the same for all logics.
This makes one cut-elimination proof work for a large class of modal logics.

## Notation

Negri writes $x : A$ and $x R y$, and names the calculi G3K, G3KT, G3S4 and so on.
Other authors write $x \Vdash A$, $A^x$ or $(x, A)$ for labelled formulas.
In some systems relational atoms may appear in the succedent, and some systems use natural deduction instead of sequents.

## Remarks

### Examples

- The calculus G3K for the logic K, with the rules ${\Box}$L, ${\Box}$R, ${\Diamond}$L and ${\Diamond}$R of the [[definition|~aff1be18]].
- G3KT, which adds the rule Ref. It derives $\Box p \to p$; the [[example of the axiom T|~c9b5ac2c]] gives the derivation.
- G3K4, which adds the rule Trans. It derives $\Box p \to \Box\Box p$; the [[example of the axiom 4|~bdb8464b]] gives the derivation.
- G3KB, which adds the rule Sym. It derives $p \to \Box\Diamond p$: ${\Diamond}$R uses the atom $y R x$ that Sym adds, and the premise closes with $x : p$ on both sides.
- G3KD, which adds the rule Ser with a fresh label. It derives $\Box p \to \Diamond p$, because Ser provides a world $y$ with $x R y$.

### Non-examples

- Provability logic GL is the logic of transitive frames with no infinite ascending $R$-chains. That frame condition is not first-order, so it is not a geometric implication and gives no frame rule; the [[non-example|~7950a2ee]] proves this.
- An ordinary modal sequent calculus, such as the calculus for K with the rule from $\Gamma \Rightarrow A$ to $\Box\Gamma \Rightarrow \Box A$, has no labels. Its rules do not mention worlds, and frame conditions cannot be added as rules on relational atoms.

### Basic properties

- Each rule is sound for the frames that satisfy the conditions of the calculus.
- For a set of geometric frame rules with the closure condition, weakening, contraction and label substitution are height-preserving admissible, all rules are height-preserving invertible, and cut is admissible. This is Negri's theorem, stated in the [[definition|~aff1be18]].
- A cut-free derivation has the subformula property for labelled formulas.
- Failed backward proof search can often be read off as a Kripke countermodel, because the sequents already describe worlds and accessibility.

### History

Gabbay developed a general theory of labelled deductive systems.
Negri proved cut elimination for labelled calculi with geometric frame rules in her paper "Proof analysis in modal logic".
The calculus extends the G3 calculi of the 2001 textbook "Structural proof theory" by Negri and von Plato.

### Common errors

- Ignoring the eigenvariable condition. In ${\Box}$R and ${\Diamond}$L the new label must not occur in the conclusion.
- Dropping the repeated principal formula in ${\Box}$L. Without $x : \Box A$ in the premise, the rule cannot be used again for another world, and contraction is no longer admissible.
- Forgetting the closure condition. Without the contracted instance of Eucl, contraction of relational atoms is not admissible.

## Explanations

### L1 human

A modal statement such as "necessarily $A$" says that $A$ holds in every world that can be reached from here.
A labelled calculus gives each world a name, like $x$ or $y$, and writes "$x : A$" for "$A$ holds at $x$".
It also writes "$x R y$" for "$y$ can be reached from $x$".
The proof rules then follow this meaning directly.
To prove "necessarily $A$" at $x$, we take a new world $y$ reachable from $x$ and prove $A$ at $y$.

### L2 human

We derive $\Box p \to p$ in G3KT.

1. $x : p, x : \Box p, x R x \Rightarrow x : p$ is an initial sequent.
2. ${\Box}$L with $y = x$ gives $x : \Box p, x R x \Rightarrow x : p$.
3. The frame rule Ref removes $x R x$ and gives $x : \Box p \Rightarrow x : p$.
4. ${\to}$R gives $\Rightarrow x : \Box p \to p$.

The typical use is to see how a frame property becomes a step in a proof: here reflexivity provides the atom $x R x$.
A trap is to apply Ref in G3K: without reflexivity the formula $\Box p \to p$ is not valid, and G3K does not derive it.

### L3 human

Labelled calculi make the semantics part of the syntax, and that gives a uniform proof theory for all logics with geometric frame conditions.
The same idea gives labelled calculi for intuitionistic and intermediate logics, where the relation is the order of a Kripke model.
Compared with [[hypersequent calculi|~908a51bf]] and [[display calculi|~eb0eba64]], labelled calculi cover many frame conditions directly, but their derivations use symbols that are not formulas of the logic.
