---
tag: X5HG1RNWQX
kind: concept
name: Proof by algorithm
aliases: [algorithmic-proof, proof-by-procedure]
msc: ["00A35", "68W01"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [9DMSG5HAQX, 01XM7JEKHY, 01BX15HSRR, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Loop_invariant
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euclidean_algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Constructive_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hoare_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions
    locator: lead section
---

## Summary

A proof by algorithm shows that an object exists by giving a procedure that builds it, and then proving two things: the procedure stops, and what it returns is correct.

Here is the pattern on a real goal: the [[Euclidean algorithm|0TRNT4X7J0]] returns the [[greatest common divisor|0C8WYW4KYQ]] of integers $a > b > 0$.
Put $r_0 = a$ and $r_1 = b$, and while $r_i \neq 0$ let $r_{i+1}$ be the remainder of $r_{i-1}$ on division by $r_i$.
Termination: $r_1 > r_2 > \cdots \ge 0$ is a strictly decreasing sequence of natural numbers, so it reaches $0$ after finitely many steps.
Invariant: $\gcd(r_{i-1}, r_i) = \gcd(r_i, r_{i+1})$, since $r_{i+1} = r_{i-1} - q_i r_i$, so the two pairs have the same common divisors.
At the stop $r_{n+1} = 0$, so $\gcd(a, b) = \gcd(r_n, 0) = r_n$, the last non-zero remainder.

In general, *termination* is proved with a natural number that decreases strictly at each step, so the [[well-ordering principle|01BX15HSRR]] forbids an infinite run.
*Correctness* is proved with an *invariant*, a statement true at the start and kept by each step, combined with the stopping condition.

## Motivation

Many existence theorems are proved by describing how to find the object.
The greatest common divisor is a combination $ax + by$, and the Euclidean algorithm finds $x$ and $y$.
Every matrix can be brought to [[row echelon form|0VYCDGMJJJ]], and [[Gaussian elimination|0JVJ2WCXZH]] does it.
For $n$ men and $n$ women who rank each other, a stable matching exists, and the [[Gale-Shapley algorithm|CHWQVJ9F5K]] finds one.

A description of a procedure is not yet a proof.
It becomes one when we show that the procedure always stops and that its result is always correct.
This is a [[constructive proof|01XM7JEKHY]] in organized form: the construction is split into repeated simple steps, and each step is checked once.
The reward is double: the proof gives existence and a way to compute the object, and the same two arguments make a computer program trustworthy.

## Notation

A procedure is often written as a loop: "while a condition holds, do a step".
The decreasing quantity of a termination proof is called a *variant*, a *ranking function*, a *potential* or a *monovariant*, depending on the field.
A statement kept by each pass through a loop is a *loop invariant*, and the loop rule of [[Hoare logic|H1M6RSBJ5H]] is built on it.
Proofs about a run index the values by the step, as $r_0, r_1, r_2, \ldots$ for the successive values of a variable $r$.

## Remarks

### Why both proofs are needed

Partial correctness says that the output is right whenever the procedure stops.
Termination says that it does stop.
These are separate claims, and a proof needs both.

"Test $n = 1, 2, 3, \ldots$ until $n$ is an odd [[perfect number|0SB7Q8SYSF]]" would return a correct answer if it stopped, but no proof shows that it stops, so it proves nothing.
The procedure behind the [[Collatz conjecture|6PCQEXEX4N]] (halve an even number, replace an odd $n$ by $3n + 1$) has no known termination proof either.
In the other direction, [[greedy change-making with coins 1, 3 and 4|61Y7Z7AC6X]] always stops and pays the right amount, but it does not always use the fewest coins, so it proves nothing about optimal payments.

### Choosing the variant and the invariant

The variant must be a natural number, or more generally an element of a well-founded order.
A positive real number can decrease forever, as $1, \tfrac12, \tfrac14, \ldots$ does, and an integer can decrease forever if it may become negative.
Sometimes the obvious quantity grows: in [[the greedy algorithm for Egyptian fractions|KR6HBC26YV]] the denominators increase, and the numerators are the variant.

The invariant should say how the current state relates to the goal.
For a procedure that builds an answer piece by piece, the usual form is "(input) $=$ (part built) $+$ (part left)", as in [[the extended Euclidean algorithm|226SFHQ3ER]], which keeps $r_i = a s_i + b t_i$.
A proof by algorithm is a proof by [[mathematical induction|0ASJVEFA9J]] on the number of steps, with the invariant as the induction statement.

### Where the pattern appears

The [[division algorithm|0CHQKZFK5S]] subtracts $b$ from $a$ while the result is at least $b$, and the count of subtractions is the quotient.
Gaussian elimination creates one more leading entry with zeros below it at each step, so it stops after at most as many steps as there are rows.
In the [[stable marriage problem|X201T4TP0Y]], each man proposes to each woman at most once, so the Gale-Shapley algorithm stops, and the invariant "a woman with a proposal stays engaged, and her partner only improves for her" gives stability.
[[Kruskal's algorithm|5FPWTYFJRA]] builds a [[spanning tree|0S4ZEZM7KE]] of minimum weight, and so proves that one exists.
An algorithmic proof often bounds the cost as well: the Euclidean algorithm needs at most five times as many divisions as $b$ has decimal digits, by a theorem of Lamé.

### Watch out

The most common slip describes a procedure and stops, with no proof of termination or of correctness.
A second slip uses a variant that is not bounded below.
A third checks that the invariant survives a step but not that it holds at the start, so the induction has no base case.
A fourth proves a weak correctness claim, such as "the coins add up to the amount", and treats it as the strong claim "the fewest coins".

### History

Euclid's Elements, Book VII, Propositions 1 and 2, find the greatest common measure of two numbers by repeated subtraction, and this is the oldest well-known algorithm.
Leonardo of Pisa (Fibonacci) described the greedy method for Egyptian fractions in his Liber Abaci of 1202.
David Gale and Lloyd Shapley proved the existence of stable matchings by their algorithm in 1962.
Robert Floyd in 1967 and Tony Hoare in 1969 made invariants and variants the standard tools for proofs about programs.

### Try it

Run the Euclidean algorithm on $a = 91$ and $b = 35$.
The remainders are $21$, $14$, $7$, $0$, so $\gcd(91, 35) = 7$.

A procedure starts from a positive integer $n$ and replaces it by $n - 2$ while $n \ge 2$.
Name a variant and an invariant, and say what the output is.
The variant is $n$ itself, the invariant is "$n$ has the same parity as the input", and the output is $0$ or $1$, the parity of the input.

## Explanations

### L1 human

Sometimes the best way to show that something exists is to explain how to build it.
But a recipe is a proof only if we know two things.
First, the recipe must end, and not go on forever.
Second, what comes out at the end must be the thing we wanted.
To find the largest number that divides both $12$ and $18$, subtract the smaller from the larger again and again: $18 - 12 = 6$, then $12 - 6 = 6$, and the two numbers are now equal, so the answer is $6$.
The numbers get smaller each time, so the recipe ends, and each step keeps the same common divisors, so the answer is right.

### L2 human

We prove that every integer $n \ge 1$ is a sum of distinct powers of $2$.
The procedure: while $n > 0$, let $2^k$ be the largest power of $2$ with $2^k \le n$, record $2^k$, and replace $n$ by $n - 2^k$.

1. Termination: each step replaces $n$ by $n - 2^k$, which is smaller and still at least $0$, so the procedure stops, with $n = 0$.
2. Invariant: (original $n$) $=$ (sum of the recorded powers) $+$ (current $n$).
   It holds at the start, and each step moves $2^k$ from the current $n$ to the sum.
3. At the end the current $n$ is $0$, so the original $n$ is the sum of the recorded powers.
4. Distinctness: $n < 2^{k+1}$ by the choice of $k$, so the new value $n - 2^k$ is less than $2^k$, and the next recorded power is smaller.
5. A run with $n = 45$ records $32$, $8$, $4$ and $1$, leaving $13$, $5$, $1$ and $0$, so $45 = 32 + 8 + 4 + 1$.

Proofs by algorithm suit existence theorems that also call for a method of computation.
Watch out: a proof that the output is correct "if the loop stops" is half a proof until a decreasing natural number forces the stop.

### L3 human

In logic the link between algorithms and proofs is exact.
By the Curry-Howard correspondence and realizability, a constructive proof of "for each $x$ there is $y$ with $P(x, y)$" contains an algorithm that computes $y$ from $x$, and proof assistants can extract it.
Termination proofs generalize from the natural numbers to any well-founded order, such as the lexicographic order on pairs, which proves that the Ackermann function is total.
In combinatorics, Hall's marriage theorem, Kőnig's theorem and the max-flow min-cut theorem have algorithmic proofs by augmenting paths, and the algorithm often returns a dual certificate that proves optimality.
The method has limits: the existence of a [[non-measurable set|PKQ7ABPVSG]] needs the axiom of choice and has no constructive proof.
