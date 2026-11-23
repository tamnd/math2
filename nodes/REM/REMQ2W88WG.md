---
tag: REMQ2W88WG
kind: example
name: A sequent derivation that breaks the eigenvariable condition
msc: ["03F05", "03B10"]
topics: [TTCRX3NFNY]
audience: grad
not_instance_of:
  - target: W72CA3R9MP
    note: the step of the right rule for the universal quantifier uses an eigenvariable that is free in the antecedent
uses: [PZX9J3VEMT, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Inference rules
---

## Example

The following tree of sequents claims to derive $\Rightarrow P(a) \to \forall x\, P(x)$, that is, "if $a$ has $P$, then everything has $P$".

1. $P(a) \Rightarrow P(a)$ is an axiom.
2. $P(a) \Rightarrow \forall x\, P(x)$ is claimed by ${\forall}$R from step 1, with eigenvariable $a$.
3. $\Rightarrow P(a) \to \forall x\, P(x)$ follows by ${\to}$R from step 2.

We check that the tree is not a derivation, and that its end sequent is not valid.

1. The rule ${\forall}$R of the [[sequent calculus|PZX9J3VEMT]] requires that the eigenvariable is not free in the antecedent of the conclusion.
2. The antecedent of step 2 is $P(a)$, and $a$ is free in it.
   So step 2 breaks the condition, and the tree is not a derivation.
3. Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\{0, 1\}$, where $P$ holds of $0$ only, and let the assignment send $a$ to $0$.
4. Then $P(a)$ is true and $\forall x\, P(x)$ is false, so the sequent of step 2 and the end sequent are false in $\mathcal{M}$ under this assignment.
5. Every rule of LK turns true sequents into a true sequent, so no derivation has the sequent of step 2 or of step 3 as its end.

## Remarks

### What goes wrong

The error treats $a$ both as a fixed object, named in the hypothesis $P(a)$, and as an arbitrary object.
Step 2 is the sequent form of the informal error "$P(a)$, therefore $\forall x\, P(x)$".
In a structure with one element the end sequent is true, so the countermodel needs two elements.

### What is allowed

From the axiom $P(a) \Rightarrow P(a)$ no step of ${\forall}$R is possible, but ${\forall}$L is: with the term $a$ it gives $\forall x\, P(x) \Rightarrow P(a)$, which is valid.
The asymmetry is the point of the rules: a universal formula on the left may be used for any term, but one on the right needs a proof for a fresh variable.
Compare the correct use of ${\forall}$R in [[a cut-free sequent derivation with quantifiers|FKQS2YNHH6]], where the eigenvariable occurs only in the premise.

## Explanations

### L1 human

From "Ann is tall" we cannot conclude "everybody is tall".
The faulty derivation does exactly this, because the name $a$ appears in the assumption.
The rule for "everybody" may only be used for a name about which nothing is assumed.

### L2 human

To check a step of ${\forall}$R with eigenvariable $y$, look at every formula of the conclusion sequent.

1. The antecedent: here it is $P(a)$, and with $y = a$ it contains $y$.
2. The other formulas of the succedent: here there are none.
3. The new formula $\forall x\, P(x)$: here $a$ does not occur in it.

The check fails at item 1, so the step is wrong.
Watch out: checking only the formula that the rule introduces, item 3, would pass this wrong step.
