---
tag: ZQB1DQR9QS
kind: example
name: The Euclidean algorithm is not a heuristic
msc: ["00A35", "11A05"]
topics: [X1NSTVGDNQ]
audience: ug1
not_instance_of:
  - target: 6KCEWEP4WA
    note: the Euclidean algorithm always stops with the correct greatest common divisor, so it is an algorithm with a guarantee, not a rule of thumb
uses: [6KCEWEP4WA, 0TRNT4X7J0, 02WF878BH1]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_algorithm
    locator: lead section
---

## Example

We find the [[greatest common divisor|02WF878BH1]] of $1071$ and $462$ with the [[Euclidean algorithm|0TRNT4X7J0]], which repeats division with remainder:
$$1071 = 2 \cdot 462 + 147, \qquad 462 = 3 \cdot 147 + 21, \qquad 147 = 7 \cdot 21 + 0.$$
So $\gcd(1071, 462) = \gcd(462, 147) = \gcd(147, 21) = \gcd(21, 0) = 21$.

Now we check the features that make this an algorithm and not a [[heuristic|6KCEWEP4WA]].

1. A rule fixes each step, and the solver makes no choice: the pair $(a, b)$ always becomes $(b, a \bmod b)$.
2. The procedure stops, because the second number decreases strictly, $462 > 147 > 21 > 0$, and a strictly decreasing sequence of natural numbers is finite.
3. The answer is correct, because each step keeps the set of common divisors.
   A common divisor of $a$ and $b$ divides $a - qb$, and a common divisor of $b$ and $a - qb$ divides $a$.
4. These guarantees hold for every pair of natural numbers, not only for this one.

A heuristic has none of these features: it leaves choices to the solver, it may not end, and it may give no answer.
So the Euclidean algorithm is not a heuristic.

## Remarks

The non-example marks the edge of the concept.
A heuristic such as "look at small cases" may or may not lead to an answer, and two solvers may use it in different ways.
The Euclidean algorithm gives every user the same answer after the same number of steps.

The edge can move.
When a class of problems gets an algorithm, heuristics are no longer needed to solve it, only to solve it fast.
For example, "is $n$ prime?" has the algorithm "try every divisor up to $\sqrt{n}$", and the clever tests for primes exist because that algorithm is slow, not because it can fail.

## Explanations

### L1 human

A recipe that always works is not a heuristic.
To find the largest number that divides both $1071$ and $462$, divide, keep the remainder, and repeat.
After three divisions the remainder is $0$, and the last divisor, $21$, is the answer.
The method works every time, for every pair of numbers.
A heuristic is different: it is a hint that often helps and can fail.

### L2 human

Compare the algorithm with a heuristic for the same problem.
A heuristic says "guess small common factors".
The digit sums of $1071$ and $462$ are $9$ and $12$, so $3$ divides both numbers.
A trial division by $7$ gives $1071 = 7 \cdot 153$ and $462 = 7 \cdot 66$, so $21$ divides both.
The guesses found $21$, but they do not show that no larger common factor exists.
The Euclidean algorithm settles that in three divisions, with a proof of correctness for every input.
So when an algorithm exists, use it, and keep heuristics for problems that have none.
Watch out: not every computer program is an algorithm in this sense, since many programs for large searches are heuristics that can stop without an answer.
