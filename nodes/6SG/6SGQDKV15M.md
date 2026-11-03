---
tag: 6SGQDKV15M
kind: statement
role: theorem
name: Euler pole of plate motion
msc: [86A60, "70E15"]
uses: [AYQQM6PBMR, 2ZVG43GSKA, 0CGYNDCWRR, 2FTZ7D8Z0F]
about: [AYQQM6PBMR]
sources:
  - url: https://en.wikipedia.org/wiki/Plate_reconstruction
---

## Statement

Let $S \subset \R^3$ be the sphere of radius $R$ centred at the origin.
Let a plate be a region of $S$ that moves rigidly on $S$.

1. Finite motion.
   The displacement of the plate between two times is given by some rotation $A \in SO(3)$.
   If $A \neq I$, then $A$ fixes exactly two points $\pm \mathbf{e}$ of $S$, and these are antipodal.
   The map $A$ is a rotation by an angle $\theta \in (0, \pi]$ about the axis through $\pm \mathbf{e}$, and $\mathbf{e}$ is a *finite rotation pole*.
2. Instantaneous motion.
   If the motion is differentiable in time, there is an angular velocity $\boldsymbol{\omega}(t) \in \R^3$.
   Each point $\mathbf{r}$ of the plate has velocity $\mathbf{v} = \boldsymbol{\omega} \times \mathbf{r}$.
   If $\boldsymbol{\omega} \neq 0$, the point $R \, \boldsymbol{\omega}/\abs{\boldsymbol{\omega}}$ is the *Euler pole*.
   A point at angular distance $\delta$ from it has speed $\abs{\mathbf{v}} = \abs{\boldsymbol{\omega}} R \sin \delta$.
3. Relative motion.
   Let two plates $P$ and $Q$ have angular velocities $\boldsymbol{\omega}_P$ and $\boldsymbol{\omega}_Q$.
   The velocity of $P$ seen from $Q$ is $(\boldsymbol{\omega}_P - \boldsymbol{\omega}_Q) \times \mathbf{r}$.

## Remarks

Part 1 is [[Euler's rotation theorem|2ZVG43GSKA]].
A rigid motion of $S$ that fixes the centre is an orthogonal map, and it has determinant $1$ because it is connected to the identity.
Every element of the [[special orthogonal group|0CGYNDCWRR]] $SO(3)$ other than $I$ has eigenvalue $1$ with a one-dimensional eigenspace.
Part 2 follows by differentiating $\mathbf{r}(t) = A(t) \mathbf{r}_0$: the matrix $\dot A A^{-1}$ is skew-symmetric, and every skew-symmetric $3 \times 3$ matrix acts as $\mathbf{r} \mapsto \boldsymbol{\omega} \times \mathbf{r}$.
Part 3 holds because angular velocities add, while finite rotations in general do not commute.
Example: with $\abs{\boldsymbol{\omega}} = 1^\circ$ per million years and $R = 6371$ km, a point at $\delta = 90^\circ$ moves $2\pi R/360 \approx 111$ km per million years, about $11$ cm per year.
Points near the Euler pole move slowly, and transform faults between two plates lie along small circles centred on their relative Euler pole.

## Explanations

### L1 human

A piece of a sphere that slides without bending can only turn about some axis through the centre of the sphere.
The axis meets the surface at the Euler pole.
Every point of the plate moves along a circle around this pole, slowly near the pole and fastest 90 degrees away from it.
So the motion of a whole plate is described by three numbers: the position of the pole and the rate of turning.

### L2 human

This result makes [[plate tectonics|AYQQM6PBMR]] quantitative.
Spreading rates at a ridge vary with the sine of the distance from the pole, and transform faults trace small circles about it.
Both facts are used to locate the pole from data.
[[Angular velocities|2FTZ7D8Z0F]] of plates around a closed circuit of boundaries must sum to zero, which checks the consistency of global plate motion models.
Finite rotations are composed by matrix multiplication and are the basis of plate reconstructions.
