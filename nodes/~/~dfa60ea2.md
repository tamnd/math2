---
tag: ~dfa60ea2
kind: concept
name: Symmetry arguments
aliases: [symmetry-argument, by-symmetry, argument-by-symmetry]
msc: ["00A35", "97E50"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: school
specializes: [0B94TKFQJX]
uses: [0B94TKFQJX, 0EPAT51DXQ, 0ZG3Z5JZ85, 0FP31SX5EA, 0VHSHB9B6J]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetry_in_mathematics
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Even_and_odd_functions
    locator: lead section
  - book: isbn:9780691164076
    locator: Part III
---

## Summary

A symmetry argument uses a transformation $T$ that leaves a problem unchanged: $T$ maps the data of the problem to themselves, and so it maps each solution to a solution.
Such a $T$ is a symmetry of the problem.
The argument uses $T$ in one of three ways.
It proves one case and transfers the result to the other cases by $T$.
It concludes that a unique answer is fixed by $T$, which often finds the answer.
Or it writes a quantity in two ways, $Q$ and $Q$ after $T$, and adds them to get a simpler expression.
The method matters because symmetry is often the shortest route to a result, and because it explains the form of the answer, for example why a formula in two variables is the same in both.

## Motivation

Many problems treat several objects in the same way.
The equation $x + y = 10$, $xy = 21$ does not change when $x$ and $y$ are exchanged.
The two base angles of an isosceles triangle play the same role.
In such a problem, two proofs that differ only by the names of the objects are the same proof.
A careful author writes the proof once and states the symmetry that transfers it.
Symmetry also guides discovery: if the problem does not change under $T$, a unique answer cannot change under $T$ either.
George Pólya lists symmetry among the heuristics of discovery, with the advice to use it and to keep it.

## Notation

1. A symmetry is often written as a map: $x \leftrightarrow y$ (exchange), $x \mapsto -x$ (reflection), $x \mapsto 1/x$ (inversion), $x \mapsto a - x$ (reflection about $a/2$).
2. A function $f(x, y)$ is symmetric when $f(x, y) = f(y, x)$. A function $f$ of one variable is even when $f(-x) = f(x)$ and odd when $f(-x) = -f(x)$, see [[even and odd functions|0FP31SX5EA]].
3. The phrase "by symmetry" in a proof means: the omitted case follows from the written case by the stated symmetry. A related phrase is "without loss of generality", see the abbreviation wlog in [[this example sentence|K35RJ9YHC0]].
4. The elementary symmetric polynomials in $x$ and $y$ are $e_1 = x + y$ and $e_2 = xy$.

## Remarks

### Examples

1. [[The integral of the square of the sine by symmetry|~f00ae59b]]: the substitution $x \mapsto \pi/2 - x$ exchanges $\sin^2$ and $\cos^2$ on $[0, \pi/2]$, so the two integrals are equal, and their sum is $\pi/2$.
2. [[A palindromic quartic equation solved by symmetry|~2a9058a9]]: the equation $x^4 + x^3 - 4x^2 + x + 1 = 0$ does not change under $x \mapsto 1/x$, and the symmetric variable $t = x + 1/x$ reduces it to a quadratic equation.
3. The sum $1 + 2 + \dots + n$: reversing the order gives the same sum, and adding the two forms term by term gives $n$ copies of $n + 1$. See [[two proofs of this formula|D6G69GNKPC]].
4. The [[isosceles triangle theorem|056VS31A0J]]: if $AB = AC$, the reflection in the bisector of the angle at $A$ exchanges $B$ and $C$ and fixes the triangle, so it maps the angle at $B$ to the angle at $C$, and the two angles are equal.
5. For an odd integrable function $f$ on $[-a, a]$, the substitution $x \mapsto -x$ gives $\int_{-a}^{a} f = -\int_{-a}^{a} f$, so the integral is $0$. For example, $\int_{-1}^{1} x^3 \cos x \, dx = 0$, with no antiderivative needed.
6. The system $x + y = 10$, $xy = 21$ is symmetric. By [[Vieta's formulas|0M8EWQJ1YV]], $x$ and $y$ are the roots of $z^2 - 10z + 21 = (z - 3)(z - 7)$, so $\{x, y\} = \{3, 7\}$.

### Non-examples

1. [[Symmetry does not place an extremum at the symmetric point|~9487c590]]: on the segment $x + y = 2$, $x, y \ge 0$, the symmetric function $x^2 + y^2$ has its minimum at the symmetric point $(1, 1)$, but its maximum at $(2, 0)$ and $(0, 2)$.
2. The function $x + 2y$ on the circle $x^2 + y^2 = 1$ is not symmetric under $x \leftrightarrow y$, so symmetry says nothing about its extremes. Its maximum is $\sqrt{5}$, at $(1/\sqrt{5}, 2/\sqrt{5})$, where $x \neq y$. The condition that fails is that the exchange preserves the problem.
3. The equation $x + y = 2$ is symmetric, but the solution $(0, 2)$ is not fixed by the exchange. A unique solution is fixed by a symmetry, but a symmetric problem with several solutions can have solutions that are not fixed.

### Basic properties

1. If $T$ is a symmetry of a problem and the problem has exactly one solution $s$, then $T(s) = s$. The reason: $T(s)$ is also a solution, and the solution is unique.
2. If $T$ is a symmetry, the set $S$ of solutions satisfies $T(S) = S$ when $T$ is a bijection whose inverse is also a symmetry. So the solutions come in orbits.
3. The symmetries of a problem are closed under composition and inverses, so they form a group, the [[symmetry group|0ZG3Z5JZ85]] of the problem. It suffices to check the generators of this group.
4. Each symmetric polynomial in $x_1, \ldots, x_n$ is a polynomial in the elementary symmetric polynomials, by the [[fundamental theorem of symmetric polynomials|0GW1ZZH0R4]]. So a symmetric problem can be rewritten in the variables $e_1, \ldots, e_n$.
5. If $\int_a^b f(x) \, dx = \int_a^b g(x) \, dx$ by a substitution, then each integral equals $\tfrac12 \int_a^b (f + g)$. This is the averaging form of the method.

### History

Symmetry arguments are as old as Greek geometry.
Proclus reports a proof of the isosceles triangle theorem by Pappus that compares the triangle $ABC$ with the same triangle read as $ACB$, a symmetry argument in place of Euclid's longer construction.
In "How to Solve It" (1945), George Pólya included symmetry in his short dictionary of heuristics.

### Common errors

1. A student assumes that the extremum of a symmetric function lies at the symmetric point. Symmetry gives no such conclusion, see the non-example above.
2. A student writes "by symmetry" when the statement is not symmetric, for example after one hypothesis treats $x$ and $y$ differently. Each use must name the symmetry and check that it preserves all hypotheses.
3. A student uses a substitution as a symmetry without checking that it maps the domain to itself. The map $x \mapsto 1/x$ is a symmetry of an equation on $\mathbb{R} \setminus \{0\}$, so the case $x = 0$ must be checked separately.

## Explanations

### L1 human

A problem is symmetric when we can swap some of its parts and get the same problem.
For example, the question "which two numbers add up to $10$ and multiply to $21$" does not care which number we call first.
So if $3$ and $7$ is an answer, then $7$ and $3$ is the same answer.
Symmetry can also save work: if a proof works for the left half of a picture, the mirror image of the proof works for the right half.
And it can find answers: if a square is cut by its diagonal, the two halves are mirror images, so each has half the area.

### L2 human

We compute $\int_0^{1} \frac{x^4}{x^4 + (1 - x)^4} \, dx$ by symmetry.

1. Let $I$ be the integral, and let $f(x) = \frac{x^4}{x^4 + (1 - x)^4}$. The denominator is positive on $[0, 1]$, because $x$ and $1 - x$ are never both $0$.
2. The substitution $x \mapsto 1 - x$ maps $[0, 1]$ to itself, and by [[integration by substitution|0D37QFPEZE]] it gives $I = \int_0^1 f(1 - x) \, dx = \int_0^1 \frac{(1 - x)^4}{(1 - x)^4 + x^4} \, dx$.
3. Adding the two forms of $I$ gives $2I = \int_0^1 \frac{x^4 + (1 - x)^4}{x^4 + (1 - x)^4} \, dx = \int_0^1 1 \, dx = 1$.
4. So $I = \tfrac12$.

The typical use is an integral or a sum that does not change under a reflection, where the sum of the two forms is simple.
A trap is to forget to check that the substitution maps the interval of integration onto itself: $x \mapsto 1 - x$ works on $[0, 1]$, but not on $[0, 2]$ with the same integrand.

### L3 human

A symmetry argument is the use of a group action that preserves a problem.
The solutions form a union of orbits, a unique solution is a fixed point, and averaging over the group (the Reynolds operator) projects a quantity onto its invariant part.
This view connects the school method to [[Galois theory|WNQDKQYZ2R]], which studies the symmetries of the roots of a polynomial, and to [[Noether's theorem|XHPDM5T2JG]], which turns a continuous symmetry of a physical system into a conservation law.
In analysis, [[Steiner symmetrization|3YF7P33WRM]] makes a set more symmetric while it keeps the area and lowers the perimeter, and this proves the isoperimetric inequality.
In combinatorics, symmetry reduces a count to the count of orbits, as in Burnside's lemma.
The method is closely related to [[reduction to a special case|~472d0870]], since a symmetry often reduces a problem to one normalized case.
