---
tag: 3NGJGNEB85
kind: example
name: The theory of dense linear orders is inductive
aliases: [dense-linear-orders-inductive]
msc: ["03C25", "06A05"]
topics: [1A9JSC5YG8]
audience: grad
instance_of: [G8TRE2KSRV]
uses: [K0PXB1979D, 2W4S2H4VYA, YR6HCMABTE, NHCRZ74JHH, E52RM0KX94]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $L = \set{<}$ and let $\mathrm{DLO}$ be the theory of [[dense linear orders without endpoints|2W4S2H4VYA]].
We show in two ways that $\mathrm{DLO}$ is [[inductive|K0PXB1979D]].
Let $(M_i)_{i \in I}$ be a chain of models of $\mathrm{DLO}$ with union $M$.

### Directly from the axioms

1. The axioms of linear orders are universal. Any finitely many elements of $M$ lie in one $M_j$, and the order of $M$ restricts to that of $M_j$. So $M$ is a linear order.
2. Density is $\forall x \, \forall y \, \exists z \, (x < y \to x < z \land z < y)$. For $a < b$ in $M$, choose $j$ with $a, b \in M_j$, and $c \in M_j$ with $a < c < b$. Then $a < c < b$ in $M$.
3. No endpoints is $\forall x \, \exists y \, \exists z \, (y < x \land x < z)$. It is checked in the same way, with witnesses found in one $M_j$.

### By model completeness

1. $\mathrm{DLO}$ has [[quantifier elimination|E52RM0KX94]], so it is [[model complete|YR6HCMABTE]].
2. For $i < j$, the inclusion $M_i \subseteq M_j$ is an inclusion of models of $\mathrm{DLO}$, so $M_i \preceq M_j$. The chain is elementary.
3. By part 1 of the [[elementary chain theorem|NHCRZ74JHH]], $M_i \preceq M$ for every $i$. So $M$ satisfies the same sentences as $M_i$, and $M \models \mathrm{DLO}$.

## Remarks

The second argument works for every model complete theory, so every model complete theory is inductive.
For example $\mathrm{ACF}$ and the theory of real closed ordered fields are inductive.

When one axiom changes, the result changes.
Dense linear orders with a least and a greatest element are not inductive: the chain $[0, n] \cap \Q$ of such orders has the union $[0, \infty) \cap \Q$, with no greatest element.
The axiom "there is a greatest element" is $\exists\forall$, and the second argument fails because this theory is not model complete.

## Explanations

### L1 human

Take a growing sequence of orders, each dense and without endpoints, like the rationals inside larger and larger sets of real numbers.
Between two points of the union there is a point at the stage where both appear, and above each point there is a larger one at the same stage.
So the union is again dense without endpoints.

### L2 human

We follow the chain $M_n = \Q \cup (\Q + \sqrt 2) \cup \cdots \cup (\Q + n \sqrt 2)$, ordered as real numbers.

1. Each $M_n$ is a union of $n + 1$ dense subsets of $\R$ without endpoints, so it is dense without endpoints.
2. The union is $\bigcup_n (\Q + n \sqrt 2)$, a countable subset of $\R$.
3. For $a = 0$ and $b = \sqrt 2 - 1$, both in $M_1$, the point $c = \frac{\sqrt 2 - 1}{2}$ lies strictly between them, and $c \in \Q + \frac 1 2 \sqrt 2$ is not in the union. But the rational $\frac{1}{5}$ lies between them and is in $M_0$.
4. In the same way every witness for density is found at a fixed stage.

The typical use is to see that the union of e.c. linear orders is still e.c.
A trap is to think that the witness must be the midpoint: any point between $a$ and $b$ in the stage is enough.
