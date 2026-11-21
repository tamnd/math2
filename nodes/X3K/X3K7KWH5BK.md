---
tag: X3K7KWH5BK
kind: example
name: Finite linear orders form a Ramsey class
aliases: [finite-linear-orders-ramsey-class]
msc: ["05D10", "03C15"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [8XS8FCTF8T]
uses: [8XS8FCTF8T, 00TQV3F5S4, 0FRXBVVR03, SCRB74SWQN]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_Ramsey_theory
    locator: Examples
---

## Example

Let $\mathcal{L}$ be the class of finite [[linear orders|0FRXBVVR03]].
We show that $\mathcal{L}$ is a [[Ramsey class|8XS8FCTF8T]].

1. Let $A, B \in \mathcal{L}$ with $\lvert A \rvert = a \le \lvert B \rvert = b$, and let $k \ge 2$.
2. An [[embedding|SCRB74SWQN]] of an $a$-element order into a linear order $C$ is determined by its image, an $a$-subset of $C$. Every $a$-subset is the image of exactly one.
3. So colorings of $\binom{C}{A}$ are colorings of the $a$-subsets of $C$.
4. By the finite [[Ramsey theorem|00TQV3F5S4]], there is $n$ such that every $k$-coloring of the $a$-subsets of $\set{1, \dots, n}$ has a $b$-subset $H$ all of whose $a$-subsets have one color.
5. Take $C$ the chain $1 < \dots < n$, and let $g \colon B \to C$ be the order isomorphism onto $H$.
6. Every $g \circ e$ with $e \in \binom{B}{A}$ has image an $a$-subset of $H$, so all have the same color. Thus $C \to (B)^A_k$.

## Remarks

The structural statement is exactly Ramsey's theorem, because a linear order on a set is unique up to isomorphism and is rigid.
By the Kechris-Pestov-Todorcevic correspondence, the automorphism group of $(\Q, <)$ is extremely amenable.

## Explanations

### L1 human

For chains, a copy of a small chain inside a big chain is just a subset of the right size.
So the Ramsey question for chains is the original Ramsey question for subsets.

### L2 human

We take $A$ a one-point order, $B$ a $3$-point order and $k = 2$.

1. Copies of $A$ are points, so a coloring of $\binom{C}{A}$ is a $2$-coloring of the points of $C$.
2. Take $C$ with $5$ points. By pigeonhole, one color has at least $3$ points.
3. Those $3$ points, in their order, form a copy of $B$ with all points of one color.

The typical use is as the base case of structural Ramsey theory.
A trap is to think the order is irrelevant here; it is what makes each subset correspond to exactly one embedding.
