---
tag: BJ4T6B8Q2M
kind: example
name: Resolution as the sequent calculus with atomic cuts
msc: ["03F20", "03F05"]
topics: [CBAF7J051K]
audience: research
instance_of: [41QJ1WEMJ3]
uses: [6JSH907W5R, PZX9J3VEMT, AYRZ98Y0NW, 41QJ1WEMJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in propositional logic
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Structural rules
---

## Example

The clause $\{\neg p, q\}$ says "if $p$ then $q$", and as a sequent it is $p \Rightarrow q$.
Resolving it with $\{p\}$, the sequent $\Rightarrow p$, gives $\{q\}$, the sequent $\Rightarrow q$, and this step is a cut on $p$.

In general, read a clause as a sequent of atoms.
The clause $\{\neg p_1, \dots, \neg p_k, q_1, \dots, q_l\}$ is the sequent $p_1, \dots, p_k \Rightarrow q_1, \dots, q_l$ of the [[sequent calculus|PZX9J3VEMT]], with sets of atoms on both sides.
Under this reading, the [[resolution rule|6JSH907W5R]] is the cut rule on an atom $x$:
$$\frac{\Gamma \Rightarrow \Delta, x \qquad x, \Gamma' \Rightarrow \Delta'}{\Gamma, \Gamma' \Rightarrow \Delta, \Delta'}.$$
The left premise is the clause $A \cup \{x\}$, the right premise is $B \cup \{\neg x\}$, and the conclusion is $A \cup B$.

So a resolution refutation of a CNF $F$ is a derivation of the empty sequent $\Rightarrow$ from the sequents of the clauses of $F$.
It uses only atomic cuts, and contraction and exchange are built into the use of sets.
Every formula in it is an atom, of depth $0$.
So resolution is the sequent calculus of depth $0$, the lowest level of [[bounded-depth Frege|41QJ1WEMJ3]] in the sequent form.

*A small case.* The refutation of $\{p\}$, $\{\neg p, q\}$, $\{\neg q\}$ becomes the following derivation.

1. $\Rightarrow p$ and $p \Rightarrow q$ give $\Rightarrow q$, by a cut on $p$.
2. $\Rightarrow q$ and $q \Rightarrow$ give $\Rightarrow$, by a cut on $q$.

## Remarks

### Why the cuts stay

The cut rule cannot be removed here.
The [[cut-elimination theorem|AYRZ98Y0NW]] removes cuts from derivations from no hypotheses.
A refutation starts from the hypotheses of $F$, and with hypotheses only the cuts on formulas of the hypotheses can be removed, so the cuts on atoms remain.
Without them, nothing at all can be derived from the sequents of $F$ except weakenings, and $\Rightarrow$ is not a weakening of any of them unless $\square \in F$.

### Higher levels

Allowing cuts on conjunctions of at most $k$ literals gives the systems $\mathrm{Res}(k)$, whose lines are disjunctions of such conjunctions.
They lie between resolution and depth-$2$ Frege.
The measures carry over: size counts the sequents or the symbols, and the width of a clause is the number of atoms in its sequent.

## Explanations

### L1 human

A clause such as "not $p$ or $q$" can be read as "if $p$, then $q$".
Combining "if $p$ then $q$" with "$p$" to get "$q$" is a cut on $p$.
So resolution is a proof system with cuts on single variables, and with no complex formulas at all.

### L2 human

We translate one resolution step.

1. Premises: $\{\neg a, x\}$ and $\{\neg x, b\}$.
2. As sequents: $a \Rightarrow x$ and $x \Rightarrow b$.
3. A cut on $x$ gives $a \Rightarrow b$.
4. As a clause: $\{\neg a, b\}$, the resolvent on $x$.

The typical use of the example is to place resolution inside the hierarchy of bounded-depth systems.
A trap: in this reading, depth is counted from $0$ for atoms.
In the Frege form a line of resolution is a clause, of depth $1$, so with that convention resolution is depth-$1$ Frege.

### L3 human

The reading shows that the only thing resolution can do is cut on atoms.
Every stronger system in the hierarchy is obtained by allowing cuts on more complex formulas: small conjunctions for $\mathrm{Res}(k)$, formulas of depth $d$ for depth-$d$ Frege, and arbitrary formulas for Frege.
Lower bounds become harder to prove at each step, because the cut formulas can hide more information.
