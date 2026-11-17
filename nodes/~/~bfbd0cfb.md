---
tag: ~bfbd0cfb
kind: example
name: The theory of dense linear orders without endpoints is decidable
msc: ["03B25", "03C10"]
topics: [E4AVTNWE9E]
audience: ug2
instance_of: [HWC687ES0Q]
uses: [HWC687ES0Q, ~269dc6e7, 2W4S2H4VYA, ZR7Y5C235P, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Dense_order
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
    locator: Examples
---

## Example

The signature is $\set{<}$ with one binary relation symbol.
Let $\mathrm{DLO}$ be the theory axiomatized by these six sentences.

1. Irreflexivity: $\forall x \, \neg (x < x)$.
2. Transitivity: $\forall x \, \forall y \, \forall z \, (x < y \wedge y < z \to x < z)$.
3. Linearity: $\forall x \, \forall y \, (x < y \vee x = y \vee y < x)$.
4. Density: $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \wedge z < y))$.
5. No endpoints: $\forall x \, \exists y \, (y < x) \wedge \forall x \, \exists y \, (x < y)$.
6. At least two elements: $\exists x \, \exists y \, (x \neq y)$.

We check that $\mathrm{DLO}$ is a [[decidable theory|HWC687ES0Q]].

1. The set of axioms is finite, hence computable.
2. $\mathrm{DLO}$ has a model: the rational numbers $(\Q, <)$ satisfy the six axioms. For density, between $a < b$ lies $(a + b)/2$.
3. $\mathrm{DLO}$ has no finite model. A finite nonempty linear order has a greatest element, which axiom 5 forbids.
4. $\mathrm{DLO}$ is $\aleph_0$-categorical: by Cantor's back-and-forth argument, every countable model is isomorphic to $(\Q, <)$; see [[dense linear order|2W4S2H4VYA]].
5. By the [[Łoś-Vaught test|ZR7Y5C235P]], steps 2 to 4 show that $\mathrm{DLO}$ is complete.
6. By the theorem that [[a complete axiomatizable theory is decidable|~269dc6e7]], steps 1 and 5 show that $\mathrm{DLO}$ is decidable.

## Remarks

The example gives the same conclusion as the theory of infinite sets, with a structure that has a relation.
$\mathrm{DLO}$ also has [[quantifier elimination|7FDDXV3JK7]], which gives a direct algorithm.
The signature has no constant symbols, so a quantifier-free sentence is built from $\top$ and $\bot$ only.
So the elimination procedure turns each sentence into $\top$ or $\bot$, and this is the answer.

When a parameter changes, the result changes in this way.

- If axiom 5 is dropped, the theory of dense linear orders with at least two elements is not complete. The sentence "there is a least element" is true in $[0, 1] \cap \Q$ and false in $\Q$.
- This weaker theory is still decidable. It has four completions, one for each choice of "least element or not" and "greatest element or not", and each completion is complete and finitely axiomatized. A sentence follows from the weaker theory if and only if it is in all four completions.
- If density is replaced by discreteness, one gets orders such as $(\Z, <)$. The theory $\operatorname{Th}(\Z, <)$ is complete and decidable, but it is not $\aleph_0$-categorical: two copies of $\Z$, one after the other, give a second countable model.

## Explanations

### L1 human

A dense order is an arrangement of points in a line where between any two points there is another one, like the fractions.
If the line has no first and no last point, all such arrangements look the same to first-order logic.
So every statement about them is either always true or always false, and a computer can find out which.
For example, "between any two points there are two more points" is always true.

### L2 human

We decide $\sigma = \forall x \, \exists y \, (x < y)$ by quantifier elimination.

1. The inner formula is $\exists y \, (x < y)$, with one free variable $x$.
2. In every model of $\mathrm{DLO}$, axiom 5 gives such a $y$ for each $x$. So $\exists y \, (x < y)$ is equivalent to $\top$ modulo $\mathrm{DLO}$.
3. The sentence becomes $\forall x \, \top$, which is equivalent to $\top$.
4. So $\sigma \in \mathrm{DLO}$.

A harder case is $\exists y \, (x < y \wedge y < z)$, with two free variables.
Modulo $\mathrm{DLO}$ it is equivalent to the quantifier-free formula $x < z$, by density in one direction and transitivity in the other.

The typical use of the example is as the simplest theory with quantifier elimination.
A trap is to forget the axiom of no endpoints: in $[0, 1] \cap \Q$, the formula $\exists y \, (x < y)$ is false at $x = 1$.
