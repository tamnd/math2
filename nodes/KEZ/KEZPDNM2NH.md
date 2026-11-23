---
tag: KEZPDNM2NH
kind: concept
name: Decomposing and recombining
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, G9NFJ55KCX, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - url: https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Discourse_on_the_Method
    locator: Part II
  - book: isbn:9780691164076
---

## Summary

When a problem has several difficulties at once, split it into parts that each carry one difficulty, solve the parts, and put the partial results back together.
The second half matters as much as the first: a split is useful only when you know how to recombine.

Here is a problem where the split is the whole idea.
What are the last two digits of $2^{100}$, that is, its remainder modulo $100$?
A first attempt reaches for [[Euler's theorem|0VC4DVE7DQ]], which gives $a^{40} \equiv 1 \pmod{100}$, but only when $\gcd(a, 100) = 1$, and here the base is $2$.
A second attempt lists the powers of $2$ modulo $100$ and waits for a repeat, which takes about twenty lines of arithmetic.
The helping move is to split the modulus: $100 = 4 \cdot 25$, and $4$ and $25$ are coprime.
Modulo $4$ the answer is $0$ at once, since $2^{100}$ is a multiple of $4$.
Modulo $25$ the base is coprime to the modulus, and
$$2^{10} = 1024 = 41 \cdot 25 - 1 \equiv -1 \pmod{25}, \qquad 2^{100} = (2^{10})^{10} \equiv (-1)^{10} = 1 \pmod{25}.$$
To recombine, look among $1, 26, 51, 76$, the numbers below $100$ that are $1$ modulo $25$, for the one divisible by $4$.
Only $76$ qualifies, and the [[Chinese remainder theorem|0FNN9B4W64]] says the answer is unique, so $2^{100}$ ends in $76$.

The parts can be pieces of a figure, cases of a statement, clauses of a condition, coprime factors of a modulus, or halves of a list.
Decomposing is a [[heuristic|6KCEWEP4WA]]: it tells you to look for a split, but some problems have none, and some splits cut through a link between the parts.

## Motivation

A problem is often hard because several difficulties meet in it.
If you can separate them, each one may be easy or already solved.
The angle sum of a polygon is unknown, but the angle sum of a triangle is known, and a polygon cuts into triangles.
A congruence modulo $100$ is awkward, but congruences modulo $4$ and $25$ are small.
A list of a million items is hard to sort at once, but two sorted halves merge in one pass.

The same move runs through computing as [[divide and conquer|G9NFJ55KCX]], through proofs as [[proof by cases|0WCP0PVET6]], and through calculus as partial fractions.
In each case the recombination rule is what makes the split pay: a sum of angles, a uniqueness theorem, a merge, or a sum of integrals.

## Notation

Pólya's entry is "decomposing and recombining", and among his questions is the advice to separate the parts of the condition.
In algorithms the name is "divide and conquer", in proofs "case analysis" or "proof by cases", and in counting "the sum rule".
When the parts overlap, the recombination is [[inclusion-exclusion|0FF7726C7P]], and when they share variables, the problem is called coupled.

## Remarks

### Splits that work

To find the angle sum of a convex polygon with $n$ sides, draw the $n - 3$ diagonals from one vertex.
They cut the polygon into $n - 2$ triangles whose angles exactly fill the angles of the polygon, so the [[sum is|4NQVWDXWMK]] $(n - 2) \cdot 180^\circ$.

For the last two digits of $3^{100}$, the same split of $100$ into $4$ and $25$ gives remainders $1$ and $1$, so the [[answer|NMEDPPK0CP]] is $01$.

[[Partial fraction decomposition|030VFEREKG]] splits a quotient into pieces that integrate one at a time:
$$\int \frac{dx}{x^2 - 1} = \frac{1}{2} \int \left( \frac{1}{x - 1} - \frac{1}{x + 1} \right) dx = \frac{1}{2} \ln \left| \frac{x - 1}{x + 1} \right| + C.$$

A proof by cases splits a statement: $n^2$ leaves remainder $0$ or $1$ on division by $4$, because $(2m)^2 = 4m^2$ and $(2m + 1)^2 = 4(m^2 + m) + 1$.

### When the parts interact

The danger is a split that ignores a link between the parts.
To minimize $(x - 1)^2 + (x - 3)^2$, a naive solver minimizes each term alone and gets $x = 1$ and $x = 3$.
The two terms share the variable $x$, so the partial answers cannot be combined, and the [[true minimum|M347T41A7J]] is $2$, at $x = 2$.

Overlapping parts cause the second failure.
Among the numbers $1$ to $100$, there are $50$ multiples of $2$ and $33$ multiples of $3$, but $50 + 33 = 83$ counts the $16$ multiples of $6$ twice.
The correct count is $50 + 33 - 16 = 67$.

A third failure uses the wrong rule of recombination.
The derivative of a product is not the product of the derivatives, since $(x \cdot x)' = 2x$ while $1 \cdot 1 = 1$, and the [[product rule|0V9A43H7WV]] is the correct rule.

### What a good split needs

A proof by cases needs cases that cover every possibility; they may overlap, since each case gives the conclusion on its own.
A count by parts needs parts that do not overlap, or a correction for the overlaps.
A split of a modulus needs coprime factors, which is why $100 = 10 \cdot 10$ is useless.
And a split pays only when the recombination is cheaper than the original problem: merge sort gains because merging two sorted lists takes one pass.

### Watch out

The common error in a written solution is to leave out the recombination.
After the parts are solved, state and prove how they give the whole.
A second error is a case analysis that misses a case: a proof for $n > 0$ and $n < 0$ says nothing about $n = 0$.

### History

In the second part of the *Discourse on the Method* (1637), Descartes made it his second rule to divide each difficulty into as many parts as the solution needs.
Pólya gave "decomposing and recombining" an entry in the dictionary part of *How to Solve It* (1945).
In computing, merge sort, an early divide-and-conquer algorithm, is credited to John von Neumann in 1945.

### Try it

Find the last two digits of $3^{2026}$.
Modulo $4$ the power is $(-1)^{2026} = 1$; modulo $25$, $3^{20} \equiv 1$ and $2026 = 20 \cdot 101 + 6$, so $3^{2026} \equiv 3^6 = 729 \equiv 4$; among $4, 29, 54, 79$ only $29$ is $1$ modulo $4$, so the answer is $29$.

How many of the numbers $1$ to $60$ are divisible by $3$ or by $5$?
There are $20$ multiples of $3$, $12$ of $5$ and $4$ of $15$, so the count is $20 + 12 - 4 = 28$.

## Explanations

### L1 human

A big job is easier when you cut it into small jobs.
To find the angles of a five-sided shape, cut it into triangles, whose angles you already know.
A pentagon cuts into $3$ triangles from one corner, so its angles add up to $3 \cdot 180^\circ = 540^\circ$.
The second half of the method matters as much: you must put the pieces back together correctly.
If you count the people who play football or tennis, the people who play both must not be counted twice.

### L2 human

We count the comparisons that merge sort makes on a list of $n = 2^k$ items.
Merge sort splits the list into halves, sorts each half the same way, and merges the sorted halves.
Merging sorted lists of $a$ and $b$ items takes at most $a + b - 1$ comparisons, because each comparison places one item and the last item needs none.
So the largest number $T(n)$ of comparisons satisfies
$$T(1) = 0, \qquad T(2^k) \le 2\, T(2^{k-1}) + 2^k - 1.$$
We show $T(2^k) \le k \cdot 2^k$ by induction.
For $k = 0$ it says $T(1) \le 0$.
If $T(2^{k-1}) \le (k - 1) 2^{k-1}$, then
$$T(2^k) \le (k - 1) 2^k + 2^k - 1 = k \cdot 2^k - 1 < k \cdot 2^k.$$
So merge sort needs at most $n \log_2 n$ comparisons, while comparing all pairs needs $\frac{n(n - 1)}{2}$.

The cost of the whole is the cost of the parts plus the cost of recombining, and that gives a recurrence.
The gain comes from the cheap merge; a split whose recombination costs as much as the original problem gains nothing.

### L3 human

In algorithms, divide and conquer leads to recurrences $T(n) = a\, T(n / b) + f(n)$, which the master theorem solves.
In number theory, the Chinese remainder theorem says that $\mathbb{Z}/m\mathbb{Z}$ is a product of the rings $\mathbb{Z}/p^e\mathbb{Z}$ for the prime powers $p^e$ in $m$, so every problem modulo $m$ splits into problems modulo prime powers.
In topology, the [[Mayer-Vietoris sequence|X8BWXFGK53]] computes the homology of a space from two open pieces and their overlap, a precise form of inclusion-exclusion.
In analysis, a [[partition of unity|KK8KZQNDVY]] splits a global object into local pieces and glues the local results.
For partial differential equations, [[separation of variables|47NFRVB564]] writes solutions as products of functions of one variable each, and superposition recombines them.
When the parts overlap and recur, [[dynamic programming|8E1CJZXC6X]] stores their solutions for reuse, and [[auxiliary elements|8TKKRAXKFN]] such as a diagonal are often what creates the parts.
