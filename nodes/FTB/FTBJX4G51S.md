---
tag: FTBJX4G51S
kind: concept
name: Specialization
msc: ["00A35", "97E50"]
topics: [X1NSTVGDNQ]
audience: school
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, F3NNR77WKP, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

Specialization, as a heuristic, is the passage from a given problem about a whole class of objects to the same problem for a smaller class or a single object of that class.
The solver tries small cases ($n = 1, 2, 3$), extreme cases (a degenerate triangle, a radius $0$, a parameter tending to infinity) and special values ($x = 0$, $x = 1$, a symmetric position).
The special cases are used in three ways: to understand the problem, to find a pattern or a method that may hold in general, and to refute a general claim by a [[counterexample|0ED72CTBNP]].
A special case can refute a universal statement, but it cannot prove one.
Specialization matters because special cases are the easiest source of data and of ideas, and they are the fastest test of a conjecture.

## Motivation

A general problem has many parameters, and the solver cannot hold them all in mind at once.
A special case removes some parameters and leaves a problem that can be computed by hand.
The computed values show what the answer looks like, and the computation often shows why.
In the other direction, a general claim must hold in each special case, so one failing case ends it.
Both uses are cheap, and so a special case is often the first thing that an experienced solver tries.

## Remarks

### The steps

1. Choose a special case: a small value of the parameter, an extreme position, or a value that makes the problem symmetric.
2. Solve the special case completely, with every number.
3. Repeat for several cases, in an order that makes a pattern visible, such as $n = 1, 2, 3, 4, 5$.
4. State a conjecture that fits the cases, and test it on a new case that was not used to form it.
5. Look in the solutions of the special cases for an argument that does not depend on the special values. That argument is the plan for a proof.

### When it applies

Specialization applies whenever a problem has a parameter: a natural number $n$, a real variable, a shape, or a dimension.
It is useful at the start, to understand the problem, and at the end, to check the result.
It is the standard first move for a statement about all $n$, before a proof by [[mathematical induction|0ASJVEFA9J]].

### Examples

1. [[Regions cut out by lines in the plane, found from small cases|Z5GX4ECAEA]]: the counts $1, 2, 4, 7, 11$ show the pattern, and the case of the fourth line shows the reason.
2. [[The napkin ring problem by an extreme case|87VKHCKSDP]]: if the answer does not depend on the radius, the extreme case of a hole of width $0$ gives it at once.
3. Special values in an identity. Putting $x = 1$ in $(1 + x)^n = \sum_{k=0}^{n} \binom{n}{k} x^k$ gives $\sum_{k} \binom{n}{k} = 2^n$, and $x = -1$ gives $\sum_{k} (-1)^k \binom{n}{k} = 0$ for $n \ge 1$.
4. A special case that refutes. The claim "$(a + b)^2 = a^2 + b^2$ for all real $a, b$" fails at $a = b = 1$, where the two sides are $4$ and $2$.
5. A check by an extreme case. A formula for the area of a trapezium with parallel sides $a$ and $b$ and height $h$ must give the area of a triangle when $b = 0$; the formula $\frac{(a + b)h}{2}$ gives $\frac{ah}{2}$, as it should.

### Non-examples

1. [[Points on a circle: the pattern 1, 2, 4, 8, 16 breaks|WJ6XJD8V71]]: five special cases suggest the powers of $2$, and the sixth case gives $31$.
2. A special case used as a proof. Checking that $n^2 - n + 41$ is prime for $n = 1, 2, 3$ does not show that it is prime for all $n$; it fails at $n = 41$, where it is $41^2$.
3. An unrepresentative special case. Checking a claim about all triangles on an equilateral triangle tests only the most symmetric case, and many false claims hold there.

### Basic properties

1. If a universal statement fails in one special case, it is false. This is disproof by [[counterexample|0ED72CTBNP]].
2. If a statement holds in many special cases, it may still be false. Special cases give evidence, not proof.
3. A special case is most useful when it is simple enough to compute and general enough to show the structure. The page [[examples in mathematical practice|F3NNR77WKP]] calls such cases generic examples, and the cases at the edge extreme examples.
4. An extreme case can give the answer when the problem is known to have an answer that does not depend on the parameter, as in example 2. Without that knowledge, the extreme case is only a guess.

### Related methods

[[Reduction to a special case|DX2H7AD66G]] is a proof method: it proves the general statement from a special case by a transformation that keeps the truth of the statement.
Specialization as a heuristic needs no such transformation.
[[Generalization|8NJ0VN9Z97]] goes the other way, and the two are often used in turn.
[[Symmetry arguments|H840D9TM2X]] often choose the special case: the symmetric position is the first case to try.

### History

Pólya gave specialization an entry of its own in the heuristic dictionary of *How to Solve It* (1945), with generalization and analogy as its companions.
In *Mathematics and Plausible Reasoning* (1954) he treated the testing of conjectures by special cases as a main form of plausible reasoning.
Mason, Burton and Stacey's *Thinking Mathematically* (1982) put "specializing" and "generalizing" at the centre of their account of mathematical thinking.

### Common errors

1. To stop after the pattern and skip the proof, as in non-example 1.
2. To test only the cases that were used to form the conjecture. A test needs a new case.
3. To choose special cases that are too special, so that they hide the difficulty, as in non-example 3.

## Explanations

### L1 human

When a question is about every number, try it for $1$, $2$ and $3$ first.
For example: is the sum of three numbers in a row always divisible by $3$?
Try $1 + 2 + 3 = 6$, $2 + 3 + 4 = 9$, $5 + 6 + 7 = 18$: yes each time.
The small cases also show why: the sum is three times the middle number, as in $5 + 6 + 7 = 3 \cdot 6$.
And if a claim fails for one small case, it is false, and we can stop.

### L2 human

We find and prove the number of diagonals of a convex polygon with $n$ vertices.

1. Specialize: a triangle has $0$ diagonals, a quadrilateral $2$, a pentagon $5$, a hexagon $9$.
2. Look at the differences: $2, 3, 4$. They grow by $1$, so the count is quadratic in $n$.
3. Look at a case for the reason. In a hexagon, each vertex has a diagonal to each vertex except itself and its $2$ neighbours, so to $6 - 3 = 3$ vertices.
4. Generalize the reason: $n$ vertices, each with $n - 3$ diagonals, and each diagonal counted from both ends. So the count is $\frac{n(n - 3)}{2}$.
5. Test on the cases of step 1: $\frac{3 \cdot 0}{2} = 0$, $\frac{4 \cdot 1}{2} = 2$, $\frac{5 \cdot 2}{2} = 5$, $\frac{6 \cdot 3}{2} = 9$.

The typical use: the numbers give the form of the answer, and one special case, looked at closely, gives the argument.

A trap: step 2 alone could also fit other formulas; step 4 is the proof, and it uses no special value.

### L3 human

Specialization is the heuristic side of a basic logical fact: a universal statement implies each of its instances, so the instances are necessary conditions for it.
In research, the special cases of a conjecture are often the first theorems: a conjecture for all dimensions is proved first in low dimension, and a conjecture for all primes first for small primes.
The choice of a good special case is a skill of its own; a case that keeps the difficulty but removes the noise is sometimes called a leading special case.
Systematic computation of special cases is the basis of [[experimental mathematics|DME0TPC348]], where the dangers of small cases, such as the [[pattern of points on a circle|WJ6XJD8V71]], are studied as the strong law of small numbers.
