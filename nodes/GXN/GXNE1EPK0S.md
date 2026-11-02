---
tag: GXNE1EPK0S
kind: definition
name: Nullary operation
msc: [08A62, 08A02]
defines: 9HPF7TE18C
uses: [EJ8YJVM9BW]
sources:
  - url: https://en.wikipedia.org/wiki/Arity
---

## Definition

Let $A$ be a set and let $A^0 = \set{()}$ be the set whose only element is the empty tuple $()$.
A *nullary operation* on $A$ is a [[finitary operation|EJ8YJVM9BW]] of arity $0$, that is, a function $c \colon A^0 \to A$.
The element $c(()) \in A$ is the *constant* given by $c$.

## Remarks

The map $c \mapsto c(())$ is a bijection from the set of nullary operations on $A$ to $A$.
So a nullary operation is usually written as an element of $A$.

Example: in $(\Z, +, 0)$ the constant $0$ is the nullary operation $c$ with $c(()) = 0$.

Non-example: on the empty set there is no nullary operation, because a function from the one-element set $A^0$ to $\emptyset$ does not exist.
This is why an algebra with a constant has a nonempty universe.
