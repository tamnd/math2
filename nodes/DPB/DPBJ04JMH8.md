---
tag: DPBJ04JMH8
kind: concept
name: Commutative algebra over a ring
msc: [13B02, 13A99]
specializes: [0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Associative_algebra
---

## Summary

A commutative algebra over a commutative ring $R$ is a [[commutative ring|0GYGHKX834]] $A$ together with a [[ring homomorphism|0GGE0Z0JQ1]] $R \to A$.
The homomorphism lets one multiply elements of $A$ by elements of $R$, so $A$ is at the same time a ring and an $R$-module.
Most rings in commutative algebra and algebraic geometry come with such a structure, for example polynomial rings over $R$ and their quotients.
The notion lets one compare rings over a fixed base and speak of $R$-algebra homomorphisms.

## Explanations

### L1 human

An $R$-algebra is a ring whose elements can be scaled by the elements of a base ring $R$.
Think of the polynomial ring $\R[x]$: one can add and multiply polynomials, and one can also multiply a polynomial by a real number.
The map that sends a real number $c$ to the constant polynomial $c$ is the structure map $\R \to \R[x]$.
Every commutative ring is an algebra over $\Z$ in exactly one way, since there is exactly one ring homomorphism $\Z \to A$.
