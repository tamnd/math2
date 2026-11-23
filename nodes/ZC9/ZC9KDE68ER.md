---
tag: ZC9KDE68ER
kind: example
name: Translating an ALC subsumption into modal logic
msc: ["03B70", "03B45"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [TXQ80B8ZSA]
uses: [G8BHVS9715, JS8W7PA6JK, YW6YGBMVQY]
sources:
  - url: https://en.wikipedia.org/wiki/Description_logic
    locator: Modal logic
  - url: https://en.wikipedia.org/wiki/Description_logic
    locator: First-order logic
---

## Example

We check the subsumption $\exists r.A \sqcap \forall r.B \sqsubseteq \exists r.(A \sqcap B)$ in [[ALC|TXQ80B8ZSA]] in three ways, and then refute a similar one.

1. Directly, let $d \in (\exists r.A \sqcap \forall r.B)^{\mathcal{I}}$.
   Some $e$ with $(d, e) \in r^{\mathcal{I}}$ has $e \in A^{\mathcal{I}}$, and every such $e$ lies in $B^{\mathcal{I}}$.
   So $e \in (A \sqcap B)^{\mathcal{I}}$ and $d \in (\exists r.(A \sqcap B))^{\mathcal{I}}$.
2. In modal logic, [[Schild's correspondence|G8BHVS9715]] with $\tau(A) = p$ and $\tau(B) = q$ turns the subsumption into $\Diamond p \wedge \Box q \to \Diamond(p \wedge q)$.
3. In $\mathsf{K}$, necessitation of the tautology $q \to (p \to p \wedge q)$ and the axiom $\mathrm{K}$ give $\Box q \to \Box(p \to p \wedge q)$.
   The $\mathsf{K}$ theorem $\Box(\varphi \to \psi) \to (\Diamond\varphi \to \Diamond\psi)$ then gives $\Box q \to (\Diamond p \to \Diamond(p \wedge q))$.
   So $\mathsf{K} \vdash \Diamond p \wedge \Box q \to \Diamond(p \wedge q)$, by the rules of [[normal modal logic K|JS8W7PA6JK]].
4. In first-order logic, the [[standard translation|YW6YGBMVQY]] turns the subsumption into $\exists y\,(r(x, y) \wedge A(y)) \wedge \forall y\,(r(x, y) \to B(y)) \to \exists y\,(r(x, y) \wedge A(y) \wedge B(y))$.
   This formula is valid, since the witness for the first conjunct is a witness for the conclusion.
5. Now consider $\exists r.A \sqcap \exists r.B \sqsubseteq \exists r.(A \sqcap B)$.
   It translates to $\Diamond p \wedge \Diamond q \to \Diamond(p \wedge q)$, which is not a theorem of $\mathsf{K}$.
6. The interpretation with $\Delta = \{d, e_1, e_2\}$, $r = \{(d, e_1), (d, e_2)\}$, $A = \{e_1\}$ and $B = \{e_2\}$ refutes the subsumption at $d$.
   Here $d$ lies in $\exists r.A$ and $\exists r.B$, but no successor of $d$ lies in $A \sqcap B$.

## Remarks

The direct check and the modal derivation are the same argument, because the semantic clauses agree.
The countermodel of step 6 is a Kripke model refuting $\Diamond p \wedge \Diamond q \to \Diamond(p \wedge q)$, read as an interpretation.
Every $\mathcal{ALC}$ concept translates into a first-order formula with one free variable that uses only two variables if bound variables are reused.

## Explanations

### L1 human

"Has some child who is a doctor, and all children are tall" implies "has a child who is a tall doctor".
"Has a child who is a doctor and a child who is tall" does not, since they may be different children.
Modal logic says the same with "possibly" and "necessarily" in place of "some child" and "all children".

### L2 human

1. Translate concept names to atoms, $\exists r$ to $\Diamond$ and $\forall r$ to $\Box$.
2. Prove the modal formula in $\mathsf{K}$ or refute it with a Kripke model.
3. Read the proof or the countermodel back as a statement about concepts.

The typical use is to reuse modal tableaux and complexity bounds for description logic reasoning.
Watch out: $\exists r$ does not distribute over $\sqcap$, just as $\Diamond$ does not distribute over $\wedge$.
