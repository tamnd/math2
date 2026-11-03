---
tag: ECVNFXD1A2
kind: definition
name: Direct simulation Monte Carlo
msc: [76P05, 65C05, 82C40]
defines: HMK0W513W6
uses: [HWP11G3HTN, MH6CSWD7F0, 22V2W7KB1D]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_simulation_Monte_Carlo
---

## Definition

Consider a dilute gas in a region $\Omega \subseteq \R^3$, divided into cells.
Binary collisions are modelled by a cross section $\sigma(\abs{g}, \cdot)$ depending on the relative speed $\abs{g}$.
Each of $N$ simulated particles has a position in $\Omega$ and a velocity in $\R^3$, and represents $W$ real molecules.
*Direct simulation Monte Carlo* advances the particles by a time step $\Delta t$ by repeating the following steps.

1. Move: each particle moves freely, $x \mapsto x + v \Delta t$, with the boundary conditions applied at the walls.
2. Collide: in each cell, random pairs of particles in the cell are chosen. Each pair collides with probability proportional to $\abs{g}$ times its total cross section. The constant is fixed by $W$, $\Delta t$ and the cell volume.
3. Update: a colliding pair gets new velocities sampled from the collision model, conserving momentum and kinetic energy.
4. Sample: density, velocity and temperature in each cell are estimated by averages over its particles.

## Remarks

The splitting into free motion and local collisions mirrors the two terms of the [[Boltzmann equation|MH6CSWD7F0]].
Wagner proved in 1992 that Bird's scheme converges to a solution of the Boltzmann equation.
The limit is taken as the number of particles tends to infinity and the cells and the time step shrink.
The cells should be smaller than the mean free path, and $\Delta t$ smaller than the mean collision time, so the method is costly at small [[Knudsen numbers|22V2W7KB1D]].

Example: for hard spheres of diameter $d$, the total cross section is $\pi d^2$.
The post-collision relative velocity has length $\abs{g}$ and a direction uniform on the sphere, and the centre of mass velocity is unchanged.

Non-example: molecular dynamics integrates Newton's equations, with deterministic collisions between particles at contact.
It is not DSMC, because its collisions do not come from random pair selection within cells.
