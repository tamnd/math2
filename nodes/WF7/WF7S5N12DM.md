---
tag: WF7S5N12DM
kind: example
name: No finitary relative consistency proof of PA plus Con(PA) from PA
msc: ["03F25", "03F40"]
topics: [H8QZY0RZXZ]
audience: grad
not_instance_of:
  - target: X3G0RG2GPZ
    note: "PA (and so PRA) cannot prove Con(PA) -> Con(PA + Con(PA)): together with the axiom Con(PA) this would give PA + Con(PA) a proof of its own consistency, against the second incompleteness theorem."
uses: [X3G0RG2GPZ, ~c79a35b5, 0QFT7Z76N5, EQH7XTZ29V]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
  - book: isbn:9780521857840
---

## Example

Let PA be [[Peano arithmetic|0QFT7Z76N5]], and let $T = \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.
We show that no [[relative consistency proof|X3G0RG2GPZ]] of $T$ from PA can be carried out in PA, and so none in PRA.

1. $T$ is consistent, because $\N$ is a model of it, as in the example [[PA plus Con(PA) is not conservative over PA|EQH7XTZ29V]].
2. $T$ contains PA, and its axioms form a computable set, since it adds one sentence to PA.
3. Suppose $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(T)$. Then $T \vdash \mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(T)$, because $T$ contains PA.
4. $T \vdash \mathrm{Con}(\mathsf{PA})$, since it is an axiom of $T$. Modus ponens with step 3 gives $T \vdash \mathrm{Con}(T)$.
5. By steps 1 and 2 and [[Gödel's second incompleteness theorem|~c79a35b5]], $T \nvdash \mathrm{Con}(T)$. This contradicts step 4.
6. So $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(T)$. PA proves every theorem of PRA, after its function symbols are defined in PA, so PRA does not prove the implication either.

## Remarks

The implication $\mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(T)$ is true, since both sides are true, and ZF proves it, since ZF proves that $\N$ is a model of $T$.
So the example does not say that $T$ is "less consistent" than PA; it says that the step from PA to $T$ cannot be justified inside arithmetic.
The same argument shows that $\mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(T)$ fails to be provable whenever $T$ is consistent, recursively axiomatized, contains PA and proves $\mathrm{Con}(\mathsf{PA})$.
In contrast, $T^- = \mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$ does have a relative consistency proof from PA inside PA.
Indeed $\mathrm{Con}(T^-)$ says that PA does not prove $\mathrm{Con}(\mathsf{PA})$, and the formalized second incompleteness theorem is the statement $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA}) \to \lnot\mathrm{Prov}_{\mathsf{PA}}(\mathrm{Con}(\mathsf{PA}))$.

## Explanations

### L1 human

A relative consistency proof says "if the old rules are safe, so are the new ones".
If the new rules include the claim "the old rules are safe", the new rules are stronger in a precise sense.
Gödel's second theorem implies that arithmetic cannot show, by its own means, that such a stronger set of rules is safe, even assuming the old rules are safe.

### L2 human

We see where an attempted proof breaks down.

1. A natural attempt is to give a model: take a model $M$ of PA and show that $\mathrm{Con}(\mathsf{PA})$ is true in $M$.
2. This fails for some models: since PA does not prove $\mathrm{Con}(\mathsf{PA})$, the completeness theorem gives a model $M$ of $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$.
3. In such an $M$ the sentence $\mathrm{Con}(\mathsf{PA})$ is false, so $M$ is not a model of $T$, and no uniform construction from $M$ is visible.
4. The argument in steps 3 to 6 of the example shows that no other construction, formalizable in PA, can work.

The typical use is as a test for a proposed relative consistency proof: if the target theory proves the consistency of the base theory, the proof must use more than arithmetic.
A trap is to confuse this with unprovability of a true statement in general; the implication is provable, but only in a stronger theory.
