---
tag: VV17NJKNAR
kind: definition
name: Computational electromagnetics
msc: [35Q61, 65Z05, 78A25]
defines: P0GHZ1HVSG
uses: [9BWWD4QK8Y, 604T74VWDK, HSPJC4VVQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Computational_electromagnetics
---

## Definition

An *electromagnetic field problem* consists of these data:

1. a region of space, possibly unbounded, with the [[constitutive relations|604T74VWDK]] of the materials in it;
2. given sources, such as currents or incident fields;
3. boundary conditions, and for unbounded regions a radiation condition such as the [[Silver–Müller condition|HSPJC4VVQ8]].

Its solution is the field that satisfies [[Maxwell's equations|9BWWD4QK8Y]] with these data, in the time domain or at a fixed frequency.
*Computational electromagnetics* is the study and use of methods that approximate this solution by the solution of a finite system of algebraic equations.
Such a method consists of a discretization, which replaces the fields by finitely many unknowns, and an algorithm that solves the resulting system.

## Remarks

Example: the finite-difference time-domain method satisfies the definition.
Its unknowns are field values on a grid, and its algebraic equations are the difference equations that update them step by step in time.

Non-example: the Mie series gives the field scattered by a homogeneous sphere as an explicit infinite sum.
It is an exact formula, not a discretization of the problem, so it is not itself a method of computational electromagnetics, though it is used to test such methods.

The methods are usually sorted in two ways: time domain or frequency domain, and differential equation on a volume or integral equation on a surface.

## Explanations

### L1 human

A field problem says where the materials are, what drives the field and what happens at the borders.
A computational method turns it into finitely many numbers and equations.
The answer is approximate, and it gets better as the discretization gets finer.
