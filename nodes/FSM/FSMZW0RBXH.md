---
tag: FSMZW0RBXH
kind: example
name: Fanno flow
msc: [76N15]
illustrates: [83Z3E8HMQ1]
uses: [83Z3E8HMQ1, GFHJ858AN1, FJC2GMVARF]
sources:
  - url: https://en.wikipedia.org/wiki/Fanno_flow
same_as:
  wikidata: Q3746868
  wikipedia: Fanno flow
---

## Example

*Fanno flow* is the steady, one-dimensional, adiabatic flow of an ideal gas through a duct of constant cross-section with wall friction.
Let $D$ be the hydraulic diameter of the duct and $f$ the Fanning friction factor, assumed constant.
Let $\gamma$ be the ratio of specific heats and $M$ the [[Mach number|GFHJ858AN1]].
The mass flux $\rho u$ and the stagnation temperature are constant along the duct, while friction raises the entropy.
Let $L^*$ be the length of duct needed to bring the flow from Mach number $M$ to $M = 1$.
Then
$$\frac{4 f L^*}{D} = \frac{1 - M^2}{\gamma M^2} + \frac{\gamma + 1}{2\gamma} \ln\frac{(\gamma + 1) M^2}{2 + (\gamma - 1) M^2}.$$
Check at $M = 1$: both terms vanish, so $L^* = 0$, as it should.
For $M \to 0$ the right side tends to $+\infty$, so a very slow flow needs a very long duct to reach sonic speed.
For $M \to \infty$ it tends to $-\frac{1}{\gamma} + \frac{\gamma + 1}{2\gamma}\ln\frac{\gamma + 1}{\gamma - 1}$, which is about $0.82$ for $\gamma = 1.4$.
So a supersonic Fanno flow can only cover a bounded length before it becomes sonic.

## Remarks

Friction drives the Mach number towards $1$ from both sides: a subsonic flow accelerates and a supersonic flow decelerates.
The entropy is largest at $M = 1$, and the second law forbids crossing it, so if the duct is longer than $L^*$ the flow is [[choked|83Z3E8HMQ1]].
Then the upstream conditions adjust, for a subsonic inlet by a lower mass flow and for a supersonic inlet by a shock in the duct.
In the enthalpy–entropy plane the states of a Fanno flow lie on a curve called the Fanno line.

## Explanations

### L1 human

Gas pushed through a long pipe rubs against the walls.
One might expect friction always to slow the gas down, but in a slow compressible flow it speeds the gas up, because the pressure drops and the gas expands.
In a fast, supersonic flow friction does slow the gas down.
Either way the gas is driven towards the speed of sound, and a pipe that is too long chokes the flow.
