---
tag: PGA5QGTCJ5
kind: definition
name: Cardinal points of an optical system
msc: [78A05]
defines: XTW602R5VX
uses: [N111BHFQ2H, 9WFT4VY2R7]
sources:
  - url: https://en.wikipedia.org/wiki/Cardinal_point_(optics)
---

## Definition

Let an optical system be rotationally symmetric about an axis, and work in the [[paraxial approximation|N111BHFQ2H]].
Suppose the system is not afocal, that is, its [[ray transfer matrix|9WFT4VY2R7]] has $C \ne 0$.
The *cardinal points* of the system are the following six points on the axis.

1. The *front focal point* $F$: every ray through $F$ leaves the system parallel to the axis.
2. The *rear focal point* $F'$: every ray that enters parallel to the axis leaves through $F'$.
3. The *front and rear principal points* $P$ and $P'$: the axial points of the principal planes.
   These are the pair of conjugate planes imaged onto each other with lateral magnification $+1$.
4. The *front and rear nodal points* $N$ and $N'$: a pair of conjugate axial points.
   Every ray entering toward $N$ leaves as if from $N'$, with the same angle to the axis.

## Remarks

The front focal length is the distance from $P$ to $F$, and the rear focal length is the distance from $P'$ to $F'$.
If the system has the same medium on both sides, then $N = P$, $N' = P'$, and the two focal lengths are equal.
In terms of the ray transfer matrix from the first to the last surface in air, the effective focal length is $f = -1/C$.

Example: a thin lens of focal length $f$ in air.
Check: $P = P' = N = N'$ is the centre of the lens, and $F$, $F'$ lie at distance $f$ on either side.

Non-example: a Galilean or Keplerian telescope set to infinity is afocal, with $C = 0$.
Parallel rays leave parallel, so there is no rear focal point, and the cardinal points are not defined.
