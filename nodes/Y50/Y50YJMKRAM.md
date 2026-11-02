---
tag: Y50YJMKRAM
kind: definition
name: Associative quotient of a magma
msc: [20N02, 20M05]
defines: T22ZTQRXGB
uses: [9689SFPVE9, DCSXXT4SER, N5KE7FH6CX, 0XMEM406JM]
sources:
  - url: https://en.wikipedia.org/wiki/Magma_(algebra)
---

## Definition

Let $(M, \cdot)$ be a [[magma|9689SFPVE9]].
Let $\sim$ be the smallest [[congruence|DCSXXT4SER]] on $M$ such that $(x \cdot y) \cdot z \sim x \cdot (y \cdot z)$ for all $x, y, z \in M$.
The *associative quotient* of $M$ is the [[quotient magma|N5KE7FH6CX]] $M/{\sim}$, with the quotient map $\pi \colon M \to M/{\sim}$, $\pi(x) = [x]$.

## Remarks

The quotient $M/{\sim}$ is a [[semigroup|0XMEM406JM]], since $([x][y])[z] = [(xy)z] = [x(yz)] = [x]([y][z])$.
Universal property: for every semigroup $S$ and every magma homomorphism $f \colon M \to S$, there is exactly one homomorphism $\bar f \colon M/{\sim} \to S$ with $\bar f \circ \pi = f$.
This holds because the kernel of $f$ is a congruence that contains all the pairs $((xy)z, x(yz))$, so it contains $\sim$.

Example: if $M$ is already a semigroup, then $\sim$ is equality and the associative quotient is $M$ itself.
Example: for the free magma on one letter $a$, the associative quotient is the free semigroup on $a$.
It is isomorphic to the positive integers under addition, with a bracketed word sent to its length.

Non-example: the one-element semigroup is a quotient of every nonempty magma, but it is not the associative quotient of the free magma on $a$.
The length map to $(\Z_{>0}, +)$ is a homomorphism to a semigroup that does not factor through the one-element quotient, so the universal property fails.

In Mathlib this construction is `Magma.AssocQuotient`.
