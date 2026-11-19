---
tag: 0ZEHZY85E6
kind: concept
name: Angle between two vectors
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
uses: [0QN3D80AWP, 0XKBKGTCPC, 0S52TNNTH9, 0RFWW56Y22]
sources:
  - url: https://en.wikipedia.org/wiki/Angle
    locator: Inner product
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Geometric definition
  - url: https://understandinglinearalgebra.org/
    locator: Section 6.1
---

## Summary

The angle between two nonzero [[vectors|0QN3D80AWP]] $u$ and $v$ is the number $\theta \in [0, \pi]$ with
$$\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|},$$
where $u \cdot v$ is the [[dot product|0S52TNNTH9]] and $\|\cdot\|$ is the [[length|0XKBKGTCPC]].
In the plane and in space this is the opening between the two arrows drawn from one point, as the [[geometric formula for the dot product|070TXS9AXM]] shows.
In $\mathbb{R}^n$ for $n \geq 4$ the formula is the [[definition|0PRAS55318]], and it makes sense only because the [[Cauchy-Schwarz inequality|0RFWW56Y22]] puts the quotient in $[-1, 1]$.
The angle matters because it measures how far two directions differ, and it gives meaning to "perpendicular" and "parallel" in any dimension.

## Motivation

In the plane, we can measure the angle between two arrows with a protractor.
With coordinates, we want a formula instead.
The law of cosines leads to the identity $u \cdot v = \|u\| \, \|v\| \cos \theta$, so the cosine of the angle is a quotient of numbers that we can compute.
For lists of length $4$ or more, there is no picture.
The quotient $\frac{u \cdot v}{\|u\| \, \|v\|}$ can still be computed, and we would like to call its arccosine the angle.
This works only if the quotient lies between $-1$ and $1$, and the Cauchy-Schwarz inequality guarantees exactly this.

## Notation

- The angle is written $\theta$, $\angle(u, v)$ or $\sphericalangle(u, v)$.
- The angle is measured in radians in $[0, \pi]$, or in degrees in $[0^\circ, 180^\circ]$.
- For a vector $v \neq 0$ of $\mathbb{R}^3$, the angles $\alpha$, $\beta$ and $\gamma$ with the axes are the direction angles. Their cosines $\cos \alpha = v_1 / \|v\|$, $\cos \beta = v_2 / \|v\|$ and $\cos \gamma = v_3 / \|v\|$ are the direction cosines.

## Remarks

### Examples

- $(1, 0)$ and $(0, 1)$: the dot product is $0$, so $\theta = \tfrac{\pi}{2}$.
- $(1, 1, 0)$ and $(1, 0, 1)$: $\cos \theta = \tfrac{1}{2}$, so $\theta = \tfrac{\pi}{3}$. The three points $0$, $(1, 1, 0)$ and $(1, 0, 1)$ form an equilateral triangle.
- $(1, 2)$ and $(-3, 1)$: $\cos \theta = -\tfrac{1}{5\sqrt{2}}$, so $\theta \approx 98.13^\circ$, an obtuse angle. The [[worked example|~e9e732b2]] gives the steps.
- In $\mathbb{R}^4$, $(1, 1, 1, 1)$ and $(1, 0, 0, 0)$: $\cos \theta = \tfrac{1}{2 \cdot 1}$, so $\theta = \tfrac{\pi}{3}$.
- The direction cosines of $(2, -1, 2)$ are $\tfrac{2}{3}$, $-\tfrac{1}{3}$ and $\tfrac{2}{3}$. The [[direction cosine example|~a7428d5d]] checks that their squares add to $1$.

### Non-examples

- The angle with the zero vector is not defined: $\|0\| = 0$ is in the denominator.
- The arccosine of $\frac{u \star v}{\sqrt{u \star u} \sqrt{v \star v}}$ for a form $\star$ that is not an inner product need not exist. The [[non-example with the Minkowski form|~ae2b64d5]] gets the value $\tfrac{2}{\sqrt{3}} > 1$.
- The oriented angle from $u$ to $v$ in the plane, in $(-\pi, \pi]$, is a different notion. It changes sign when we swap $u$ and $v$, and the angle between vectors does not.

### Basic properties

- Symmetry: the angle between $u$ and $v$ equals the angle between $v$ and $u$, since $u \cdot v = v \cdot u$.
- Scaling: for $a, b > 0$ the angle between $au$ and $bv$ equals the angle between $u$ and $v$. The factor $ab$ cancels in the quotient.
- Reversal: the angle between $-u$ and $v$ is $\pi - \theta$, since $\cos(\pi - \theta) = -\cos \theta$.
- The angle is acute ($\theta < \tfrac{\pi}{2}$) if $u \cdot v > 0$, right if $u \cdot v = 0$, and obtuse ($\theta > \tfrac{\pi}{2}$) if $u \cdot v < 0$. The reason is that the lengths are positive.
- $\theta = 0$ if and only if $v = cu$ with $c > 0$, and $\theta = \pi$ if and only if $v = cu$ with $c < 0$. This is the equality case of the Cauchy-Schwarz inequality.
- The direction cosines of $v$ are the components of the unit vector $v / \|v\|$, so $\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma = 1$.

### History

The measure of angles is as old as geometry, and Euclid's Elements studies angles without numbers.
The definition of the angle by the arccosine of the quotient, in any dimension, is possible only after the Cauchy-Schwarz inequality.
Cauchy proved the inequality for sums in 1821, and Schwarz proved a version for integrals in 1888.

### Common errors

- In $\mathbb{R}^n$, students use the arccosine formula before they know that the quotient is in $[-1, 1]$. Without the [[Cauchy-Schwarz inequality|0RFWW56Y22]] the formula has no meaning.
- Students take the arccosine of $u \cdot v$ without dividing by the lengths. This works only for unit vectors.
- Students give an angle larger than $\pi$, or a negative angle. The angle between vectors is always in $[0, \pi]$.

## Explanations

### L1 human

Put two arrows at the same start point.
The angle between them is the opening between the arrows, from $0^\circ$ (same direction) to $180^\circ$ (opposite directions).
For the arrows $(1, 0)$ and $(1, 1)$, the opening is half a right angle, $45^\circ$.
The formula gives the same: $\cos \theta = \frac{1}{1 \cdot \sqrt{2}}$, and the angle with this cosine is $45^\circ$.

### L2 human

Worked example: the angle between $u = (2, 1, -2)$ and $v = (1, 1, 0)$.

1. $u \cdot v = 2 + 1 + 0 = 3$.
2. $\|u\| = \sqrt{4 + 1 + 4} = 3$ and $\|v\| = \sqrt{2}$.
3. $\cos \theta = \frac{3}{3\sqrt{2}} = \frac{1}{\sqrt{2}}$.
4. So $\theta = \tfrac{\pi}{4} = 45^\circ$.

The typical use is to find angles in triangles and between lines in coordinates.
The trap is the one in Common errors: in $\mathbb{R}^n$ the formula needs the Cauchy-Schwarz inequality first, and a proof that uses angles in $\mathbb{R}^n$ cannot be used to prove that inequality.

### L3 human

In any real [[inner product space|1D4JTZ9VS3]] the same formula defines the angle, for example between two functions with the inner product $\int_0^1 f g$.
The angle is the distance on the unit sphere: for unit vectors, $\theta$ is the length of the shortest arc of the great circle through them.
Angles between subspaces, principal angles, extend the idea, and they come from the singular values of a matrix of the sub-area on [[positive matrices and singular values|SS4EVPKT3A]].
In statistics, the cosine of the angle between two centred data vectors is their correlation coefficient.
