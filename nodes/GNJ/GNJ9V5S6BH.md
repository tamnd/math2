---
tag: GNJ9V5S6BH
kind: statement
role: theorem
name: Manley–Rowe relations
msc: [78A60]
uses: [7N71T3FKZ6, J7NEMSG2MD, NM024G378A, 8K67PTYTJ7]
about: [7N71T3FKZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Manley%E2%80%93Rowe_relations
same_as:
  wikidata: Q4428892
  wikipedia: Manley–Rowe relations
---

## Statement

Let a lossless medium have a second-order [[nonlinear susceptibility|7N71T3FKZ6]] with full permutation symmetry.
Let three collinear monochromatic [[plane waves|NM024G378A]] of frequencies $\omega_1, \omega_2$ and $\omega_3 = \omega_1 + \omega_2$ interact in it.
Let $I_j(z)$ be the intensity of the wave of frequency $\omega_j$ at position $z$ along the direction of travel, in the slowly varying envelope approximation.
Then
$$\frac{1}{\omega_1} \frac{dI_1}{dz} = \frac{1}{\omega_2} \frac{dI_2}{dz} = -\frac{1}{\omega_3} \frac{dI_3}{dz}.$$

## Remarks

The coupled amplitude equations of the three waves have coupling constants that, by permutation symmetry in a lossless medium, are all the same effective coefficient.
Substituting them into $dI_j/dz$ gives the same expression for $I_1'/\omega_1$ and $I_2'/\omega_2$ and its negative for $I_3'/\omega_3$.
The relations hold for any [[phase mismatch|J7NEMSG2MD]].
Adding them gives conservation of total intensity, $I_1 + I_2 + I_3$ constant, since $\omega_3 = \omega_1 + \omega_2$.
In terms of photons, $I_j / (\hbar \omega_j)$ is a photon flux, so each photon at $\omega_3$ that disappears produces one photon at $\omega_1$ and one at $\omega_2$.
Manley and Rowe first derived such relations in 1956 for lossless nonlinear reactances in electrical circuits.

## Explanations

### L1 human

When a strong pump wave splits into two lower-frequency waves, energy is shared in a fixed way.
For each pump photon lost, exactly one photon appears in each of the two other waves.
Since a photon carries energy proportional to its frequency, the energy flows in proportion to the frequencies.
This limits, for example, how much of the pump energy an amplifier can give to the signal.

### L2 human

In an [[optical parametric amplifier|8K67PTYTJ7]], the relations show that the signal and the idler gain equal numbers of photons.
In sum-frequency generation they give the maximum conversion efficiency from the lower frequencies to $\omega_3$.
For second-harmonic generation, with $\omega_1 = \omega_2$, they reduce to conservation of energy between the fundamental and the harmonic.
They are a first integral of the coupled amplitude equations and help to solve them in terms of Jacobi elliptic functions.
