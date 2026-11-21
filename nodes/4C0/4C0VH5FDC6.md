---
tag: 4C0VH5FDC6
kind: example
name: The existentially closed linear orders are the dense linear orders without endpoints
aliases: [existentially-closed-linear-orders-dense]
msc: ["03C25", "06A05"]
topics: [1A9JSC5YG8]
audience: grad
instance_of: [6M98MCW575]
uses: [60HQMM380F, 0FRXBVVR03, 2W4S2H4VYA, E52RM0KX94]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: Model companion and model completion
  - book: isbn:9780521587136
---

## Example

Let $T$ be the theory of [[linear orders|0FRXBVVR03]] in the signature $\set{<}$.
We show that a linear order $M$ is an [[existentially closed model|60HQMM380F]] of $T$ if and only if $M$ is a [[dense linear order without endpoints|2W4S2H4VYA]].

1. Let $M$ be e.c., and let $a < b$ in $M$. Insert a new point $c$ with $a < c < b$; this gives a linear order $N \supseteq M$. The formula $\exists y \, (a < y \wedge y < b)$ is true in $N$, so it is true in $M$. So $M$ is dense.
2. Let $a \in M$. Add a new point above all of $M$; this gives a linear order $N \supseteq M$ where $\exists y \, (a < y)$ holds. So it holds in $M$, and $M$ has no greatest element. In the same way $M$ has no least element.
3. Conversely, let $M$ be dense without endpoints and $N \supseteq M$ a linear order. Let $\exists \bar y \, \chi(\bar a, \bar y)$ be true in $N$, with $\chi$ quantifier-free and $\bar a$ in $M$. Let $\bar b$ in $N$ be a witness.
4. The truth of $\chi(\bar a, \bar b)$ depends only on the order and the equalities between the entries of $(\bar a, \bar b)$.
5. We choose $\bar b'$ in $M$ in the same position relative to $\bar a$, one entry at a time. An entry that equals some $a_i$ is replaced by $a_i$.
6. An entry between two consecutive values among $\bar a$ and the chosen entries is placed between them, by density. An entry above or below all of them is placed there, since $M$ has no endpoints.
7. Then $(\bar a, \bar b')$ has the same order and equalities as $(\bar a, \bar b)$, so $M \models \chi(\bar a, \bar b')$, and $M \models \exists \bar y \, \chi(\bar a, \bar y)$.

So the e.c. linear orders are exactly the dense linear orders without endpoints.

## Remarks

The example shows that the theory of linear orders has the model companion $\mathrm{DLO}$.
Since $\mathrm{DLO}$ has [[quantifier elimination|E52RM0KX94]] and linear orders have the amalgamation property, $\mathrm{DLO}$ is even the model completion of the theory of linear orders.

When the class changes, the result changes in this way.

- The one-element order is a linear order, and it is not e.c., by step 2. So an e.c. linear order is infinite.
- For partial orders the class of e.c. models is again elementary. Its theory is the theory of the generic countable partial order, the [[Fraïssé limit|HJVRBDQSGG]] of the finite partial orders.

## Explanations

### L1 human

A linear order is a list in which any two different items are compared: one is before the other.
It is existentially closed when every new arrangement that a longer list can show already appears in the list.
For the whole numbers $1, 2, 3, \dots$ this fails: a longer list can have an item between $1$ and $2$, but the whole numbers have none.
For the fractions it holds, because there is always room between two fractions and beyond each one.

### L2 human

We follow steps 5 to 7 for $M = \Q$, $N = \R$, $\bar a = (0, 1)$ and the witness $\bar b = (\sqrt 2, 1/\pi)$.

1. In $N$ the order is $0 < 1/\pi < 1 < \sqrt 2$.
2. We replace $1/\pi$ by $1/2$, which lies between $0$ and $1$.
3. We replace $\sqrt 2$ by $2$, which lies above $1$.
4. The tuple $(0, 1/2, 1, 2)$ has the same order as $(0, 1/\pi, 1, \sqrt 2)$, so it satisfies the same quantifier-free formulas.

The typical use of the example is to show that a model companion can be found by a back-and-forth argument on finite configurations.
A trap is to forget the inequalities: a witness that differs from all $a_i$ must be replaced by a new point of $M$, not by some $a_i$.
