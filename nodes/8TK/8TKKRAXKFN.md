---
tag: 8TKKRAXKFN
kind: concept
name: Auxiliary elements
msc: ["00A35", "97E50"]
topics: [X1NSTVGDNQ]
audience: school
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, 0BARQY52N5, 0194DY35BG]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
    locator: Proof
  - book: isbn:9780691164076
---

## Summary

An auxiliary element is an object that the problem does not mention but that you add because it connects the data to the unknown.
It can be a line or a point in a figure, a new variable, or a function built for the purpose.

The standard first case is the angle sum of a triangle.
Why do the angles $\alpha$, $\beta$ and $\gamma$ of a triangle $ABC$ add up to $180^\circ$?
A first attempt measures the angles of a drawn triangle and gets $179^\circ$ or $181^\circ$, which is evidence but not a proof.
A second attempt looks for a theorem about three angles at three different corners, and there is none: the figure keeps the angles apart.
The known fact closest to the goal is that angles along a straight line add up to $180^\circ$.
So we want the three angles side by side at one point, on one line.
The helping move is to draw the line $\ell$ through $A$ parallel to $BC$.
The side $AB$ crosses the two parallel lines, so the angle between $\ell$ and $AB$ equals $\beta$ as alternate angles, and in the same way the angle between $\ell$ and $AC$ equals $\gamma$.
At $A$ the three angles now fill the straight angle along $\ell$:
$$\beta + \alpha + \gamma = 180^\circ.$$
The [[full example|DA40QCPX63]] checks each step.

The line $\ell$ is not in the statement and not in the answer, but without it there is no proof.
The heuristic is to ask which new object would let a known theorem apply.
It is advice, not a procedure: nothing tells you in advance which line to draw.

## Motivation

Many problems fail to start because no known fact links the data to the unknown.
An auxiliary element is the bridge.
In the angle sum, one parallel brings in the theorems on parallels.
In the [[mean value theorem|0BARQY52N5]], the hypothesis is about a function $f$, but the known result, [[Rolle's theorem|0194DY35BG]], needs a function with equal values at the ends, and an auxiliary function supplies one.
In algebra, a new variable turns a tangled expression into a simple one.

The element is usually found by working back from a known result.
Ask which theorem gives an unknown of this kind, and which object is missing for that theorem to apply.
That is why a stock of solved problems helps: the auxiliary line of a similar problem is a good first guess, as [[analogy|7KDT0R1HF2]] suggests.

## Notation

Pólya's term is "auxiliary element", and in geometry books the usual phrase is "auxiliary construction" or "auxiliary line".
In analysis the same idea goes by "auxiliary function", and in algebra by "substitution" or "new variable".
In transcendence theory the "auxiliary polynomial" is the name of a whole method.

## Remarks

### Three bridges

Here is the auxiliary function of the mean value theorem.
Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$, and let $m = \frac{f(b) - f(a)}{b - a}$ be the slope of the chord.
The goal $f'(c) = m$ says that $(f(x) - mx)'$ vanishes at $c$, so we try
$$g(x) = f(x) - mx, \qquad g(b) - g(a) = f(b) - f(a) - m(b - a) = 0.$$
Rolle's theorem applies to $g$ and gives $c \in (a, b)$ with $g'(c) = 0$, that is $f'(c) = m$, as in the [[proof from Rolle's theorem|YBRVDSFRE7]].

In a shortest-path problem, two points $A$ and $B$ lie on one side of a line, and you want the point $P$ on the line that makes $AP + PB$ smallest.
The [[reflected point|52DGE85AR1]] $B'$ of $B$ has $PB' = PB$, so the bent path becomes a straight segment $AB'$, and the triangle inequality finishes the problem.

In algebra, to find $x > 0$ with $x^2 + \frac{1}{x^2} = 7$, add the variable $s = x + \frac{1}{x}$.
Then $s^2 = 7 + 2 = 9$, so $s = 3$, and $x^2 - 3x + 1 = 0$ gives $x = \frac{3 \pm \sqrt{5}}{2}$.

### When the element misleads

An auxiliary element brings its own conditions.
The half-angle variable $t = \tan \frac{x}{2}$ is a standard helper for trigonometric integrals, but it is not defined at $x = \pi$.
Used blindly on $[0, 2\pi]$, it gives
$$\int_0^{2\pi} \frac{dx}{2 + \cos x} = 0,$$
although the integrand is positive, and the [[full non-example|YYC7CRH6M4]] finds the true value $\frac{2\pi}{\sqrt{3}}$.

A line can also carry too many conditions.
"The bisector of angle $A$, which meets $BC$ at its midpoint" exists only when $AB = AC$, so a proof that draws it proves something only about isosceles triangles.
Adding many lines without a plan is a third failure: the figure grows, and no known theorem comes closer.

### The rules of the scaffold

An auxiliary element must be defined from the data alone, not from the unknown in a hidden way.
Its existence must be justified.
The parallel of the angle sum exists and is unique by the [[parallel postulate|2PC3XY0PYZ]], and the reflected point always exists.
The final result usually does not mention the element, which works like scaffolding around a building.
Different elements can solve the same problem: Euclid drew a parallel through $C$ instead of $A$.

### Watch out

Do not read a property of the auxiliary element off the figure.
If you draw two auxiliary lines and the drawing shows them meeting inside the triangle, that is a claim to prove, and [[a too special figure|SXA7G1N6HZ]] shows how a drawing can deceive.
Check also that a new variable is defined and invertible on the whole range you use; equal limits after a substitution, as with $\tan 0 = \tan \pi = 0$, are a warning sign.

### History

Euclid's *Elements* is full of auxiliary constructions.
Proposition 32 of Book I proves the angle sum of a triangle by producing one side and drawing a parallel to another.
Heron of Alexandria explained the [[law of reflection|JSTZ7M5VEB]] by the shortest path through a reflected point.
Pólya made "auxiliary elements" an entry in the dictionary part of *How to Solve It* (1945).

### Try it

Find the angle sum of a convex pentagon.
The diagonals from one vertex are auxiliary segments that cut the pentagon into $3$ triangles, so the sum is $3 \cdot 180^\circ = 540^\circ$.

Find the real numbers $x \ne 0$ with $x^2 + \frac{1}{x^2} = 2$.
With $s = x + \frac{1}{x}$ we get $s^2 = 4$, so $s = \pm 2$, and $x + \frac{1}{x} = \pm 2$ gives $x = 1$ or $x = -1$.

## Explanations

### L1 human

Sometimes a problem seems stuck because a piece is missing.
An auxiliary element is a piece that you add yourself: a line in a drawing, or a new letter in an equation.
Tear the three corners off a paper triangle and put their tips together; they make a straight line.
The proof does the same with a line through one corner, parallel to the opposite side, which copies the other two angles next to the first.
The new line was not in the problem, but it made the answer visible.

### L2 human

We find the shortest path from $A = (1, 2)$ to $B = (5, 4)$ that touches the $x$-axis.
The path bends at the axis, so we add the reflected point $B' = (5, -4)$, and every point $P$ of the axis has $PB = PB'$.
The shortest path from $A$ to $B'$ is the straight segment, and its slope is
$$\frac{-4 - 2}{5 - 1} = -\frac{3}{2}.$$
The segment meets the axis where $2 - \frac{3}{2}(x - 1) = 0$, so at $P^* = \left(\frac{7}{3}, 0\right)$.
The least length is $AB' = \sqrt{4^2 + 6^2} = 2\sqrt{13} \approx 7.21$.
Check with another point, $P = (3, 0)$: $AP + PB = \sqrt{8} + \sqrt{20} \approx 2.83 + 4.47 = 7.30$, which is larger.

The reflection did the real work, and the answer does not mention it.
That is the typical shape of an auxiliary element: it changes a problem with no known method into one with a known method.

### L3 human

In analysis, auxiliary functions are routine in proofs.
The Cauchy mean value theorem uses $h(x) = (f(b) - f(a))\, g(x) - (g(b) - g(a))\, f(x)$, and Taylor's theorem with remainder uses a similar construction.
In transcendence theory, the auxiliary polynomial is a named method, used in the proofs that $e$ and $\pi$ are transcendental and in the Gelfond-Schneider theorem.
In modern geometry, many auxiliary lines are replaced by transformations: reflections, rotations and [[homotheties|0ZG1PNEP35]].
In logic, adding a new constant or a definition to a theory gives a conservative extension, which is the formal version of scaffolding: the new symbol proves nothing new about the old language.
Auxiliary elements change the figure or the variables, while an [[auxiliary problem|DYSJB93V11]] changes the question, and [[working backwards|3QTB9S1THS]] is often how the right element is found.
