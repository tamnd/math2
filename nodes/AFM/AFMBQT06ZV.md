---
tag: AFMBQT06ZV
kind: statement
role: theorem
name: Kepler conjecture
msc: [52C17, 11H31, 05B40]
uses: [HF32CBN5MA, 4P5PSWADJD]
about: [HF32CBN5MA]
sources:
  - url: https://en.wikipedia.org/wiki/Kepler_conjecture
same_as:
  wikidata: Q966873
  wikipedia: Kepler conjecture
---

## Statement

Every [[sphere packing|HF32CBN5MA]] of equal balls in $\R^3$ has upper [[packing density|4P5PSWADJD]] at most
$$\frac{\pi}{\sqrt{18}} = \frac{\pi}{3\sqrt 2} \approx 0.7405.$$
The face-centred cubic packing attains this density.

## Remarks

Johannes Kepler stated the claim in 1611.
Gauss proved it for lattice packings in 1831.
Thomas Hales announced a proof in 1998, completed with Samuel Ferguson.
It reduces the problem to the minimization of a function over finitely many local configurations, and checks these by computer with linear programming bounds.
The Flyspeck project, led by Hales, completed a formal proof checked by the proof assistants HOL Light and Isabelle in 2014.
The bound is attained by infinitely many packings.
Any stacking of hexagonal layers, each layer resting in the hollows of the one below, has density $\pi/\sqrt{18}$.
The face-centred cubic and the hexagonal close packings are two of them.

## Explanations

### L1 human

The usual way grocers stack oranges, in layers where each orange sits in a dip of the layer below, fills about $74\%$ of space.
Kepler guessed that no arrangement of equal balls fills more.
This took almost four hundred years to prove, and the proof needed extensive computer checks.

### L2 human

The Kepler conjecture is the three-dimensional case of the sphere packing problem; the two-dimensional case is [[Thue's theorem|3P246RHXMF]].
Unlike in the plane, the densest local cluster of balls around one ball does not extend to a packing of space, so local arguments alone fail.
Hales's proof uses a carefully chosen partition of space into cells around the balls and a weighted volume score that handles this.
The other dimensions where the answer is known are $8$ and $24$, by the work of [[Viazovska and her coauthors|YJ48S89BZA]].
