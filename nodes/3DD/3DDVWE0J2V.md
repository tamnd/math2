---
tag: 3DDVWE0J2V
kind: statement
role: theorem
name: Gibbs–Helmholtz equation
msc: [80A10, 80A50]
uses: [RBG5ZBM35Y, 722RZK72P5, KK46Q2YV1D, SPY89W0RJ7]
about: [RBG5ZBM35Y, 722RZK72P5]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs–Helmholtz_equation
same_as:
  wikidata: Q900590
  wikipedia: Gibbs–Helmholtz equation
---

## Statement

Let a closed system with a fixed amount of matter have absolute [[temperature|KK46Q2YV1D]] $T > 0$ and pressure $p$.
Let $G(T, p)$ be its [[Gibbs free energy|RBG5ZBM35Y]] and let $H = G + TS$ be its [[enthalpy|722RZK72P5]], where $S$ is the [[entropy|SPY89W0RJ7]].
Assume that $G$ is differentiable in $T$.
Then
$$\left( \frac{\partial (G/T)}{\partial T} \right)_p = -\frac{H}{T^2}.$$

## Remarks

The proof uses only the relation $(\partial G / \partial T)_p = -S$, which follows from $dG = -S\,dT + V\,dp$.
By the quotient rule, $\partial (G/T)/\partial T = -S/T - G/T^2 = -(G + TS)/T^2 = -H/T^2$.
The same argument applied to the Helmholtz free energy $F = U - TS$ at constant volume gives $(\partial (F/T)/\partial T)_V = -U/T^2$, where $U$ is the internal energy.
For a chemical reaction, apply the equation to the change $\Delta G$ and $\Delta H$ of the reaction.
With $\Delta G^\circ = -RT \ln K$ for the equilibrium constant $K$ and the gas constant $R$, it gives $d \ln K / dT = \Delta H^\circ / (R T^2)$.
So if $\Delta H$ is known as a function of $T$, the equation lets one compute $\Delta G$ at one temperature from its value at another.

## Explanations

### L1 human

The Gibbs free energy tells whether a process can happen by itself at fixed temperature and pressure.
The enthalpy measures the heat exchanged at fixed pressure.
The Gibbs–Helmholtz equation says how the free energy, divided by the temperature, changes when the temperature changes, and the rate is fixed by the enthalpy.
So heat measurements alone tell how the drive of a reaction depends on temperature.

### L2 human

The equation is a direct consequence of $G = H - TS$ and $(\partial G/\partial T)_p = -S$.
Its main use is in chemistry: integrating it from a reference temperature gives $\Delta G(T)$ from calorimetric data for $\Delta H(T)$.
Written for the equilibrium constant, it becomes the van 't Hoff equation for $\ln K$.
The analogue for the Helmholtz free energy links $F$ and the internal energy $U$ at constant volume.
In statistical mechanics it is the identity $U = -\partial \ln Z / \partial \beta$ for the partition function $Z$, with $\beta = 1/(kT)$.
