---
tag: FNGWJR2FPK
kind: concept
name: Method of lines
msc: [65M20]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_lines
same_as:
  wikidata: Q1826712
  wikipedia: Method of lines
---

## Summary

The method of lines solves a time-dependent partial differential equation in two stages.
First only the space variables are discretised, by [[finite differences|X7HYEBA5SA]], finite volumes or finite elements.
This turns the equation into a large system of ordinary differential equations in time.
Then this system is solved with a numerical method for [[initial value problems|0FXDW992DS]].
This separation lets one reuse mature ODE solvers, with their error control and their methods for stiff problems.

## Explanations

### L1 human

Picture the space-time plane with a few vertical lines, one for each grid point in space.
Along each line the unknown is a function of time only, and the PDE couples each line to its neighbours.
So the PDE becomes a system of ODEs, one per line, which a standard ODE solver can handle.
For the [[heat equation|VP2HN86VAG]] $u_t = u_{xx}$, replacing $u_{xx}$ at $x_j$ by $(u_{j+1} - 2u_j + u_{j-1})/\Delta x^2$ gives the system $u_j'(t) = (u_{j+1}(t) - 2u_j(t) + u_{j-1}(t))/\Delta x^2$.
