---
tag: 6Q7AHAZ6Q4
kind: concept
name: Induced representation of a locally compact group
msc: [22D30, 22D10]
sources:
  - url: https://en.wikipedia.org/wiki/Induced_representation
---

## Summary

Unitary induction builds a [[unitary representation|74BPYJNZTM]] of a [[locally compact group|AHV05ZBCYW]] $G$ from a unitary representation of a closed subgroup $H$.
The new space consists of square-integrable vector-valued functions on $G$ that transform under $H$ by the given representation, and $G$ acts by translation.
It extends the [[induced representation|JJP4JFH3C6]] of finite groups to subgroups of infinite index, such as lattices and parabolic subgroups.
Mackey's theory of induced representations uses it to build and classify irreducible representations, for example the principal series of semisimple Lie groups.

## Explanations

### L1 human

Suppose you know how a closed subgroup $H$ of $G$ acts on a Hilbert space $K$.
Look at functions on $G$ with values in $K$ whose behaviour along each coset $gH$ is dictated by the action of $H$.
Such a function is really a section of a bundle over the coset space $G/H$, and $G$ moves these sections around by translation.
For example, inducing the trivial representation of the trivial subgroup gives $L^2(G)$, where $G$ acts by left translation.
Inducing a character of $\Z$ up to $\R$ gives functions on the line that repeat up to a fixed phase factor after each step of length $1$.
