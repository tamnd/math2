---
tag: ~e18beae4
kind: example
name: Discrete linear orders without endpoints are not inductive
aliases: [discrete-linear-orders-not-inductive]
msc: ["03C25", "06A05"]
topics: [1A9JSC5YG8]
audience: grad
not_instance_of:
  - target: ~719ccde0
    note: the chain of the orders of the multiples of 2 to the power minus n has the dense union of the dyadic rationals, where no element has an immediate successor
uses: [~ae02f1e0, 0FRXBVVR03, 0C4JS9RF5M, 676H7EGTKJ, YR6HCMABTE]
sources:
  - url: https://en.wikipedia.org/wiki/Existentially_closed_model
    locator: Definition
  - book: isbn:9780521587136
---

## Example

Let $L = \set{<}$ and let $T$ be the theory of discrete linear orders without endpoints.
Its axioms say that $<$ is a [[total order|0FRXBVVR03]] and that every element has an immediate successor and an immediate predecessor:
$$\forall x \, \exists y \, \big(x < y \land \neg \exists z \, (x < z \land z < y)\big), \qquad \forall x \, \exists y \, \big(y < x \land \neg \exists z \, (y < z \land z < x)\big).$$
We show that $T$ is not [[inductive|~ae02f1e0]].

1. For $n \in \N$ let $M_n = 2^{-n} \Z = \set{k / 2^n : k \in \Z}$, ordered as rational numbers.
2. Each $M_n$ is a model of $T$: the map $k \mapsto k / 2^n$ is an order isomorphism from the [[integers|0C4JS9RF5M]] onto $M_n$, and in $\Z$ the successor of $k$ is $k + 1$ and the predecessor is $k - 1$.
3. $M_n \subseteq M_{n+1}$, since $k / 2^n = 2k / 2^{n+1}$, and the order of $M_{n+1}$ restricts to that of $M_n$. So $(M_n)$ is a chain of models, each a [[substructure|676H7EGTKJ]] of the next.
4. The union $D = \bigcup_n M_n$ is the set of dyadic rationals. For $a < b$ in $D$, the midpoint $(a + b)/2$ is again in $D$ and lies strictly between them.
5. So no element of $D$ has an immediate successor, and the first axiom fails in $D$.

So the union of a chain of models of $T$ is not a model of $T$, and $T$ is not inductive.

## Remarks

The successor axiom has the form $\forall\exists\forall$, and its witness is destroyed at the next stage: the successor $2^{-n}$ of $0$ in $M_n$ is not the successor of $0$ in $M_{n+1}$.

The theory $T$ is the complete theory of $(\Z, <)$.
Since it is not inductive, it is not [[model complete|YR6HCMABTE]]; indeed $M_0 \subseteq M_1$ is not elementary, because $\exists z \, (0 < z < 1)$ holds in $M_1$ and fails in $M_0$.

When the signature changes, the result changes.
Add a function symbol $s$ for the successor, with the universal axioms $x < s(x)$ and $\neg (x < z \land z < s(x))$, and the $\forall\exists$ axiom $\forall x \, \exists y \, (s(y) = x)$.
This theory is axiomatized by $\forall\exists$ sentences, so it is inductive.
The chain above is no longer a chain of substructures, since $s(0)$ is $1$ in $M_0$ but $\frac 1 2$ in $M_1$.

## Explanations

### L1 human

In the integers, every number has a next number.
Make the steps smaller and smaller: first the integers, then the halves, then the quarters, and so on.
At each stage, every number still has a next number, but the next number keeps moving closer.
In the union of all stages, a number has no next one, because there is always a point in between.

### L2 human

We follow the element $0$ through the chain.

1. In $M_0 = \Z$, the successor of $0$ is $1$.
2. In $M_1$, the point $\frac 1 2$ appears between $0$ and $1$, and the successor of $0$ is $\frac 1 2$.
3. In $M_n$, the successor of $0$ is $2^{-n}$.
4. In the union $D$, any candidate $y = k / 2^n > 0$ fails, since $k / 2^{n+1}$ lies between $0$ and $y$.

The typical use of this example is to show that the chain condition is not automatic for theories with $\forall\exists\forall$ axioms.
A trap is to think that each stage being isomorphic to $\Z$ forces the union to be like $\Z$: isomorphic stages can have a very different union.
