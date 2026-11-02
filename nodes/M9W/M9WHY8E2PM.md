---
tag: M9WHY8E2PM
kind: concept
name: Gabor frame
msc: [42C15, 94A12]
sources:
  - url: https://en.wikipedia.org/wiki/Gabor_transform
---

## Summary

A Gabor frame is a frame of $L^2(\R)$ made of time shifts and frequency shifts of one window function $g$.
The shifts run over a lattice $a\Z \times b\Z$ of the time–frequency plane.
It gives a stable, discrete version of the [[short-time Fourier transform|3DHNP5NEWH]].
A function is determined by the samples of $V_g f$ on the lattice, and can be rebuilt from them.
A Gabor frame can exist only when $ab \le 1$.
At $ab = 1$, the [[Balian–Low theorem|XVVHKCYF2Z]] shows that the window cannot be well localized in both time and frequency.

## Explanations

### L1 human

Pick one short wave packet, say a bell curve.
Make copies of it shifted in time by multiples of $a$ and shifted in pitch by multiples of $b$.
If these copies are dense enough in the time–frequency plane, every signal can be written as a stable combination of them.
This is how one turns a continuous time–frequency picture into a grid of numbers that still holds all the information.
