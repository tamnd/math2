---
tag: QXKJPEM4ZM
kind: definition
name: Flory–Huggins solution theory
msc: [82D60, 82B26]
defines: 16F0WBT5E0
uses: [M5WZKH7ZDV, 1DGJYHG10E]
sources:
  - url: https://en.wikipedia.org/wiki/Flory%E2%80%93Huggins_solution_theory
---

## Definition

Consider a lattice in which each site is occupied either by a solvent molecule or by one segment of a polymer chain of $N \ge 1$ segments.
Let $\varphi \in (0, 1)$ be the volume fraction of polymer, that is, the fraction of sites occupied by polymer segments.
Let $\chi \in \R$ be the Flory interaction parameter, the effective contact energy between polymer and solvent in units of $k_B T$.
The *Flory–Huggins free energy of mixing* per lattice site is
$$\frac{\Delta F(\varphi)}{k_B T} = \frac{\varphi}{N} \ln \varphi + (1 - \varphi) \ln (1 - \varphi) + \chi \varphi (1 - \varphi).$$
For a blend of two polymers with $N_A$ and $N_B$ segments, the first two terms are replaced by $\frac{\varphi}{N_A} \ln \varphi + \frac{1 - \varphi}{N_B} \ln(1 - \varphi)$.

## Remarks

The first two terms are the entropy of placing the chains, and the last term is a [[mean-field|1DGJYHG10E]] estimate of the energy of polymer-solvent contacts.
The mixture is locally unstable where $\Delta F'' < 0$, and the critical point solves $\Delta F'' = \Delta F''' = 0$.
This gives $\varphi_c = 1/(1 + \sqrt{N})$ and $\chi_c = \frac12 (1 + 1/\sqrt{N})^2$.
Check: $\Delta F''/(k_B T) = \frac{1}{N \varphi} + \frac{1}{1 - \varphi} - 2\chi$ and $\Delta F'''/(k_B T) = -\frac{1}{N \varphi^2} + \frac{1}{(1 - \varphi)^2}$.
The second vanishes when $1 - \varphi = \sqrt{N} \varphi$, and then the first vanishes when $2\chi = (1 + \sqrt{N})^2 / N$.
Example: for $N = 1$ the model is the regular solution model, with $\varphi_c = 1/2$ and $\chi_c = 2$.
As $N \to \infty$, $\chi_c \to 1/2$ and $\varphi_c \to 0$.
Non-example: real molecules do not sit on a lattice of equal-sized sites, so for them the lattice is only a heuristic.
Then $\chi$ is usually fitted to data and may depend on $\varphi$ and $T$.

## Explanations

### L1 human

The free energy has three parts: two entropy terms that favour mixing and one energy term that may oppose it.
The factor $1/N$ in front of the polymer entropy is what makes long chains so easy to demix.
