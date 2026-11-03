---
tag: N0RZ8F0AYZ
kind: example
name: Rayleigh flow
msc: [76N15]
illustrates: [83Z3E8HMQ1]
uses: [83Z3E8HMQ1, GFHJ858AN1, FJC2GMVARF]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_flow
same_as:
  wikidata: Q3746869
  wikipedia: Rayleigh flow
---

## Example

*Rayleigh flow* is the steady, one-dimensional, frictionless flow of an ideal gas through a duct of constant cross-section.
Heat is added or removed through the walls.
Let $\gamma$ be the ratio of specific heats and $M$ the [[Mach number|GFHJ858AN1]].
The mass flux $\rho u$ and the momentum flux $p + \rho u^2$ are constant along the duct, and the stagnation temperature $T_0$ changes with the heat added.
With the index $*$ for the state at $M = 1$ on the same flow, the relations are
$$\frac{p}{p^*} = \frac{1 + \gamma}{1 + \gamma M^2}, \qquad \frac{T}{T^*} = \frac{(1 + \gamma)^2 M^2}{(1 + \gamma M^2)^2}, \qquad \frac{T_0}{T_0^*} = \frac{2(\gamma + 1) M^2 \left(1 + \frac{\gamma - 1}{2} M^2\right)}{(1 + \gamma M^2)^2}.$$
Check at $M = 1$: each right side equals $1$; for the last one, $2(\gamma + 1) \cdot \frac{\gamma + 1}{2} = (\gamma + 1)^2$.
The function $T_0 / T_0^*$ increases on $0 < M < 1$, decreases for $M > 1$, and has its maximum $1$ at $M = 1$.

## Remarks

So adding heat raises $T_0$ and drives the Mach number towards $1$: a subsonic flow accelerates and a supersonic flow decelerates.
The largest heat that can be added is $c_p (T_0^* - T_{0,\text{in}})$, with $c_p$ the specific heat at constant pressure; adding more makes the flow [[choked|83Z3E8HMQ1]] and changes the inlet conditions.
For subsonic heating between $M = 1/\sqrt{\gamma}$ and $M = 1$ the static temperature falls although heat is added, since $T/T^*$ has its maximum at $M = 1/\sqrt{\gamma}$.
In the enthalpy–entropy plane the states lie on a curve called the Rayleigh line.

## Explanations

### L1 human

Heat a gas flowing through a straight pipe, as in a combustion chamber, and ignore friction.
In a slow flow the heated gas expands and speeds up; in a supersonic flow heating slows it down.
Either way heating pushes the flow towards the speed of sound.
There is a limit to the heat one can add before the flow chokes, which matters in the design of jet engines and ramjets.
