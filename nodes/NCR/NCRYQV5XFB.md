---
tag: NCRYQV5XFB
kind: statement
role: proposition
name: Sagnac effect
msc: [83A05]
uses: [8CJ62QP9SN, G49G4R1K04, YG74WHC3S9]
about: [8CJ62QP9SN]
sources:
  - url: https://en.wikipedia.org/wiki/Sagnac_effect
same_as:
  wikidata: Q582007
  wikipedia: Sagnac effect
---

## Statement

Let $c$ be the speed of light.
Let a platform rotate with constant angular velocity $\Omega$ relative to an inertial frame of [[Minkowski space|G49G4R1K04]].
Let a closed light path, guided by mirrors or an optical fibre, lie on the platform in a plane perpendicular to the axis.
Let $A$ be the area enclosed by the path.
Let two light signals leave the same point of the platform at the same time and travel around the path in opposite directions.
Then, to first order in $\Omega$, the signal that moves with the rotation returns later than the other one by
$$\Delta t = \frac{4 A \Omega}{c^2}.$$
For light of vacuum wavelength $\lambda$ this gives the phase difference $\Delta\varphi = 8\pi A\Omega / (\lambda c)$.

## Remarks

Take a circular path of radius $R$ and work in the inertial frame.
The co-rotating signal must also cover the distance moved by the starting point, so it takes the time $2\pi R/(c - R\Omega)$.
The other signal takes $2\pi R/(c + R\Omega)$.
The difference is $4\pi R^2 \Omega/(c^2 - R^2\Omega^2)$, which is $4A\Omega/c^2$ to first order; the clock on the rim measures this times $\sqrt{1 - R^2\Omega^2/c^2}$, its [[proper time|YG74WHC3S9]] factor.
For a path of any shape the first-order result is the same, with $A$ the enclosed area, and it does not depend on the position of the rotation axis.
If the platform does not rotate, $\Omega = 0$ and the two signals return together.
Sagnac demonstrated the effect with a rotating interferometer in 1913.
Ring laser gyroscopes and fibre-optic gyroscopes use it to measure rotation, and satellite navigation systems correct their time signals for it.

## Explanations

### L1 human

Send two light beams around a loop in opposite directions and let them meet again.
If the loop turns, the beam that goes with the turning has a little further to go, so it arrives late.
The delay is proportional to the area of the loop and to the rate of turning.
This lets a closed box of mirrors detect its own rotation without looking outside, which is how optical gyroscopes in aircraft work.

### L2 human

The Sagnac effect is a result of [[special relativity|8CJ62QP9SN]] in a rotating frame.
In rotating coordinates the metric has a cross term $g_{t\varphi}$, so the time light needs to go around a loop depends on the direction.
This shows that clocks around a rotating loop cannot be synchronised consistently.
The same cross term, produced by the rotation of a mass rather than of the observer, appears in general relativity as frame-dragging.
