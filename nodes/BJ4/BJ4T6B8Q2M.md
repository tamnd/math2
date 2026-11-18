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

Read a clause as a sequent of atoms.
The clause $\set{\neg p_1, \dots, \neg p_k, q_1, \dots, q_l}$ is the sequent $p_1, \dots, p_k \Rightarrow q_1, \dots, q_l$ of the [[sequent calculus|PZX9J3VEMT]], with sets of atoms on both sides.

Under this reading, the [[resolution rule|6JSH907W5R]] is the cut rule on an atom $x$:
$$\frac{\Gamma \Rightarrow \Delta, x \qquad x, \Gamma' \Rightarrow \Delta'}{\Gamma, \Gamma' \Rightarrow \Delta, \Delta'}.$$
The left premise is the clause $A \cup \set{x}$, the right premise is $B \cup \set{\neg x}$, and the conclusion is $A \cup B$.

So a resolution refutation of a CNF $F$ is a derivation of the empty sequent $\Rightarrow$ from the sequents of the clauses of $F$.
It uses only atomic cuts, and contraction and exchange are built into the use of sets.
Every formula in it is an atom, of depth $0$.
So resolution is the sequent calculus of depth $0$, the lowest level of [[bounded-depth Frege|41QJ1WEMJ3]] in the sequent form.

*A small case.* The refutation of $\set{p}$, $\set{\neg p, q}$, $\set{\neg q}$ becomes the following derivation.

1. $\Rightarrow p$ and $p \Rightarrow q$ give $\Rightarrow q$, by a cut on $p$.
2. $\Rightarrow q$ and $q \Rightarrow$ give $\Rightarrow$, by a cut on $q$.

## Remarks

The cut rule cannot be removed here.
The [[cut-elimination theorem|AYRZ98Y0NW]] removes cuts from derivations of sequents from no hypotheses, but a refutation starts from the hypotheses of $F$, and cuts on atoms remain necessary.
Allowing cuts on clauses or on conjunctions of small width gives the systems $\mathrm{Res}(k)$, which lie between resolution and depth-$2$ Frege.

## Explanations

### L1 human

A clause such as "not $p$ or $q$" can be read as "if $p$, then $q$".
Combining "if $p$ then $q$" with "$p$" to get "$q$" is a cut on $p$.
So resolution is a proof system with cuts on single variables, and with no complex formulas at all.

### L2 human

We translate one resolution step.

1. Premises: $\set{\neg a, x}$ and $\set{\neg x, b}$.
2. As sequents: $a \Rightarrow x$ and $x \Rightarrow b$.
3. A cut on $x$ gives $a \Rightarrow b$.
4. As a clause: $\set{\neg a, b}$, the resolvent on $x$.

The typical use of the example is to place resolution inside the hierarchy of bounded-depth systems.
A trap: in this reading, depth is counted from $0$ for atoms; with other conventions resolution is depth-$1$ Frege.
