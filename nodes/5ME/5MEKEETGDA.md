---
tag: 5MEKEETGDA
kind: concept
name: Weak dimension
msc: ["16E10", 16D40]
sources:
  - url: https://en.wikipedia.org/wiki/Flat_module
---

## Summary

The weak dimension, or flat dimension, of a [[module|0NZ8JA25WK]] is the shortest length of a resolution of it by [[flat modules|73RYYEVDKA]].
The weak global dimension of a [[ring|0B1261B5ED]] is the supremum of the weak dimensions of its modules.
It is measured by the vanishing of the [[Tor functors|DDQRERAQCV]] and is the same for left and right modules.
It is at most the [[global dimension|GWA0T1WKCN]] and often easier to compute; rings of weak global dimension $0$ are exactly the von Neumann regular rings.

## Explanations

### L1 human

Flat modules are the modules that behave well under tensor products, and every free module is flat.
A general module can be approximated by flat modules in a chain, called a flat resolution.
The weak dimension counts how many steps such a chain needs at least.
Over the integers, a module like $\Z/2$ needs one step: $0 \to \Z \to \Z \to \Z/2 \to 0$, so its weak dimension is $1$.
A ring of small weak dimension has a simple homological theory.
