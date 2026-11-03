---
tag: XXG4AC7H20
kind: statement
role: fact
name: Carathéodory's principle
msc: [80A05, 80A10]
uses: [TD4C13V3J6, 5EKTEE00FZ, W1RS8DA2H6, 0E3G0GRPZ6, 5Q4BHBFXJY]
about: [W1RS8DA2H6]
sources:
  - url: https://en.wikipedia.org/wiki/Second_law_of_thermodynamics
    locator: Carathéodory's principle
---

## Statement

In every neighbourhood of every equilibrium [[state|TD4C13V3J6]] of a thermodynamic system, there are equilibrium states that cannot be reached from it by an [[adiabatic process|W1RS8DA2H6]].

## Remarks

The principle is a form of the second law due to Constantin Carathéodory.
It is used with a theorem of Carathéodory on Pfaffian forms.
Let $\omega$ be a smooth [[differential form|0E3G0GRPZ6]] of degree $1$ on an open set of $\R^n$.
If every neighbourhood of every point contains points that cannot be joined to it by curves along which $\omega = 0$, then locally $\omega = \lambda \, d\sigma$ for functions $\lambda$ and $\sigma$.
Applied to the heat form $\delta Q_{\mathrm{rev}}$ of a simple system, this gives $\delta Q_{\mathrm{rev}} = T \, dS$, and so the existence of temperature and entropy.
The states with the same entropy form a hypersurface in the state space, and quasistatic adiabatic processes stay on it.
States of lower entropy near a given state are then not adiabatically accessible from it.

## Explanations

### L1 human

Near any state of a system, some other states cannot be reached without exchanging heat, no matter how one does work on it.
For example, one cannot cool a gas at fixed volume just by stirring it: stirring only heats it.
This simple fact is enough to build the whole theory of entropy.

### L2 human

Carathéodory's approach avoids heat engines and cycles.
It replaces them by a geometric statement about the space of states.
The mathematics behind it is the integrability of Pfaffian forms, which is related to the [[Frobenius theorem|5Q4BHBFXJY]].
