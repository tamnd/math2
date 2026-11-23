---
tag: A5P0CNY0GF
kind: example
name: A cut-free ω-derivation of ∀x (x + 0 = x)
msc: ["03F05", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
instance_of: [XAMKAB1BZM]
uses: [0QFT7Z76N5, 1QD0KDDGYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Ω-consistent_theory
    locator: ω-logic
---

## Example

We derive the sentence $\forall x \, (x + 0 = x)$ in the infinitary system of [[the ω-rule|XAMKAB1BZM]], and we measure the derivation.

1. For each $n$, the closed term $\bar n + 0$ has the value $n + 0 = n$, and the numeral $\bar n$ has the value $n$.
2. So the literal $\bar n + 0 = \bar n$ is true, and the sequent that consists of it is an axiom (Ax) of height $0$.
3. The ω-rule takes these infinitely many axioms as premises and concludes $\forall x \, (x + 0 = x)$.
4. The height of the conclusion is one more than the supremum of the heights of the premises:
   $$\sup_n 0 + 1 = 1.$$
   There are no cuts, so $\vdash^1_0 \forall x \, (x + 0 = x)$.

## Remarks

In [[Peano arithmetic|0QFT7Z76N5]] this sentence is an axiom, so the example is about the shape of infinitary derivations, not about strength.
The interesting change comes when we swap the order of the sum.

The sentence $\forall x \, (0 + x = x)$ needs the [[induction schema|1QD0KDDGYJ]] in PA.
In the ω-system it again has height $1$, because each closed instance $0 + \bar n = \bar n$ is a true literal that evaluation checks.
So induction disappears in the infinitary system, and only the evaluation of closed terms remains.
This is the reason the ω-rule makes cut elimination possible for arithmetic.

## Explanations

### L1 human

To show that adding $0$ to any number leaves it unchanged, the ω-rule lets us check $0 + 0 = 0$, $1 + 0 = 1$, $2 + 0 = 2$, and so on, one by one.
Each of these is a true calculation.
One application of the rule then gives the statement for all numbers at once.

### L2 human

We compare two derivations of $\forall x \, (0 + x = x)$.
In PA, we prove $0 + 0 = 0$, then derive $0 + Sx = Sx$ from $0 + x = x$ with the axiom $0 + Sx = S(0 + x)$, and then apply induction.
In the ω-system, for each $n$ the literal $0 + \bar n = \bar n$ is true by evaluation, so it is an axiom, and one ω-rule gives the sentence with height $1$.

The typical use is the embedding of PA into the ω-system, where every induction turns into ω-rules over instances.
Watch out: height $1$ does not mean a small object, since the derivation has infinitely many leaves.
