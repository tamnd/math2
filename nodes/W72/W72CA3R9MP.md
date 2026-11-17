---
tag: W72CA3R9MP
kind: concept
name: Sequent calculus
msc: ["03F05", "03F03"]
topics: [TTCRX3NFNY]
audience: grad
uses: [N4EDJNMTEF, 086QKPF0A6, 6KT3BJZ7D1]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: The system LK
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Sequent calculus
same_as:
  wikidata: Q1771121
  wikipedia: Sequent calculus
---

## Summary

A sequent calculus is a proof system whose lines are sequents $\Gamma \Rightarrow \Delta$, where $\Gamma$ and $\Delta$ are finite sequences of formulas.
A sequent is read as "if all formulas of $\Gamma$ hold, then some formula of $\Delta$ holds".
A derivation is a tree of sequents whose leaves are axioms $A \Rightarrow A$.
Each other node follows by a structural rule (weakening, contraction, exchange), by the cut rule, or by a logical rule.
A logical rule introduces one connective or quantifier on the left or on the right, and ${\forall}$R and ${\exists}$L carry an eigenvariable condition.
Gentzen's calculus LK for classical [[first-order logic|086QKPF0A6]] and its intuitionistic restriction LJ are given in the [[definition|PZX9J3VEMT]].
The calculus matters because every logical rule adds one symbol to its premises, so a cut-free derivation uses only subformulas of its conclusion, and this makes it the main tool of structural [[proof theory|N4EDJNMTEF]].

## Motivation

In [[natural deduction|6KT3BJZ7D1]] the open assumptions of a formula are spread over the leaves of the tree above it.
Gentzen wanted to study derivations as objects, and for this he wrote the assumptions next to each formula: a node $\Gamma \Rightarrow A$ records that $A$ is derived from $\Gamma$.
Elimination rules of natural deduction then become rules that introduce a symbol on the left, so every rule builds its conclusion from smaller formulas.
Allowing several formulas on the right made the calculus symmetric, and it gave classical logic without a special rule such as RAA.
The cut rule keeps the old way of reasoning through a lemma, and Gentzen's main theorem says that it can be removed.

## Notation

We write $\Gamma \Rightarrow \Delta$ for a sequent and $\vdash_{\mathsf{LK}} \Gamma \Rightarrow \Delta$ for derivability; many books write the sequent as $\Gamma \vdash \Delta$.
For a set of sentences $\Gamma$ and a sentence $\varphi$, we write $\Gamma \vdash_{\mathsf{LK}} \varphi$ when $\Gamma_0 \Rightarrow \varphi$ is derivable for some finite list $\Gamma_0$ of members of $\Gamma$.
Rule names are ${\to}$L, ${\to}$R and so on, with W, C and X for weakening, contraction and exchange.
Variants use multisets or sets instead of sequences, one-sided sequents $\Rightarrow \Delta$, or Kleene's G3 calculi, in which weakening and contraction are built into the other rules.

## Remarks

### Examples

- [[A sequent derivation of the drinker paradox|~b4da6e0a]]: $\Rightarrow \exists x\, (D(x) \to \forall y\, D(y))$ in nine steps. It needs contraction on the right, so two formulas in the succedent.
- [[A cut-free sequent derivation with quantifiers|~68658292]]: $\forall x\, (P(x) \to Q(x)), \forall x\, P(x) \Rightarrow \forall x\, Q(x)$ in six steps. Every formula in it is a subformula of the conclusion, up to terms.
- The [[law of excluded middle|0RYYK8PG4S]]: $\Rightarrow A \vee \neg A$ from $A \Rightarrow A$ by ${\neg}$R, ${\vee}$R twice and contraction, as in the definition.
- The sequent $\forall x\, P(x) \Rightarrow \exists x\, P(x)$: ${\exists}$R with $t = y$ turns $P(y) \Rightarrow P(y)$ into $P(y) \Rightarrow \exists x\, P(x)$, and ${\forall}$L with $t = y$ gives the result.

### Non-examples

- [[A sequent derivation that breaks the eigenvariable condition|~a8d7aeab]]: ${\forall}$R from $P(a) \Rightarrow P(a)$ to $P(a) \Rightarrow \forall x\, P(x)$. The condition that fails: $a$ is free in the antecedent.
- The same steps as for the excluded middle are not an LJ derivation. The condition that fails: $\Rightarrow A, \neg A$ has two formulas in the succedent.
- A tree with the leaf $P(a) \Rightarrow P(b)$, for different variables $a$ and $b$. The condition that fails: an axiom has the same formula on both sides.

### Basic properties

- Soundness: every rule turns true sequents into a true sequent in each structure, under each assignment, so every derivable sequent is valid. The eigenvariable condition is used for ${\forall}$R and ${\exists}$L.
- Completeness: every valid sequent has a derivation, and even one without cut. So LK derives the same consequences as the other systems; see [[equivalence of proof systems|~c9d242a1]].
- [[Cut elimination|AYRZ98Y0NW]]: every derivation can be turned into a derivation of the same sequent without cut. The cost can be a non-elementary increase in size.
- Subformula property: in a cut-free derivation, every formula is a subformula of a formula of the conclusion, up to the substitution of terms for bound variables.
- Relation to tableaux: a closed [[semantic tableau|~78632a29]] for $\Gamma$ read from the leaves upward is a cut-free derivation of $\Gamma \Rightarrow$ in a one-sided form of LK.
- The rules are invertible in the G3 form: if the conclusion of a propositional rule is derivable, so are its premises. This makes backward proof search possible without backtracking in the propositional case.

### History

Gentzen introduced LK and LJ in his paper "Investigations into logical deduction" of 1934 to 1935, and proved the cut-elimination theorem there.
He used the theorem to prove the consistency of these calculi and the midsequent theorem.
Kleene introduced the G3 calculi in his book *Introduction to Metamathematics* of 1952.

### Common errors

- To break the eigenvariable condition of ${\forall}$R or ${\exists}$L by an eigenvariable that is free in another formula of the sequent.
- To read a sequent with a conjunction on the right: $\Rightarrow A, B$ says "$A$ or $B$", not "$A$ and $B$".
- To think that cut is needed for completeness. Cut-free LK is already complete, and cut only shortens derivations.

## Explanations

### L1 human

A sequent is a claim of the form "if all of these hold, then at least one of those holds".
For example, "it rains, it is cold $\Rightarrow$ I stay home, I wear a coat" claims that rain and cold force at least one of the two actions.
The calculus starts from claims of the form "$A \Rightarrow A$", which are always true.
Each rule adds one logical word, on the left or on the right, until the claim that we want appears at the bottom.
Because the rules only add words, we can search for a proof by taking words away, starting from the bottom.

### L2 human

We derive $\Rightarrow \neg \neg A \to A$ in LK.

1. $A \Rightarrow A$ is an axiom.
2. ${\neg}$R gives $\Rightarrow A, \neg A$.
3. ${\neg}$L gives $\neg \neg A \Rightarrow A$.
4. ${\to}$R gives $\Rightarrow \neg \neg A \to A$.

Step 2 has two formulas in the succedent, so this is not an LJ derivation, and indeed $\neg \neg A \to A$ is not intuitionistically valid.
The typical use is backward proof search: start from the goal and apply rules upward, choosing the rule by the main symbol of a formula.
A trap is to apply ${\forall}$L only once: the formula $\forall x\, A$ may be needed with two different terms, and then contraction must keep a copy of it.

### L3 human

The sequent calculus treats derivations as finite combinatorial objects, and cut elimination is a statement about them; this is the start of structural proof theory, as in [[structural proof theory|R10RMQCJQX]].
The left and right rules correspond to the elimination and introduction rules of natural deduction, and cut corresponds to a detour; normalization of natural deduction and cut elimination are two forms of one result.
Removing structural rules gives substructural logics: without contraction and weakening one gets linear logic, and without exchange non-commutative logics; see [[weakening|VHRXX0T5XT]] and [[exchange|YAFD18WYJ8]].
Craig interpolation, Herbrand's theorem and many consistency proofs are proved by induction on cut-free derivations.
