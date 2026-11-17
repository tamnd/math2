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

For a triangle $ABC$, we look for the point $P$ that minimizes $f(P) = |PA| + |PB| + |PC|$.
We use a [[physical argument|THJV0NFPDQ]] and then check it with a computation.

1. The machine. Drill holes at $A$, $B$ and $C$ in a horizontal table. Pass a string through each hole, tie the three strings in a knot on the table, and hang an equal weight on each string below.
2. The energy. The total length of string is fixed. The weights hang lowest when the length on the table, $|PA| + |PB| + |PC|$, is smallest. By the [[principle of virtual work|ZC3YKMKRGP]], the knot comes to rest where $f$ is smallest.
3. The balance of forces. At rest, the knot is pulled by three forces of equal size, towards $A$, $B$ and $C$. Three vectors of equal length add up to zero only when each pair makes an angle of $120^\circ$.
4. The prediction. The minimizer is the point $P$ inside the triangle from which each side is seen at an angle of $120^\circ$. This is the [[Fermat point|QM0CGSQ4TF]].
5. A test. For $A = (0, 0)$, $B = (4, 0)$, $C = (1, 3)$ the angles of the triangle are about $71.6^\circ$, $45^\circ$ and $63.4^\circ$. A numerical minimization gives $P \approx (1.302, 1.047)$ with $f(P) \approx 6.541$, and the angles $APB$, $BPC$, $CPA$ are $120^\circ$.
6. A comparison. At the centroid $(5/3, 1)$, $f \approx 6.590$; at the vertex $A$, $f = 4 + \sqrt{10} \approx 7.162$. Both are larger, as predicted.
7. A limit of the machine. For $A = (0, 0)$, $B = (4, 0)$, $C = (-1, 0.5)$ the angle at $A$ is about $153^\circ$. The knot is pulled into the hole at $A$ and stops there, and the minimum is $f(A) = 4 + \sqrt{1.25} \approx 5.118$.

## Remarks

The proof today is short.
The function $f$ is convex, as a sum of distances.
Away from the vertices its gradient is the sum of the three unit vectors from $A$, $B$ and $C$ towards $P$, and it vanishes exactly at the point with three angles of $120^\circ$.
A convex function is smallest at a critical point, so this point is the minimum when it exists inside the triangle.
It exists exactly when every angle of the triangle is less than $120^\circ$; otherwise the minimum is at the vertex with the large angle, as step 7 shows.

The machine is often called the Varignon frame.
With unequal weights $w_A$, $w_B$, $w_C$ the same machine minimizes $w_A|PA| + w_B|PB| + w_C|PC|$, a problem of locating a facility.

## Explanations

### L1 human

Three towns want one meeting point with the least total road length.
Make holes in a table at the towns, pass a string through each hole, and tie the strings together on top.
Hang equal weights below, and let go.
The knot slides to the best meeting point, where the three strings meet at equal angles of $120^\circ$.
A proof with calculus confirms what the strings show.

### L2 human

We check the balance of forces at $P \approx (1.302, 1.047)$ from step 5.

1. The unit vector from $P$ towards $A = (0,0)$ is about $(-0.779, -0.627)$.
2. The unit vector towards $B = (4,0)$ is about $(0.932, -0.362)$.
3. The unit vector towards $C = (1,3)$ is about $(-0.153, 0.988)$.
4. Their sum is about $(0.000, -0.001)$, which is zero up to the rounding of the coordinates.

The typical use: the balance condition gives an equation for the minimizer that a computation can test.
A trap: the machine assumes frictionless holes and a knot that stays on the table; at an angle of $120^\circ$ or more the knot falls into a hole, and the condition of step 3 no longer applies.
