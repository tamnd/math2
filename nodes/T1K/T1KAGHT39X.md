---
tag: T1KAGHT39X
kind: problem
name: Hilbert's sixth problem and the hydrodynamic limit
msc: [82C40, 76P05, 35Q20]
uses: [MH6CSWD7F0, RW0JK9VDZE, 18KXZHVF4M, CS1VGMQAG3, EFGYPV0VGJ]
about: [MH6CSWD7F0, 18KXZHVF4M]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_sixth_problem
history:
  posed_by: "David Hilbert"
  first_stated: "1900"
---

## Problem

Hilbert's sixth problem asks for a mathematical, axiomatic treatment of the physical theories in which mathematics plays a central role.
Within it, Hilbert asked for a rigorous account of the limits from the atomistic picture of a gas to the motion of continua.
In its standard modern form, the problem is the following.
Start from Newtonian dynamics of $N$ hard spheres of diameter $d$ with random initial data.
First derive the [[Boltzmann equation|MH6CSWD7F0]] in the Boltzmann–Grad limit $N \to \infty$, $d \to 0$, $N d^2$ fixed.
Then derive the compressible [[Euler equations|RW0JK9VDZE]] and the incompressible [[Navier–Stokes equations|18KXZHVF4M]] from the Boltzmann equation as the Knudsen number tends to $0$, the hydrodynamic limit.

## Remarks

The formal derivation of fluid equations from the Boltzmann equation is given by the Hilbert expansion and by [[Chapman–Enskog theory|CS1VGMQAG3]].
Lanford proved in 1975 that the Boltzmann equation is the limit of hard-sphere dynamics for a short time, a fraction of the mean free time.
Bardos, Golse and Levermore started in the early 1990s a program to derive weak solutions of fluid equations from the [[DiPerna–Lions renormalized solutions|EFGYPV0VGJ]] of the Boltzmann equation.
Golse and Saint-Raymond completed its main step in 2004, obtaining Leray solutions of the incompressible Navier–Stokes equations in this way.
In 2024 and 2025, Yu Deng, Zaher Hani and Xiao Ma announced a derivation of the Boltzmann equation from hard-sphere dynamics for long times.
Combined with hydrodynamic limits, their work gives a derivation of fluid equations from hard-sphere dynamics in certain settings.

## Explanations

### L1 human

Water and air are made of molecules, but engineers describe them by smooth fields such as velocity and pressure.
Hilbert asked in 1900 to prove that the smooth equations really follow from the laws of motion of the molecules.
The route goes in two steps: from molecules to Boltzmann's statistical equation, and from Boltzmann's equation to the fluid equations.
Each step is a hard limit theorem, and for a long time only short times or weak solutions were within reach.
