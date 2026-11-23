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

Analogy is the habit of asking "where have I seen a problem like this?" and then copying the method that solved the old problem.
It works when the two problems share the relations that the old solution used, and it misleads when they only look alike.

Here is a problem where the habit pays off.
Find the greatest common divisor of
$$f = x^5 + x + 1 \quad \text{and} \quad g = x^4 + x^2 + 1$$
as polynomials with rational coefficients.
The first idea is to factor both polynomials and compare the factors.
The only possible rational roots are $\pm 1$, and $f(1) = 3$, $f(-1) = -1$, $g(1) = g(-1) = 3$, so neither polynomial has a linear factor, and the attempt stalls.

The helping question is whether we know a way to find a greatest common divisor without factoring.
We do, for integers: the [[Euclidean algorithm|0TRNT4X7J0]] finds $\gcd(a, b)$ by repeated division with remainder, and polynomials over a field also have division with remainder.
So we copy the algorithm.
Divide $f$ by $g$, then $g$ by the remainder, and so on:
$$x^5 + x + 1 = x \cdot (x^4 + x^2 + 1) + (1 - x^3),$$
$$x^4 + x^2 + 1 = x \cdot (x^3 - 1) + (x^2 + x + 1),$$
$$x^3 - 1 = (x - 1)(x^2 + x + 1) + 0.$$
In the second line we divided by $x^3 - 1$ instead of $1 - x^3$, which changes only a constant factor.
The last nonzero remainder is $x^2 + x + 1$, so that is the greatest common divisor, up to a nonzero constant.
Check: $(x^2 + x + 1)(x^3 - x^2 + 1) = x^5 + x + 1$ and $(x^2 + x + 1)(x^2 - x + 1) = x^4 + x^2 + 1$.
The factor has no rational root, which is why the search for roots could not find it.

In general, analogy as a heuristic uses a likeness of relations between two problems or two theories to carry a method, a result or a conjecture from one to the other.
It gives a plan or a guess, never a proof, and every step of the copied argument must be checked in the new setting.

## Motivation

A new problem is seldom new in every respect.
A problem about a tetrahedron often resembles a solved problem about a triangle, and a problem about polynomials often resembles a solved problem about integers.
If the resemblance lies in the relations that the old solution uses, the old solution can be copied with small changes.
This is why "Do you know a related problem?" is the first question of the plan stage of [[Pólya's four steps|DYD57G2Y5Z]].

Analogy is also a main source of conjectures.
Euler guessed the value of $\sum 1/k^2$ by treating the sine function as a polynomial with infinitely many roots, and the guess was right.
A conjecture found this way is evidence in the sense of [[plausible reasoning|8DHD3H1CJ9]], and it still needs a proof.
When an analogy works across many cases, it usually points to a shared structure, and mathematicians then define that structure and study it for itself.

## Notation

Pólya used the plain word "analogy" and asked the solver to look for an "analogous problem" or a "related problem".
Some books speak of the "transfer" of a method from one setting to another.
There are no symbols.
When you write a solution, make the correspondence explicit, for example "integer $\leftrightarrow$ polynomial, absolute value $\leftrightarrow$ degree", so that the reader can check each transferred step.

## Remarks

### How to use an analogy

The habit has four steps, but they are advice, not an algorithm, and nothing guarantees that an analogous problem exists or that its method transfers.

1. Look for a problem with the same kind of unknown or the same structure that is solved or easier.
2. Write down which object of one problem matches which object of the other.
3. Carry the method or the result along that correspondence.
4. Check each step in the new setting, and replace any step that used a property with no analogue.

Common pairs are triangle and tetrahedron, plane and space, finite sums and integrals, integers and polynomials, and finite and infinite dimension.

### Worked analogies

The opening problem is one case of a general transfer, and [[the greatest common divisor of two polynomials by analogy with integers|9YWVE7QTZH]] works another one with the integer version beside it.
The analogy goes deeper: the [[fundamental theorem of arithmetic|084HH1NDCB]] has the analogue that every nonconstant polynomial over a field is a product of irreducible polynomials, unique up to order and constant factors.

Triangle and tetrahedron give a second pair.
The medians of a triangle $ABC$ meet at $\tfrac{1}{3}(A + B + C)$, which divides each median in the ratio $2 : 1$ from the vertex.
By analogy, the segments from the vertices of a tetrahedron $ABCD$ to the centroids of the opposite faces meet at $\tfrac{1}{4}(A + B + C + D)$.
That point divides each segment in the ratio $3 : 1$, and the vector computation is the same as in the triangle.

The boldest example is Euler's, worked in [[Euler's sum of the reciprocal squares by analogy with polynomials|7PBNK2E6DC]].
There the analogy is between a polynomial and an infinite product, and it gave the right answer before anyone could justify the step.

### Sums and integrals

The sum $\sum_{k=1}^{n} k$ is analogous to the integral $\int_0^n x \, dx = \tfrac{n^2}{2}$, and indeed $\sum_{k=1}^{n} k = \tfrac{n^2}{2} + \tfrac{n}{2}$.
The analogy suggests that $\sum_{k=1}^{n} k^2$ is $\tfrac{n^3}{3}$ plus terms of lower degree.
The exact value is
$$\sum_{k=1}^{n} k^2 = \frac{n^3}{3} + \frac{n^2}{2} + \frac{n}{6},$$
which you can check at $n = 2$: $\tfrac{8}{3} + 2 + \tfrac{1}{3} = 5 = 1 + 4$.
The analogy gave the leading term, and a separate argument, such as induction, gives the rest.

### When an analogy misleads

An analogy misleads when the step that the old proof needs has no analogue.
The ring $\mathbb{Z}[\sqrt{-5}]$ looks like the integers, yet [[unique factorization fails in Z[√-5]|XXEAV5BBNT]], because the integer proof uses division with remainder and this ring has none of the right kind.

A likeness of form is not enough either.
The equations $x^2 + y^2 = z^2$ and $x^3 + y^3 = z^3$ look alike, but the first has infinitely many solutions in positive integers and the second has none.
Real and complex functions give a third warning.
A real function can have a derivative at every point and a second derivative at no point, while a complex function with a derivative on an open set has derivatives of every order there.

### Watch out

The usual error is to transfer a statement and skip the check of the step that has no analogue.
For example, "if $2$ divides a product, it divides a factor" holds in $\mathbb{Z}$.
In $\mathbb{Z}[\sqrt{-5}]$, $2$ divides $(1 + \sqrt{-5})(1 - \sqrt{-5}) = 6$ and divides neither factor.
The correct move is to find the lemma on which the old proof rests and to test that lemma first.
A second error is to stop at the analogy and report the guess as a result.

### History

Euler found the sum of the reciprocal squares by an argument from analogy in the 1730s, and he gave other arguments for it later.
Pólya made analogy a main theme of *How to Solve It* (1945) and of the first volume of *Mathematics and Plausible Reasoning* (1954), whose subtitle is "Induction and Analogy in Mathematics".
André Weil described the analogy between number fields and function fields of curves over finite fields, and that analogy guided much of twentieth-century number theory.

### Try it

First, use the Euclidean algorithm to find the greatest common divisor of $x^3 + 1$ and $x^2 - 1$ over $\mathbb{Q}$.
Division gives $x^3 + 1 = x(x^2 - 1) + (x + 1)$ and then $x^2 - 1 = (x - 1)(x + 1) + 0$, so the answer is $x + 1$.

Second, a square has $2$ diagonals between opposite corners; how many segments join opposite corners of a cube?
The $8$ corners of a cube form $4$ opposite pairs, so there are $4$ such segments.

## Explanations

### L1 human

When a problem is hard, ask whether you have met a problem like it before.
A square has $2$ diagonals, each joining a corner to the opposite corner.
A cube is the square's analogue in space, so we ask how many segments join opposite corners of a cube.
The idea "pair each corner with its opposite" carries over: the $8$ corners form $4$ pairs, so there are $4$ such segments.
The square did not give the number, but it gave the idea that found the number.

### L2 human

We use the analogy of plane and space to find how many regions $3$ planes in general position cut space into.
The plane problem is solved: $n$ lines in general position cut the plane into $1 + n + \binom{n}{2}$ regions, so $3$ lines give $7$.
Its method is that each new line is cut by the earlier lines into pieces, and each piece splits one region into two.

Copy the method one dimension up.
Two planes cut space into $4$ regions.
The third plane meets the first two in two crossing lines, and these cut the third plane into $4$ pieces.
Each piece splits one region of space into two, so the count is
$$4 + 4 = 8.$$
Check: the three coordinate planes in general position cut space into $8$ octants.

The analogy carried the method, not the number: the plane gives $7$ and space gives $8$.
The claim "each piece splits one region" also had to be checked again in space, and it holds because a convex piece of plane cuts the region it lies in into two parts.

### L3 human

Analogies that work in many cases are often the first sign of a common structure.
The analogy of $\mathbb{Z}$ and $k[x]$ became the theory of [[Euclidean domains|023VY493K0]] and principal ideal domains, where both are special cases, and this step from analogy to structure is a form of [[abstraction|976RZZCT1H]].
The analogy of number fields and function fields became a guide for conjectures, such as the Riemann hypothesis for curves over finite fields, which Weil proved.

In category theory an analogy is often made exact as a functor or as a shared universal property.
The failures of analogy have been just as fruitful: the failure of unique factorization in rings of algebraic integers led to the theory of ideals.
Analogy as a source of conjectures returns in [[plausible reasoning and experimental mathematics|DME0TPC348]], and its partner heuristics are [[generalization|8NJ0VN9Z97]], which turns two analogous problems into cases of one, and the [[auxiliary problem|DYSJB93V11]].
