---
tag: CX8GDHENTT
kind: concept
name: TKNN invariant
msc: [81V70, 81Q70, 82D20]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Hall_effect
---

## Summary

The TKNN invariant of a filled energy band of a two-dimensional crystal is the first Chern number of the band.
Here the band is viewed as a line bundle over the Brillouin zone torus.
David Thouless, Mahito Kohmoto, Peter Nightingale and Marcel den Nijs studied it in 1982.
They showed that the Hall conductance of a band insulator is $e^2/h$ times the sum of these integers over the filled bands.
This explains why the conductance in the integer quantum Hall effect is an exact integer multiple of $e^2/h$.
In geometric terms it is the integral of the first [[Chern class|PAD37GKDPD]] of this line bundle over the torus.

## Explanations

### L1 human

Each energy band of a crystal comes with a Bloch wave for every point of the Brillouin zone, and these waves have phases.
Going around a small loop in the zone, the phase of the wave may turn, like the [[Berry phase|VKEYXGFS6E]].
Adding up all these turns over the whole zone, which is a torus, gives a whole number of full turns.
This number is the TKNN invariant.
It cannot change under small deformations, which is why the Hall conductance it controls is so robust.
