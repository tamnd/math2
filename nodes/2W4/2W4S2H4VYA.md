---
tag: 2W4S2H4VYA
kind: example
name: Theory of dense linear orders
aliases: [dense-linear-order-theory, dlo]
msc: ["03C35", "03C10", "06A05"]
topics: [6XEXRME4C1]
audience: ug2
instance_of: [1JJCGNX240, A22K1X8GKD]
uses: [0FRXBVVR03, K4D3S1MBZH, 0NCJ5WXN6Z, 6F2DB4HTJR, ABN5PTXEHY, ZR7Y5C235P, 7FDDXV3JK7, NJY30DQG3H]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.aleph0_categorical_dlo
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Dense_order
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Omega-categorical_theory
    locator: Examples
  - book: isbn:9780387987606
---

## Example

The theory $\mathrm{DLO}$ is the theory in the signature $\set{<}$ with these axioms.

1. $<$ is a strict [[linear order|0FRXBVVR03]]: irreflexive, transitive, and any two distinct elements are comparable.
2. Density: $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \wedge z < y))$.
3. No least element: $\forall x \, \exists y \, (y < x)$. No greatest element: $\forall x \, \exists y \, (x < y)$.
4. Nontriviality: $\exists x \, \exists y \, (x \ne y)$.

The [[rational numbers|0NCJ5WXN6Z]] and the real numbers with their usual order are models.

### Four facts

We check four facts.

1. No finite models. A model has two elements $a < b$ by axioms 4 and 1. Density gives $a < c_1 < b$, then $a < c_2 < c_1$, and so on, so the model is infinite.
2. $\aleph_0$-categorical. Two countable models are isomorphic by [[Cantor's isomorphism theorem|ABN5PTXEHY]], proved by the [[back-and-forth method|6F2DB4HTJR]].
3. Complete. The signature is finite, so the [[Łoś-Vaught test|ZR7Y5C235P]] with $\kappa = \aleph_0$ and facts 1 and 2 give completeness.
4. Not $\kappa$-categorical for uncountable $\kappa$. This is shown below.

### Proof of fact 4

For fact 4, let $\Q \cdot I$ be the [[ordered sum|NJY30DQG3H]] of copies of $\Q$ indexed by a linear order $I$, ordered first by the index.

1. For nonempty $I$, $\Q \cdot I$ is dense without endpoints. Between $(i, p) < (i, q)$ lies $(i, \frac{p + q}{2})$, and between $(i, p) < (j, q)$ with $i < j$ lies $(j, q - 1)$. Also $(i, p - 1) < (i, p) < (i, p + 1)$.
2. Let $A = \Q \cdot \kappa + \Q$ and $B = \Q \cdot \kappa + \Q \cdot \omega_1$. Both are models of $\mathrm{DLO}$ by step 1, and both have size $\kappa$, since $\aleph_1 \le \kappa$.
3. In $A$, the copy of $\N$ in the final copy of $\Q$ is a countable set with no upper bound.
4. In $B$, let $S$ be countable. The indices in $\omega_1$ of the elements of $S$ in the final part form a countable set, which is bounded by some $\alpha < \omega_1$. Then the element $(\alpha + 1, 0)$ of the final part is above all of $S$.
5. An isomorphism maps unbounded sets to unbounded sets. By steps 3 and 4, $A \not\cong B$.

## Remarks

The theory has [[quantifier elimination|7FDDXV3JK7]], and it is decidable; see [[this example|NF13NBMSVJ]].
The proof of fact 2 shows more: in $(\Q, <)$, two $n$-tuples with the same order pattern are mapped to each other by an automorphism.
There are finitely many order patterns of $n$ points, so the automorphism group has finitely many orbits on $n$-tuples, as the [[Ryll-Nardzewski theorem|1513J40TKA]] requires.
For $\kappa = 2^{\aleph_0}$ there is a shorter pair: $\R$ and $\R + \Q$.
Every bounded nonempty subset of $\R$ has a least upper bound, while the copy of $\R$ in $\R + \Q$ is bounded and has none.
If axiom 3 is dropped, the theory of dense linear orders has four completions, by the presence or absence of a least and of a greatest element.
Each completion is $\aleph_0$-categorical, by the same back-and-forth argument applied to the interior.

## Explanations

### L1 human

In a dense order, between any two points there is a third, like the fractions on the number line.
Every countable dense order with no first and no last point is a copy of the fractions.
So the rules of dense orders without endpoints have only one countable world.
For larger sizes there are many worlds: one can end with a short tail, like a ray of fractions, or with a very long tail that no countable list of points can climb.

### L2 human

We use fact 2 to show that $\Q$ and $\Q \cap (0, 1)$ are isomorphic orders.

1. Both are countable, and both are dense, since the average of two points lies between them.
2. $\Q$ has no endpoints. $\Q \cap (0, 1)$ has none either: for $x$ in it, $x / 2 < x$ and $\frac{x + 1}{2} > x$ lie in it.
3. So both are countable models of $\mathrm{DLO}$, and fact 2 gives an isomorphism.
4. An explicit one is $x \mapsto \frac{1}{2} + \frac{x}{2(1 + \abs{x})}$, which is an increasing bijection from $\Q$ onto $\Q \cap (0, 1)$.

The typical use of $\mathrm{DLO}$ is as a first test case for every new notion of model theory.
A trap is to think that the explicit map in step 4 is always available; for two arbitrary countable dense orders the back-and-forth construction is needed.

### L3 human

$\mathrm{DLO}$ is the theory of the [[Fraïssé limit|HJVRBDQSGG]] of the finite linear orders, and its automorphism group is a standard example of an oligomorphic permutation group.
It is the basic example of an unstable theory and of an [[o-minimal|DTWHAW1N0V]] structure.
With infinitely many constants added, it gives [[Ehrenfeucht's theory|~51f2568c]] with exactly three countable models.
