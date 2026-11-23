---
tag: DYSJB93V11
kind: concept
name: Auxiliary problem
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, KCK4AQ469Q]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

An auxiliary problem is a second problem that you solve, not for its own sake, but because its answer helps with the problem you were given.
When the given problem resists every method you know, a related problem in a better form may fit one of them.

Here is a small case of the move.
How many triples $(x, y, z)$ of nonnegative integers satisfy $x + y + z = 10$?
A first attempt sorts the triples by the value of $x$.
When $x = k$, the pair $(y, z)$ solves $y + z = 10 - k$, and that equation has $11 - k$ solutions, so the count is
$$11 + 10 + 9 + \dots + 1 = 66.$$
The attempt works, but it does not scale: with four unknowns the same idea gives a double sum, and with ten unknowns it is hopeless.
The helping move is to change the question.
Write a triple as a row of $10$ stars and $2$ bars, with $x$ stars before the first bar, $y$ stars between the bars and $z$ stars after the second bar.
Each row gives one triple and each triple gives one row, so the given problem is equivalent to the auxiliary problem "choose $2$ places for the bars among $12$ places":
$$\binom{12}{2} = \frac{12 \cdot 11}{2} = 66.$$
The [[full example|5DKC774S00]] writes out the bijection.

An auxiliary problem can be a special case, a more general problem, an analogous problem, a part of the problem, or the same problem in another form.
It is a [[heuristic|6KCEWEP4WA]]: a piece of advice that says where to look, not a procedure that is sure to find the detour.

## Motivation

Many problems have no method that fits them as they are stated.
A change of form can make a known method fit.
A quartic equation in $x^2$ is a quadratic equation in disguise, a count with conditions becomes a count of subsets after a bijection, and a geometry problem becomes algebra in coordinates.
The skill is to look for such a detour on purpose, and to know what its answer is worth when you come back.

The value of the answer depends on how the two problems are related.
If they are equivalent, the answer of the auxiliary problem is the answer you want.
If the auxiliary problem is stronger, its solution solves the given problem, but it may be harder or even false.
If it is weaker, its solution gives only candidates or a bound.
The [[inventor's paradox|FVRKDXBJF6]] studies the case of a stronger problem that turns out to be easier, and [[variation of the problem|KT5SASGTQ5]] lists the ways to change a problem into another one.

## Notation

Pólya's word is "auxiliary problem", and he calls the passage between two equivalent problems a "bilateral reduction".
A passage that works in one direction only is a "unilateral reduction", toward a problem that is "more ambitious" or "less ambitious" than the given one.
If $P$ is the given statement and $Q$ the auxiliary one, a bilateral reduction means $P \Leftrightarrow Q$.
A unilateral reduction means $Q \Rightarrow P$, a [[stronger statement|KCK4AQ469Q]], or $P \Rightarrow Q$, a weaker one.
Other books speak of reformulation, transformation or reduction of a problem.

## Remarks

### Three detours that work

In the equation $x^4 - 13x^2 + 36 = 0$ the unknown appears only through $x^2$.
Put $y = x^2$, and the [[auxiliary equation|SCV1PRX55T]] $y^2 - 13y + 36 = 0$ gives $y = 4$ or $y = 9$, so $x \in \{-3, -2, 2, 3\}$.
The reduction is bilateral, provided you remember that $y = x^2$ cannot be negative.

To find the distance from the point $(3, 4)$ to the circle $x^2 + y^2 = 1$, solve first the auxiliary problem of the distance to the center.
That distance is $\sqrt{9 + 16} = 5$, and the nearest point of the circle lies on the segment to the center, so the answer is $5 - 1 = 4$.

To prove that $30$ divides $n^5 - n$ for every integer $n$, prove three auxiliary statements: $2$, $3$ and $5$ divide it.
Because $2$, $3$ and $5$ are pairwise coprime, the three statements together are equivalent to the given one.
The L2 explanation below carries this out, and [[decomposing and recombining|KEZPDNM2NH]] treats such splits in general.

### What the answer is worth

The detour is only half the work, because you must come back.
An equivalent problem returns the exact answer.
A stronger problem returns a proof when you can solve it, and nothing when it is false.
A weaker problem returns a necessary condition, and every candidate it gives must be checked against the original conditions.
A substitution $y = g(x)$ gives an equivalent problem only for values of $y$ in the range of $g$, so roots outside the range must be dropped.

### When the detour misleads

The common failure is to treat a weaker problem as if it were equivalent.
An integer program asks for integer points, and its [[linear programming relaxation|R09YNAR948]] drops that condition.
The relaxation is easier, but rounding its optimum can give a point that breaks a constraint, so the relaxation yields a bound and not an answer.

A smaller case of the same error: solve $x^2 = 3x$ by dividing by $x$ to get $x = 3$.
The auxiliary equation $x = 3$ is not equivalent to the given one, because division by $x$ needs $x \ne 0$, and the solution $x = 0$ is lost.

A detour can also lead to a harder problem with no answer in view.
Replacing "is $2^{31} - 1$ prime?" by "find all primes of the form $2^p - 1$" is a more ambitious problem that is still open.

### Watch out

Do not forget the return step.
The auxiliary equation $y^2 - 13y + 36 = 0$ has the solutions $y = 4$ and $y = 9$, but the question asked for $x$, and the answer has four values.
Do not forget the range of the new unknown either.
For $x^4 + 3x^2 - 4 = 0$, the auxiliary equation $y^2 + 3y - 4 = 0$ has the roots $1$ and $-4$, and only $y = 1$ comes from a real $x$, so the real solutions are $x = \pm 1$.

### Related heuristics

[[Specialization|FTBJX4G51S]] and [[generalization|8NJ0VN9Z97]] produce auxiliary problems that are weaker or stronger than the given one.
[[Analogy|7KDT0R1HF2]] produces an auxiliary problem of the same form in another setting.
[[Auxiliary elements|8TKKRAXKFN]] are the new objects, such as the unknown $y = x^2$, that an auxiliary problem brings in.
[[Reduction to a special case|DX2H7AD66G]] is the proof pattern in which a special case is equivalent to the general one.

### History

Pólya gave "auxiliary problem" an entry in the dictionary part of *How to Solve It* (1945), and there he separated bilateral from unilateral reduction.
The idea is much older: the Greek method of analysis, as Pappus described it, reduces a problem step by step to problems that are already solved, as in [[working backwards|3QTB9S1THS]].

### Try it

Find the real solutions of $x^6 - 9x^3 + 8 = 0$.
Put $y = x^3$, so $y^2 - 9y + 8 = (y - 1)(y - 8) = 0$ and $y \in \{1, 8\}$; then $x = 1$ or $x = 2$, since a real number has exactly one real cube root.

How many solutions in positive integers has $a + b + c + d = 10$?
Put $a = a' + 1$ and the same for the others, so that $a' + b' + c' + d' = 6$ in nonnegative integers, and stars and bars gives $\binom{9}{3} = 84$.

## Explanations

### L1 human

Sometimes a problem is hard as it is asked, but a related problem is easy.
How far is the point $(3, 4)$ from the circle of radius $1$ around the origin?
That is a new kind of question, but "how far is $(3, 4)$ from the origin?" is easy: the answer is $5$, by the Pythagorean theorem.
The nearest point of the circle is on the way to the origin, so the answer is $5 - 1 = 4$.
We solved an easier problem first and then used its answer.

### L2 human

We prove that $30$ divides $n^5 - n$ for every integer $n$, through three auxiliary problems.
Since $30 = 2 \cdot 3 \cdot 5$ and the factors are pairwise coprime, $30$ divides a number exactly when $2$, $3$ and $5$ all divide it.
So the given problem is equivalent to three smaller ones.
Factor first:
$$n^5 - n = n(n^4 - 1) = (n - 1)\, n\, (n + 1)(n^2 + 1).$$
The product $(n - 1)n$ of two consecutive integers is even, and the product $(n - 1)n(n + 1)$ of three consecutive integers is a multiple of $3$.
For $5$, look at the remainder of $n$.
If $n \equiv 0, 1$ or $4 \pmod 5$, then one of $n$, $n - 1$, $n + 1$ is a multiple of $5$.
If $n \equiv 2$ or $3 \pmod 5$, then $n^2 + 1 \equiv 5$ or $10$, and both are $0 \pmod 5$.
So all three auxiliary statements hold, and $30$ divides $n^5 - n$.

Check: for $n = 2$, $n^5 - n = 30$.
The split works only because the factors are coprime.
Divisibility by $2$ and by $4$ does not give divisibility by $8$, as the number $4$ shows.

### L3 human

The auxiliary problem is the informal side of reduction, which is exact in other parts of mathematics.
In computability and complexity theory, a reduction of a problem $A$ to a problem $B$ transforms instances so that a solver for $B$ gives a solver for $A$, and NP-completeness is defined this way.
In number theory, an equation over $\mathbb{Z}$ is often studied through its images modulo primes or over the $p$-adic numbers, which are weaker auxiliary problems, and a local-global principle says when they are together equivalent to the original.
In optimization, a relaxation is a unilateral reduction that gives a bound, and the dual problem is a second auxiliary problem that bounds the value from the other side.
The sub-area on [[plausible reasoning and experimental mathematics|DME0TPC348]] continues with the evidence that such detours give.
