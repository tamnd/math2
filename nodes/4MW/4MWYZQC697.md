---
tag: 4MWYZQC697
kind: statement
role: theorem
name: Morawetz theorem on shockless airfoils
msc: [76H05, 35M10]
uses: [20G6N8JGEH, 84K7TEWZ2Z, SH8FHGTMSE, 9AR4ZZRRAM, 21DD2334NR, JSDMGGTG7G]
about: [20G6N8JGEH]
sources:
  - url: https://en.wikipedia.org/wiki/Cathleen_Synge_Morawetz
---

## Statement

Consider steady, plane, inviscid, irrotational and [[isentropic|SH8FHGTMSE]] flow of a compressible gas past a profile $P$, with a subsonic uniform stream at infinity.
Suppose that past $P$ there is a continuous [[transonic flow|20G6N8JGEH]], that is, a flow without [[shocks|JSDMGGTG7G]].
Suppose its supersonic region is bounded and adjacent to the profile.
Then this flow is not stable under changes of the profile.
There are arbitrarily small smooth changes of $P$, made only on the arc of $P$ that bounds the supersonic region, with the following property.
The changed profile admits no continuous transonic flow close to the original one.

## Remarks

The idea of the proof is to pass to the hodograph plane by the [[hodograph transformation|9AR4ZZRRAM]].
There the [[potential flow|84K7TEWZ2Z]] equation becomes linear and of mixed type, like the [[Tricomi equation|21DD2334NR]].
The perturbation of the flow then solves a linear boundary value problem with data on the whole boundary of the region, including its hyperbolic part.
Morawetz showed that this problem is overdetermined, so that for general perturbations of the profile it has no solution.
So a shockless transonic profile is an exceptional, isolated design, and generic small changes create shocks.
Shockless airfoils can still be designed, but each one works only at its design conditions.

## Explanations

### L1 human

Engineers would like wings on which the air goes faster than sound over the top and slows down again smoothly, without a shock wave, because shocks cause drag.
Such wings exist, but the theorem says that they are fragile.
Change the shape of the wing a tiny bit, in the right way, and the smooth flow is gone.
In practice a shock wave appears, although for good designs it stays weak.

### L2 human

The result explains why steady transonic flows past airfoils must in general be sought as weak solutions with shocks.
One solves the full potential or Euler equations in this weak sense, rather than looking for smooth solutions.
It is a statement about the ill-posedness of a boundary value problem for a mixed-type equation, and it motivated much of the later theory of such problems.
It also guides numerical methods for transonic flow, which must be able to capture shocks rather than assume smoothness.
