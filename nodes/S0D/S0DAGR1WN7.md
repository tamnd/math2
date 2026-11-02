---
tag: S0DAGR1WN7
kind: example
name: Median algebra as a ternary algebra
msc: [08A99, 06D99, 05C05]
instance_of: [QJGPT2W0FT]
uses: [WC47MFR6GW, 0HM0HQCK6N, 0FRXBVVR03, 062D9KXJB1, 9879ZMW5AA]
sources:
  - url: https://en.wikipedia.org/wiki/Median_algebra
---

## Example

A median algebra is a set $A$ with one [[ternary operation|WC47MFR6GW]] $m$, written $\langle x, y, z \rangle$, such that for all $x, y, z, w \in A$:

1. $\langle x, y, y \rangle = y$;
2. $\langle x, y, z \rangle = \langle z, x, y \rangle$;
3. $\langle x, y, z \rangle = \langle x, z, y \rangle$;
4. $\langle \langle x, w, y \rangle, w, z \rangle = \langle x, w, \langle y, w, z \rangle \rangle$.

So it is an algebra with a single operation of arity $3$, defined by identities.

The basic instance is a [[distributive lattice|0HM0HQCK6N]] $(L, \wedge, \vee)$ with
$$\langle x, y, z \rangle = (x \wedge y) \vee (y \wedge z) \vee (z \wedge x).$$
On a [[total order|0FRXBVVR03]] this is the middle one of the three elements.
For instance on $\Z$ with the usual order, $\langle 1, 5, 3 \rangle = 3$ and $\langle 4, 4, 9 \rangle = 4$.
On $\set{0, 1}$ it is the majority function, and on $\set{0, 1}^n$ it is the majority taken in each coordinate.
Laws 1 to 3 are clear for the majority function, and law 4 can be checked on $\set{0, 1}$ by going through the cases.

## Remarks

In a [[tree|062D9KXJB1]], the median of three vertices is the unique vertex that lies on all three paths between them, and this gives a median algebra on the vertex set.
By laws 1 to 3, $\langle x, x, y \rangle = \langle x, y, x \rangle = \langle y, x, x \rangle = x$.
So $m$ is a [[majority term|9879ZMW5AA]] for the variety of median algebras.
The operation $x - y + z$ on $\Z$ is a non-example: it fails law 1, since it gives $x - y + y = x$, which differs from $y$ when $x \ne y$.

## Explanations

### L1 human

Given three numbers, the median picks the one in the middle.
A median algebra keeps only this operation and the rules it obeys.
If two of the three inputs agree, the answer is that common value, and the order of the inputs does not matter.
The same rules hold for the majority vote of three bits, and for the meeting point of three towns joined by roads that form a tree.
