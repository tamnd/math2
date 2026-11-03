---
tag: WVVF2EJAH2
kind: statement
role: theorem
name: Hohenberg–Kohn theorems
msc: [81V70, 81V55, 81Q10]
uses: [VXDEQB46GV, HRBTG31X66, EYARCVGB0V]
about: [HRBTG31X66]
sources:
  - url: https://en.wikipedia.org/wiki/Density_functional_theory
---

## Statement

Let $N \ge 1$, and for a real potential $v \in L^{3/2}(\R^3) + L^\infty(\R^3)$ let
$$H_v = -\frac12 \sum_{i=1}^{N} \Delta_i + \sum_{1 \le i < j \le N} \frac{1}{\abs{x_i - x_j}} + \sum_{i=1}^{N} v(x_i)$$
be the [[Hamiltonian|VXDEQB46GV]] of $N$ electrons on the antisymmetric functions of $L^2((\R^3 \times \set{\uparrow, \downarrow})^N)$, in atomic units.
Write $\rho_\Psi$ for the one-particle density of a state $\Psi$ and $E_0(v)$ for the bottom of the spectrum of $H_v$.
Let $v$ and $v'$ be two such potentials for which $H_v$ and $H_{v'}$ have ground states.
Assume that these ground states do not vanish on any set of positive measure (unique continuation).

1. If some ground state of $H_v$ and some ground state of $H_{v'}$ have the same density, then $v - v'$ is constant almost everywhere.
2. Let $F_{\mathrm{HK}}[\rho] = E_0(v) - \int v \rho$ when $\rho$ is the density of a ground state of $H_v$; by part 1 this is well defined.
   Then $E_0(v) = \min_\rho \left( F_{\mathrm{HK}}[\rho] + \int v \rho \right)$ for every such potential $v$.
   Here $\rho$ runs over the ground state densities of all such potentials.
   The minimum is attained exactly at the ground state densities of $H_v$.

## Remarks

Proof of part 1: let $\Psi$ and $\Psi'$ be the ground states, with energies $E$ and $E'$ and common density $\rho$.
If $\Psi'$ is not a ground state of $H_v$, the [[variational method|EYARCVGB0V]] gives $E < \ip{\Psi'}{H_v \Psi'} = E' + \int (v - v')\rho$.
If also $\Psi$ is not a ground state of $H_{v'}$, the same argument gives $E' < E + \int (v' - v)\rho$, and adding the two gives $E + E' < E + E'$, a contradiction.
So one of them, say $\Psi$, is a ground state of both, and subtracting the two eigenvalue equations gives $\sum_i (v - v')(x_i)\Psi = (E - E')\Psi$; since $\Psi \ne 0$ almost everywhere, $v - v'$ is constant.
Part 2 is then the variational principle rewritten in terms of densities.

The unique continuation hypothesis is a gap in the original 1964 argument that later work had to fill.
It holds for broad classes of potentials, but its general proof is delicate.
The theorems justify [[density functional theory|HRBTG31X66]]: the ground state density determines $v$ up to a constant, hence $H_v$, hence every property of the ground state.

## Explanations

### L1 human

The first theorem says that the electron density of the ground state already fixes the external potential that produced it, up to an additive constant.
So, in principle, the density carries all the information about the system.
The second says that the ground state energy can be found by minimising an energy expressed through the density alone.

### L2 human

The functional $F_{\mathrm{HK}}$ is defined only on densities that come from ground states, the $v$-representable densities, a set that is hard to describe.
This is why the rigorous theory uses instead the Levy–Lieb functional, defined on all densities of finite kinetic energy, which agrees with $F_{\mathrm{HK}}$ where both are defined.
In practice the theorems are used through the Kohn–Sham equations, which replace the interacting electrons by non-interacting ones with the same density.
