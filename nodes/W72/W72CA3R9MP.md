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

A sequent calculus proves claims of the form "these assumptions give one of these conclusions", and each rule adds exactly one logical symbol, on the left or on the right.
Here is a derivation of $\exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y)$ in Gentzen's calculus LK, read from the top down:
$$\begin{array}{rll} 1. & R(a, b) \Rightarrow R(a, b) & \text{axiom} \\ 2. & \forall y\, R(a, y) \Rightarrow R(a, b) & {\forall}\mathrm{L} \text{ with the term } b \\ 3. & \forall y\, R(a, y) \Rightarrow \exists x\, R(x, b) & {\exists}\mathrm{R} \text{ with the term } a \\ 4. & \forall y\, R(a, y) \Rightarrow \forall y\, \exists x\, R(x, y) & {\forall}\mathrm{R} \text{ with eigenvariable } b \\ 5. & \exists x\, \forall y\, R(x, y) \Rightarrow \forall y\, \exists x\, R(x, y) & {\exists}\mathrm{L} \text{ with eigenvariable } a \\ 6. & \Rightarrow \exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y) & {\to}\mathrm{R} \end{array}$$
Check: at line 4, $b$ is not free in $\forall y\, R(a, y)$ or in $\forall y\, \exists x\, R(x, y)$; at line 5, $a$ is not free in either formula of the sequent.
So both eigenvariable conditions hold, and every formula in the derivation is a subformula of the last line, up to the variables $a$ and $b$.

In general, a sequent is an expression $\Gamma \Rightarrow \Delta$, where $\Gamma$ and $\Delta$ are finite sequences of formulas.
It is read as "if all formulas of $\Gamma$ hold, then some formula of $\Delta$ holds".
A derivation is a tree of sequents whose leaves are axioms $A \Rightarrow A$, and each other node follows by a structural rule (weakening, contraction, exchange), by the cut rule, or by a logical rule.
The rules ${\forall}$R and ${\exists}$L carry an eigenvariable condition.
The [[definition|PZX9J3VEMT]] gives LK for classical [[first-order logic|086QKPF0A6]] and its intuitionistic restriction LJ.

## Motivation

In [[natural deduction|6KT3BJZ7D1]] the open assumptions of a formula are spread over the leaves of the tree above it.
Gentzen wanted to study derivations as objects, and for this he wrote the assumptions next to each formula: a node $\Gamma \Rightarrow A$ records that $A$ is derived from $\Gamma$.
The elimination rules of natural deduction then become rules that introduce a symbol on the left, so every rule builds its conclusion from smaller formulas.
Allowing several formulas on the right made the calculus symmetric, and it gave classical logic without a special rule such as RAA.

The cut rule keeps the old way of reasoning through a lemma, and Gentzen's main theorem says that it can be removed.
A derivation without cut uses only subformulas of its end sequent, so proof search can work backward from the goal and never has to guess a lemma.
This makes the calculus the main tool of structural [[proof theory|N4EDJNMTEF]], and of many automated provers.
Later results of the area, such as [[Herbrand's theorem|VZ21F10WRS]] and [[Craig interpolation|E2CBFNAVZY]], are proved by induction on cut-free derivations.

## Notation

We write $\Gamma \Rightarrow \Delta$ for a sequent and $\vdash_{\mathsf{LK}} \Gamma \Rightarrow \Delta$ for derivability; many books write the sequent as $\Gamma \vdash \Delta$.
For a set of sentences $\Gamma$ and a sentence $\varphi$, we write $\Gamma \vdash_{\mathsf{LK}} \varphi$ when $\Gamma_0 \Rightarrow \varphi$ is derivable for some finite list $\Gamma_0$ of members of $\Gamma$.
Rule names are ${\to}$L, ${\to}$R and so on, with W, C and X for weakening, contraction and exchange.
Variants use multisets or sets in place of sequences, one-sided sequents $\Rightarrow \Delta$, or Kleene's G3 calculi, in which weakening and contraction are built into the other rules.

## Remarks

### How to read a sequent

The sequent $A_1, \dots, A_m \Rightarrow B_1, \dots, B_n$ says the same as $(A_1 \wedge \dots \wedge A_m) \to (B_1 \vee \dots \vee B_n)$.
So the commas on the left mean "and", and the commas on the right mean "or".
An empty left side reads as true, and an empty right side reads as false, so $\Gamma \Rightarrow$ says that the formulas of $\Gamma$ cannot all hold.
For example, $\Rightarrow A, \neg A$ is the sequent form of excluded middle, and it is derivable in LK in two steps from the axiom $A \Rightarrow A$.

### More derivations

[[A cut-free sequent derivation with quantifiers|FKQS2YNHH6]] derives $\forall x\, (P(x) \to Q(x)), \forall x\, P(x) \Rightarrow \forall x\, Q(x)$ in six steps, and it is also an LJ derivation.
[[A sequent derivation of the drinker paradox|VHY65FC0JZ]] derives $\Rightarrow \exists x\, (D(x) \to \forall y\, D(y))$ in nine steps.
It needs two formulas on the right and a contraction, so it is not an LJ derivation.

The sequent $\forall x\, P(x) \Rightarrow \exists x\, P(x)$ takes two steps.
From the axiom $P(y) \Rightarrow P(y)$, ${\exists}$R with the term $y$ gives $P(y) \Rightarrow \exists x\, P(x)$, and ${\forall}$L with the term $y$ gives the result.
This derivation is sound only because structures have nonempty domains.

### What is not a derivation

[[A sequent derivation that breaks the eigenvariable condition|REMQ2W88WG]] passes from $P(a) \Rightarrow P(a)$ to $P(a) \Rightarrow \forall x\, P(x)$ by ${\forall}$R, although $a$ is free on the left.
Its end sequent is false when $a$ names an element with $P$ and some other element lacks $P$.

The converse of the opening formula shows the same condition at work.
Search backward from $\forall y\, \exists x\, R(x, y) \Rightarrow \exists x\, \forall y\, R(x, y)$: ${\exists}$R with a term $a$, then ${\forall}$R with a new $b$, then ${\forall}$L with $b$, give $\exists x\, R(x, b) \Rightarrow R(a, b)$.
Now ${\exists}$L needs an eigenvariable not free in $R(a, b)$, so it cannot be $a$, and the leaf $R(c, b) \Rightarrow R(a, b)$ is not an axiom.
No other order of rules can succeed, because the sequent is false in $(\mathbb{N}, <)$ with $R(x, y)$ read as $y < x$.

### The facts you can use

LK is sound: every rule turns true sequents into a true sequent in each structure under each assignment, and the eigenvariable condition is what makes ${\forall}$R and ${\exists}$L sound.
It is complete, even without cut: every valid sequent has a cut-free derivation.
So LK derives the same consequences as the other calculi, by the [[equivalence of proof systems|A9AAHN4BMH]].

The [[cut-elimination theorem|AYRZ98Y0NW]] turns every LK derivation into a cut-free derivation of the same sequent, and the same holds for LJ.
The price can be a non-elementary growth in the size of the derivation.
A cut-free derivation has the [[subformula property|Z2NXKDK06G]]: every formula in it is a subformula of the end sequent, up to the substitution of terms for bound variables.
A closed [[semantic tableau|WGWBBVE8GX]] for $\Gamma$, read from the leaves upward, is a cut-free derivation of $\Gamma \Rightarrow$ in a one-sided form of LK.
In Kleene's classical G3 calculus every rule is invertible, so propositional proof search needs no backtracking.

### Watch out

Three slips are common.
The first is an eigenvariable that is free in another formula of the sequent, as in the non-example above.
The second is to read the right side as a conjunction: $\Rightarrow A, B$ says "$A$ or $B$", not "$A$ and $B$".
The third is to think that cut is needed for completeness; cut-free LK is already complete, and cut only shortens derivations.

### History

Gentzen introduced LK and LJ in "Untersuchungen über das logische Schließen" of 1934 to 1935, and he proved the cut-elimination theorem there.
In the same paper he drew consequences from it, among them the consistency of the calculi and the [[midsequent theorem|1FPWTGE14W]].

### Try it

First, derive $A \wedge B \Rightarrow B \wedge A$.
${\wedge}$L turns the axioms $B \Rightarrow B$ and $A \Rightarrow A$ into $A \wedge B \Rightarrow B$ and $A \wedge B \Rightarrow A$, and ${\wedge}$R joins them.

Second, say why the step from $Q(y), P(y) \Rightarrow P(y)$ to $Q(y), P(y) \Rightarrow \forall x\, P(x)$ is not an instance of ${\forall}$R.
The eigenvariable $y$ is free in $Q(y)$ and $P(y)$ on the left, so the condition fails.

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
2. ${\neg}$R moves $A$ from the left to the right as $\neg A$, and gives $\Rightarrow A, \neg A$.
3. ${\neg}$L moves $\neg A$ to the left as $\neg \neg A$, and gives $\neg \neg A \Rightarrow A$.
4. ${\to}$R gives $\Rightarrow \neg \neg A \to A$.

Step 2 has two formulas on the right, so this is not an LJ derivation, and indeed $\neg \neg A \to A$ is not intuitionistically valid.
The typical use is backward proof search: start from the goal and apply rules upward, choosing the rule by the main symbol of a formula.
Watch out: a formula $\forall x\, A$ on the left may be needed with two different terms, and then you must keep a copy of it by contraction before you apply ${\forall}$L.

### L3 human

The sequent calculus treats derivations as finite combinatorial objects, and cut elimination is a statement about them; this is the start of [[structural proof theory|R10RMQCJQX]].
The left and right rules correspond to the elimination and introduction rules of natural deduction, and cut corresponds to a detour, so normalization and cut elimination are two forms of one result.
Removing structural rules gives substructural logics: without contraction and [[weakening|VHRXX0T5XT]] one reaches [[linear logic|2P2184B6HE]], and without [[exchange|YAFD18WYJ8]] the non-commutative logics.
Craig interpolation, Herbrand's theorem and many consistency proofs are proved by induction on cut-free derivations.
