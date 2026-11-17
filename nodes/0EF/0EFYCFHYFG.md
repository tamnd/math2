---
tag: 0EFYCFHYFG
kind: concept
name: Proof by infinite descent
aliases: [infinite-descent, method-of-descent]
msc: ["11D99", "00A35"]
topics: [G9JFJGY4TQ, EEH2F76CYQ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [01BX15HSRR, ~f8c099da, 0J0XBKG64S, 08B1RTW7VZ]
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

A proof by infinite descent shows that a set $S$ of objects is empty, where each object $x$ has a size $s(x)$ in the [[natural numbers|0MWKJ44V5A]].
The proof shows one thing: for each $x$ in $S$ there is a $y$ in $S$ with $s(y) < s(x)$.
If $S$ had an element $x_0$, this would give elements $x_1, x_2, \ldots$ of $S$ with $s(x_0) > s(x_1) > s(x_2) > \cdots$, an infinite strictly decreasing sequence of natural numbers.
No such sequence exists, by the [[well-ordering principle|01BX15HSRR]], so $S$ is empty.
The method matters because it proves impossibility results, above all that a [[Diophantine equation|08B1RTW7VZ]] has no solution in positive integers.

## Motivation

To show that an equation has no solution, we cannot test all candidates, because there are infinitely many.
A descent finds a rule that turns each solution into a smaller solution.
A single solution would then start an endless chain of smaller and smaller positive integers.
The positive integers do not allow such a chain, so there is no solution at all.
The rule is often found with divisibility: if a prime divides every term of a solution, we divide the solution by that prime.

## Notation

1. The size is usually one entry of the solution, such as $z$ or the denominator $b$, or a sum such as $|x| + |y| + |z|$.
2. Fermat's French name is *descente infinie*. Books also write "the method of descent" or "Fermat's method of descent".
3. In the theory of elliptic curves the word "descent" has a wider, technical meaning, and the Mordell-Weil theorem uses that meaning.

## Remarks

### The steps of the method

1. Name the set $S$ that should be empty, for example the set of positive integer solutions of an equation.
2. Choose a size $s \colon S \to \mathbb{N}$.
3. Take an arbitrary $x$ in $S$, and build a $y$ from $x$.
4. Check that $y$ is again in $S$: it satisfies the equation, and its entries are again positive integers.
5. Check that $s(y) < s(x)$.
6. Conclude that $S$ is empty.

The minimal form replaces steps 3 to 6 by one contradiction: take $x$ in $S$ with the least size, and build $y$ in $S$ with $s(y) < s(x)$.
This minimal form is the [[minimal counterexample|~f8c099da]] method, in which the counterexamples are the solutions.

### Examples

1. The [[irrationality of the square root of 2|0DZGSDHD92]]: a solution of $a^2 = 2 b^2$ in positive integers gives the smaller solution $(2b - a, a - b)$.
2. [[The equation x² + y² = 3z² has only the zero solution|~1b04b102]]: $3$ divides $x$, $y$ and $z$, so $(x/3, y/3, z/3)$ is a smaller solution.
3. [[The equation x³ + 2y³ + 4z³ = 0 has only the zero solution|~40e4e331]]: $2$ divides $x$, $y$ and $z$, so $(x/2, y/2, z/2)$ is a smaller solution.
4. [[Fermat's right triangle theorem|086BE0J3FZ]]: no right triangle with integer sides has a square area. Its [[proof by descent|8195EFVX2N]] builds a smaller such triangle from each one, and it gives [[Fermat's Last Theorem for n = 4|0E741HSMJ1]].
5. [[Lagrange's four-square theorem|0KYYSMEVHH]]: its [[proof by descent|GBQDYYA8SE]] lowers the multiple $m p$ of a prime $p$ that is a sum of four squares until $m = 1$.
6. [[Every integer at least 2 has a prime divisor|~f5eefa58]]: a number with no prime divisor has a smaller factor with no prime divisor.

### Non-examples

1. [[The pairs with x = 2y do not descend|~e4645793]]: the map $(x, y) \mapsto (y, y/2)$ makes smaller pairs, but it leaves the positive integers, so step 4 fails. The equation does have solutions.
2. A chain in $\mathbb{Z}$ such as $0 > -1 > -2 > \cdots$ is infinite and decreasing. A descent with sizes in $\mathbb{Z}$ proves nothing, because step 2 needs sizes in $\mathbb{N}$.
3. A chain in the positive rationals such as $1 > \tfrac12 > \tfrac14 > \cdots$ is also infinite and decreasing. Sizes in $\mathbb{Q}$ fail for the same reason.

### Basic properties

1. There is no infinite strictly decreasing sequence $a_0 > a_1 > a_2 > \cdots$ of natural numbers. Proof: the set $\{a_0, a_1, a_2, \ldots\}$ is not empty, so it has a least element $a_k$ by the [[well-ordering principle|01BX15HSRR]]; but $a_{k+1}$ is in the set and $a_{k+1} < a_k$.
2. Property 1 is the only fact that the method needs, so the method is valid.
3. The descent form and the minimal form prove the same statements. Each is a form of [[strong induction|0KMVFSHFGZ]] applied to the property "no element of $S$ has size $n$".
4. The method works with any size in a set with a [[well-founded relation|0DQPNJNPYK]], for example pairs of natural numbers in the lexicographic order.
5. A descent proof that also bounds the number of steps is an algorithm. The Euclidean algorithm and the proof of Lagrange's four-square theorem are of this kind.

### History

Euclid's *Elements*, Book VII, Proposition 31, proves that each composite number has a prime divisor by an argument of descent.
Fermat developed the method, named it *descente infinie*, and used it for Diophantine problems, for example to prove his right triangle theorem.
In the twentieth century the [[Mordell-Weil theorem|MXRCPAH09H]] used a descent argument for the rational points of an elliptic curve, and Weil extended it to abelian varieties.

### Common errors

1. The new object is not checked to lie in $S$. If it is not a positive integer solution, the chain stops and there is no contradiction.
2. The size does not decrease strictly. A chain of equal sizes can go on forever.
3. The size takes values in $\mathbb{Z}$ or $\mathbb{Q}$. Then infinite decreasing chains exist, and the argument proves nothing.

## Explanations

### L1 human

Think of a staircase that starts at some floor and goes down, one or more steps at a time.
It must reach the ground floor after finitely many steps, because there are only finitely many floors below.
A descent proof shows that every solution of a puzzle leads to a smaller solution, so the solutions would give a staircase with no bottom.
Such a staircase does not exist, so the puzzle has no solution.
For example, if $x^2 + y^2 = 3 z^2$ had a solution in positive whole numbers, then all three numbers would be multiples of $3$, and dividing by $3$ would give a smaller solution.

### L2 human

We prove by descent that $\sqrt{2}$ is irrational.

1. Suppose that $\sqrt{2} = a/b$ with positive integers $a$ and $b$. Then $a^2 = 2 b^2$.
2. Let $S$ be the set of pairs $(a, b)$ of positive integers with $a^2 = 2 b^2$, and let the size be $b$.
3. From $b^2 < 2 b^2 = a^2 < 4 b^2$ we get $b < a < 2b$.
4. Let $a' = 2b - a$ and $b' = a - b$. By step 3, $a' > 0$ and $b' > 0$, and $b' < b$ because $a < 2b$.
5. We check the equation: $a'^2 - 2 b'^2 = 4b^2 - 4ab + a^2 - 2a^2 + 4ab - 2b^2 = 2b^2 - a^2 = 0$.
6. So $(a', b')$ is in $S$, and its size $b'$ is less than $b$.
7. By the method, $S$ is empty, and $\sqrt{2}$ is not a quotient of positive integers.

The typical use of descent is an equation whose solutions are all divisible by a fixed number, or a geometric figure that contains a smaller copy of itself.
A trap is step 4: the new pair must again consist of positive integers, and this needs the bounds of step 3.

### L3 human

Infinite descent is the statement that the order of $\mathbb{N}$ is well-founded, used as a proof rule.
In this form it extends to every [[well-founded relation|0DQPNJNPYK]], and it is the same principle as well-founded induction.
In number theory, descent became a structural method: for an elliptic curve $E$ over $\mathbb{Q}$, a height function plays the role of the size, and the finiteness of $E(\mathbb{Q})/2E(\mathbb{Q})$ together with descent on the height gives the [[Mordell-Weil theorem|MXRCPAH09H]].
In logic, a proof that a process terminates by a measure that decreases in a well-ordered set is a descent argument, and Gentzen's consistency proof of arithmetic uses a descent along ordinals below $\varepsilon_0$.
The related pages are the [[minimal counterexample|~f8c099da]] and the [[equivalence of induction and well-ordering|~00389da2]].
