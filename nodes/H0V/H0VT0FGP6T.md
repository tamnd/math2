---
tag: H0VT0FGP6T
kind: statement
role: theorem
name: Quantum triviality
msc: [81T08, 81T27, 82B20]
uses: [R0KGM32QN6, P0DV2TCH1N, HVGDXMPB29]
about: [HVGDXMPB29]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_triviality
---

## Statement

Let $d \ge 4$.
Consider the ferromagnetic nearest-neighbour [[Ising model|R0KGM32QN6]] and the lattice $\phi^4$ models on $\Z^d$, at or near their critical point.
Take any continuum scaling limit of their field correlation functions.
Normalize the field so that the limiting two-point function is finite and nonzero.
Then the limit is [[Gaussian|P0DV2TCH1N]].
That is, its $n$-point functions are given by Wick's rule from its two-point function.

## Remarks

For $d \ge 5$ this was proved by Aizenman and by Fröhlich in the early 1980s.
The case $d = 4$ was proved by Aizenman and Duminil-Copin, and is called marginal triviality.
The proofs use random current or random walk representations of the correlation functions.
They bound the four-point Ursell function, which measures the deviation from Gaussian behaviour, by a quantity that tends to $0$ in the scaling limit.

So the lattice approach cannot give an interacting [[quartic interaction|HVGDXMPB29]] in four dimensions.
In $d = 2$ and $d = 3$, interacting $\phi^4$ theories exist; they are built by the methods of constructive field theory.
In perturbation theory, triviality shows up as a running coupling that grows at high energy and has a Landau pole.
So the renormalized coupling must vanish when the cutoff is removed.
The same is expected, but not proved, for quantum electrodynamics.

## Explanations

### L1 human

One tries to build an interacting field theory by placing it on a fine lattice and then letting the lattice spacing go to zero.
In four or more dimensions, for the simplest scalar model, the interaction disappears in this limit.
What is left is a free field.
So the $\phi^4$ model in four dimensions only makes sense as an effective theory with a cutoff.

### L2 human

Triviality is a statement about the scaling limit, studied with the renormalization group.
In $d > 4$ the Gaussian fixed point is stable, and in $d = 4$ the coupling is marginally irrelevant, decreasing only logarithmically.
For the Higgs sector of the Standard Model, which contains a quartic coupling, triviality is read as an upper bound on the energy scale where new physics must appear.
