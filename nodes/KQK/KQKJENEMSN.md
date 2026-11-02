---
tag: KQKJENEMSN
kind: concept
name: Self-injective ring
msc: [16D50]
specializes: [0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-Frobenius_ring
---

## Summary

A left self-injective ring is a [[ring|0B1261B5ED]] that is an [[injective module|85H7PRHDPZ]] when viewed as a left module over itself.
Rings $\Z/n\Z$, [[Frobenius algebras|8EVP1K2CZH]] and products of fields are self-injective, while $\Z$ is not.
A left Noetherian left self-injective ring is exactly a [[quasi-Frobenius ring|KP1PP7A6JR]].

## Explanations

### L1 human

Every ring acts on itself by multiplication, so it is a module over itself.
Injective modules are those into which maps can always be extended from a submodule to a bigger module.
A self-injective ring is one for which the ring itself has this extension property.
For $\Z/6\Z$ this holds: any map from an ideal of $\Z/6\Z$ into $\Z/6\Z$ is multiplication by some element.
For $\Z$ it fails: the map $2\Z \to \Z$ sending $2$ to $1$ cannot be extended to $\Z$, since $1$ would have to go to $1/2$.
