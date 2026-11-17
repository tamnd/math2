---
tag: 2B6XC7XJA8
kind: concept
name: Fitch-style natural deduction
aliases: [fitch-style-natural-deduction, fitch-notation, fitch-system]
msc: ["03F03", "03B10"]
topics: [TTCRX3NFNY]
audience: ug1
uses: [6KT3BJZ7D1, PAQ4ZX2TX1]
sources:
  - url: https://en.wikipedia.org/wiki/Fitch_notation
    locator: Structure
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: Fitch-style propositional logic
---

## Summary

Fitch-style natural deduction is a layout of [[natural deduction|6KT3BJZ7D1]] in which a proof is a numbered list of lines, each with a justification.
An assumption opens a subproof, which a vertical scope line marks, and a rule that discharges the assumption closes it.
A line may cite only earlier lines and closed subproofs whose scope contains it, and never a line inside a closed subproof.
The quantifier rules ${\forall}$ Intro and ${\exists}$ Elim use a subproof that starts with a boxed constant $\boxed{c}$.
The constant $\boxed{c}$ must not occur outside that subproof.
The rules are those of the [[tree form|PAQ4ZX2TX1]], with free variables replaced by constants and with reiteration of earlier lines.
The layout matters because it is how most first courses in logic write formal proofs, and it shows the scope of each assumption at a glance.

## Motivation

A tree derivation grows sideways, and a long argument needs a wide page.
A tree also cannot reuse a formula: if a line is used twice, its subtree must be written twice.
Mathematicians write proofs as a sequence of lines, and they say "assume", "let $c$ be arbitrary" or "let $c$ be such that" to open a part of the argument.
The Fitch layout writes natural deduction in the same way: lines in order, and an indented block for each temporary assumption.
The block shows which lines depend on the assumption and where the dependence ends.

## Notation

We draw proofs as text, one line per formula, in the form below.
```text
 1 │ premise
   ├───────
 2 │ │ assumption
   │ ├────────
 3 │ │ formula          rule: cited lines
 4 │ formula            rule: 2-3
```
The vertical bars are scope lines, and the short horizontal bar (the Fitch bar) separates the assumptions of a subproof from its body.
A citation "2-3" cites the whole subproof from line 2 to line 3.
The quantifier rules, in the form of Barwise and Etchemendy, are as follows.

- ${\forall}$ Elim: from $\forall x\, \varphi$, infer $\varphi[c/x]$ for any constant $c$.
- ${\forall}$ Intro: from a subproof that starts with a new boxed constant $\boxed{c}$ and ends with $\varphi[c/x]$, infer $\forall x\, \varphi$.
- ${\exists}$ Intro: from $\varphi[c/x]$, infer $\exists x\, \varphi$.
- ${\exists}$ Elim: from $\exists x\, \varphi$ and a subproof that starts with $\boxed{c}\ \varphi[c/x]$ and ends with $\chi$, infer $\chi$.

In both rules with a box, $c$ must not occur outside the subproof that it starts, so $c$ does not occur in $\chi$, in $\forall x\, \varphi$ or in earlier lines.
Reiteration (Reit) copies an earlier line into a subproof that lies in its scope.

## Remarks

### Examples

- [[A Fitch proof of a universal conclusion|B9MN0E708Q]]: $\forall x\, Q(x)$ from $\forall x\, (P(x) \to Q(x))$ and $\forall x\, P(x)$, in seven lines with one box for ${\forall}$ Intro.
- [[A Fitch proof with existential elimination|ZJN5K6GBDC]]: $\exists x\, P(x) \wedge \exists x\, Q(x)$ from $\exists x\, (P(x) \wedge Q(x))$, in eight lines with one box for ${\exists}$ Elim.
- The proof of $P \to (Q \to P)$: open a subproof with $P$, open a subproof with $Q$, reiterate $P$, close with ${\to}$ Intro twice. It uses five lines.
- The proof of $\neg \neg P$ from $P$: open a subproof with $\neg P$, derive $\bot$ from $P$ and $\neg P$, close it with ${\neg}$ Intro. It uses four lines.

### Non-examples

- [[A Fitch proof with a reused boxed constant|2RRB1KHNHR]]: a "proof" of $\exists x\, (P(x) \wedge Q(x))$ from $\exists x\, P(x) \wedge \exists x\, Q(x)$. The condition that fails: the second box reuses the constant $c$ of the first box.
- A list that cites line 3 at line 6, after the subproof of lines 2 to 4 has closed. The condition that fails: a line inside a closed subproof is not available outside it.
- A list whose last line lies inside a subproof. The condition that fails: a proof of $\varphi$ from the premises must end with $\varphi$ in the main scope, where only the premises are open.

### Basic properties

- Fitch proofs and tree derivations prove the same sequents. A tree becomes a Fitch proof by listing its nodes in order; a Fitch proof becomes a tree by copying each subtree that is cited more than once.
- The copying can make the tree longer, so Fitch proofs can be shorter than trees with the same conclusion. Both are sound and complete; see [[equivalence of proof systems|A9AAHN4BMH]].
- Reiteration has no counterpart in the tree form: a tree reuses a formula by writing its subtree again.
- Without the rule ${\neg}$ Elim (from $\neg \neg \varphi$ infer $\varphi$) the system is intuitionistic.
- The scope lines make the [[deduction theorem|8M9ZFDR4DH]] visible: ${\to}$ Intro turns a subproof from $\varphi$ to $\psi$ into the line $\varphi \to \psi$.

### History

Jaśkowski in 1934 wrote suppositional proofs with boxes around the parts that depend on an assumption.
Fitch's textbook *Symbolic Logic* of 1952 used vertical lines for the same purpose, and the layout is named after him.
The textbook *Language, Proof and Logic* by Barwise and Etchemendy comes with a proof checker called Fitch, and it uses the boxed constants of this page.

### Common errors

- To cite a line of a closed subproof. The line depends on an assumption that is no longer open.
- To use a boxed constant that occurs earlier in the proof. The proof then treats a known object as arbitrary, as the non-example shows.
- To conclude ${\exists}$ Elim with a formula that contains the boxed constant. The constant names only a witness inside the box.

## Explanations

### L1 human

A Fitch proof looks like an outline with indents.
Each line has a number, a formula and a reason, such as "from lines 2 and 3".
When we say "suppose", we start a new indented block, and the block ends when the supposition is used up.
For "every", we start a block with a new name, such as $c$, prove the claim for $c$, and close the block.
For example, to show that every number $n$ satisfies $n + 0 = n$, we prove it for a new $c$ and conclude it for all $n$.

### L2 human

We prove $\forall x\, (P(x) \wedge Q(x)) \to \forall x\, P(x)$.
```text
 1 │ │ ∀x (P(x) ∧ Q(x))
   │ ├────────────────
 2 │ │ │ [c]
   │ │ ├────
 3 │ │ │ P(c) ∧ Q(c)          ∀ Elim: 1
 4 │ │ │ P(c)                 ∧ Elim: 3
 5 │ │ ∀x P(x)                ∀ Intro: 2-4
 6 │ ∀x (P(x) ∧ Q(x)) → ∀x P(x)   → Intro: 1-5
```

1. Line 1 opens a subproof with the antecedent as assumption.
2. Line 2 opens a box with the new constant $c$; $c$ does not occur before.
3. Lines 3 and 4 use ${\forall}$ Elim with $c$ and ${\wedge}$ Elim.
4. Line 5 closes the box with ${\forall}$ Intro; $c$ does not occur in $\forall x\, P(x)$.
5. Line 6 closes the first subproof with ${\to}$ Intro.

The typical use is in a first course, where a proof checker verifies each line.
A trap is to cite line 4 after line 5: it lies in a closed box.

### L3 human

The Fitch layout is a linear notation for natural deduction proofs as directed acyclic graphs, since a line can be cited many times.
Proof assistants such as Isar in Isabelle and the structured proofs of Lamport use the same idea of nested blocks with local assumptions and local constants; see [[structured and hierarchical proofs|H2W8D7BMSW]].
The boxed constants play the role of eigenvariables in the tree form and in the [[sequent calculus|W72CA3R9MP]], and the block structure corresponds to the context $\Gamma$ of a sequent $\Gamma \vdash \varphi$.
