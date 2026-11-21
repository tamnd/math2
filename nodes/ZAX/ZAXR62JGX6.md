---
tag: ZAXR62JGX6
kind: example
name: The five-element Nelson chain as a twist structure
msc: ["03G25"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [XRGDT262HQ]
uses: [GN34CR1AH1, NG943XNQWH]
sources:
  - book: isbn:9780444521415
---

## Example

Let $H = \set{0, h, 1}$ be the three-element [[Heyting algebra|NG943XNQWH]] chain, with $h \to 0 = 0$.
Let $A = \set{(a, b) \in H^2 : a \land b = 0}$, with the twist operations of [[the definition|GN34CR1AH1]].

1. Elements. $A = \set{(0, 1), (0, h), (0, 0), (h, 0), (1, 0)}$.
2. Order. $(a, b) \le (c, d)$ iff $a \le c$ and $d \le b$. So $(0, 1) < (0, h) < (0, 0) < (h, 0) < (1, 0)$, a chain.
3. Negation. $\sim(a, b) = (b, a)$ reverses the chain and fixes $(0, 0)$.
4. Implication. $(a, b) \to (c, d) = (a \to c, a \land d)$, with the Heyting implication of $H$.
5. The twist structure over any Heyting algebra satisfies the four clauses, so $A$ is a [[Nelson algebra|XRGDT262HQ]].

## Remarks

1. Name the elements $0 < p < u < q < 1$ in the order of item 2. Then $u \to p = (0 \to 0, 0 \land h) = (1, 0) = 1$, while the Heyting implication of the chain gives $u \to p = p$.
2. $q \to 0 = (h \to 0, h \land 1) = (0, h) = p$.
3. The quotient by $x \equiv y$ iff $x \to y = y \to x = 1$ has the classes $\set{0, p, u}$, $\set{q}$, $\set{1}$, and it is again $H$.

## Explanations

### L1 human

Each element is a pair: how strongly the claim is verified, and how strongly it is refuted.
Verification and refutation never both hold, even partly.
This gives five possible pairs, and they line up in a chain.

### L2 human

1. Compute $q \to q = (h \to h, h \land 0) = (1, 0) = 1$.
2. Compute $1 \to q = (1 \to h, 1 \land 0) = (h, 0) = q$.
3. Compute $\sim q = (0, h) = p$.

The typical use: the example shows how a Nelson algebra is built from a Heyting algebra.
The trap: the order on pairs reverses in the second coordinate.
