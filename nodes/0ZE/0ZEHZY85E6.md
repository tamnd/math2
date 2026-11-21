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

The angle between two vectors measures how far apart their directions are, and the dot product lets you compute it from coordinates alone.
For nonzero [[vectors|0QN3D80AWP]] $u$ and $v$ the angle is the number $\theta \in [0, \pi]$ with
$$\cos \theta = \frac{u \cdot v}{\|u\| \, \|v\|},$$
where $u \cdot v$ is the [[dot product|0S52TNNTH9]] and $\|\cdot\|$ is the [[length|0XKBKGTCPC]].
In the plane and in space this is the opening between the two arrows drawn from one point, by the [[geometric formula for the dot product|070TXS9AXM]].
In $\mathbb{R}^n$ for $n \ge 4$ the formula is the [[definition|0PRAS55318]], and it makes sense only because the [[Cauchy-Schwarz inequality|0RFWW56Y22]] keeps the quotient in $[-1, 1]$.

## Motivation

In the plane you can measure the angle between two arrows with a protractor, but with coordinates you want a formula.
The law of cosines leads to the identity $u \cdot v = \|u\| \, \|v\| \cos \theta$, so the cosine of the angle is a quotient of numbers that you can compute.

For lists of length $4$ or more there is no picture, and yet the angle is still useful.
In statistics the cosine of the angle between two centered data vectors is their correlation, and in a search engine the angle between two lists of word counts measures how similar two texts are.
The quotient $\frac{u \cdot v}{\|u\| \, \|v\|}$ can always be computed, and we would like to call its arccosine the angle.
That works only if the quotient lies between $-1$ and $1$, and the Cauchy-Schwarz inequality guarantees exactly that.
The angle then gives a meaning to "perpendicular" in every dimension, the subject of the [[criterion for perpendicular vectors|03NK6RSRQ1]].

## Notation

The angle is written $\theta$ or $\angle(u, v)$, and it is measured in radians in $[0, \pi]$ or in degrees in $[0^\circ, 180^\circ]$.
For a nonzero vector $v$ of $\mathbb{R}^3$, the angles $\alpha$, $\beta$ and $\gamma$ that it makes with the three axes are its direction angles.
Their cosines, the direction cosines, are
$$\cos \alpha = \frac{v_1}{\|v\|}, \qquad \cos \beta = \frac{v_2}{\|v\|}, \qquad \cos \gamma = \frac{v_3}{\|v\|}.$$

## Remarks

### A first computation

Take $u = (2, 1, -2)$ and $v = (1, 1, 0)$.
The dot product and the lengths are
$$u \cdot v = 2 + 1 + 0 = 3, \qquad \|u\| = \sqrt{4 + 1 + 4} = 3, \qquad \|v\| = \sqrt{2}.$$
So $\cos \theta = 3 / (3\sqrt{2}) = 1 / \sqrt{2}$, and $\theta = \tfrac{\pi}{4} = 45^\circ$.
The same recipe gives $\theta = \tfrac{\pi}{3}$ for $(1, 1, 0)$ and $(1, 0, 1)$, whose tips form an equilateral triangle with the origin.
It also works where you cannot draw: in $\mathbb{R}^4$, the vectors $(1, 1, 1, 1)$ and $(1, 0, 0, 0)$ give $\cos \theta = 1 / (2 \cdot 1) = \tfrac{1}{2}$, so $\theta = \tfrac{\pi}{3}$.

### Acute, right and obtuse

The lengths in the denominator are positive, so the sign of $\cos \theta$ is the sign of $u \cdot v$.
The angle is acute when $u \cdot v > 0$, right when $u \cdot v = 0$, and obtuse when $u \cdot v < 0$.
For $u = (1, 2)$ and $v = (-3, 1)$ the dot product is $-3 + 2 = -1$, so the angle is obtuse before you compute anything else.
The [[worked example|KK2HKZ8F1A]] finishes the computation: $\cos \theta = -1 / \sqrt{50}$ and $\theta \approx 98.13^\circ$, just past a right angle.

### Direction cosines

The angles with the axes come from dot products with $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$, which pick out the components.
For $v = (2, -1, 2)$, with $\|v\| = 3$, the direction cosines are $\tfrac{2}{3}$, $-\tfrac{1}{3}$ and $\tfrac{2}{3}$, as the [[direction cosines example|8NJY1C9GVH]] shows.
They are the components of the unit vector $v / \|v\|$, so they always satisfy
$$\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma = 1.$$

### The rules you can use

The angle is symmetric, because $u \cdot v = v \cdot u$.
It does not change when you stretch either vector by a positive factor, since for $a, b > 0$ the factor $ab$ cancels in the quotient.
Reversing one vector replaces $\theta$ by $\pi - \theta$, because $(-u) \cdot v = -(u \cdot v)$ and $\cos(\pi - \theta) = -\cos \theta$.
The extreme values mean parallel vectors: $\theta = 0$ exactly when $v = cu$ with $c > 0$, and $\theta = \pi$ exactly when $v = cu$ with $c < 0$.
This is the case of equality in the Cauchy-Schwarz inequality.

### What is not an angle

The zero vector has no angle with anything, because $\|0\| = 0$ would be in the denominator.
A form that is not an inner product can push the quotient out of $[-1, 1]$.
The [[Minkowski example|VDK0B2K1XT]] gets the value $2 / \sqrt{3} > 1$, which is the cosine of no angle.
The oriented angle from $u$ to $v$ in the plane, a number in $(-\pi, \pi]$, is a different idea: it changes sign when you swap $u$ and $v$, and the angle between vectors does not.

### Watch out

In $\mathbb{R}^n$ the arccosine formula has no meaning until you know that the quotient lies in $[-1, 1]$.
So a proof of the [[Cauchy-Schwarz inequality|0RFWW56Y22]] in $\mathbb{R}^n$ cannot use angles in $\mathbb{R}^n$; that would be circular.
A second slip is to take the arccosine of $u \cdot v$ without dividing by the lengths.
For $(1, 1)$ and $(1, 0)$ that gives $\arccos 1 = 0$, but the true angle is $45^\circ$, since $\cos \theta = 1 / \sqrt{2}$.
The shortcut works only for unit vectors.

### History

The measure of angles is as old as geometry, and Euclid's *Elements* studies angles without numbers.
Cauchy proved the inequality for finite sums in 1821, and Schwarz proved a version for integrals in 1888.
The definition of the angle by the arccosine of the quotient, in any dimension, rests on that inequality.

### Try it

Find the angle between $(1, 0, 1)$ and $(0, 1, 1)$.
The dot product is $1$ and both lengths are $\sqrt{2}$, so $\cos \theta = \tfrac{1}{2}$ and $\theta = 60^\circ$.

Is the angle between $(3, -1, 2)$ and $(1, 5, 1)$ acute, right or obtuse?
The dot product is $3 - 5 + 2 = 0$, so it is a right angle.

## Explanations

### L1 human

Put two arrows at the same start point.
The angle between them is the opening between the arrows, from $0^\circ$ for the same direction to $180^\circ$ for opposite directions.
For the arrows $(1, 0)$ and $(1, 1)$ the opening is half a right angle, $45^\circ$.
The formula agrees: $\cos \theta = \frac{1}{1 \cdot \sqrt{2}}$, and the angle with this cosine is $45^\circ$.

### L2 human

Here is a typical use: find the angle at $A$ in the triangle with corners $A = (1, 0, 0)$, $B = (2, 1, 0)$ and $C = (1, 1, 1)$.
The sides that leave $A$ are
$$u = B - A = (1, 1, 0), \qquad v = C - A = (0, 1, 1).$$
Their dot product is $0 + 1 + 0 = 1$, and both lengths are $\sqrt{2}$, so
$$\cos \theta = \frac{1}{\sqrt{2} \cdot \sqrt{2}} = \frac{1}{2}, \qquad \theta = 60^\circ.$$
Check: the third side is $C - B = (-1, 0, 1)$, of length $\sqrt{2}$, so the triangle is equilateral and every angle is $60^\circ$.
The method needs only the two side vectors at the corner, and that is how angles in triangles and between lines are found in coordinates.

### L3 human

In any real [[inner product space|1D4JTZ9VS3]] the same formula defines the angle, for example between two functions with the inner product $\int_0^1 f g$.
For unit vectors the angle is a distance on the unit sphere: it is the length of the shorter arc of the great circle through them.
Angles between subspaces, the principal angles, extend the idea, and they come from the singular values of a matrix, as in the sub-area on [[positive matrices and singular values|SS4EVPKT3A]].
In statistics the cosine of the angle between two centered data vectors is their correlation coefficient.
