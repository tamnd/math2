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

An auxiliary element is an object that is not in the statement of a problem but is added to help solve it.
It can be a line or a point in a figure, a new variable, a function, or a quantity that is computed along the way.
The [[heuristic|6KCEWEP4WA]] is to ask: which new element would link the data to the unknown, or turn the problem into one whose solution is known?
A typical case is the proof of the [[mean value theorem|0BARQY52N5]], where an auxiliary function turns the statement into [[Rolle's theorem|0194DY35BG]].
The added element must be well defined and must fit the conditions of the problem.
Like every heuristic, it does not guarantee success: the right element is found by trial, guided by known solutions.

## Motivation

Many problems fail to start because the data and the unknown are not connected by any known fact.
In the angle sum of a triangle, no theorem on the three angles is at hand, but one parallel line brings in the theorems on parallels.
In the mean value theorem, the hypothesis is about $f$, but the known result, Rolle's theorem, needs a function with equal values at the ends.
An auxiliary element is the bridge in such a case.
It carries the problem into a region where known theorems apply.

## Remarks

### The steps

1. Look at the unknown and recall a known problem or theorem with the same kind of unknown.
2. Ask which object is missing for that known result to apply: a parallel, a midpoint, a reflected point, a function with special values.
3. Add the object and state exactly how it is defined.
4. Check that the object exists and has the properties needed, under the hypotheses of the problem.
5. Solve the problem with the help of the object, then check whether the object can be removed from the final statement.

### When it applies

- In geometry: a figure lacks a line or point that would create congruent or similar triangles, parallels, or a known circle.
- In analysis: a theorem applies to functions of a special form, and the given function can be adjusted to that form.
- In algebra and calculus: a new variable turns a complicated expression into a simpler one, as in a substitution.
- In optimisation: a path with a corner becomes a straight segment after a reflection.

### Examples

1. [[The angle sum of a triangle with an auxiliary parallel line|DA40QCPX63]]: the line through one vertex parallel to the opposite side turns the three angles into angles along a straight line.
2. [[The shortest path that touches a line, found with a reflected point|52DGE85AR1]]: the reflected point turns a broken path into a straight segment.
3. The proof of the mean value theorem. For $f$ continuous on $[a, b]$ and differentiable on $(a, b)$, set
   $$g(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}(x - a).$$
   Then $g(a) = g(b) = 0$, so Rolle's theorem gives $c$ with $g'(c) = 0$, that is $f'(c) = \frac{f(b) - f(a)}{b - a}$, as in the [[proof from Rolle's theorem|YBRVDSFRE7]].
4. [[Constructing a triangle from two sides and the median|ZKWF9YNS66]]: the auxiliary point is the end of the median produced to twice its length.
5. To find $x$ with $x^2 + \frac{1}{x^2} = 7$ and $x > 0$, introduce $s = x + \frac{1}{x}$. Then $s^2 = 7 + 2 = 9$, so $s = 3$, and $x^2 - 3x + 1 = 0$ gives $x = \frac{3 \pm \sqrt{5}}{2}$.

### Non-examples

1. [[An auxiliary variable that breaks the integral of 1/(2 + cos x) over a full period|YYC7CRH6M4]]: the variable $t = \tan \frac{x}{2}$ is not defined at $x = \pi$, and the naive computation gives $0$ for a positive integral.
2. An auxiliary line with two conditions that cannot both hold. In a triangle, "the bisector of angle $A$, which meets $BC$ at its midpoint" is legitimate only if $AB = AC$. A proof that adds such a line proves things about isosceles triangles only.
3. Adding many lines to a figure without a plan. The figure gets more complicated, and no known theorem comes closer.

### Basic properties

1. An auxiliary element must be defined from the data alone. It may not depend on the unknown in a hidden way.
2. Its existence must be justified: the parallel exists by the parallel postulate, the reflected point always exists, but a substitution may be undefined at some points.
3. The final result usually does not mention the auxiliary element. It is scaffolding, and the statement stays the same with or without it.
4. Different auxiliary elements can solve the same problem. The angle sum also follows from a parallel through a point on a side, or from a walk around the triangle.
5. The heuristic gives no rule for choosing the element. Choices come from experience with similar problems, so a stock of known solutions helps.

### Related methods

- [[Auxiliary problem|DYSJB93V11]]: the auxiliary element changes the figure or the variables, and the auxiliary problem changes the question.
- [[Working backwards|3QTB9S1THS]]: the analysis of a construction often reveals the auxiliary element.
- [[Draw a figure and introduce notation|6CVYB413ER]]: a good figure and a good name for a quantity are the simplest auxiliary elements.
- [[Symmetry arguments|H840D9TM2X]]: a reflection or rotation often gives the auxiliary point.
- [[Analogy|7KDT0R1HF2]]: the auxiliary line used for a similar problem is a good first guess.

### History

Euclid's Elements is full of auxiliary constructions.
In Book I, Proposition 32 proves the angle sum of a triangle by producing a side and drawing a parallel.
Heron of Alexandria explained the [[law of reflection|JSTZ7M5VEB]] by the shortest path through a reflected point.
George Pólya made "auxiliary elements" an entry of the heuristic dictionary in How to Solve It (1945).
He asked: "Should you introduce some auxiliary element in order to make its use possible?"

### Common errors

1. Adding an element with too many conditions, so that it exists only in special cases.
2. Using an auxiliary variable where it is undefined or not invertible, as in non-example 1.
3. Reading a property of the auxiliary element off the figure without proof, for example that two auxiliary lines meet inside the triangle.

## Explanations

### L1 human

Sometimes a problem seems stuck because a piece is missing.
An auxiliary element is a piece that we add ourselves: a line in a drawing, a new letter in an equation.
For example, to show that the angles of a triangle add up to $180^\circ$, draw a line through one corner, parallel to the opposite side.
The three angles now sit side by side along that line, and angles along a straight line add up to $180^\circ$.
The new line was not in the problem, but it made the answer visible.

### L2 human

We prove the mean value theorem from Rolle's theorem and show how the auxiliary function is found.

1. Rolle's theorem: if $g$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $g(a) = g(b)$, then $g'(c) = 0$ for some $c \in (a, b)$.
2. The goal is $f'(c) = m$, where $m = \frac{f(b) - f(a)}{b - a}$ is the slope of the chord. This means $(f(x) - m x)'$ is $0$ at $c$.
3. So try $g(x) = f(x) - m x$. Then $g(b) - g(a) = f(b) - f(a) - m(b - a) = 0$, so $g(a) = g(b)$.
4. The function $g$ is continuous and differentiable wherever $f$ is, since $m x$ is a polynomial.
5. Rolle's theorem gives $c \in (a, b)$ with $g'(c) = 0$, that is $f'(c) = m$.

The typical use: the goal $f'(c) = m$ was rewritten as $g'(c) = 0$, which suggested $g$.

A trap: the usual textbook form subtracts also the constant $f(a) - m a$, so that $g(a) = g(b) = 0$; this constant changes nothing, and step 3 shows that only $g(a) = g(b)$ is needed.

### L3 human

In analysis, auxiliary functions are standard in proofs: the Cauchy mean value theorem uses $h(x) = (f(b) - f(a)) g(x) - (g(b) - g(a)) f(x)$, and Taylor's theorem with remainder uses a similar construction.
In transcendence theory, the auxiliary polynomial or function is a named method, used in the proofs for $e$ and $\pi$ and in the Gelfond-Schneider theorem.
In geometry, the auxiliary elements of the classical problems are now often replaced by transformations: reflections, rotations and [[homotheties|0ZG1PNEP35]].
In logic, adding a new constant or a new definition to a theory gives a conservative extension, which is the formal version of scaffolding: the new symbol proves nothing new about the old language.
