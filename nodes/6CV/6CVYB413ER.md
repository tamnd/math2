---
tag: 6CVYB413ER
kind: concept
name: Draw a figure and introduce notation
msc: ["00A35", "97E50"]
topics: [X1NSTVGDNQ]
audience: school
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, H840D9TM2X, 0RWKYX8339]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

Many problems are hard only while they live in words.
A figure puts the data and the unknown on paper where the eye can see their relations, and good names turn the condition into equations that you can compute with.

Here is a problem that changes as soon as you draw it.
A rectangle has its four corners on a circle of radius $5$, and one side of the rectangle has length $6$.
How long is the other side?
A first attempt in words names the four corners as unknown points, which gives eight coordinates and a tangle of conditions for "rectangle" and "on the circle".
Now draw the figure and add one diagonal.
Each corner of the rectangle is a right angle, and a right angle with its vertex on a circle stands on a diameter, so the diagonal is a diameter of length $10$.
Name the unknown side $x$, and the diagonal cuts off a right triangle with legs $6$ and $x$:
$$6^2 + x^2 = 10^2, \qquad x^2 = 64, \qquad x = 8.$$
Good notation gives a second solution.
Put the center of the circle at the origin with the sides parallel to the axes, so that the corners are $(\pm a, \pm b)$ with $a^2 + b^2 = 25$.
The side of length $6$ gives $2a = 6$, so $a = 3$, $b = 4$, and the other side is $2b = 8$.

"Draw a figure" and "introduce suitable notation" are two [[heuristics|6KCEWEP4WA]] from Pólya's first phase, understanding the problem.
They suggest a route and do not guarantee one: a figure can mislead, and bad names can hide the structure of a problem.

## Motivation

A problem in words asks you to keep many facts in memory at once.
A figure stores them on paper, and then you notice relations, such as two equal angles or three points on a line, that the words never mentioned.
Names do the same work in algebra.
"The smaller of the two numbers" is long and hard to compute with, while $x$ can be squared, added and compared.

The choice of names is not neutral.
Names that treat two interchangeable objects alike keep the [[symmetry|H840D9TM2X]] of the problem visible, and a [[coordinate system|0RWKYX8339]] that puts the figure in a simple position makes the algebra short.
Both ideas return later: a figure is the first tool of [[mathematical intuition|4BT08RE4CR]], and a good choice of coordinates is the everyday form of [[without loss of generality|Y7NE0E6PCV]].

## Notation

Pólya's advice on notation asks for signs with one meaning each and for related signs for related objects, such as $a$, $b$, $c$ for the sides opposite the vertices $A$, $B$, $C$.
The usual conventions follow it: $x$, $y$, $z$ for unknowns, $a$, $b$, $c$ for known numbers, $n$, $m$, $k$ for integers, and $\alpha$, $\beta$, $\gamma$ for the angles at $A$, $B$, $C$.
The topic [[notation, conventions and jargon|Z2WNQ1DNTX]] treats these conventions in general.

## Remarks

### Coordinates with many zeros

To prove that the diagonals of a parallelogram $ABCD$ bisect each other, place $A = (0, 0)$, $B = (a, 0)$ and $D = (b, c)$, so that $C = (a + b, c)$.
Both diagonals have the [[midpoint|B222G2H8TZ]]
$$\left( \frac{a + b}{2}, \frac{c}{2} \right),$$
so they meet there.
Three letters describe every parallelogram, because translations and rotations do not change midpoints, and the statement does not change under them.

### Names that keep a symmetry

Find two numbers with sum $10$ and product $21$.
The names $x$ and $10 - x$ give $x^2 - 10x + 21 = 0$, which is correct but hides the fact that the two numbers play the same role.
The [[symmetric names|NSCRV68VNS]] $5 + d$ and $5 - d$ use up the sum at once and turn the product into
$$25 - d^2 = 21, \qquad d = \pm 2,$$
so the numbers are $7$ and $3$.

### A figure that proves nothing alone

A figure of a staircase of $n$ columns of heights $1, 2, \dots, n$, with a copy turned upside down beside it, makes an $n \times (n + 1)$ rectangle.
So $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$, and the picture tells you why.
Still, a figure suggests relations and the proof must check them.
If your drawing shows two lines meeting inside a triangle, that is a claim, and [[proofs without words|V6ESFEFKJC]] discusses when a picture can count as a proof.

### When a figure misleads

The classic failure is a figure that is too special.
A student who draws an isosceles triangle "because it is easy" will see the median from the apex fall along the altitude, and may conclude that [[medians are altitudes|SXA7G1N6HZ]].
In a triangle with three different sides the two segments differ.
The same happens with coordinates: $A = (0, 0)$, $B = (2, 0)$, $C = (0, 2)$ make a calculation short, but they describe one right isosceles triangle, and a result proved there is proved only there.

### Watch out

Draw the figure as general as the hypotheses allow: no right angles and no equal sides unless the problem gives them.
Use one letter for one object, and never $x$ for both a length and a point.
Before you trust a relation you see in a figure, move one point a little and look again.

### History

Pólya listed drawing a figure and introducing suitable notation among the questions for understanding a problem in *How to Solve It* (1945), and he gave notation its own entry in the dictionary part of the book.
Descartes's *La Géométrie*, published in 1637 as an appendix to the *Discourse on the Method*, turned geometric problems into algebra with coordinates.

### Try it

Two numbers have sum $14$ and product $45$; find them.
With $7 + d$ and $7 - d$ you get $49 - d^2 = 45$, so $d = \pm 2$ and the numbers are $9$ and $5$.

A right triangle has legs $3$ and $4$; how far is the right-angle vertex from the midpoint of the hypotenuse?
Put the vertex at $(0, 0)$ and the other corners at $(3, 0)$ and $(0, 4)$, so the midpoint is $(1.5, 2)$ and the distance is $\sqrt{2.25 + 4} = 2.5$.

## Explanations

### L1 human

A rectangle has a perimeter of $20$ cm, and one side is $4$ cm longer than the other.
That sentence is hard to hold in your head, so draw the rectangle and call the short side $s$.
The long side is then $s + 4$, and the perimeter is $s + (s + 4) + s + (s + 4) = 4s + 8$.
So $4s + 8 = 20$, the short side is $3$ cm and the long side is $7$ cm.
The picture and the letter $s$ did most of the work.
A picture can also fool you when it is too neat, so draw shapes without extra equal sides or right angles.

### L2 human

We prove that the segment joining the midpoints of two sides of a triangle is parallel to the third side and half as long.
Draw a triangle $ABC$ in general position, and let $M$ and $N$ be the midpoints of $AB$ and $AC$.
Lengths and parallel lines do not change under translations and rotations, so we may put
$$A = (0, 0), \qquad B = (2p, 0), \qquad C = (2q, 2r), \quad r \ne 0,$$
where the factors $2$ avoid fractions later.
Then $M = (p, 0)$ and $N = (q, r)$, and
$$\overrightarrow{MN} = (q - p, r), \qquad \overrightarrow{BC} = (2q - 2p, 2r) = 2\, \overrightarrow{MN}.$$
So $MN$ is parallel to $BC$ and half as long.

Coordinates with many zeros, and names with a factor that prevents fractions, keep the calculation short.
The letters $p$, $q$, $r$ are free, so the proof covers every triangle; with fixed numbers it would cover only one.

### L3 human

Choosing notation is choosing coordinates in a wide sense: a symmetry of the problem moves it to a position where its description is short.
In linear algebra the same idea is a choice of basis, and a good basis, such as an eigenbasis or an orthonormal basis, makes a matrix simple.
Klein's view of a geometry as the study of the invariants of a group of transformations explains why the choice is allowed: an invariant statement can be checked in any convenient frame.
A symmetric notation leads to equations that do not change when the names are exchanged, and such equations simplify in the sum and the product of the unknowns, as in [[Vieta's formulas|0M8EWQJ1YV]].
A figure plays a similar role for intuition, as a guide that must be checked, and [[rigor and the acceptance of proofs|1BTHSHST4M]] discusses when a picture is accepted.
