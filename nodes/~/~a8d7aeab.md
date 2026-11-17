---
tag: ~a8d7aeab
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

Consider the following tree of sequents, which claims to derive $\Rightarrow P(a) \to \forall x\, P(x)$.

1. $P(a) \Rightarrow P(a)$. Axiom.
2. $P(a) \Rightarrow \forall x\, P(x)$. Claimed ${\forall}$R from step 1, with eigenvariable $a$.
3. $\Rightarrow P(a) \to \forall x\, P(x)$. ${\to}$R from step 2.

We check that the tree is not a derivation, and that its end sequent is not valid.

4. The rule ${\forall}$R in the [[definition|PZX9J3VEMT]] requires that the eigenvariable is not free in the antecedent of the conclusion.
5. The antecedent of step 2 is $P(a)$, and $a$ is free in it. So step 2 breaks the condition, and the tree is not a derivation.
6. Let $\mathcal{M}$ be the [[structure|983GZBQYT4]] with domain $\{0, 1\}$, where $P$ holds of $0$ only, and let $s(a) = 0$.
7. Under $s$, $P(a)$ is true and $\forall x\, P(x)$ is false. So the sequent of step 2 is false in $\mathcal{M}$ under $s$.
8. Every rule of LK turns true sequents into a true sequent. So no derivation has the end sequent of step 2 or of step 3.

## Remarks

The error treats $a$ both as a fixed object, named in the hypothesis $P(a)$, and as an arbitrary object.
The step from the axiom to $P(a) \Rightarrow \forall x\, P(x)$ is the sequent form of the error "$P(a)$, therefore $\forall x\, P(x)$".
The correct step ${\forall}$R from $P(a) \Rightarrow P(a)$ is impossible, but ${\forall}$L is allowed: it gives $\forall x\, P(x) \Rightarrow P(a)$, which is valid.
In a structure with one element the end sequent is true, so the countermodel needs two elements.

## Explanations

### L1 human

From "Ann is tall" we cannot conclude "everybody is tall".
The faulty derivation does exactly this, because the name $a$ appears in the assumption.
The rule for "everybody" may only be used for a name about which nothing is assumed.

### L2 human

To check a step of ${\forall}$R with eigenvariable $y$, list the formulas of the conclusion sequent.

1. The antecedent: here $P(a)$, which contains $y = a$.
2. The other formulas of the succedent: here there are none.
3. The new formula $\forall x\, P(x)$: here $a$ does not occur in it.

The check fails at item 1, so the step is wrong.
A trap is to check only the formula that the rule introduces.
