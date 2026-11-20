---
tag: YAFD18WYJ8
kind: concept
name: Exchange
msc: ["03F05", "03B47"]
topics: [98QF5J4W16]
audience: grad
uses: [PZX9J3VEMT, W72CA3R9MP]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section E
    note: adopted
    mention: wikipedia://en/76765067#FH55
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Structural_rule
    locator: Common structural rules
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 1.2 Commutativity
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 2.3 The Lambek Calculus
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - doi: 10.1080/00029890.1958.11989160
    locator: pages 154-170
    note: Lambek, The Mathematics of Sentence Structure, American Mathematical Monthly 65 (1958)
inventory: [C0TJKGJAYY]
---

## Summary

*Exchange*, also called permutation, is the structural rule of a [[sequent calculus|W72CA3R9MP]] that swaps two neighboring formulas: from $\Gamma, A, B, \Gamma' \Rightarrow \Delta$ infer $\Gamma, B, A, \Gamma' \Rightarrow \Delta$, and the same on the right; see [[the definition|3ZNQNN1A45]].
It says that the order of the hypotheses does not matter.
In Hilbert style it corresponds to the axiom $(A \to (B \to C)) \to (B \to (A \to C))$, and in residuated lattices to the commutativity of fusion, $x \cdot y = y \cdot x$.
Logics without exchange, such as the [[Lambek calculus|5FAC9KX4H0]], are called non-commutative, and in them implication splits into two residuals.

## Motivation

In ordinary reasoning, a list of premises is a set, and its order plays no role.
In the analysis of language, the order of words carries meaning: "the dog bites" and "bites the dog" differ.
A logic of grammar must therefore keep the order of its hypotheses, and it must drop exchange.
The same need appears for actions in time, where "first do $a$, then do $b$" differs from the reverse order.

## Notation

In [[LK|PZX9J3VEMT]] the rules are named XL and XR, or PL and PR for permutation.
In the full Lambek calculus, the subscript $e$ marks exchange: $\mathsf{FL}_e$, $\mathsf{FL}_{ew}$.
When exchange is present, sequents are often written with multisets, and the rule becomes implicit.
Without exchange, there are two implications: $A \backslash B$ (hypothesis $A$ on the left) and $B / A$ (hypothesis $A$ on the right).

## Remarks

### Examples

1. LK and LJ have exchange, so their sequents can be read as multisets.
2. Linear logic has exchange, and it derives $A \otimes B \multimap B \otimes A$; see [[the derivation|8KN0QTZ1ED]].
3. In $\mathsf{FL}_e$, fusion is commutative: $p \cdot q \Rightarrow q \cdot p$ is derivable; see [[the example|SSHRBKVCK6]].
4. The relevance logic $\mathbf{R}$ has the permutation axiom $(A \to (B \to C)) \to (B \to (A \to C))$.

### Non-examples

1. The [[Lambek calculus|5FAC9KX4H0]] has no exchange, and $p, q \Rightarrow p \cdot q$ does not give $q, p \Rightarrow p \cdot q$; see [[exchange fails in the Lambek calculus|7PY2HR7ND5]].
2. The languages over the alphabet $\set{a, b}$, with concatenation as fusion, form a residuated lattice in which $\set{a} \cdot \set{b} = \set{ab}$ differs from $\set{b} \cdot \set{a} = \set{ba}$.
3. The relevance logic $\mathbf{E}$ of entailment has no full permutation axiom, since it is a logic of necessary implication.

### Basic properties

1. Exchange is sound in a residuated lattice exactly when fusion is commutative; see [[the definition|3ZNQNN1A45]].
2. With exchange, the two implications coincide: $A \backslash B$ and $B / A$ prove each other.
3. Exchange is independent of weakening and contraction: linear logic has exchange but neither of the other two, and the Lambek calculus has none of the three.

### History

The Stanford Encyclopedia of Philosophy entry on substructural logics presents the Lambek calculus as a logic without exchange.
Lambek introduced this calculus in 1958, in a paper on the mathematics of sentence structure.
The entry also treats commutativity as one of the structural rules that a substructural logic can reject.

### Common errors

1. Thinking that exchange is harmless because "and" is commutative.
   In a non-commutative logic, fusion is an ordered "and then".
2. Forgetting that without exchange $A \backslash B$ and $B / A$ are different formulas with different rules.
3. Treating a sequent of the Lambek calculus as a set.
   Its antecedent is a list, and the order of its formulas matters.

## Explanations

### L1 human

Exchange is the rule "the order of the facts does not matter".
In a proof about numbers, "$x > 0$ and $y > 0$" says the same as "$y > 0$ and $x > 0$".
In a sentence, the order of words matters: "John sees Mary" is not "Mary sees John".
A logic of sentences drops the exchange rule.

### L2 human

We show that with exchange the two implications of the full Lambek calculus prove each other, in one direction.

1. The axioms $A \Rightarrow A$ and $B \Rightarrow B$ give $A, A \backslash B \Rightarrow B$ by the left rule for $\backslash$.
2. Exchange gives $A \backslash B, A \Rightarrow B$.
3. The right rule for $/$ moves $A$ from the right end of the antecedent: $A \backslash B \Rightarrow B / A$.
4. Without step 2, the rule for $/$ cannot apply, since $A$ is at the left end.

The typical use of exchange is to bring a hypothesis to the position where a rule needs it.
A trap: some authors write $B / A$ as $A \rightarrow B$ or as $B \leftarrow A$, so check the convention of the source.

### L3 human

Algebraically, exchange is commutativity of the monoid of a residuated lattice, and categorically it is a symmetry of a monoidal category.
A non-commutative residuated lattice has two residuals, as a monoidal closed category that is not symmetric has two internal homs.
The [[Lambek calculus|5FAC9KX4H0]] is the logic of residuated semigroups, and the [[full Lambek calculus|V5XVVN16GS]] is the logic of residuated lattices without any structural rule.
