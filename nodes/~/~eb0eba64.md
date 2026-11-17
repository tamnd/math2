---
tag: ~eb0eba64
kind: concept
name: Display calculus
msc: ["03F05", "03B45", "03B47"]
topics: [R10RMQCJQX]
audience: research
uses: [W72CA3R9MP, PZX9J3VEMT, C3RZY20ETK, AYRZ98Y0NW]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Structures and connectives
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Locality
---

## Summary

A *display calculus* is a [[sequent calculus|W72CA3R9MP]] whose sequents $X \vdash Y$ relate structures built from formulas with structural connectives, such as a unit $\mathrm{I}$, a negation ${*}$, a comma $\circ$ and a modal ${\bullet}$.
It has invertible structural rules, the *display postulates*, with the *display property*: every antecedent part $Z$ of a sequent can be brought to the form $Z \vdash W$, and every succedent part to $W \vdash Z$.
Its logical rules introduce a connective only in a formula that forms the whole antecedent or the whole succedent.
The [[definition|~c1a4d015]] gives Belnap's calculus for the tense logic $\mathrm{K_t}$.
Belnap's theorem gives cut elimination for every display calculus whose rules satisfy eight syntactic conditions, so one proof covers a large family of logics.

## Motivation

Gentzen's [[cut-elimination theorem|AYRZ98Y0NW]] is proved again for each new sequent calculus, and each proof checks many cases by hand.
For modal and substructural logics, ordinary sequent calculi often fail to have cut elimination at all.
Belnap asked for a format in which cut elimination follows from simple checks on the shape of each rule.
The difficulty in a cut-elimination proof is the parametric case, where the cut formula sits deep inside a sequent.
If every part of a sequent can be displayed, the cut formula can always be brought to the surface, and a uniform argument handles that case.
A second aim was modularity: the structural rules carry the properties of a logic, and the logical rules stay the same for all logics.

## Notation

Belnap writes $\mathrm{I}$, ${*}$ and $\circ$ for the structural unit, negation and comma.
Later papers often write a comma or a semicolon for $\circ$, and use $\sharp$ for structural negation in substructural settings.
Modal structural connectives are written ${\bullet}$ or $\circ$, depending on the author.
In this page, $\Box$ is the forward box and $\blacklozenge$ the backward diamond, and ${\bullet}$ reads as $\blacklozenge$ in the antecedent and as $\Box$ in the succedent.

## Remarks

### Examples

- Belnap's calculus $\mathrm{DK_t}$ for minimal tense logic, given in the [[definition|~c1a4d015]]. Its display postulate D4 is ${\bullet}X \vdash Y \iff X \vdash {\bullet}Y$, which mirrors the adjunction between $\blacklozenge$ and $\Box$.
- The sequent $p \circ (q \circ {*}r) \vdash s$ is display equivalent to ${*}({*}q \circ ({*}p \circ s)) \vdash r$, which displays $r$. The [[example of displaying a substructure|~654b26fe]] checks each step.
- The sequent $\Box p \wedge \Box q \vdash \Box(p \wedge q)$ has a cut-free derivation in $\mathrm{DK_t}$ that moves ${\bullet}$ across the turnstile three times. The [[example of the box over a conjunction|~f8eb9798]] gives all steps.
- Removing the rules W and C from $\mathrm{DK_t}$ without its modal part gives a display calculus for a substructural logic without weakening and contraction. The logical rules and Belnap's theorem stay the same.
- Adding the structural rule "from $X \vdash {\bullet}Y$ infer $X \vdash Y$" gives a display calculus that is sound for reflexive frames. The axiom $\Box A \to A$ follows: from $A \vdash A$, ${\Box}$L gives $\Box A \vdash {\bullet}A$, and the new rule gives $\Box A \vdash A$.

### Non-examples

- Gentzen's [[LK|PZX9J3VEMT]] has no display property. From $p, q \Rightarrow r$ no structural rule produces a sequent with antecedent $p$ alone; the [[non-example|~865ec2a9]] proves this.
- The usual sequent rule for K infers $\Box\Gamma \Rightarrow \Box A$ from $\Gamma \Rightarrow A$. It introduces every formula of $\Box\Gamma$ at once, so its principal formulas do not stand alone, and condition C5 fails.
- A sequent calculus with a rule whose principal formula sits inside a larger antecedent, such as ${\wedge}$L of LK, breaks condition C5. This is harmless in LK, but Belnap's general theorem does not apply to it.

### Basic properties

- The display theorem: every antecedent part and every succedent part of a sequent can be displayed by the display postulates, and the steps are invertible.
- Belnap's theorem: if the rules satisfy his conditions C2 to C8, then cut is eliminable; with C1, cut-free derivations have the [[subformula property|~694ac127]].
- Each condition is checked on single rules, so adding a new structural rule that satisfies the conditions keeps cut elimination.
- Soundness is checked rule by rule with the formula reading of structures, which differs in the antecedent and the succedent.

### History

Belnap introduced display logic in his 1982 paper "Display logic" in the Journal of Philosophical Logic.
In his framework, structural connectives can be as complex as the logical connectives.
Display calculi were later given for many modal, tense and substructural logics.

### Common errors

- Forgetting that ${*}$ changes the side: in ${*}r \vdash Y$, the structure $r$ is a succedent part.
- Reading ${\bullet}$ as $\Box$ in the antecedent. In the antecedent it reads as the backward diamond $\blacklozenge$.
- Thinking that display postulates change the meaning of a sequent. They are invertible, and both forms have equivalent formula readings.

## Explanations

### L1 human

A sequent is a claim that some assumptions give some conclusions.
A display calculus adds moves that shift a piece of a sequent from one side to the other without changing the claim.
For instance, "$x$ and $y$ give $z$" says the same as "$x$ gives: not $y$, or $z$".
With these moves, any piece can be made to stand alone on one side.
Every rule for a logical symbol then works on a formula that stands alone.
Because all rules have this simple shape, one general argument shows that detours through lemmas can be removed from proofs.

### L2 human

We derive necessitation in $\mathrm{DK_t}$: if $\mathrm{I} \vdash A$ is derivable, then so is $\mathrm{I} \vdash \Box A$.

1. From $\mathrm{I} \vdash A$, weakening W gives $\mathrm{I} \circ {\bullet}\mathrm{I} \vdash A$.
2. The rule IL, from right to left with $X = {\bullet}\mathrm{I}$, removes the unit and gives ${\bullet}\mathrm{I} \vdash A$.
3. D4 gives $\mathrm{I} \vdash {\bullet}A$.
4. The rule ${\Box}$R gives $\mathrm{I} \vdash \Box A$.

The typical use of the display postulates is in step 3: they move a structure so that a logical rule can act.
A trap is to apply ${\Box}$R to $\mathrm{I} \vdash A$ directly; the rule needs the succedent ${\bullet}A$, not $A$.

### L3 human

Display calculi separate structure from logic.
The structural connectives are residuated families, and the display postulates state the residuation laws, as in residuated lattices and Heyting algebras.
This explains why display works well for tense logics and for the [[Lambek calculus|5FAC9KX4H0]], where every connective has an adjoint, and less well for a modal logic with no backward modality.
Compared with [[hypersequent calculi|~908a51bf]] and [[labelled sequent calculi|~fddc9de5]], display calculi have a very general cut-elimination theorem, at the price of a more complex notion of structure.
