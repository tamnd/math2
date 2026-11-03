---
tag: XBVMWZJ5FF
kind: concept
name: Index map
msc: [46L80, 19K56]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Summary

The index map is the connecting homomorphism $\partial \colon K_1(B) \to K_0(I)$ attached to a short exact sequence $0 \to I \to A \to B \to 0$ of C*-algebras.
It measures the obstruction to lifting a [[unitary|KK9S67F8CA]] of $B$ to a unitary of $A$.
For the extension of the compact operators by the bounded operators, it is the [[Fredholm index|2V9Q4KHY1T]] of an operator.
It is one of the two connecting maps of the six-term exact sequence in operator K-theory.

## Explanations

### L1 human

Suppose $B$ is a quotient of $A$ by an ideal $I$, and $u$ is a unitary in $B$.
One can always lift $u$ to some element of $A$, but maybe not to a unitary.
The index map turns the failure into a class in $K_0(I)$, built from the projections that measure how far the lift is from being unitary.
In the main example, $A$ is the algebra of bounded operators, $I$ the compact operators, and $B$ the Calkin algebra.
A Fredholm operator $T$ gives a unitary-like element of $B$, and the index map returns $\dim \ker T - \dim \ker T^*$.
