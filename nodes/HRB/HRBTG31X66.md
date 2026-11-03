---
tag: HRBTG31X66
kind: concept
name: Density functional theory
msc: [81V70, 81V55, 81Q05]
sources:
  - url: https://en.wikipedia.org/wiki/Density_functional_theory
same_as:
  wikidata: Q1048589
  wikipedia: Density functional theory
---

## Summary

Density functional theory describes the ground state of a many-electron system through its electron density.
The density is a function of only three variables, while the wave function of $N$ electrons depends on $3N$ variables.
The [[Hohenberg–Kohn theorems|WVVF2EJAH2]] show that the density determines the external potential.
They also show that the ground state energy is the minimum of a functional of the density.
The universal part of this functional is unknown, and practical DFT uses approximations of it, mostly through the Kohn–Sham scheme of non-interacting electrons.
It is the most widely used method for computing the electronic structure of molecules and solids.

## Explanations

### L1 human

The wave function of $N$ electrons is a function on a space of $3N$ dimensions, which is hopeless to store for large $N$.
The density only says how much electron charge sits at each point of ordinary space.
DFT shows that, in principle, the density alone is enough to find the ground state energy.
In practice one needs an approximate formula for the energy of the electrons in terms of their density, and good approximations make the method both fast and accurate.
