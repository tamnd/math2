---
tag: DDAHG7QRY8
kind: statement
role: theorem
name: Kleene fixed-point theorem
msc: [06B35, 03B70, 68Q55]
uses: [T4BCQHR68Y, C6GAHS1Z2P, DBD64TH52D, 0R3H5PANRQ, 0AANKKNHS4]
about: [DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Kleene_fixed-point_theorem
same_as:
  wikidata: Q3527263
  wikipedia: Kleene fixed-point theorem
---

## Statement

Let $(P, \le)$ be an [[omega-complete partial order|T4BCQHR68Y]]: every increasing sequence $x_0 \le x_1 \le x_2 \le \cdots$ in $P$ has a [[supremum|0R3H5PANRQ]] in $P$.
Assume that $P$ has a [[least element|0AANKKNHS4]] $\bot$.
Let $f \colon P \to P$ be [[continuous|C6GAHS1Z2P]] in this sense: $f$ is monotone, and $f\left(\sup_n x_n\right) = \sup_n f(x_n)$ for every increasing sequence $(x_n)$.
Then $f$ has a [[least fixed point|DBD64TH52D]], and
$$\operatorname{lfp}(f) = \sup_{n \ge 0} f^n(\bot),$$
where $f^0(\bot) = \bot$ and $f^{n+1}(\bot) = f(f^n(\bot))$.

## Remarks

Proof idea: $\bot \le f(\bot)$, and monotonicity gives $f^n(\bot) \le f^{n+1}(\bot)$ by induction, so the iterates form an increasing sequence with supremum $x$.
Continuity gives $f(x) = \sup_n f^{n+1}(\bot) = x$.
If $y$ is any fixed point, then $\bot \le y$ and induction gives $f^n(\bot) \le f^n(y) = y$, so $x \le y$.
The same statement holds for a directed-complete partial order with least element and a Scott-continuous $f$.
Example: on the power set of $\N$, the map $f(S) = \set{0} \cup \set{n + 2 : n \in S}$ preserves unions of increasing sequences.
Its iterates from $\emptyset$ are $\set{0}$, $\set{0, 2}$, $\set{0, 2, 4}$, and so on, and their union, the even numbers, is the least fixed point.
Continuity cannot be dropped from the formula: on the chain $\N \cup \set{\omega, \omega + 1}$, the monotone map with $f(n) = n + 1$, $f(\omega) = \omega + 1$ and $f(\omega + 1) = \omega + 1$ has least fixed point $\omega + 1$, while $\sup_n f^n(0) = \omega$.

## Explanations

### L1 human

Start at the bottom and apply $f$ again and again.
The values climb up step by step, and their limit is the least fixed point of $f$.
This gives a way to compute least fixed points, not only to know that they exist.
It is how the meaning of a recursive program is defined: run the recursion $0, 1, 2, \ldots$ levels deep and take the limit.

### L2 human

The theorem is the main tool of denotational semantics, where recursive definitions are interpreted as least fixed points of continuous maps on domains.
Compared with the [[Knaster–Tarski theorem|RHXP3HA64M]], it needs less of the order, only suprema of increasing sequences, but more of the map, namely continuity, and it gives an explicit construction.
For a monotone map that is not continuous, the iteration has to continue transfinitely, through $f^\omega(\bot) = \sup_n f^n(\bot)$, $f^{\omega + 1}(\bot)$, and so on, until it stabilises.
In Datalog and in dataflow analysis on finite lattices, the iteration stops after finitely many steps.
