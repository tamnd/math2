---
tag: 7KDT0R1HF2
kind: concept
name: Analogy
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, DYD57G2Y5Z]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - url: https://en.wikipedia.org/wiki/Analogy
    locator: lead section
  - book: isbn:9780691164076
---

## Summary

Analogy, as a heuristic, is the use of a similarity between two problems or two theories to transfer a method, a result or a conjecture from one to the other.
Two systems are analogous when their parts agree in their relations: for example, division with remainder relates integers in the same way as it relates polynomials over a field.
The heuristic has three common forms: solve a similar, simpler problem first and copy its method; transfer a theorem from one area to an analogous area; and form a conjecture by analogy with a known result.
An analogy proves nothing by itself, because two analogous systems can differ in the property that matters.
Analogy matters because it is one of the main sources of conjectures and of new theories, and it is the first question of the plan phase of [[Pólya's four steps|DYD57G2Y5Z]]: "Do you know a related problem?"

## Motivation

A new problem is seldom new in every respect.
A problem about a tetrahedron often resembles a solved problem about a triangle, and a problem about polynomials often resembles a solved problem about integers.
If the resemblance is in the relations that the solution uses, then the old solution can be copied.
The difficulty is to see which resemblances matter.
Analogy as a heuristic is the habit of looking for such resemblances, testing them, and using them.

## Remarks

### The steps

1. Find an analogous problem: a problem with the same kind of unknown or the same structure, which is solved or easier.
2. Make the correspondence explicit: list which object of one problem matches which object of the other.
3. Transfer the method or the result along the correspondence.
4. Check each step in the new setting. A step that used a property without an analogue must be replaced or proved anew.

### When it applies

Analogy applies when the problem has a simpler relative of lower dimension, of a smaller degree, or in a better known area.
Typical pairs are triangle and tetrahedron, plane and space, finite sums and integrals, integers and polynomials, and finite and infinite dimension.

### Examples

1. [[Euler's sum of the reciprocal squares by analogy with polynomials|7PBNK2E6DC]]: Euler treated $\frac{\sin x}{x}$ like a polynomial with known roots and found $\sum \frac{1}{k^2} = \frac{\pi^2}{6}$.
2. [[The greatest common divisor of two polynomials by analogy with integers|9YWVE7QTZH]]: the [[Euclidean algorithm|0TRNT4X7J0]] for integers transfers to polynomials over a field.
3. Triangle and tetrahedron. The three medians of a triangle meet in a point that divides each median in the ratio $2 : 1$. By analogy, the four segments from the vertices of a tetrahedron to the centroids of the opposite faces meet in a point, and it divides each segment in the ratio $3 : 1$. Both facts follow from the centroid $\frac{1}{3}(A + B + C)$ and $\frac{1}{4}(A + B + C + D)$.
4. Sums and integrals. The sum $\sum_{k=1}^{n} k = \frac{n^2}{2} + \frac{n}{2}$ is analogous to $\int_0^n x \, dx = \frac{n^2}{2}$, and the analogy suggests that $\sum_{k=1}^{n} k^2$ is $\frac{n^3}{3}$ plus lower terms; the exact value is $\frac{n^3}{3} + \frac{n^2}{2} + \frac{n}{6}$.
5. Integers and polynomials. The [[fundamental theorem of arithmetic|084HH1NDCB]] has the analogue that every nonconstant polynomial over a field is a product of irreducible polynomials, unique up to order and constant factors.

### Non-examples

1. [[Unique factorization fails in Z[√-5]|XXEAV5BBNT]]: the analogy with the integers suggests unique factorization, and it is false in this ring.
2. Real and complex numbers. On $\mathbb{R}$, a function with a derivative at every point can have a second derivative nowhere; by analogy one may expect the same on $\mathbb{C}$, but a complex differentiable function on an open set has derivatives of all orders.
3. A surface likeness without shared relations. The equations $x^2 + y^2 = z^2$ and $x^3 + y^3 = z^3$ look alike, but the first has infinitely many solutions in positive integers and the second has none.

### Basic properties

1. An analogy is a correspondence of relations, not of objects. Integers and polynomials are different objects, and the analogy lies in division with remainder.
2. Analogy can transfer a method, a statement or a definition. Each transfer needs its own check in the new setting.
3. When an analogy works in many cases, it often points to a common structure. The analogy of integers and polynomials led to the notion of a [[Euclidean domain|023VY493K0]], where both are special cases; this is [[abstraction|976RZZCT1H]].
4. Analogy is a form of [[plausible reasoning|DME0TPC348]]: a verified analogue makes a conjecture more credible, but not certain.

### Related methods

[[Generalization|8NJ0VN9Z97]] often follows analogy: two analogous problems become special cases of one general problem.
An [[auxiliary problem|DYSJB93V11]] is often an analogous problem that is easier.
[[Specialization|FTBJX4G51S]] produces the simple analogues, such as the plane case of a space problem.

### History

Euler found the sum of the reciprocal squares by an argument from analogy in the 1730s, and gave other arguments for it later.
Pólya made analogy a main theme of *How to Solve It* (1945) and of the first volume of *Mathematics and Plausible Reasoning* (1954), whose subtitle is "Induction and Analogy in Mathematics".
André Weil described the analogy between number fields and function fields of curves over finite fields, which guided much of twentieth-century number theory.

### Common errors

1. To transfer a statement without checking the step that uses a property with no analogue, as in non-example 1.
2. To take a likeness of form for an analogy of structure, as in non-example 3.
3. To stop at the analogy. An analogy gives a conjecture or a plan, and a proof is still needed.

## Explanations

### L1 human

When a problem is hard, it helps to ask: have I seen a problem like this one?
For example, a square has $2$ diagonals, and a cube has $4$ long diagonals from corner to opposite corner.
We can guess the number for the cube by thinking of the square: each long diagonal joins a corner to the one opposite it.
A cube has $8$ corners, and they form $4$ opposite pairs, so there are $4$ long diagonals.
The square helped us to see the idea of opposite pairs.

### L2 human

We use the analogy of plane and space to find the number of regions into which $3$ planes in general position divide space.

1. The analogous problem one dimension lower: $n$ lines in general position divide the plane into $1 + n + \binom{n}{2}$ regions, so $3$ lines give $7$ regions.
2. Its method: the $n$-th line is cut by the earlier lines into $n$ pieces, and each piece splits one region into two.
3. Transfer: the third plane meets the first two planes in two lines in general position, which cut the third plane into $4$ regions.
4. Each of these $4$ regions of the third plane splits one region of space into two.
5. Two planes divide space into $4$ regions, so three planes give $4 + 4 = 8$ regions.

The typical use: the lower-dimensional problem gives the method, and the method is checked in the new setting.

A trap: the answer for the plane is $7$, and the answer for space is $8$; the analogy transfers the method, not the number.

### L3 human

Analogies that work across many cases are often the first sign of a common structure, and the structure is then defined and studied for itself.
The analogy of $\mathbb{Z}$ and $k[x]$ became the theory of Euclidean domains and principal ideal domains.
The analogy of number fields and function fields became a guide for conjectures, such as the Riemann hypothesis for curves over finite fields, which Weil proved.
In category theory, an analogy is often made exact as a functor or as a common universal property.
Analogy is also the main source of conjectures studied in [[plausible reasoning and experimental mathematics|DME0TPC348]], and its failures, such as the failure of unique factorization in rings of algebraic integers, led to the theory of ideals.
