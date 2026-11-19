---
tag: XFQSTCC4YM
kind: example
name: An intuitionistic derivation of a quantifier law
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
instance_of: [MW0RVDRFTA]
uses: [52XCYMK0WW, 9X08XK5RV2]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: Existential vs. universal quantification
---

## Example

We show $\mathsf{IQC} \vdash \exists x\, \neg A(x) \to \neg \forall x\, A(x)$, for every formula $A(x)$, in [[intuitionistic predicate logic|MW0RVDRFTA]].
We use the axioms and rules of [[remark 5 of the definition|52XCYMK0WW]] and the [[deduction theorem|9X08XK5RV2]] for sentences.

1. The axiom $\forall x\, A(x) \to A(x)$ is an instance of $\forall x\, \varphi \to \varphi[t/x]$ with $t = x$.
2. From $\neg A(x)$ and $A(x)$, modus ponens gives $\bot$. So $\vdash \neg A(x) \to (A(x) \to \bot)$.
3. With step 1, $\vdash \neg A(x) \to (\forall x\, A(x) \to \bot)$, that is, $\vdash \neg A(x) \to \neg \forall x\, A(x)$.
4. The variable $x$ is not free in $\neg \forall x\, A(x)$. The rule for $\exists$ gives $\vdash \exists x\, \neg A(x) \to \neg \forall x\, A(x)$.
5. In the same way, $\vdash \forall x\, \neg A(x) \to \neg \exists x\, A(x)$ and its converse are provable.

## Remarks

The law says that a counterexample refutes a universal claim.
Its converse, $\neg \forall x\, A(x) \to \exists x\, \neg A(x)$, is not provable; see [[the countermodel|SF981BPVYJ]].
The proof uses the witness from $\exists x$ only inside the scope of the rule for $\exists$, which is why no choice of object is needed.

## Explanations

### L1 human

If some number fails a property, then not all numbers have it.
This holds in intuitionistic logic: the failing number is a concrete counterexample.
The proof takes this number, applies "all numbers have the property" to it, and reaches a contradiction.

### L2 human

1. Take $A(x)$ to be "$x$ is even", over the natural numbers.
2. The witness $1$ gives $\exists x\, \neg A(x)$.
3. If $\forall x\, A(x)$ held, then $A(1)$ would hold, which contradicts $\neg A(1)$.

The typical use is as a basic quantifier law in constructive proofs.
A trap: the law has only this direction; the other direction needs a witness that the premise does not give.
