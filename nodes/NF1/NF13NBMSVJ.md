---
tag: NF13NBMSVJ
kind: example
name: The theory of dense linear orders without endpoints is decidable
msc: ["03B25", "03C10"]
topics: [E4AVTNWE9E]
audience: ug2
instance_of: [HWC687ES0Q]
uses: [HWC687ES0Q, HZ7A7B2ERA, 2W4S2H4VYA, ZR7Y5C235P, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Dense_order
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
    locator: Examples
---

## Example

Start with one formula and watch its quantifier disappear.
In the rational numbers, the formula $\exists x \, (a < x \wedge x < b)$ asks whether some number lies strictly between $a$ and $b$.
If $a < b$, the midpoint $(a + b)/2$ works, and if $a \ge b$, no number can be above $a$ and below $b$.
So the formula says exactly the same as a formula without quantifiers:
$$\exists x \, (a < x \wedge x < b) \quad \text{is equivalent to} \quad a < b.$$
Check: for $a = 1$, $b = 2$ both sides are true, with $x = 3/2$, and for $a = 2$, $b = 1$ both sides are false.
Steps of this kind decide every sentence about dense orders.

The signature is $\{ < \}$ with one binary relation symbol.
Let $\mathrm{DLO}$ be the theory axiomatized by these six sentences.

1. Irreflexivity: $\forall x \, \neg (x < x)$.
2. Transitivity: $\forall x \, \forall y \, \forall z \, (x < y \wedge y < z \to x < z)$.
3. Linearity: $\forall x \, \forall y \, (x < y \vee x = y \vee y < x)$.
4. Density: $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \wedge z < y))$.
5. No endpoints: $\forall x \, \exists y \, (y < x) \wedge \forall x \, \exists y \, (x < y)$.
6. At least two elements: $\exists x \, \exists y \, (x \neq y)$.

We check that $\mathrm{DLO}$ is a [[decidable theory|HWC687ES0Q]].

1. The set of axioms is finite, hence computable.
2. $\mathrm{DLO}$ has a model: the rational numbers $(\mathbb{Q}, <)$ satisfy the six axioms.
   For density, between $a < b$ lies $(a + b)/2$.
3. $\mathrm{DLO}$ has no finite model.
   A finite nonempty linear order has a greatest element, which axiom 5 forbids.
4. $\mathrm{DLO}$ is $\aleph_0$-categorical: by Cantor's back-and-forth argument, every countable model is isomorphic to $(\mathbb{Q}, <)$, as the page on [[dense linear orders|2W4S2H4VYA]] shows.
5. By the [[Łoś-Vaught test|ZR7Y5C235P]], steps 2 to 4 show that $\mathrm{DLO}$ is complete.
6. By the theorem that [[a complete axiomatizable theory is decidable|HZ7A7B2ERA]], steps 1 and 5 show that $\mathrm{DLO}$ is decidable.

## Remarks

### Two algorithms

The proof above gives an algorithm that searches for a proof of $\sigma$ or of $\neg \sigma$.
It always stops, but it says nothing about how long the search takes.
[[Quantifier elimination|7FDDXV3JK7]] gives a direct algorithm, as in the opening computation.
Each step removes one innermost quantifier and replaces the formula by an equivalent one without it.
The signature has no constant symbols, so a quantifier-free sentence is built from $\top$ and $\bot$ only.
So the procedure turns each sentence into $\top$ or $\bot$, and that is the answer.

### What changes when an axiom changes

If you drop axiom 5, the theory of dense linear orders with at least two elements is no longer complete.
The sentence "there is a least element" is true in $[0, 1] \cap \mathbb{Q}$ and false in $\mathbb{Q}$.
This weaker theory is still decidable.
It has four completions, one for each choice of "least element or not" and "greatest element or not".
Each completion is finitely axiomatized and $\aleph_0$-categorical, hence complete and decidable.
A sentence follows from the weaker theory exactly when it lies in all four completions, so we run four decision procedures.

If you replace density by discreteness, you get orders such as $(\mathbb{Z}, <)$.
The theory $\operatorname{Th}(\mathbb{Z}, <)$ is complete and decidable, but it is not $\aleph_0$-categorical: two copies of $\mathbb{Z}$, one after the other, give a second countable model.
So the Łoś-Vaught route fails there, and a different proof of decidability is needed.

## Explanations

### L1 human

A dense order is an arrangement of points on a line where between any two points there is another one, like the fractions.
If the line has no first and no last point, all such arrangements look the same to first-order logic.
So every statement about them is either always true or always false, and a computer can find out which.
For example, "between any two points there are two more points" is always true.

### L2 human

We decide $\sigma = \forall x \, \exists y \, (x < y)$ by quantifier elimination.
The inner formula is $\exists y \, (x < y)$, with one free variable $x$.
In every model of $\mathrm{DLO}$, axiom 5 gives such a $y$ for each $x$, so $\exists y \, (x < y)$ is equivalent to $\top$ modulo $\mathrm{DLO}$.
The sentence becomes $\forall x \, \top$, which is equivalent to $\top$, so $\sigma \in \mathrm{DLO}$.

A harder case is $\exists y \, (x < y \wedge y < z)$, with two free variables, which is the opening example with new letters.
Modulo $\mathrm{DLO}$ it is equivalent to $x < z$, by density in one direction and transitivity in the other.

The typical use of the example is as the simplest theory with quantifier elimination.
Watch out: the axiom of no endpoints is essential, since in $[0, 1] \cap \mathbb{Q}$ the formula $\exists y \, (x < y)$ is false at $x = 1$.
