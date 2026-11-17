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

A proof by algorithm proves that an object exists by giving a procedure that builds it, together with two proofs about the procedure.
The proof of *termination* shows that the procedure stops after finitely many steps on each allowed input.
The proof of *correctness* shows that the output, when the procedure stops, has the required property.
Termination is usually proved with a quantity that takes values in the natural numbers and decreases strictly at each step, so the [[well-ordering principle|01BX15HSRR]] forbids an infinite run.
Correctness is usually proved with an *invariant*, a statement that holds at the start and that each step preserves, combined with the stopping condition.
The method matters because it gives existence and a way to compute the object at once, and because the same two proofs make a computer program trustworthy.

## Motivation

Many existence theorems are proved by a description of how to find the object.
The [[greatest common divisor|0C8WYW4KYQ]] of two integers is a combination $ax + by$, and the [[Euclidean algorithm|0TRNT4X7J0]] finds $x$ and $y$.
Every matrix can be brought to [[row echelon form|0VYCDGMJJJ]], and [[Gaussian elimination|0JVJ2WCXZH]] does it.
For $n$ men and $n$ women who rank each other, a stable matching exists, and the [[Gale-Shapley algorithm|CHWQVJ9F5K]] finds one.
A description of a procedure is not yet a proof.
It becomes a proof when we show that the procedure always stops and that its result is always correct.
This is a [[constructive proof|01XM7JEKHY]] in an organized form: the construction is split into repeated simple steps, and each step is checked once.

## Notation

1. A procedure is often written as pseudocode with a loop: "while condition, do step".
2. The decreasing quantity of a termination proof is called a *variant*, a *ranking function*, a *potential* or a *monovariant*, depending on the field.
3. A statement preserved by each pass through a loop is called a *loop invariant*. In [[Hoare logic|H1M6RSBJ5H]] the rule for loops uses it.
4. Proofs about a run often index the values by the step: $r_0, r_1, r_2, \ldots$ for the successive values of a variable $r$.

## Remarks

### Examples

1. [[The extended Euclidean algorithm proves Bézout's identity|226SFHQ3ER]]: the remainders decrease, so the algorithm stops, and the invariant $r_i = a s_i + b t_i$ gives the identity at the end.
2. [[The greedy algorithm for Egyptian fractions|KR6HBC26YV]]: each rational number between $0$ and $1$ is a sum of distinct unit fractions, because the numerators decrease and the denominators increase.
3. The [[division algorithm|0CHQKZFK5S]] for natural numbers: subtract $b$ from $a$ while the result is at least $b$. The number of subtractions is the quotient, and what remains is the remainder.
4. [[Gaussian elimination|0JVJ2WCXZH]]: each step creates one more leading entry with zeros below it, so after at most as many steps as there are rows the matrix is in row echelon form.
5. The [[stable marriage problem|X201T4TP0Y]]: in the Gale-Shapley algorithm each man proposes to each woman at most once, so it stops. The invariant "a woman who has received a proposal stays engaged, and her partner only gets better for her" gives stability.
6. [[Kruskal's algorithm|5FPWTYFJRA]] builds a [[spanning tree|0S4ZEZM7KE]] of minimum weight in a connected weighted graph, and so proves that such a tree exists and can be built greedily.

### Non-examples

1. [[Greedy change-making with coins 1, 3 and 4 is not optimal|61Y7Z7AC6X]]: the procedure always stops, but its output is not always correct, so it proves nothing about optimal payments.
2. The procedure behind the [[Collatz conjecture|6PCQEXEX4N]] (halve an even number, replace an odd $n$ by $3n + 1$) has no known proof of termination. A description of it proves no existence statement.
3. "Test $n = 1, 2, 3, \ldots$ until $n$ is an odd [[perfect number|0SB7Q8SYSF]]" is a procedure whose output would be correct, but no proof shows that it stops, so it does not prove that an odd perfect number exists.

### Basic properties

1. A proof by algorithm is a proof by [[mathematical induction|0ASJVEFA9J]] on the number of steps: the invariant is the induction statement, and the step of the procedure is the induction step.
2. A strictly decreasing sequence of natural numbers is finite. This is the form of the well-ordering principle that termination proofs use.
3. Partial correctness (the output is correct whenever the procedure stops) and termination are separate claims, and a proof needs both.
4. An algorithmic proof often gives a bound on the size of the object or on the time to find it. For the Euclidean algorithm, the number of division steps is at most a constant times the number of digits of the smaller input.

### History

Euclid's Elements, Book VII, Propositions 1 and 2, find the greatest common measure of two numbers by repeated subtraction, and this is the oldest well-known algorithm.
Leonardo of Pisa (Fibonacci) described the greedy method for Egyptian fractions in his Liber Abaci of 1202.
David Gale and Lloyd Shapley proved the existence of stable matchings by their algorithm in 1962.
Robert Floyd in 1967 and Tony Hoare in 1969 made invariants and variants the standard tools for proofs about programs.

### Common errors

1. A student describes a procedure and stops, without a proof of termination or of correctness.
2. A student proves termination with a quantity that decreases but is not bounded below, such as an integer that can become negative, or a positive real number that can decrease forever, as $1, \tfrac12, \tfrac14, \ldots$ does.
3. A student checks the invariant after one step but not at the start, so the induction has no base case.

## Explanations

### L1 human

Sometimes the best way to show that something exists is to explain how to build it.
But a recipe is only a proof if we know two things.
First, the recipe must end, and it must not go on forever.
Second, what comes out at the end must be the thing we wanted.
For example, to find the largest number that divides both $12$ and $18$, subtract the smaller from the larger again and again: $18 - 12 = 6$, then $12 - 6 = 6$, and the two numbers are now equal, so the answer is $6$.
The numbers get smaller each time, so the recipe ends, and each step keeps the same common divisors, so the answer is right.

### L2 human

We prove that every natural number $n \ge 1$ is a sum of distinct powers of $2$, by an algorithm.
Procedure: while $n > 0$, let $2^k$ be the largest power of $2$ with $2^k \le n$, record $2^k$, and replace $n$ by $n - 2^k$.

1. Termination: each step replaces $n$ by $n - 2^k < n$, and $n - 2^k \ge 0$. A strictly decreasing sequence of natural numbers is finite, so the procedure stops, and it stops with $n = 0$.
2. Invariant: (original $n$) $=$ (sum of the recorded powers) $+$ (current $n$). It holds at the start, with nothing recorded, and each step moves $2^k$ from the current $n$ to the sum.
3. At the end the current $n$ is $0$, so the original $n$ is the sum of the recorded powers.
4. Distinctness: after recording $2^k$, the new value is $n - 2^k < 2^{k+1} - 2^k = 2^k$, because $n < 2^{k+1}$ by the choice of $k$. So the next recorded power is less than $2^k$.
5. A run with $n = 45$: record $32$ (rest $13$), then $8$ (rest $5$), then $4$ (rest $1$), then $1$ (rest $0$). So $45 = 32 + 8 + 4 + 1$.

The typical use is an existence theorem in number theory, combinatorics or linear algebra that also needs a method of computation.
A trap is to prove only that the output is correct "if the loop stops", without a decreasing natural number that forces the stop.

### L3 human

In logic, the link between algorithms and proofs is exact.
By the Curry-Howard correspondence and realizability, a constructive proof of "for each $x$ there is $y$ with $P(x, y)$" contains an algorithm that computes $y$ from $x$.
Proof assistants can extract this program.
Termination proofs generalize from the natural numbers to any well-founded order, such as the lexicographic order on pairs, which proves that the Ackermann function is total.
Correctness by invariants is the basis of Hoare logic and of verified software.
In combinatorics, many existence theorems (Hall's marriage theorem, Kőnig's theorem, the max-flow min-cut theorem) have algorithmic proofs by augmenting paths, and the algorithm often gives a dual certificate that proves optimality.
The method has limits: some existence theorems, such as the existence of a [[non-measurable set|PKQ7ABPVSG]], need the axiom of choice and have no constructive proof.
