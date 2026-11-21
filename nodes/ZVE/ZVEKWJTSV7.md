---
tag: ZVEKWJTSV7
kind: example
name: Vector proofs in plane geometry
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [0QN3D80AWP]
illustrates: [0GPQ67XV7N]
uses: [0QN3D80AWP, 0S52TNNTH9, 0N5N15HWZ7, 0X7EEWES5G]
sources:
  - url: https://en.wikipedia.org/wiki/Centroid
    locator: Of a triangle
  - url: https://en.wikipedia.org/wiki/Parallelogram
    locator: Characterizations
  - url: https://en.wikipedia.org/wiki/Euclidean_vector
    locator: Physics
---

## Example

Once points are written as [[vectors|0QN3D80AWP]], a theorem of plane geometry becomes a short calculation with sums and multiples, and the same calculations describe forces and velocities.
We prove two theorems this way and then solve four small problems from mechanics.
Throughout, a point stands for its position vector, so the midpoint of $P$ and $Q$ is the average $\tfrac{1}{2}(P + Q)$.

**The medians of a triangle meet in one point.**

1. Let $A$, $B$, $C$ be the vertices. The midpoint of $BC$ is $M_A = \tfrac{1}{2}(B + C)$.
2. The point two thirds of the way from $A$ to $M_A$ is
   $$A + \tfrac{2}{3}(M_A - A) = \tfrac{1}{3}A + \tfrac{2}{3} \cdot \tfrac{1}{2}(B + C) = \tfrac{1}{3}(A + B + C).$$
3. The result does not change when $A$, $B$, $C$ are permuted, so the same point lies on the medians from $B$ and from $C$.
4. So the three medians meet at $G = \tfrac{1}{3}(A + B + C)$, the [[centroid|0X7EEWES5G]]. This is the [[median theorem|0GPQ67XV7N]].
5. In numbers, $A = (0, 0)$, $B = (6, 0)$ and $C = (0, 9)$ give $G = (2, 3)$.
6. Check from $B$: the midpoint of $AC$ is $(0, 4.5)$, and $(6, 0) + \tfrac{2}{3}\bigl((0, 4.5) - (6, 0)\bigr) = (6, 0) + (-4, 3) = (2, 3)$.

**The diagonals of a parallelogram bisect each other.**

1. Let $ABCD$ be a parallelogram with $B = A + u$, $D = A + v$ and $C = A + u + v$.
2. The midpoint of $AC$ is $\tfrac{1}{2}(A + A + u + v) = A + \tfrac{1}{2}(u + v)$.
3. The midpoint of $BD$ is $\tfrac{1}{2}(A + u + A + v) = A + \tfrac{1}{2}(u + v)$.
4. The two midpoints are equal, so the diagonals cut each other in half.
5. In numbers, $A = (1, 1)$, $u = (4, 0)$ and $v = (1, 3)$ give $B = (5, 1)$, $C = (6, 4)$ and $D = (2, 4)$, and both midpoints are $(3.5, 2.5)$.

**Forces and velocities.**

1. A boat moves at $(0, 4)$ m/s relative to the water, and the current flows at $(3, 0)$ m/s. The [[velocity|K160D2Z0CS]] over the ground is the sum $(3, 4)$ m/s, a speed of $5$ m/s.
2. Forces $(3, 4)$ N and $(5, -4)$ N act on one point. Their resultant is $(8, 0)$ N, so the extra force $(-8, 0)$ N would keep the point at rest.
3. The force $(8, 0)$ N moves the point by $(2, 1)$ m. The [[work|0CDZ684TCD]] done is the [[dot product|0S52TNNTH9]] $(8, 0) \cdot (2, 1) = 16$ J.
4. A force $F = (0, 3, 0)$ N acts at $r = (2, 0, 0)$ m from a point on an axis. The [[torque|9636MFFSGC]] is the [[cross product|0N5N15HWZ7]]
   $$r \times F = (0 \cdot 0 - 0 \cdot 3, \; 0 \cdot 0 - 2 \cdot 0, \; 2 \cdot 3 - 0 \cdot 0) = (0, 0, 6) \text{ N·m}.$$

## Remarks

The two geometric proofs use no coordinates and no angles, only sums and multiples of vectors.
That is why they hold for every triangle and every parallelogram at once, while the numbers only check one case.
The [[coordinate proof|B222G2H8TZ]] of the parallelogram theorem does the same computation with coordinates.
The dot product gives a vector proof of Thales's theorem, in the [[Thales proof|RTYJ2DHDSJ]], and the [[Euler line proof|X90TK61BYB]] uses the same methods.
The first two mechanics problems use the parallelogram rule for adding vectors, which Newton stated for forces in the Principia.

## Explanations

### L1 human

A vector proof replaces a picture by a computation with arrows.
The midpoint of two points is their average, and the centroid of a triangle is the average of its three corners.
Forces and velocities add like arrows, tip to tail.

### L2 human

The method for a geometry proof has three moves: name the points as vectors, write each point of interest as a combination of them, and compare the combinations.
In step 3 of the median proof, symmetry replaces three computations by one.
Watch out: the centroid is two thirds of the way from a vertex to the opposite midpoint, not halfway.
At the halfway point you get $\tfrac{1}{2}A + \tfrac{1}{4}B + \tfrac{1}{4}C$, which changes when the vertices are permuted.
