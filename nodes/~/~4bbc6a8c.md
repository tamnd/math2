---
tag: ~4bbc6a8c
kind: example
name: Not every universal statement that fails has a counterexample
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
not_instance_of:
  - target: ~d18966da
    note: the classical law from not all x P(x) to some x not P(x) is not a theorem of IQC
uses: [~11b532e9]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: Existential vs. universal quantification
---

## Example

The formula $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$ is classically valid.
We show that it is not a theorem of [[intuitionistic predicate logic|~d18966da]].

1. Take worlds $w_0 \leq w_1$ with domains $D(w_0) = \set{a}$ and $D(w_1) = \set{a, b}$.
2. Let $P(a)$ hold at both worlds and $P(b)$ nowhere.
3. $w_1 \nVdash \forall x\, P(x)$, since $w_1 \nVdash P(b)$. Then $w_0 \nVdash \forall x\, P(x)$, by the clause for $\forall$.
4. So no world forces $\forall x\, P(x)$, and $w_0 \Vdash \neg \forall x\, P(x)$.
5. At $w_0$ the only object is $a$. $w_0 \nVdash \neg P(a)$, since $w_0 \Vdash P(a)$.
6. So $w_0 \nVdash \exists x\, \neg P(x)$, and the implication fails at $w_0$.
7. By soundness, $\mathsf{IQC}$ does not prove the formula.

## Remarks

The formula is a quantifier form of a De Morgan law.
The direction $\exists x\, \neg P(x) \to \neg \forall x\, P(x)$ is provable; see [[the derivation|~e68056ae]].
The weaker formula $\neg \forall x\, P(x) \to \neg \neg \exists x\, \neg P(x)$ holds at $w_0$ in this model, since $w_1 \Vdash \exists x\, \neg P(x)$.
That weaker formula is equivalent to the double negation shift for $P$, and refuting it needs an infinite Kripke frame.

## Explanations

### L1 human

Knowing that "not all objects have $P$" does not give a particular object without $P$.
In the model, the object without $P$ exists only at a later stage.
At the first stage, the claim "not all" holds, but no counterexample is yet available.

### L2 human

1. Check that $w_1 \Vdash \neg P(b)$: no world above $w_1$ forces $P(b)$.
2. Check that $b \notin D(w_0)$, so $b$ can not witness $\exists x\, \neg P(x)$ at $w_0$.

The typical use is to show that intuitionistic proofs of existence need witnesses.
A trap: the same model, with $b$ added to $D(w_0)$, forces $\exists x\, \neg P(x)$ at $w_0$ and does not refute the law.
