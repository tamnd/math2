---
tag: NQFYY76BSM
kind: concept
name: Connexive logic
aliases: [aristotles-thesis, boethiuss-thesis, connexive-implication]
msc: ["03B60", "03B53"]
topics: [NJB94B39QK]
audience: grad
uses: [09K9MWD2QQ, 029JBBF693, 4KTD8GB5PV, 22K4GWJ0WM, WK2P0E82B4, C7YWCR87QJ]
sources:
  - wikipedia: en:12859904@r1339752880
    locator: Connexive logic
    note: adopted
    mention: wikipedia://en/12859904
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/logic-connexive/
    locator: Connexive Logic (SEP entry), sections 1, 2, 3.4 and 4.5.1
same_as:
  wikidata: Q5161806
  wikipedia: Connexive logic
inventory: [Z4XTBHMCSS]
---

## Summary

A *connexive logic* is a logic in which no formula implies its own [[negation|029JBBF693]], and no formula is implied by its own negation.
In the standard notion, four schemas are theorems: [[Aristotle's theses|4KTD8GB5PV]] AT and AT′, and [[Boethius' theses|22K4GWJ0WM]] BT and BT′.

$$\text{AT: } \sim(\sim A \to A), \qquad \text{AT}'\text{: } \sim(A \to \sim A),$$

$$\text{BT: } (A \to B) \to \sim(A \to \sim B), \qquad \text{BT}'\text{: } (A \to \sim B) \to \sim(A \to B).$$

Also, the implication must not be symmetric: $(A \to B) \to (B \to A)$ is not a theorem.
These schemas are not classical tautologies.
So a connexive logic is not a subsystem of classical [[propositional logic|09K9MWD2QQ]].
It is not an extension either, because classical propositional logic is [[Post complete|WK2P0E82B4]].

## Motivation

A connexive conditional expresses a connection between the antecedent and the consequent.
The SEP entry quotes a view that Sextus Empiricus reports: a conditional is sound when the contradictory of its consequent is incompatible with its antecedent.
On this view, "if $A$ then not $A$" can never be sound.
Angell wanted a logic of subjunctive conditionals in which "if $A$ then $B$" and "if $A$ then not $B$" cannot both hold.
McCall used connexive implication to get all the valid moods of Aristotle's syllogistic in a first-order language.
Wansing used a connexive negation in categorial grammar, where a type $\sim(n \to s)$ is read as $n \to \sim s$.

## Notation

We write $\sim$ for the negation and $\to$ for the connexive implication.
The equivalence $A \leftrightarrow B$ abbreviates $(A \to B) \land (B \to A)$.
For Wansing's system $\mathbf{C}$, we write $\vdash_{\mathbf{C}} A$ when $A$ is a theorem of $\mathbf{C}$.
The axioms of $\mathbf{C}$ are those of positive intuitionistic logic, together with:

- a2: $\sim\sim A \leftrightarrow A$;
- a3: $\sim(A \lor B) \leftrightarrow (\sim A \land \sim B)$;
- a4: $\sim(A \land B) \leftrightarrow (\sim A \lor \sim B)$;
- a5: $\sim(A \to B) \leftrightarrow (A \to \sim B)$.

The only rule is modus ponens.

## Remarks

### Examples

- [[Aristotle's theses in Wansing's C|~a45c6718]]: AT and AT′ are theorems of $\mathbf{C}$.
- [[Boethius' theses in Wansing's C|~7018a484]]: BT and BT′ are theorems of $\mathbf{C}$, and the implication is not symmetric.
- The system CC1, due to Angell (1962) and McCall (1966), validates AT and BT′.

### Non-examples

- [[Classical logic is not connexive|~02c938fb]]: each of AT, AT′, BT and BT′ fails in some row of the truth table.
- Every subsystem of classical logic, for example intuitionistic logic, fails AT, because AT is not a classical tautology.

### Basic properties

- In a logic with the theorem $A \to A$ and the rule modus ponens, AT′ follows from BT, and AT follows from BT′.
  For AT′, put $B := A$ in BT and apply modus ponens to $A \to A$.
  For AT, put $\sim A$ for $A$ and $A$ for $B$ in BT′, and apply modus ponens to $\sim A \to \sim A$.
- Humberstone (2000) calls a logic *contra-classical* if it proves a formula that classical logic does not prove.
  Every connexive logic in the classical vocabulary is contra-classical.
- A non-trivial connexive logic must omit some classical theorems, because adding any non-tautology to classical propositional logic gives the trivial logic.
- In $\mathbf{C}$, axiom a5 is the only contra-classical axiom.
  The logic $\mathbf{C}$ differs from Nelson's logic $\mathbf{N4}$ only in the falsity condition for implication; $\mathbf{N4}$ has $\sim(A \to B) \leftrightarrow (A \land \sim B)$.
- $\mathbf{C}$ is sound and complete for a Kripke-style semantics with separate support of truth and support of falsity.
  It is decidable and has the disjunction property.
- $\mathbf{C}$ is [[paraconsistent|C7YWCR87QJ]] and proves some contradictions, for example both $(p \land \sim p) \to (\sim p \lor p)$ and its negation.

### History

The SEP entry gives these sources.
Aristotle argues in the Prior Analytics (57b14) that it is impossible that "if not $A$, then $A$".
Kneale and Kneale ascribe to Boethius the view that "if $A$ then not $B$" is the negation of "if $A$ then $B$"; the SEP entry questions this reading.
MacColl (1878) is a forerunner.
Modern connexive logic began with Nelson (1930), Angell (1962) and McCall (1966).
McCall introduced the name "connexive logic" in 1963 and 1964.
Wansing introduced the system $\mathbf{C}$ in 2005.

### Common errors

- To confuse AT with the law of non-contradiction $\sim(\sim A \land A)$. AT is about an implication, not a conjunction.
- To think that a connexive logic adds AT to classical logic. That gives the trivial logic.
- To read $\sim(A \to B)$ as $A \land \sim B$. In $\mathbf{C}$, it is equivalent to $A \to \sim B$.
- To call every logic with AT connexive. The standard notion also asks for AT′, BT, BT′ and non-symmetry of implication; weaker variants have other names.

## Explanations

### L1 human

"If it does not rain, then it rains" sounds wrong in any situation.
Classical logic accepts it when it rains, because a true consequent makes any conditional true.
Connexive logic says that this conditional is always false.
A statement never follows from its own denial.

### L2 human

Classically, $\neg p \to p$ is equivalent to $p$, so AT is equivalent to $\neg p$.
So AT is false when $p$ is true, and it is not a tautology.
Connexive logic keeps AT and gives up some classical laws instead.
In Wansing's $\mathbf{C}$, AT follows in two steps from the axiom $\sim(A \to B) \leftrightarrow (A \to \sim B)$.
A trap is to add AT to classical logic; the result proves every formula.

### L3 human

Connexive logics come in many forms: relevance-style systems, conditional logics with selection functions, and constructive systems based on Nelson's strong negation.
The constructive system $\mathbf{C}$ is the result when the falsity condition of implication in $\mathbf{N4}$ is changed to "$A$ forces the falsity of $B$".
Then BT holds in the strong form $(A \to B) \leftrightarrow \sim(A \to \sim B)$, and the logic is contra-classical but not trivial.
The cost is that $\mathbf{C}$ is negation-inconsistent, so its non-triviality rests on its paraconsistency.
