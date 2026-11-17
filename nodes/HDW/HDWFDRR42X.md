---
tag: HDWFDRR42X
kind: example
name: Labelled derivation of the axiom T
msc: ["03F05", "03B45"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [F46GV42XCE]
uses: [VW8XP95XCB, 0X8NMST0J2, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
---

## Example

We derive the axiom T, $\Box p \to p$, in the calculus G3KT of the [[definition of labelled sequent calculus|VW8XP95XCB]].
G3KT is G3K with the frame rule for [[reflexivity|0X8NMST0J2]]:
$$\dfrac{x R x, \Gamma \Rightarrow \Delta}{\Gamma \Rightarrow \Delta} \ (\mathrm{Ref})$$
The goal is the sequent $\Rightarrow x : \Box p \to p$.

1. The sequent $x : p, x : \Box p, x R x \Rightarrow x : p$ is initial, because $x : p$ occurs on both sides.
2. Apply ${\Box}$L with principal formula $x : \Box p$ and relational atom $x R x$, so the world $y$ of the rule is $x$. The premise is step 1, and the conclusion is $x : \Box p, x R x \Rightarrow x : p$.
3. Apply Ref with $\Gamma = x : \Box p$ and $\Delta = x : p$. The premise is step 2, and the conclusion is $x : \Box p \Rightarrow x : p$.
4. Apply ${\to}$R with $A = \Box p$ and $B = p$. The conclusion is $\Rightarrow x : \Box p \to p$.

Each step is an initial sequent or one rule of G3KT, and no step uses cut.

We also check that the same sequent is not derivable in G3K, by a countermodel.

5. Take the Kripke model with one world $w$, no accessible worlds, and $p$ false at $w$.
6. $\Box p$ holds at $w$, because no world is accessible from $w$.
7. $p$ fails at $w$, so $\Box p \to p$ fails at $w$.
8. G3K is sound for all frames, so it does not derive $\Rightarrow x : \Box p \to p$.

## Remarks

The rule Ref is the only step that uses reflexivity.
It adds the atom $x R x$ in the backward reading, and ${\Box}$L then uses $x$ itself as an accessible world.
The frame of step 5 is not reflexive, which is why Ref is unsound there.

For a schematic formula $A$ in place of $p$, step 1 uses the derivable sequent $x : A, x : \Box A, x R x \Rightarrow x : A$ instead of an initial sequent.
This gives $\Rightarrow x : \Box A \to A$ for every formula $A$, which is the axiom schema T from the list of [[common modal axiom schemata|FDFQFWPM4X]].

## Explanations

### L1 human

The axiom T says: if $p$ is necessary, then $p$ is true.
In Kripke semantics, "necessary at $x$" means "true at every world reachable from $x$".
If $x$ can reach itself, then "true at every reachable world" includes $x$, so $p$ is true at $x$.
The proof follows exactly this thought: the rule Ref says that $x$ reaches itself, and the box rule uses $x$ as one of the reachable worlds.

### L2 human

The derivation reads well from the bottom up, as a proof search.

1. Goal $\Rightarrow x : \Box p \to p$: apply ${\to}$R backward to get $x : \Box p \Rightarrow x : p$.
2. No rule for $\Box$ on the left applies yet, because there is no relational atom. Apply Ref backward to add $x R x$.
3. Now ${\Box}$L applies with the atom $x R x$, and it adds $x : p$ to the antecedent.
4. The sequent $x : p, x : \Box p, x R x \Rightarrow x : p$ is initial, and the search ends.

The typical use of a frame rule in proof search is to create the relational atoms that a modal rule needs.
A trap is to apply ${\Box}$L without a matching atom $x R y$ in the antecedent; the rule needs that atom.
