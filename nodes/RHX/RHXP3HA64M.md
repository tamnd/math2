---
tag: RHXP3HA64M
kind: statement
role: theorem
name: Knaster–Tarski theorem
msc: [06B23, 47H10]
uses: [D7A0ZGZT5S, 0A7KV2WB7A, DBD64TH52D, 0R3H5PANRQ, 0QF1MZ9FRG]
about: [D7A0ZGZT5S, DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Knaster%E2%80%93Tarski_theorem
same_as:
  wikidata: Q609612
  wikipedia: Knaster–Tarski theorem
---

## Statement

Let $(L, \le)$ be a [[complete lattice|D7A0ZGZT5S]] and let $f \colon L \to L$ be a [[monotone|0A7KV2WB7A]] map, so that $x \le y$ implies $f(x) \le f(y)$.
Let $\operatorname{Fix}(f) = \set{x \in L : f(x) = x}$.
Then $\operatorname{Fix}(f)$, with the order of $L$, is a complete lattice.
In particular $f$ has a [[least fixed point|DBD64TH52D]] and a greatest fixed point.
They are given by
$$\operatorname{lfp}(f) = \inf \set{x \in L : f(x) \le x}, \qquad \operatorname{gfp}(f) = \sup \set{x \in L : x \le f(x)},$$
where $\inf$ and $\sup$ are the [[infimum|0QF1MZ9FRG]] and the [[supremum|0R3H5PANRQ]] in $L$.

## Remarks

Proof idea for the least fixed point: let $D = \set{x : f(x) \le x}$ and $m = \inf D$.
For $x \in D$, $m \le x$ gives $f(m) \le f(x) \le x$, so $f(m)$ is a lower bound of $D$ and $f(m) \le m$.
Then $f(f(m)) \le f(m)$, so $f(m) \in D$ and $m \le f(m)$; hence $f(m) = m$, and every fixed point lies in $D$, so $m$ is the least one.
Let $W$ be a set of fixed points with supremum $a$ in $L$.
The map $f$ sends the complete lattice $\set{x \in L : a \le x}$ into itself.
Its least fixed point there is the join of $W$ in $\operatorname{Fix}(f)$, and meets are handled dually.
The join of a set of fixed points in $\operatorname{Fix}(f)$ need not be its join in $L$.
Example: on the power set of $\N$, the map $f(S) = \set{0} \cup \set{n + 2 : n \in S}$ is monotone, and its least fixed point is the set of even numbers.
Monotonicity is needed: on the two-element lattice $\set{0, 1}$, the map that swaps $0$ and $1$ has no fixed point.
Completeness is needed too: on the lattice $\Z$ the monotone map $x \mapsto x + 1$ has no fixed point.

## Explanations

### L1 human

If a rule moves the points of a complete lattice and never reverses the order, then some points stay put.
There is a smallest such point and a largest one, and the fixed points even form a complete lattice themselves.
The smallest fixed point is the meet of all points that the rule pushes downward.
This is why inductive definitions, such as "the smallest set containing $0$ and closed under adding $2$", always make sense.

### L2 human

The theorem is the basic existence result for fixed points in order theory.
In logic and computer science it gives the semantics of inductive and coinductive definitions as least and greatest fixed points.
It also underlies the proof of the Cantor–Schröder–Bernstein theorem through a monotone map on a power set.
When $f$ is moreover Scott-continuous, the [[Kleene fixed-point theorem|DDAHG7QRY8]] computes the least fixed point as the supremum of the iterates $f^n(\bot)$.
A converse holds: a lattice in which every monotone self-map has a fixed point is complete.
