---
tag: 42GA7FHGW2
kind: example
name: A Kripke model with growing domains refutes the constant domain axiom
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
instance_of: [MW0RVDRFTA]
uses: [5GTQ69W47T]
sources:
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 6.1 Subintuitionistic and Intermediate Logics
---

## Example

Let $q$ be a sentence letter and $P$ a unary predicate.
The constant domain axiom is $\forall x\,(q \vee P(x)) \to q \vee \forall x\, P(x)$.
We refute it in a Kripke model for [[intuitionistic predicate logic|MW0RVDRFTA]].

1. Take worlds $w_0 \leq w_1$ with domains $D(w_0) = \set{a}$ and $D(w_1) = \set{a, b}$.
2. Let $P(a)$ hold at $w_0$ and $w_1$, $P(b)$ nowhere, and $q$ only at $w_1$.
3. The atomic facts persist from $w_0$ to $w_1$, so this is a model.
4. At $w_0$, the only object is $a$, and $w_0 \Vdash P(a)$, so $w_0 \Vdash q \vee P(a)$.
5. At $w_1$, $w_1 \Vdash q$, so $w_1 \Vdash q \vee P(d)$ for $d = a, b$.
6. By steps 4 and 5, $w_0 \Vdash \forall x\,(q \vee P(x))$.
7. $w_0 \nVdash q$. Also $w_0 \nVdash \forall x\, P(x)$, since $b \in D(w_1)$ and $w_1 \nVdash P(b)$.
8. So $w_0 \nVdash q \vee \forall x\, P(x)$, and the axiom fails at $w_0$.
9. By soundness for Kripke models with growing domains, $\mathsf{IQC}$ does not prove the axiom.

## Remarks

The new object $b$ arrives together with the truth of $q$, so it never witnesses a failure of the premise.
In a model with constant domains, $b$ would exist at $w_0$, and then $w_0 \nVdash q \vee P(b)$.
Indeed the axiom is valid in every Kripke model with constant domains, and the logic $\mathsf{CD}$ that it axiomatizes is complete for them.

## Explanations

### L1 human

At the start only one object is known, and it has the property $P$.
Later a new object appears, and at the same time $q$ becomes true.
So every object, at every stage, has $P$ or comes with $q$.
But at the start we can assert neither $q$ nor "every object has $P$".

### L2 human

1. Change the model so that $D(w_0) = D(w_1) = \set{a, b}$.
2. Then $w_0 \nVdash q \vee P(b)$, since $w_0$ forces neither disjunct.
3. So the premise fails at $w_0$, and the model no longer refutes the axiom.

The typical use is to separate $\mathsf{IQC}$ from the constant domain logic $\mathsf{CD}$.
A trap: the formula is classically valid, so the countermodel must use the growth of the domain.
