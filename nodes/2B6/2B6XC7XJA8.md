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

Fitch-style natural deduction writes a proof as a numbered list of lines, and it marks each temporary assumption with an indented block.
Here is a proof of $\forall x\, (P(x) \wedge Q(x)) \to \forall x\, P(x)$ in this layout:
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
Line 1 assumes the antecedent, and line 2 opens a box for a new constant $c$, the "arbitrary object".
Lines 3 and 4 work inside the box, line 5 closes the box with ${\forall}$ Intro, and line 6 closes the first block with ${\to}$ Intro.
Check: $c$ appears only inside its box, and the last line stands in the main scope, where no assumption is open.

In general, a Fitch proof is a sequence of lines, each with a formula and a justification.
An assumption opens a subproof, marked by a vertical scope line, and a rule that discharges the assumption closes it.
A line may cite earlier lines whose scope contains it, and whole closed subproofs, but never a single line inside a closed subproof.
The rules ${\forall}$ Intro and ${\exists}$ Elim use a subproof that starts with a boxed constant $\boxed{c}$, which must not occur outside that subproof.
The rules are those of [[natural deduction|6KT3BJZ7D1]] in [[tree form|PAQ4ZX2TX1]], with constants in place of eigenvariables and with a rule that repeats earlier lines.

## Motivation

A tree derivation grows sideways, and a long argument needs a wide page.
A tree also cannot reuse a formula: if a formula is used twice, its subtree must be written twice.
Mathematicians write proofs as a sequence of steps, and they say "assume", "let $c$ be arbitrary" or "let $c$ be such that" to open a part of the argument.
The Fitch layout writes natural deduction in the same way, with lines in order and an indented block for each temporary assumption.
The block shows at a glance which lines depend on the assumption and where the dependence ends.
That is why most first courses in logic, and many proof checkers for teaching, use it.

## Notation

The vertical bars are scope lines, and the short horizontal bar under an assumption, the Fitch bar, separates the assumption from the body of its subproof.
A citation "2-4" cites the whole subproof from line 2 to line 4.
The quantifier rules, in the form of Barwise and Etchemendy, are as follows.

- ${\forall}$ Elim: from $\forall x\, \varphi$, infer $\varphi[c/x]$ for any constant $c$.
- ${\forall}$ Intro: from a subproof that starts with a new boxed constant $\boxed{c}$ and ends with $\varphi[c/x]$, infer $\forall x\, \varphi$.
- ${\exists}$ Intro: from $\varphi[c/x]$, infer $\exists x\, \varphi$.
- ${\exists}$ Elim: from $\exists x\, \varphi$ and a subproof that starts with $\boxed{c}\ \varphi[c/x]$ and ends with $\chi$, infer $\chi$.

In both rules with a box, $c$ must not occur outside the subproof that it starts, so $c$ does not occur in $\chi$, in $\forall x\, \varphi$ or in earlier lines.
Reiteration (Reit) copies an earlier line into a subproof that lies in its scope.
Some books draw boxes instead of scope lines, and some write the new constant as a flagged variable.

## Remarks

### Proofs to read

[[A Fitch proof of a universal conclusion|B9MN0E708Q]] derives $\forall x\, Q(x)$ from $\forall x\, (P(x) \to Q(x))$ and $\forall x\, P(x)$ in seven lines, with one box for ${\forall}$ Intro.
[[A Fitch proof with existential elimination|ZJN5K6GBDC]] derives $\exists x\, P(x) \wedge \exists x\, Q(x)$ from $\exists x\, (P(x) \wedge Q(x))$ in eight lines, with one box for ${\exists}$ Elim.

The propositional rules work the same way.
To prove $P \to (Q \to P)$, assume $P$ at line 1, assume $Q$ at line 2, copy $P$ by Reit at line 3, and close the two blocks with ${\to}$ Intro at lines 4 and 5.
To prove $\neg \neg P$ from the premise $P$, assume $\neg P$ at line 2, get $\bot$ from lines 1 and 2 at line 3, and close with ${\neg}$ Intro at line 4.

### What is not a Fitch proof

[[A Fitch proof with a reused boxed constant|2RRB1KHNHR]] claims $\exists x\, (P(x) \wedge Q(x))$ from $\exists x\, P(x) \wedge \exists x\, Q(x)$.
Its second box reuses the constant $c$ of the first box, so the two witnesses become one, and the condition of ${\exists}$ Elim fails.

A list that cites line 3 at line 6, after a subproof of lines 2 to 4 has closed, is not a proof either.
Line 3 rests on the assumption of line 2, which is no longer in force at line 6.
Nor is a list whose last line lies inside a subproof: a proof from premises must end in the main scope, where only the premises are open.

### Trees and lines

Fitch proofs and tree derivations prove the same conclusions from the same premises.
A tree becomes a Fitch proof when we list its nodes in order and turn each discharged assumption into a block.
A Fitch proof becomes a tree when we copy each part that is cited more than once, so Fitch proofs can be shorter.
Reit has no counterpart in a tree, where a formula is reused by writing its subtree again.
Both layouts are sound and complete, by the [[equivalence of proof systems|A9AAHN4BMH]].
The scope lines also make the [[deduction theorem|8M9ZFDR4DH]] visible, since ${\to}$ Intro turns a block from $\varphi$ to $\psi$ into the line $\varphi \to \psi$.
Without the rule ${\neg}$ Elim, from $\neg \neg \varphi$ infer $\varphi$, the system proves only the intuitionistic laws.

### Watch out

Three slips are common.
Citing a line of a closed block uses an assumption that is no longer open.
Choosing a boxed constant that occurs earlier treats a known object as arbitrary, as the reused constant shows.
Ending ${\exists}$ Elim with a line that contains the boxed constant, such as $P(c)$, carries the witness name out of its box.

### History

Jaśkowski in 1934 wrote suppositional proofs with boxes around the parts that depend on an assumption.
Fitch's textbook *Symbolic Logic* of 1952 used vertical lines for the same purpose, and the layout is named after him.
The textbook *Language, Proof and Logic* by Barwise and Etchemendy comes with a proof checker called Fitch, and it uses the boxed constants described here.

### Try it

First, prove $\forall x\, P(x) \to \forall y\, P(y)$.
Assume $\forall x\, P(x)$, open a box with a new $\boxed{c}$, get $P(c)$ by ${\forall}$ Elim, close the box with ${\forall}$ Intro to get $\forall y\, P(y)$, and close the first block with ${\to}$ Intro.

Second, find the error in this list: line 1 is the premise $P(a)$, line 2 opens a box with $\boxed{a}$, line 3 is $P(a)$ by Reit, and line 4 is $\forall x\, P(x)$ by ${\forall}$ Intro from lines 2 to 3.
The boxed constant $a$ occurs in line 1, outside its box, so line 4 breaks the condition of ${\forall}$ Intro.

## Explanations

### L1 human

A Fitch proof looks like an outline with indents.
Each line has a number, a formula and a reason, such as "from lines 2 and 3".
When we say "suppose", we start a new indented block, and the block ends when the supposition is used up.
For "every", we start a block with a new name, such as $c$, prove the claim for $c$, and close the block.
For example, to show that every number $n$ satisfies $n + 0 = n$, we prove it for a new $c$ and conclude it for all $n$.

### L2 human

We prove $\exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y)$.
```text
 1 │ │ ∃x ∀y R(x,y)
   │ ├────────────
 2 │ │ │ [d]
   │ │ ├────
 3 │ │ │ │ [c] ∀y R(c,y)
   │ │ │ ├──────────────
 4 │ │ │ │ R(c,d)             ∀ Elim: 3
 5 │ │ │ │ ∃x R(x,d)          ∃ Intro: 4
 6 │ │ │ ∃x R(x,d)            ∃ Elim: 1, 3-5
 7 │ │ ∀y ∃x R(x,y)           ∀ Intro: 2-6
 8 │ ∃x ∀y R(x,y) → ∀y ∃x R(x,y)   → Intro: 1-7
```
The box of line 2 is for the arbitrary $d$, and the box of line 3 is for the witness $c$.
Line 6 is correct because $c$ does not occur in line 6, in line 1 or anywhere outside lines 3 to 5.
Line 7 is correct because $d$ occurs only inside the box of lines 2 to 6.
The typical use is in a first course, where a proof checker verifies each line.
Watch out: citing line 5 at line 7 would be wrong, because line 5 sits in the closed box of line 3.

### L3 human

The Fitch layout is a linear notation for natural deduction proofs as directed acyclic graphs, since a line can be cited many times.
Proof languages such as Isar in Isabelle and the structured proofs of Lamport use the same idea of nested blocks with local assumptions and local constants; see [[structured and hierarchical proofs|H2W8D7BMSW]].
The boxed constants play the role of eigenvariables in the tree form and in the [[sequent calculus|W72CA3R9MP]], and the stack of open blocks at a line corresponds to the context $\Gamma$ of a sequent $\Gamma \vdash \varphi$.
