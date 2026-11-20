---
tag: VHRXX0T5XT
kind: concept
name: Weakening
msc: ["03F05", "03B47"]
topics: [98QF5J4W16]
audience: grad
uses: [PZX9J3VEMT, W72CA3R9MP]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section W
    note: adopted
    mention: wikipedia://en/76765067#62KI
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Structural_rule
    locator: Common structural rules
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 1.1 Weakening
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
inventory: [2GPQGR9T5S]
---

## Summary

*Weakening* is the structural rule of a [[sequent calculus|W72CA3R9MP]] that adds a formula to a derivable sequent: from $\Gamma \Rightarrow \Delta$ infer $\Gamma, A \Rightarrow \Delta$ (left weakening) or $\Gamma \Rightarrow \Delta, A$ (right weakening); see [[the definition|JNYY1WD8SR]].
The rule says that a valid inference stays valid when we add a premise or a possible conclusion.
In Hilbert style it corresponds to the axiom $A \to (B \to A)$, and in residuated lattices to integrality, $x \leq 1$.
Logics without weakening, such as [[relevance logic|KXTCZ2FY5M]] and [[linear logic|2P2184B6HE]], require every hypothesis to be used.

## Motivation

In classical logic, if $A$ follows from $\Gamma$, then $A$ follows from $\Gamma$ together with any extra premise $B$.
This is monotonicity of consequence, and in a sequent calculus it is the weakening rule.
Weakening is also the source of the "paradoxes" $A \to (B \to A)$ and $A \to (B \to B)$, where the premise $B$ plays no role.
A relevance logician rejects these formulas, and a resource reading rejects weakening because a resource cannot be thrown away for free.

## Notation

In [[LK|PZX9J3VEMT]] the rules are named WL and WR.
In one-sided sequents the rule reads: from $\vdash \Gamma$ infer $\vdash \Gamma, A$.
In linear logic the rule is restricted to formulas $?A$, and Girard writes it as $?W$.
In the names $\mathsf{FL}_w$ and $\mathsf{FL}_{ew}$ of extensions of the full Lambek calculus, the letter $w$ stands for weakening.

## Remarks

### Examples

1. In LJ, weakening derives $p \to (q \to p)$; see [[weakening derives the paradox of weakening|M7Z40M37TQ]].
2. In linear logic, weakening on $?$-formulas derives $A \multimap (!B \multimap A)$; see [[controlled weakening in linear logic|K428NVQY1M]].
3. [[Affine logic|K67C2N2QAH]] is linear logic with unrestricted weakening, so it proves $A \otimes B \multimap A$; see [[the example|W1B5YCDK93]].
4. In a Heyting algebra, weakening is the inequality $x \wedge y \leq x$.

### Non-examples

1. In linear logic without exponentials, weakening is not admissible: $A \multimap (B \multimap A)$ has no derivation; see [[weakening is not admissible in linear logic|V1ZRAX3GBM]].
2. In the relevance logic $\mathbf{R}$, the formula $p \to (q \to p)$ is not a theorem; see [[the paradox of weakening fails in R|8V97CTCPS9]].
3. In [[abelian logic|W3CPQAFQJ3]], the formula $p \to (q \to p)$ takes the value $-q$ in $\mathbb{Z}$, so it is not valid.

### Basic properties

1. In LK and LJ, weakening is admissible in the cut-free calculus without the weakening rules, if the axioms are $\Gamma, A \Rightarrow A, \Delta$; this is the form used in [[contraction-free calculi|KP5KA51FC4]].
2. In the full Lambek calculus, left weakening is sound in a residuated lattice exactly when $x \leq 1$ for all $x$, and right weakening exactly when $0 \leq x$ for all $x$; see [[the definition|JNYY1WD8SR]].
3. With weakening, the multiplicative conjunction implies the additive one: from $A, B \Rightarrow A$ and $A, B \Rightarrow B$ we get $A \cdot B \Rightarrow A \wedge B$.

### History

The Stanford Encyclopedia of Philosophy entry on substructural logics describes relevant logics as the logics that reject weakening.
Wikipedia lists weakening, contraction and exchange as the three common structural rules of a sequent calculus.

### Common errors

1. Confusing weakening with the rule "from $A \wedge B$ infer $A$".
   That rule is a logical rule for $\wedge$ and holds in linear logic for the additive $\mathbin{\&}$; weakening is about the context.
2. Thinking that a logic without weakening uses each hypothesis exactly once.
   The relevance logic $\mathbf{R}$ has contraction, so it proves $(A \to (A \to B)) \to (A \to B)$.

## Explanations

### L1 human

Weakening says: if some facts prove a claim, then more facts prove it too.
If "it rains" proves "the street is wet", then "it rains and it is Monday" also proves it.
This sounds harmless, but it lets an argument carry facts that it never uses.
Logics that care about relevance or about resources reject this rule.

### L2 human

We derive $\Rightarrow q \to (p \to q)$ in LJ.

1. $q \Rightarrow q$ is an axiom.
2. Left weakening WL gives $p, q \Rightarrow q$.
3. The rule ${\to}\mathrm{R}$ moves $p$ to the right: $q \Rightarrow p \to q$.
4. The rule ${\to}\mathrm{R}$ again gives $\Rightarrow q \to (p \to q)$.

The typical use of weakening is to make two contexts equal before a rule with a shared context.
A trap: step 3 moves $p$, which is the leftmost formula, so in a calculus with lists of formulas one may need exchange first.

### L3 human

Weakening is the existence of projections: in a category of proofs it gives maps $A \otimes B \to A$, which make the unit $1$ a terminal object.
A symmetric monoidal category with weakening and contraction, natural in a suitable sense, is cartesian; so weakening is half of the step from linear to intuitionistic logic.
In residuated lattices weakening is integrality, and in the later sub-area on algebraic logic, BCK-algebras are the algebras of the implication fragment with weakening and exchange.
