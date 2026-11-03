---
tag: DHN1NV44A3
kind: statement
role: proposition
name: Thomas precession
msc: [83A05, 70B05]
uses: [H63B6HRZQA, 2E9AJVZS6E, CFE9SNEHMP]
about: [H63B6HRZQA]
sources:
  - url: https://en.wikipedia.org/wiki/Thomas_precession
same_as:
  wikidata: Q1760062
  wikipedia: Thomas precession
---

## Statement

Let a particle move in an inertial frame $S$ with velocity $\mathbf{v}(t)$, $\abs{\mathbf{v}(t)} < c$, and acceleration $\mathbf{a}(t) = d\mathbf{v}/dt$.
Let $\gamma = 1/\sqrt{1 - \abs{\mathbf{v}}^2/c^2}$ be the [[Lorentz factor|2E9AJVZS6E]].
Carry a rest frame along the particle so that its values at infinitesimally close moments differ by a pure boost, without rotation.
Compare it at each moment with the frame obtained from $S$ by the pure boost with velocity $\mathbf{v}(t)$.
Then, relative to these boosted lab axes, the axes of the carried rest frame rotate, a [[precession|CFE9SNEHMP]] with angular velocity
$$\boldsymbol{\omega}_T = \frac{\gamma^2}{\gamma + 1} \, \frac{\mathbf{a} \times \mathbf{v}}{c^2}.$$

## Remarks

Proof idea: compare the boost $B(\mathbf{v} + \mathbf{a} \, dt)$ with the composition of $B(\mathbf{v})$ and the small boost relating consecutive rest frames.
By [[Wigner rotation|H63B6HRZQA]], the two differ by a small rotation, and computing it to first order in $dt$ gives $\boldsymbol{\omega}_T \, dt$.
The precession vanishes for straight-line motion, where $\mathbf{a} \times \mathbf{v} = 0$.
For $\abs{\mathbf{v}} \ll c$ one has $\gamma \approx 1$ and $\boldsymbol{\omega}_T \approx \frac{1}{2c^2} \mathbf{a} \times \mathbf{v}$.
Example: for an electron in an atom, this precession reduces the naive spin-orbit coupling by a factor $\tfrac{1}{2}$, the Thomas half, which brings the fine structure in agreement with experiment.

## Explanations

### L1 human

A gyroscope carried along a curved path at high speed turns slowly, even if nothing twists it.
The turning comes from the geometry of Lorentz transformations, not from any force.
It is tiny at everyday speeds but matters in atoms, where it changes the energy levels of electrons.

### L2 human

Thomas precession is the infinitesimal form of Wigner rotation.
In the language of four-vectors, the rest frame is carried along the world line by Fermi–Walker transport.
Then $\boldsymbol{\omega}_T$ is the rotation of this transported frame relative to the lab axes.
In general relativity it is one part of the precession of a gyroscope in orbit, next to the geodetic effect and frame-dragging.
