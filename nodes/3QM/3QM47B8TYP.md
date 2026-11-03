---
tag: 3QM47B8TYP
kind: concept
name: Batalin–Vilkovisky formalism
msc: [81T70, 81T13, 58A50]
sources:
  - url: https://en.wikipedia.org/wiki/Batalin%E2%80%93Vilkovisky_formalism
same_as:
  wikidata: Q4868564
  wikipedia: Batalin–Vilkovisky formalism
---

## Summary

The Batalin–Vilkovisky (BV) formalism is a method for the quantization of gauge theories that extends [[BRST quantization|DCHKJBKCMR]].
To each field, including the ghosts, it adds an antifield of opposite parity.
On the functions of fields and antifields it defines an odd bracket, the antibracket, and a second-order operator $\Delta$, the BV Laplacian.
The action $S$ must satisfy the quantum master equation $\frac12 (S, S) = i\hbar\, \Delta S$.
Gauge fixing becomes the choice of a Lagrangian submanifold on which the path integral is taken.
The algebraic structure behind it is a [[Batalin–Vilkovisky algebra|ARMX1P0X0S]], and the formalism handles gauge symmetries whose algebra closes only up to equations of motion.

## Explanations

### L1 human

Gauge theories have redundant variables, and quantizing them needs extra bookkeeping.
BRST quantization handles the simplest cases with ghost fields.
The BV formalism doubles the set of variables: each field gets a partner, its antifield, with the opposite rule for commuting.
The doubled space carries an odd analogue of the symplectic structure of classical mechanics.
A single equation for the action, the master equation, then encodes the gauge symmetry and the consistency of the quantum theory.
