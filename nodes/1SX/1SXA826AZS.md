---
tag: 1SXA826AZS
kind: example
name: The Fermat point from weights on strings
msc: ["51M16", "70C20"]
topics: [DME0TPC348]
audience: ug2
instance_of: [THJV0NFPDQ]
uses: [THJV0NFPDQ, QM0CGSQ4TF, ZC3YKMKRGP]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat_point
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Geometric_median
    locator: lead section
---

## Example

For the triangle with corners $A = (0, 0)$, $B = (4, 0)$ and $C = (1, 3)$, the point that minimizes the total distance to the corners is about $P = (1.302, 1.047)$, and the three corners are seen from it at angles of exactly $120^\circ$.
A table with three holes and three weights finds this point.
For a triangle $ABC$ we want the point $P$ that minimizes
$$f(P) = |PA| + |PB| + |PC|.$$
We use a [[physical argument|THJV0NFPDQ]] to predict the answer and then check it by computation.

1. We build the machine.
   Drill holes at $A$, $B$ and $C$ in a horizontal table, pass a string through each hole, tie the three strings in a knot on the table, and hang an equal weight on each string below.
2. We find the energy.
   The total length of string is fixed, so the weights hang lowest when the length on the table, $f(P)$, is smallest.
   By the [[principle of virtual work|ZC3YKMKRGP]], the knot comes to rest where $f$ is smallest.
3. We balance the forces.
   At rest the knot is pulled by three forces of equal size, toward $A$, $B$ and $C$.
   Three vectors of equal length add up to zero only when each pair of them makes an angle of $120^\circ$.
4. The machine predicts that the minimizer is the point inside the triangle from which each side is seen at an angle of $120^\circ$.
   This is the [[Fermat point|QM0CGSQ4TF]].
5. We test the prediction on the triangle above, whose angles are about $71.6^\circ$, $45^\circ$ and $63.4^\circ$.
   A numerical minimization gives $P \approx (1.302, 1.047)$ with $f(P) \approx 6.541$, and the angles $APB$, $BPC$ and $CPA$ are $120^\circ$ to within rounding.
6. We compare with other points.
   At the centroid $(5/3, 1)$ the total is $f \approx 6.590$, and at the corner $A$ it is
$$f(A) = 4 + \sqrt{10} \approx 7.162.$$
   Both are larger.
7. We push the machine to its limit with $A = (0, 0)$, $B = (4, 0)$ and $C = (-1, 0.5)$, where the angle at $A$ is about $153.4^\circ$.
   The knot is pulled into the hole at $A$ and stops there, and the minimum is
$$f(A) = 4 + \sqrt{1.25} \approx 5.118.$$

## Remarks

### The proof the machine still needs

The proof today is short.
The function $f$ is convex, since each distance $|PX|$ is a convex function of $P$.
Away from the corners its gradient is the sum of the three unit vectors from $A$, $B$ and $C$ toward $P$, and this sum vanishes exactly at the point with three angles of $120^\circ$.
A convex function has its minimum at any critical point, so this point is the minimum when it lies inside the triangle.
It lies inside exactly when every angle of the triangle is less than $120^\circ$, and otherwise the minimum is at the corner with the large angle, as step 7 shows.

### Variations of the machine

The machine is often called the Varignon frame.
With unequal weights $w_A$, $w_B$ and $w_C$, the same machine minimizes $w_A|PA| + w_B|PB| + w_C|PC|$, a problem of locating a facility.
With more holes it finds the geometric median of more points, where the unit vectors toward the points still add to zero at an interior minimum.

### Watch out

The machine assumes frictionless holes and a knot that stays on the table.
When one angle of the triangle is $120^\circ$ or more, the knot reaches a hole, and the balance of step 3 no longer applies there.
So the physical picture gives the right answer only after you add a constraint that the first description left out.

### Try it

For an equilateral triangle, where is the Fermat point?
By symmetry it is the center, and each side is seen from the center at $120^\circ$.

For the triangle $(0, 0)$, $(1, 0)$, $(0, 1)$, is the minimum at a corner?
No, because the largest angle is $90^\circ$, which is less than $120^\circ$, so the minimum lies inside.

## Explanations

### L1 human

Three towns want one meeting point with the least total road length.
Make holes in a table at the towns, pass a string through each hole, and tie the strings together on top.
Hang equal weights below, and let go.
The knot slides to the best meeting point, where the three strings meet at equal angles of $120^\circ$.
A proof with calculus is still needed, because a real table has friction and a real knot can get stuck.

### L2 human

We check the balance of forces at $P \approx (1.302, 1.047)$ from step 5.
The unit vectors from $P$ toward the three corners are about
$$u_A \approx (-0.779, -0.627), \qquad u_B \approx (0.932, -0.362), \qquad u_C \approx (-0.153, 0.988).$$
Add the first entries and then the second entries:
$$-0.779 + 0.932 - 0.153 = 0.000, \qquad -0.627 - 0.362 + 0.988 = -0.001.$$
The sum is zero up to the rounding of the coordinates, so the three equal forces balance.
The typical use: the balance condition gives an equation for the minimizer that a computation can test.
Watch out: the balance condition holds only at an interior minimum, so check the angles of the triangle first.
