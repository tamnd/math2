---
tag: A0H8Q91FPB
kind: example
name: The generic partial order
aliases: [generic-partial-order, random-partial-order]
msc: ["03C15", "06A06"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [CWKWP7G6HB, HJVRBDQSGG]
uses: [CWKWP7G6HB, HJVRBDQSGG, XSCSX39GEZ, V5CKNFP3HC]
sources:
  - book: isbn:9780521587136
---

## Example

Let $\mathcal{P}$ be the class of finite strict partial orders, in the signature $\set{<}$.
We show that $\mathcal{P}$ has the [[amalgamation property|XSCSX39GEZ]], so it has a [[Fraïssé limit|HJVRBDQSGG]], the generic partial order.

1. Let $B, C \in \mathcal{P}$ with $B \cap C = A$, where $B$ and $C$ induce the same order on $A$.
2. On $D = B \cup C$, let $<_D$ be the transitive closure of $<_B \cup <_C$.
3. Take a chain $x = z_0 < z_1 < \dots < z_k = x'$ with $x, x' \in B$, each step in $B$ or in $C$.
4. Merge consecutive steps in the same structure. A switch between $B$ and $C$ happens at a point of $B \cap C = A$.
5. So each $C$-step joins two points of $A$, and it is also a $B$-step.
6. So $x <_B x'$ by transitivity. The same holds for $C$.
7. In particular $x <_D x$ never holds, so $<_D$ is a strict partial order that restricts to $<_B$ and $<_C$.
8. HP and JEP are clear, so [[Fraïssé's theorem|V5CKNFP3HC]] gives the limit.

## Remarks

The generic partial order is universal for countable partial orders.
It is one entry of Schmerl's list of countable homogeneous partial orders.
For $x \in B \setminus A$ and $y \in C \setminus A$, the construction gives $x <_D y$ exactly when $x <_B a <_C y$ for some $a \in A$.

## Explanations

### L1 human

Two finite orderings that agree on a common part can be combined.
Put both together and add only the comparisons forced by transitivity.
No new comparison inside either ordering appears, so both survive unchanged.

### L2 human

We amalgamate over $A = \set{a}$.

1. Let $B = \set{b < a}$ and $C = \set{a < c}$.
2. Transitivity forces $b < c$ in $D$.
3. $D$ is the chain $b < a < c$, which contains $B$ and $C$.

The typical use is to build a universal homogeneous partial order.
A trap is to add the union of the relations without closing under transitivity; the result need not be a partial order.
