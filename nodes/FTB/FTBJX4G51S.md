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

Specialization means: when a question is about every case, try a few particular cases first.
Small cases, extreme cases and special values are easy to compute, and they show what the answer looks like and often why it is true.

Here is a question where this works at once.
What is the sum of the first $n$ odd numbers,
$$1 + 3 + 5 + \cdots + (2n - 1)?$$
Staring at the general sum gives nothing to hold on to, since we do not yet know what kind of formula to look for.
So we compute the first few cases:
$$1 = 1, \quad 1 + 3 = 4, \quad 1 + 3 + 5 = 9, \quad 1 + 3 + 5 + 7 = 16, \quad 1 + 3 + 5 + 7 + 9 = 25.$$
These are the squares $1^2, 2^2, 3^2, 4^2, 5^2$, so we guess that the sum is $n^2$.

The small cases also suggest the reason.
Draw $4 = 2^2$ as a $2 \times 2$ square of dots, and add $5$ dots along the right side and the top: they make a $3 \times 3$ square.
In general an $(n - 1) \times (n - 1)$ square plus an L-shaped border of $2n - 1$ dots is an $n \times n$ square, because
$$(n - 1)^2 + (2n - 1) = n^2 - 2n + 1 + 2n - 1 = n^2.$$
This identity is the step of a proof by [[mathematical induction|0ASJVEFA9J]], so the sum is $n^2$ for every $n \ge 1$.
Check: $n = 10$ gives $1 + 3 + \cdots + 19 = 100$.

In general, specialization passes from a problem about a whole class of objects to the same problem for a smaller class or a single member.
Special cases serve three purposes: to understand the problem, to find a pattern or a method, and to refute a general claim by a [[counterexample|0ED72CTBNP]].
One failing case refutes a universal claim, but no number of agreeing cases proves one.

## Motivation

A general problem has many parameters, and nobody can keep them all in mind at once.
A special case removes some of them and leaves a problem that you can do by hand.
The numbers show what the answer looks like, and the work on one case often shows a method that does not depend on the case.

The other direction is just as useful.
A general claim must hold in each special case, so a single failing case ends it.
Both uses are cheap, which is why experienced solvers try a special case before almost anything else.
Specialization is also the usual first move before a proof by induction, and it is the daily practice of [[experimental mathematics|BPEPTN0TT9]].

## Notation

Pólya's term is "specialization", and he listed it in the heuristic dictionary of *How to Solve It* with "generalization" and "analogy" beside it.
Mason, Burton and Stacey call the same move "specializing" and pair it with "generalizing".
A case that is simple to compute but still shows the structure is often called a generic example, and a case at the edge of the allowed range is an extreme case; [[examples in mathematical practice|F3NNR77WKP]] discusses both.
Do not confuse the heuristic with [[reduction to a special case|DX2H7AD66G]], a proof method that proves the general statement from a special case by a transformation.

## Remarks

### Small cases, extreme cases, special values

Small cases are the values $n = 0, 1, 2, 3, \ldots$ of a parameter, taken in order so that a pattern can show.
In [[regions cut out by lines in the plane|Z5GX4ECAEA]] the counts $1, 2, 4, 7, 11$ give the pattern, and a close look at the fourth line gives the reason.

An extreme case puts a parameter at the edge of its range.
In [[the napkin ring problem by an extreme case|87VKHCKSDP]] the radius of the ball is not given, so the answer cannot depend on it, and the smallest ball gives the volume at once.

Special values make an identity collapse.
Put $x = 1$ and then $x = -1$ in $(1 + x)^n = \sum_{k=0}^{n} \binom{n}{k} x^k$:
$$\sum_{k=0}^{n} \binom{n}{k} = 2^n, \qquad \sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0 \quad (n \ge 1).$$

### Special cases as tests

A special case is also the fastest check of a formula you already have.
A formula for the area of a trapezoid with parallel sides $a$ and $b$ and height $h$ must give a triangle when $b = 0$, and $\frac{(a + b)h}{2}$ gives $\frac{ah}{2}$, as it should.
A special case also refutes.
The claim "$(a + b)^2 = a^2 + b^2$ for all real $a, b$" fails at $a = b = 1$, where the sides are $4$ and $2$.

### When specialization misleads

The danger is to believe a pattern because it held in the cases you tried.
In [[points on a circle, the pattern 1, 2, 4, 8, 16 breaks|WJ6XJD8V71]], five cases suggest powers of $2$, and the sixth case gives $31$.
The polynomial $n^2 - n + 41$ is prime for $n = 1, 2, \ldots, 40$ and fails at $n = 41$, where it equals $41^2$.
More such cases are collected in [[patterns that eventually fail|A2KSJSQSF6]], and the [[strong law of small numbers|8AFXPXCE3N]] names the danger.

A case can also be too special.
A claim about all triangles that you check only on an equilateral triangle has passed the easiest test, since many false claims hold in the most symmetric case.
A good special case is simple enough to compute and general enough to keep the difficulty.

### Watch out

Three errors are common, and each has a fix.
The first is to stop at the pattern and skip the proof; the fix is to look in the special cases for a reason, as the L-shaped border did for the odd numbers.
The second is to test a conjecture only on the cases used to form it; the fix is to test a new case, such as $n = 6$ for the circle.
The third is to read an extreme case as a proof; it gives the answer only when you already know that the answer does not depend on the parameter.

### History

Pólya gave specialization its own entry in the heuristic dictionary of *How to Solve It* (1945).
In *Mathematics and Plausible Reasoning* (1954) he treated the testing of conjectures on special cases as a main pattern of [[plausible reasoning|8DHD3H1CJ9]].
Mason, Burton and Stacey's *Thinking Mathematically* (1982) put specializing and generalizing at the center of their account of mathematical thinking.

### Try it

First, is the sum of three consecutive integers always divisible by $3$?
Try $1 + 2 + 3 = 6$ and $5 + 6 + 7 = 18$; the second case shows the reason, since the sum is three times the middle number, $(m - 1) + m + (m + 1) = 3m$.

Second, test the claim "$2^n > n^2$ for every $n \ge 1$".
The case $n = 2$ gives $4 > 4$, which is false, and $n = 3$ gives $8 > 9$, also false, so the claim fails; it holds for $n = 1$ and for every $n \ge 5$.

## Explanations

### L1 human

When a question is about every number, try it for $1$, $2$ and $3$ first.
Add up odd numbers: $1$, then $1 + 3 = 4$, then $1 + 3 + 5 = 9$.
The answers $1$, $4$, $9$ are square numbers, so the guess is that the sum is always a square.
A picture shows why: a square of dots grows into the next square when you add an L-shaped border, and the border always has an odd number of dots.
And if a guess fails for even one small case, it is false, and you can stop.

### L2 human

We find and prove the number of diagonals of a convex polygon with $n$ vertices.
Specialize first: a triangle has $0$ diagonals, a quadrilateral $2$, a pentagon $5$ and a hexagon $9$.
The differences $2, 3, 4$ grow by $1$, so the count looks quadratic in $n$, but many quadratics could fit four values.

So look at one case for the reason.
In a hexagon, each vertex has a diagonal to every vertex except itself and its $2$ neighbors, that is, to $6 - 3 = 3$ vertices.
The same holds for $n$ vertices, and each diagonal is counted from both ends, so the count is
$$\frac{n(n - 3)}{2}.$$
Check on the cases: $\frac{3 \cdot 0}{2} = 0$, $\frac{4 \cdot 1}{2} = 2$, $\frac{5 \cdot 2}{2} = 5$ and $\frac{6 \cdot 3}{2} = 9$.

This is the typical use: the numbers give the form of the answer, and one special case, read closely, gives an argument with no special values in it.
Watch out: the differences alone are not a proof, and the counting argument is.

### L3 human

Specialization is the heuristic side of a logical fact: a universal statement implies each of its instances, so the instances are necessary conditions for it.
In research, the special cases of a conjecture are often the first theorems, such as a conjecture for all dimensions proved first in low dimension.
Choosing a case that keeps the difficulty and removes the noise is a skill of its own.

[[Generalization|8NJ0VN9Z97]] goes the other way, and solvers often use the two in turn: specialize to find a pattern, generalize to see the structure.
[[Symmetry arguments|H840D9TM2X]] often choose the special case, since the symmetric position is the first one to try.
The systematic computation of special cases is the subject of [[plausible reasoning and experimental mathematics|DME0TPC348]].
