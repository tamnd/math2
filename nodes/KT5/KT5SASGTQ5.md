---
tag: KT5SASGTQ5
kind: concept
name: Variation of the problem
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, 0RVYE75E2M]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

When a problem does not move, change it a little: drop part of the condition, change the data, change the unknown, or turn the statement around.
The changed problem is easier or more revealing, and what it teaches you is then carried back to the problem you were given.

Here is a small problem that yields to one change.
Find the least positive integer that leaves remainder $1$ when divided by $2$, $3$, $4$, $5$ and $6$, and is divisible by $7$.
A first attempt walks through the multiples of $7$, namely $7, 14, 21, \dots$, and tests each one against five divisions; it works, but slowly, and it shows no structure.
The helping move is to drop the last condition for a moment.
Without it, the number $n$ just needs $n - 1$ to be a multiple of $2$, $3$, $4$, $5$ and $6$, that is, of their least common multiple $60$, so the weaker problem has the family of solutions
$$n = 60k + 1 = 1, 61, 121, 181, 241, 301, \dots$$
Now restore the dropped condition.
Since $60 = 8 \cdot 7 + 4$, we need $4k + 1 \equiv 0 \pmod 7$, so $k \equiv 5 \pmod 7$, and the least answer is $n = 301 = 7 \cdot 43$.
The [[full example|57YGZR5YNR]] checks each step.

The changes can touch the unknown, the data or the condition, and forming the [[converse|0RVYE75E2M]] is one of them.
[[Specialization|FTBJX4G51S]], [[generalization|8NJ0VN9Z97]] and [[analogy|7KDT0R1HF2]] are special kinds of variation.
Variation is a [[heuristic|6KCEWEP4WA]]: it keeps you moving, but it does not say which change will help, and a changed problem can be harder or unrelated.

## Motivation

A problem that is stuck stays stuck as long as you look at it in the same form.
A small change can make a known method fit, or show how the unknown depends on the data.
When you drop one condition, the unknown is no longer fixed, and you can watch how it varies.
The solutions of the weaker problem often form a simple family, a progression or a line, and the dropped condition then picks the answer out of the family.
That is the pattern of the opening problem, and it is also the classical way to solve a construction problem as the intersection of two loci.

Variation also feeds research.
After a theorem is proved, its converse, its generalizations and its versions with weaker hypotheses are the natural next questions, and [[problem posing|Y896GWYF8A]] turns such changes into a method for asking new questions.

## Notation

Pólya's term is "variation of the problem", and his questions include keeping only a part of the condition and changing the unknown or the data so that they come nearer to each other.
Other books speak of relaxing a constraint, perturbing the data, or reformulating.
A variation used as a step is an [[auxiliary problem|DYSJB93V11]], and the [[contrapositive|04T1CT7212]] is not a variation at all, since it is equivalent to the original statement.

## Remarks

### Dropping a condition in a construction

Pólya's own example is to inscribe a square in a triangle $ABC$, with two vertices on $BC$ and one on each other side.
Four conditions at once are hard, so drop the condition that the fourth vertex lies on $CA$.
The squares that meet the other three conditions all come from one of them by a homothety with center $B$, so their free vertices run along a ray from $B$.
The ray meets $CA$ in the vertex you want, and the [[full example|5C38AKJ4N1]] works it with numbers.

### Changing the unknown

To find the space diagonal of a box with edges $a$, $b$ and $c$, first change the unknown to the diagonal of a face, $\sqrt{a^2 + b^2}$.
The space diagonal is the hypotenuse of a right triangle with legs $\sqrt{a^2 + b^2}$ and $c$, so it is
$$\sqrt{a^2 + b^2 + c^2},$$
as in [[the diagonal of a rectangular box|FGMDA7TF3Q]].
The new unknown lies between the data and the old unknown, which is why it helps.

### Turning a statement around

The [[Pythagorean theorem|0VP3A1290K]] says that a right angle at $C$ gives $a^2 + b^2 = c^2$.
Its converse, that $a^2 + b^2 = c^2$ gives a right angle at $C$, is also true, and Euclid proved it separately as Proposition 48 of Book I.
Changing a number gives a third question: $a^2 + b^2 = c^2$ has infinitely many solutions in positive integers, but $a^3 + b^3 = c^3$ has none, by the case $n = 3$ of [[Fermat's Last Theorem|0Y5X3SDBCZ]].

### When a variation misleads

A variation raises a question, and it does not answer it.
The converse of [[Fermat's little theorem|ZHMHBFQ2E4]] holds for $n = 3, 5, 7, 11, 13$, and a student may take it as a primality test.
It is false: $341 = 11 \cdot 31$ is composite, yet $2^{340} \equiv 1 \pmod{341}$.

The other common failure is to forget the way back.
Asked for all real solutions of $x^3 = x$, a solver who changes the task to "find a solution" and reports $x = 0$ has answered a different question, since the solutions are $-1$, $0$ and $1$.
A variation so large that it shares neither data nor unknown with the original gives nothing to carry back.

### What each change gives you

Dropping a condition gives a weaker problem, whose solutions include those of the original, so its answers must be checked against the dropped condition.
Adding a condition gives a stronger problem, and any solution of it solves the original.
The converse of a true statement is a new statement, which may be true, as for the Pythagorean theorem, or false, as for Fermat's little theorem.

### Watch out

Change one thing at a time.
If you vary the data and drop a condition at once and the new problem is easy, you will not know which change helped, and you cannot carry the answer back.
And restore what you dropped: if the line in a locus problem misses the family of solutions, the original problem has no solution, which is also an answer.

### History

Pólya gave "variation of the problem" an entry in the dictionary part of *How to Solve It* (1945).
Euclid already proved converses as separate propositions, as with Propositions 47 and 48 of Book I.
Brown and Walter built systematic variation into a method for posing problems, the "what if not" strategy, in *The Art of Problem Posing* (1983).

### Try it

Find the least positive integer that leaves remainder $2$ on division by $3$, $4$ and $5$, and is divisible by $7$.
Dropping the last condition gives $n = 60k + 2$, and $4k + 2 \equiv 0 \pmod 7$ gives $k \equiv 3$, so $n = 182 = 7 \cdot 26$.

State the converse of "if $4$ divides $n$, then $n$ is even", and decide whether it is true.
The converse says "if $n$ is even, then $4$ divides $n$", and $n = 2$ refutes it.

## Explanations

### L1 human

When a puzzle is too hard, change it a little and try again.
You might ignore one of its rules for a moment, try smaller numbers, or ask the question backwards.
The changed puzzle is often easier, and solving it shows how the real puzzle works.
Then put the ignored rule back, or return to the real numbers.
The answer to the changed puzzle is only a step, and you must still answer the puzzle you were given.

### L2 human

We look for a point $X$ on the line $y = 3$ at distance $5$ from $O = (0, 0)$ and at distance $5$ from $A = (8, 0)$.
First drop the condition that $X$ lies on the line.
The points at distance $5$ from both $O$ and $A$ lie on the perpendicular bisector $x = 4$ of $OA$, and
$$4^2 + y^2 = 25 \implies y = \pm 3,$$
so the weaker problem has the solutions $(4, 3)$ and $(4, -3)$.
Now restore the condition: only $(4, 3)$ lies on $y = 3$.
Check: the distance from $(4, 3)$ to $O$ and to $A$ is $\sqrt{16 + 9} = 5$.

Each condition is a locus, a dropped condition leaves a simpler locus, and the answer is an intersection.
The weaker problem can have solutions when the original has none.
On the line $y = 4$ the same family gives no point, and the original problem has no solution.

### L3 human

Systematic variation is a working method of research.
A theorem is tested by weakening each hypothesis in turn and looking for a counterexample, which shows which hypotheses are needed.
Inverse problems arise by exchanging the data and the unknown, as when a shape is recovered from measurements of a solution.
Deformation theory studies an object as a member of a family and asks how it changes as a parameter moves.
Homotopy continuation in numerical algebraic geometry solves a polynomial system by deforming an easy system into the given one and following the solutions along the path.
All of these are precise forms of the advice to change the problem and watch how the unknown moves.
