---
tag: 0EFYCFHYFG
kind: concept
name: Proof by infinite descent
aliases: [infinite-descent, method-of-descent]
msc: ["11D99", "00A35"]
topics: [G9JFJGY4TQ, EEH2F76CYQ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [01BX15HSRR, JGRCNPKNGG, 0J0XBKG64S, 08B1RTW7VZ]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: Number theory
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: Application examples
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Infinite descent
same_as:
  wikidata: Q619388
  wikipedia: Proof by infinite descent
---

## Summary

Infinite descent proves that something cannot exist, because each example of it would give a smaller example, without end.
Let $S$ be a set of objects, and give each object $x$ a size $s(x)$ in the [[natural numbers|0MWKJ44V5A]].
The proof shows that for each $x$ in $S$ there is a $y$ in $S$ with $s(y) < s(x)$.
An element $x_0$ of $S$ would then give elements $x_1, x_2, \ldots$ of $S$ with $s(x_0) > s(x_1) > s(x_2) > \cdots$.
That is an infinite strictly decreasing sequence of natural numbers, and the [[well-ordering principle|01BX15HSRR]] rules it out, so $S$ is empty.
The method is a main tool to show that a [[Diophantine equation|08B1RTW7VZ]] has no solution in positive integers.

## Motivation

To show that an equation has no solution, we cannot test all candidates, because there are infinitely many.
A descent finds a rule that turns each solution into a smaller solution.
A single solution would then start an endless chain of smaller and smaller positive integers.
The positive integers do not allow such a chain, so there is no solution at all.
The rule often comes from divisibility: if a prime divides every entry of a solution, we divide the solution by that prime.

## Notation

The size is usually one entry of the solution, such as $z$ or the denominator $b$, or a sum such as $|x| + |y| + |z|$.
Fermat's French name for the method is *descente infinie*, and books also say "the method of descent" or "Fermat's method of descent".
In the theory of elliptic curves the word "descent" has a wider, technical meaning, and the Mordell-Weil theorem uses that meaning.

## Remarks

### A first proof by descent

Here is a short theorem that the method proves: $\sqrt{2}$ is not a quotient of two positive integers.
Suppose that $\sqrt{2} = a/b$ with positive integers $a$ and $b$, so that $a^2 = 2b^2$.
Let $S$ be the set of such pairs $(a, b)$, and let the size of a pair be $b$.
From $b^2 < 2b^2 = a^2 < 4b^2$ we get $b < a < 2b$.
Put $a' = 2b - a$ and $b' = a - b$.
The bounds give $a' > 0$ and $0 < b' < b$.
Expand: $a'^2 - 2b'^2 = (4b^2 - 4ab + a^2) - (2a^2 - 4ab + 2b^2) = 2b^2 - a^2 = 0$.
So $(a', b')$ is again in $S$, and its size is smaller.
By descent $S$ is empty, which proves the [[irrationality of the square root of 2|0DZGSDHD92]].

Check: the map turns $a^2 - 2b^2$ into $-(a^2 - 2b^2)$.
For $(7, 5)$ we have $49 - 50 = -1$, and the map gives $(3, 2)$ with $9 - 8 = 1$.
A pair with value $0$ goes to a pair with value $0$, which is what the proof needs.

### Why the method is valid

The method needs one fact: there is no infinite strictly decreasing sequence $a_0 > a_1 > a_2 > \cdots$ of natural numbers.
Suppose there were one.
Its set of terms is nonempty, so it has a least element $a_k$ by the [[well-ordering principle|01BX15HSRR]].
But $a_{k+1}$ is also a term, and $a_{k+1} < a_k$, which is impossible.

The fact holds for $\mathbb{N}$ and fails for $\mathbb{Z}$ and for the positive rationals.
So every descent must stay inside $\mathbb{N}$: the sizes must be natural numbers, and each new object must again lie in $S$.

A second form takes an $x$ in $S$ of least size and builds a $y$ in $S$ of smaller size, a contradiction in one step.
This is the [[minimal counterexample|JGRCNPKNGG]] method, in which the counterexamples are the solutions.
Both forms are [[strong induction|0KMVFSHFGZ]] applied to the property "no element of $S$ has size $n$".

### When to choose it

Choose descent to prove that something does not exist, when each example of it contains a smaller one.
The commonest case is an equation in which a prime must divide every entry of a solution.
[[The equation x² + y² = 3z²|SWDMY3XJKF]] forces $3$ to divide $x$, $y$ and $z$, and [[the equation x³ + 2y³ + 4z³ = 0|TTMCPREC0F]] forces $2$ to divide all three.
Division by the prime then gives a smaller solution.

Some descents build the smaller object by a cleverer rule.
[[Fermat's right triangle theorem|086BE0J3FZ]] says that no right triangle with integer sides has a square area.
Its [[proof by descent|8195EFVX2N]] builds a smaller such triangle from each one, and it gives [[Fermat's Last Theorem for n = 4|0E741HSMJ1]].
In [[Lagrange's four-square theorem|0KYYSMEVHH]], the [[proof by descent|GBQDYYA8SE]] starts from a multiple $mp$ of a prime $p$ that is a sum of four squares, and lowers $m$ until $m = 1$.
That descent shows existence, and a descent that also bounds its number of steps is an algorithm.

Descent also proves facts outside number equations.
[[Every integer at least 2 has a prime divisor|VSHHBWWXVX]], because a number with no prime divisor would have a smaller factor with no prime divisor.

### How it fails

A descent fails when the new object leaves $S$.
In [[the pairs with x = 2y|3VFY8XCBEQ]], the map $(x, y) \mapsto (y, y/2)$ gives smaller pairs, but $y/2$ is not an integer when $y$ is odd.
The chain stops, and indeed the equation has solutions such as $(2, 1)$.

A descent fails when the sizes are not natural numbers.
The chain $0 > -1 > -2 > \cdots$ in $\mathbb{Z}$ and the chain $1 > \tfrac12 > \tfrac14 > \cdots$ in the positive rationals are infinite and decreasing.
So "each $x$ gives a smaller $y$" proves nothing for sizes in $\mathbb{Z}$ or $\mathbb{Q}$.

A descent fails when the size does not drop strictly.
A chain of equal sizes can go on forever.

### Descent beyond the natural numbers

The method works for sizes in any set with a [[well-founded relation|0DQPNJNPYK]], since such a relation also has no infinite decreasing chain.
Pairs of natural numbers in the lexicographic order are an example.
The chain $(2, 0) > (1, 100) > (1, 99) > \cdots > (1, 0) > (0, 5) > \cdots$ can be long, but it always ends.
A proof that a program stops is often a descent of this kind, on a measure that drops at each step of the program.

### Watch out

Check both conditions for the new object, every time.
It must lie in $S$, which for an equation means that it solves the equation with positive integer entries.
Its size must be strictly smaller.
In the $\sqrt{2}$ proof, the bounds $b < a < 2b$ are what make $2b - a$ and $a - b$ positive, so a proof that skips them has a gap.
Also choose $S$ with care.
For $x^2 + y^2 = 3z^2$, the triple $(0, 0, 0)$ divided by $3$ is itself, so its size does not drop, and $S$ must leave it out.

### History

Euclid's *Elements*, Book VII, Proposition 31, proves that each composite number has a prime divisor by an argument of descent.
Fermat developed the method, named it *descente infinie*, and used it for Diophantine problems, for example to prove his right triangle theorem.
In the twentieth century the [[Mordell-Weil theorem|MXRCPAH09H]] used a descent argument for the rational points of an elliptic curve, and Weil extended it to abelian varieties.

### Try it

First, show that $x^2 = 3y^2$ has no solution in positive integers.
From $3 \mid x^2$ we get $3 \mid x$, so $x = 3u$ and $9u^2 = 3y^2$, which gives $y^2 = 3u^2$.
So $(y, u)$ is a new solution, and $y < x$ because $y^2 = x^2 / 3$.

Second, find the error: "Each positive rational $q$ gives a smaller positive rational $q/2$, so by descent there is no positive rational."
The sizes are rationals and not natural numbers, so the chain $q > q/2 > q/4 > \cdots$ is allowed and there is no contradiction.

## Explanations

### L1 human

Think of a staircase that starts at some floor and goes down, one or more steps at a time.
It must reach the ground floor after finitely many steps, because there are only finitely many floors below.
A descent proof shows that every solution of a puzzle leads to a smaller solution, so the solutions would give a staircase with no bottom.
Such a staircase does not exist, so the puzzle has no solution.
For example, if $x^2 + y^2 = 3z^2$ had a solution in positive whole numbers, then all three numbers would be multiples of $3$.
Dividing them by $3$ would give a smaller solution, and so on forever.

### L2 human

We prove by descent that $x^2 + y^2 = 3z^2$ has no solution in integers other than $(0, 0, 0)$.
Let $S$ be the set of integer solutions that are not all zero, with size $|x| + |y| + |z|$, a positive natural number.
A square leaves the remainder $0$ or $1$ on division by $3$, so $x^2 + y^2$ is a multiple of $3$ only when $x^2$ and $y^2$ both are.
So $3$ divides $x$ and $y$, and then $9$ divides $3z^2$, so $3$ divides $z^2$ and $z$.
The triple $(x/3, y/3, z/3)$ is again an integer solution, it is not all zero, and its size is one third of the old size.
So each element of $S$ gives a smaller one, and $S$ is empty.
Check the remainders: $0^2 = 0$, $1^2 = 1$ and $2^2 = 4 = 3 + 1$.

The typical use of descent is an equation whose solutions are all divisible by a fixed number, or a figure that contains a smaller copy of itself.
Watch out: the new triple must again be a nonzero integer solution, and here the division by $3$ is exact because of the remainder argument.

### L3 human

Infinite descent is the statement that the order of $\mathbb{N}$ is well-founded, used as a proof rule.
In this form it extends to every [[well-founded relation|0DQPNJNPYK]], and it is the same principle as well-founded induction, seen in the contrapositive.
In number theory, descent became a structural method.
For an elliptic curve $E$ over $\mathbb{Q}$, a height function plays the role of the size.
The finiteness of $E(\mathbb{Q})/2E(\mathbb{Q})$, together with descent on the height, gives the [[Mordell-Weil theorem|MXRCPAH09H]].
In logic, a proof that a process stops by a measure that drops in a well-ordered set is a descent argument.
Gentzen's consistency proof of arithmetic uses a descent along the ordinals below $\varepsilon_0$.
The [[equivalence of induction and well-ordering|J2P9FWBP3Q]] gives the exact link between descent and induction over $\mathbb{N}$.
