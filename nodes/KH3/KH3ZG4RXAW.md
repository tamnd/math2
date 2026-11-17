---
tag: KH3ZG4RXAW
kind: example
name: A sentence with only infinite models
aliases: [axiom-of-infinity-in-first-order-logic]
msc: ["03B10", "03C13"]
topics: [E4AVTNWE9E]
audience: ug2
not_instance_of:
  - target: SERN6CRVWW
    note: the sentence uses the binary relation symbol <, and it has a model but no finite model, so the finite model property of monadic logic does not extend to it
uses: [SERN6CRVWW, AS0NHQMAKA, MVCH6N9SNW, 05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_model_property
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Trakhtenbrot%27s_theorem
    locator: lead section
---

## Example

Let $<$ be a binary relation symbol, and let $\sigma_\infty$ be the conjunction of these three sentences.

1. Irreflexivity: $\forall x \, \neg (x < x)$.
2. Transitivity: $\forall x \, \forall y \, \forall z \, (x < y \wedge y < z \to x < z)$.
3. No greatest element: $\forall x \, \exists y \, (x < y)$.

We check that $\sigma_\infty$ has a model, that it has no finite model, and that it is not in the [[monadic predicate calculus|SERN6CRVWW]].

1. The structure $(\N, <)$ is a [[model|MVCH6N9SNW]]. No number is less than itself, the order is transitive, and $n < n + 1$ for each $n$.
2. Let $\mathcal{A}$ be any model. Its domain is nonempty, so pick $a_0$. By axiom 3, pick $a_1$ with $a_0 < a_1$, then $a_2$ with $a_1 < a_2$, and so on.
3. By axiom 2 and induction on $j - i$, $a_i < a_j$ for all $i < j$.
4. If $a_i = a_j$ with $i < j$, then $a_i < a_i$, which contradicts axiom 1. So the elements $a_0, a_1, a_2, \ldots$ are pairwise distinct.
5. Hence every model of $\sigma_\infty$ is infinite.
6. The symbol $<$ is a [[binary relation|05AVARPXA2]] symbol, so $\sigma_\infty$ is not monadic.

## Remarks

The example shows that the [[finite model property of monadic logic|AS0NHQMAKA]] fails as soon as one binary relation symbol is allowed.
So for full first-order logic, a search through finite structures cannot decide satisfiability: on $\sigma_\infty$ it runs forever.
Each axiom is needed for the conclusion.

- Without irreflexivity, a one-element structure with $a < a$ is a model.
- Without transitivity, the structure $\set{0, 1}$ with $0 < 1$ and $1 < 0$ is a model.
- Without axiom 3, the empty relation on one element is a model.

Transitivity uses three variables, and $\sigma_\infty$ in prenex form has the prefix $\forall \forall \forall \exists$.
So $\sigma_\infty$ lies outside the [[two-variable fragment|S7C3C7DJRF]] and outside the [[Bernays-Schönfinkel-Ramsey class|ZF79MZRQ8V]] with prefix $\exists^* \forall^*$.
Both of these fragments have the finite model property, so they cannot contain a sentence like $\sigma_\infty$.

## Explanations

### L1 human

The sentence says: nothing is smaller than itself, "smaller than" chains together, and for each thing there is something bigger.
Starting from any thing, we can keep finding bigger things forever.
They are all different, because a repeated thing would be smaller than itself.
So any world where the sentence is true must have infinitely many things, like the whole numbers.

### L2 human

We try to build a model with three elements and see where it fails.

1. Take $\set{a, b, c}$. Axiom 3 at $a$ gives a bigger element; take $a < b$.
2. Axiom 3 at $b$ gives a bigger element. It is not $b$ by axiom 1, and if it were $a$, transitivity would give $a < a$. So $b < c$.
3. Axiom 3 at $c$ gives a bigger element. By transitivity $a < c$ and $b < c$, so any choice among $a$, $b$, $c$ gives $x < x$ for some $x$.
4. So no three-element model exists, and the same argument works for every finite size.

The typical use of $\sigma_\infty$ is to show that a fragment of first-order logic does not have the finite model property.
A trap is to drop transitivity and keep the conclusion: a cycle of length $2$ then satisfies the other two axioms.
