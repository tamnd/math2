---
tag: FKQS2YNHH6
kind: example
name: A cut-free sequent derivation with quantifiers
msc: ["03F05", "03B10"]
topics: [TTCRX3NFNY]
audience: grad
instance_of: [W72CA3R9MP]
uses: [PZX9J3VEMT]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Example derivations
---

## Example

We derive $\forall x\, (P(x) \to Q(x)), \forall x\, P(x) \Rightarrow \forall x\, Q(x)$ in LK, with the rules of the [[sequent calculus|PZX9J3VEMT]].
In words: if every $P$ is a $Q$ and everything is a $P$, then everything is a $Q$.
We leave the exchange rule implicit.

1. $P(y) \Rightarrow P(y)$ is an axiom.
2. $Q(y) \Rightarrow Q(y)$ is an axiom.
3. $P(y) \to Q(y), P(y) \Rightarrow Q(y)$ follows by ${\to}$L from steps 1 and 2.
   Here $\Gamma$ is $P(y)$, $\Delta$ and $\Pi$ are empty, and $\Lambda$ is $Q(y)$.
4. $\forall x\, (P(x) \to Q(x)), P(y) \Rightarrow Q(y)$ follows by ${\forall}$L from step 3, with the term $y$.
5. $\forall x\, (P(x) \to Q(x)), \forall x\, P(x) \Rightarrow Q(y)$ follows by ${\forall}$L from step 4, with the term $y$.
6. $\forall x\, (P(x) \to Q(x)), \forall x\, P(x) \Rightarrow \forall x\, Q(x)$ follows by ${\forall}$R from step 5, with eigenvariable $y$.

Check step 6: $y$ is not free in $\forall x\, (P(x) \to Q(x))$, in $\forall x\, P(x)$, or in $\forall x\, Q(x)$, so the eigenvariable condition holds.
So the six steps form a derivation in LK.
Every succedent has at most one formula, so it is also a derivation in LJ.

## Remarks

### What the example shows

The derivation has no cut, and each formula in it is a subformula of the end sequent, up to the variable $y$.
This is the subformula property of cut-free derivations in the [[sequent calculus|W72CA3R9MP]].
It also shows the order in which backward search must work: ${\forall}$R first, because it needs a fresh variable, and ${\forall}$L afterward, with that same variable as its term.

### What changes when the order or a premise changes

If backward search applies ${\forall}$L first, say with a term $z$, the formula $P(z)$ enters the left side.
Then ${\forall}$R can no longer use $z$ as its eigenvariable, and it must pick a new variable that the left side says nothing about.

If the second premise is $P(a)$ for a variable $a$, the sequent $\forall x\, (P(x) \to Q(x)), P(a) \Rightarrow \forall x\, Q(x)$ is not valid.
In the domain $\{0, 1\}$ with $P$ and $Q$ true of $0$ only and $a$ read as $0$, both premises hold and $\forall x\, Q(x)$ fails.
The search fails at ${\forall}$R, because the eigenvariable must differ from $a$, and nothing on the left gives $P$ of the new variable.

## Explanations

### L1 human

The sequent says: "if every $P$ is a $Q$, and everything is a $P$, then everything is a $Q$".
The derivation picks an arbitrary object $y$.
It uses each hypothesis for $y$, gets "$y$ is a $Q$", and then concludes "everything is a $Q$".
Read from top to bottom, each step adds one logical word.

### L2 human

To find the derivation, work upward from the goal.

1. The right side is $\forall x\, Q(x)$, so apply ${\forall}$R with a new variable $y$; the goal becomes $\dots \Rightarrow Q(y)$.
2. Apply ${\forall}$L to each formula on the left with the term $y$.
3. Apply ${\to}$L to $P(y) \to Q(y)$, and both premises become axioms.

The typical use of such small derivations is in proofs of the subformula property and of interpolation, where a cut-free derivation is taken apart step by step.
Watch out: choose the eigenvariable before you instantiate the universal formulas on the left.
