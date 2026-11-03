---
tag: RFNGJ09WDR
kind: concept
name: Weyl quantization
msc: [81S30, 35S05, 81S08]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner%E2%80%93Weyl_transform
---

## Summary

Weyl quantization is a rule that sends a function $a(x, \xi)$ on phase space $\R^{2n}$, called a symbol, to an operator $\mathrm{Op}^w(a)$ on functions on $\R^n$.
It sends the coordinates $x_j$ and $\xi_j$ to the position and momentum operators.
It treats products of them symmetrically, so that real symbols give symmetric operators.
It is one concrete answer to the ordering problem of [[canonical quantization|7NW2C10YSR]].
Its inverse, which sends an operator to its symbol, is the Wigner transform.
In analysis it is one of the standard quantizations of [[pseudo-differential operators|FF27N0BWTP]].

## Explanations

### L1 human

A classical observable is a function of position $x$ and momentum $\xi$.
To make it a quantum operator one must decide in which order to put the non-commuting operators $X$ and $P$.
Weyl's rule averages over all orders in a balanced way.
For example, the product $x\xi$ becomes $\frac12(XP + PX)$, halfway between $XP$ and $PX$.
The rule also respects the symmetries of phase space under linear symplectic changes of coordinates.
