---
tag: AK41NNRHGD
kind: proof
name: Proof that the product of countable sets is countable
msc: ["03E10"]
proves: 08G4XH86JC
uses: [0ZG61TFBES, 0C81YBVTWH, 0NP5N5PYW5, 0PVG1CRAJN, 01FPXMTBX1]
sources:
  - url: https://proofwiki.org/wiki/Cartesian_Product_of_Countable_Sets_is_Countable
    locator: Formal Proof 1
---

## Proof

1. Let $A$ and $B$ be [[countable sets|0ZG61TFBES]]. By definition, there are [[injective functions|0PVG1CRAJN]] $f \colon A \to \N$ and $g \colon B \to \N$.
2. Define $h \colon A \times B \to \N \times \N$ on the [[Cartesian product|0C81YBVTWH]] by $h(a, b) = (f(a), g(b))$.
3. The map $h$ is injective. If $h(a, b) = h(a', b')$, then $f(a) = f(a')$ and $g(b) = g(b')$. So $a = a'$ and $b = b'$, since $f$ and $g$ are injective.
4. Let $\pi \colon \N \times \N \to \N$ be the [[Cantor pairing function|0NP5N5PYW5]], $\pi(x, y) = (x + y)(x + y + 1)/2 + y$. It is a bijection, so it is injective.
5. The composite $\pi \circ h \colon A \times B \to \N$ is [[injective|01FPXMTBX1]], as a composition of injections.
6. Hence $A \times B$ is countable.

## Idea

Countable means "can be labelled by natural numbers without repeats". A pair gets a pair of labels, and the Cantor pairing function packs a pair of natural numbers into one natural number without collisions.
