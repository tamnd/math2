---
tag: 9NQD3BC9N0
kind: example
name: The uniqueness of a product is abstract nonsense
msc: ["00A35", "18A30"]
topics: [Z2WNQ1DNTX]
audience: grad
instance_of: [STHWD1K9AN]
uses: [A2DE66937D, 859F0TFVA3, S5744QZV4N, EN4DD2FAJH, PZMGQMDN25, STHWD1K9AN]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_nonsense
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Product_(category_theory)
    locator: lead section
---

## Example

Let $\mathcal{C}$ be a [[category|A2DE66937D]], and let $X$ and $Y$ be objects of $\mathcal{C}$.
A [[product|S5744QZV4N]] of $X$ and $Y$ is an object $P$ with [[morphisms|859F0TFVA3]] $\pi_1 \colon P \to X$ and $\pi_2 \colon P \to Y$ that has the [[universal property|EN4DD2FAJH]]: for every object $Z$ with morphisms $f_1 \colon Z \to X$ and $f_2 \colon Z \to Y$, there is exactly one $u \colon Z \to P$ with $\pi_1 u = f_1$ and $\pi_2 u = f_2$.
We prove by [[abstract nonsense|STHWD1K9AN]] that two products $(P, \pi_1, \pi_2)$ and $(Q, q_1, q_2)$ of $X$ and $Y$ are isomorphic.

1. The universal property of $Q$, applied to $Z = P$ with $\pi_1$ and $\pi_2$, gives a unique $u \colon P \to Q$ with $q_1 u = \pi_1$ and $q_2 u = \pi_2$.
2. The universal property of $P$, applied to $Z = Q$ with $q_1$ and $q_2$, gives a unique $v \colon Q \to P$ with $\pi_1 v = q_1$ and $\pi_2 v = q_2$.
3. The composite $vu \colon P \to P$ satisfies
   $$\pi_1 (vu) = (\pi_1 v) u = q_1 u = \pi_1, \qquad \pi_2 (vu) = (\pi_2 v) u = q_2 u = \pi_2.$$
4. The identity $\mathrm{id}_P$ satisfies the same two equations.
   The universal property of $P$, applied to $Z = P$ with $\pi_1$ and $\pi_2$, allows only one such morphism, so $vu = \mathrm{id}_P$.
5. The same argument with $P$ and $Q$ exchanged gives $uv = \mathrm{id}_Q$.
   So $u$ is an [[isomorphism|PZMGQMDN25]], and by step 1 it is the only morphism $P \to Q$ that commutes with the projections.

So a product is unique up to a unique isomorphism that commutes with the projections.

## Remarks

The proof never uses elements, sets, groups or spaces.
So it applies at once to the Cartesian product of sets, the direct product of groups and the product of topological spaces.
This is the typical sense of "abstract nonsense": a complete proof from the general structure of a category, which then holds in every field that has that structure.

The same five steps prove that any two objects with the same universal property are isomorphic, for example two coproducts or two tensor products.
What the argument does not give is existence: in some categories two objects have no product at all, and the proof says nothing about that case.

## Explanations

### L1 human

"Abstract nonsense" is a joke name for proofs that use only very general rules.
This proof shows that a "product" is unique, in any setting where products make sense.
It uses only the rule that defines a product, and no details of sets, numbers or shapes.
So one short proof covers many fields at once.

### L2 human

In the category of sets, a product of $X = \{1, 2\}$ and $Y = \{a, b\}$ is the set of pairs
$$X \times Y = \{(1, a), (1, b), (2, a), (2, b)\},$$
with the two projections.
Another product is $Y \times X$, with the maps $(y, x) \mapsto x$ and $(y, x) \mapsto y$.
The abstract argument produces the map $u \colon X \times Y \to Y \times X$ with $u(x, y) = (y, x)$, and it shows that $u$ is the only map that respects the projections.
The two products are isomorphic but not equal: $(1, a)$ and $(a, 1)$ are different elements.
This is why the result says "up to isomorphism", and it is the usual reason to prove such facts once, abstractly, and not again in each field.
