---
tag: GQCW6RG3GB
kind: example
name: Euclid's proof of his first proposition is not rigorous by modern standards
msc: ["00A35", "51M05"]
topics: [1BTHSHST4M]
audience: ug1
not_instance_of:
  - target: E1PE9R8DBB
    note: the step in which two circles meet follows from no stated axiom or postulate
uses: [E1PE9R8DBB, 83WHDAV68J, KM1FB8XZ2R, 0DZGSDHD92]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_Elements
    locator: Axiomatics
  - url: https://en.wikipedia.org/wiki/Rigour
    locator: Mathematics
---

## Example

Proposition 1 of Book I of [[Euclid's Elements|83WHDAV68J]] says that on a given segment $AB$ we can construct an equilateral triangle.
Euclid's proof is short.
Draw the circle with center $A$ through $B$, and the circle with center $B$ through $A$.
Let $C$ be a point where the two circles meet.
Then $CA = AB$ and $CB = BA$, so $CA = CB = AB$, and the triangle $ABC$ is equilateral.

The step "let $C$ be a point where the circles meet" has no reason among Euclid's postulates, so the proof is not [[rigorous|E1PE9R8DBB]] by the modern standard.
We show this with a plane in which the drawing rules hold and the meeting point does not exist.

1. Euclid's postulates let us draw a segment between two points, extend a segment, and draw a circle with a given center through a given point. None of them says that two circles meet.
2. Take as the plane the set $\mathbb{Q}^2$ of points with rational coordinates. A line is the set of rational points on a real line through two rational points, and a circle is the set of rational points at a given distance from a rational center.
3. In this plane the three drawing rules still work, since the lines and circles they ask for are sets of the kind just described.
4. Take $A = (0, 0)$ and $B = (1, 0)$. The circle with center $A$ through $B$ is $x^2 + y^2 = 1$, and the circle with center $B$ through $A$ is $(x - 1)^2 + y^2 = 1$.
5. A common point satisfies both equations. Subtract the second from the first:
$$x^2 - (x - 1)^2 = 0, \quad \text{so} \quad 2x - 1 = 0 \quad \text{and} \quad x = \tfrac{1}{2}.$$
6. Then $y^2 = 1 - \tfrac{1}{4} = \tfrac{3}{4}$, so $y = \sqrt{3}/2$ or $y = -\sqrt{3}/2$.
7. The number $\sqrt{3}$ is irrational, by the same argument as for [[the square root of 2|0DZGSDHD92]], so $y$ is not rational. The two circles therefore have no common point in $\mathbb{Q}^2$.
8. So the drawing rules do not force the circles to meet, and the meeting point is an extra assumption that Euclid did not state.

## Remarks

Euclid's proof is correct in the real plane, and his readers saw the meeting point in the figure.
The figure, not an axiom, supplied the step.
In the late 19th century mathematicians made such hidden assumptions explicit, and [[Hilbert's axioms|KM1FB8XZ2R]] include axioms of continuity from which the meeting of the two circles follows.

The plane $\mathbb{Q}^2$ does not satisfy every one of Euclid's axioms and common notions in every reading, and the argument does not need it to.
It shows only that the meeting of circles does not follow from the rules for drawing lines and circles.

What changes if we change the plane?
In the plane of points whose coordinates lie in $\mathbb{Q}(\sqrt{3}) = \{a + b\sqrt{3} : a, b \in \mathbb{Q}\}$ the point $(\tfrac{1}{2}, \tfrac{\sqrt{3}}{2})$ exists, so this particular pair of circles meets.
Other pairs still miss each other there.
The circle with center $(0, 0)$ through $(1, 0)$ and the circle with center $(2, 0)$ through $(0, 0)$ meet in $\mathbb{R}^2$ at $x = \tfrac{1}{4}$, $y = \pm \sqrt{15}/4$, and $\sqrt{15}$ is not of the form $a + b\sqrt{3}$ with rational $a$ and $b$.
Adding one square root at a time does not end the problem, and an axiom about intersections is what settles every case at once.

The example does not say that Euclid was careless.
For more than two thousand years the *Elements* was the model of a rigorous text, and the gap became visible only when the standard changed.
This is what it means for rigor to depend on the period.

## Explanations

### L1 human

Euclid wanted to draw a triangle with three equal sides on a given segment.
He drew two circles, one around each end of the segment, and took the point where they cross.
In a drawing the two circles plainly cross, so nobody asked why.
Much later, mathematicians noticed that none of Euclid's starting rules says that two circles cross.
On a "plane" made only of points with fraction coordinates these two circles do not cross at all, because the crossing point would have the coordinate $\sqrt{3}/2$, which is not a fraction.
So the proof needs one more rule, and modern systems of axioms state it.

### L2 human

We check the claim of step 7 that $\sqrt{3}/2$ is not rational.
Suppose that $\sqrt{3}/2 = p/q$ with integers $p$ and $q \neq 0$.
Then
$$\frac{3}{4} = \frac{p^2}{q^2}, \quad \text{so} \quad 3 q^2 = 4 p^2 = (2p)^2.$$
So $3 = (2p/q)^2$ would be the square of a rational number, and that is false because $\sqrt{3}$ is irrational.

The typical use of the example is to show why modern geometry needs axioms of continuity or of intersection.
Watch out for the belief that a correct figure makes a correct proof.
The figure shows one case in one plane, and the proof must work from the axioms alone.
