---
tag: AMYQ47TB3F
kind: example
name: The predicate "n is prime" on the numbers 1 to 10
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0QHEWQD30B]
uses: [0QHEWQD30B, 0T3DPBG981, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Predicate_(logic)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
---

## Example

Let $D = \{1, 2, \dots, 10\}$ and let $P(n)$ be the open sentence "$n$ is a [[prime number|01826KMG2H]]".
We check that $P$ is a unary [[predicate|0T3DPBG981]] on $D$, and we find its truth set.

1. The only free variable of $P(n)$ is $n$, and it ranges over $D$.
2. A prime number is an integer greater than $1$ whose only positive divisors are $1$ and itself.
   So for each $a \in D$ the sentence "$a$ is prime" is true or false, and $P(a)$ is a proposition.
3. $P(1)$ is false, because $1$ is not greater than $1$.
4. $P(2)$, $P(3)$, $P(5)$ and $P(7)$ are true, because none of these numbers has a divisor strictly between $1$ and itself.
5. $P(4)$, $P(6)$, $P(8)$, $P(9)$ and $P(10)$ are false, because $4 = 2 \cdot 2$, $6 = 2 \cdot 3$, $8 = 2 \cdot 4$, $9 = 3 \cdot 3$ and $10 = 2 \cdot 5$.
6. So the truth set is $T_P = \{2, 3, 5, 7\}$.

## Remarks

The example shows three levels at once.
The predicate $P(n)$ has no truth value, each instance $P(a)$ is a proposition, and the truth set collects the true instances.
From the truth set you can read off quantified statements: $\exists n \in D \; P(n)$ is true because $T_P$ is nonempty, and $\forall n \in D \; P(n)$ is false because $T_P \neq D$.

The truth set changes with the domain.
On $\{1, \dots, 20\}$ it is $\{2, 3, 5, 7, 11, 13, 17, 19\}$, and on $\mathbb{N}$ it is the infinite set of all primes.

## Explanations

### L1 human

Take the sentence "___ is prime" and the numbers from $1$ to $10$.
Put each number in the blank and decide whether the result is true.
It is true for $2$, $3$, $5$ and $7$, and false for the six other numbers.
So the truth set is $\{2, 3, 5, 7\}$.

### L2 human

Find the truth set of $Q(n)$: "$n$ is prime and $n + 2$ is prime" on the same domain.
Since $Q(n)$ needs $n \in T_P$, only $n = 2, 3, 5, 7$ are candidates.
For $n = 2$ the number $4$ is not prime, so $Q(2)$ is false.
For $n = 3$ and $n = 5$ the numbers $5$ and $7$ are prime, so $Q(3)$ and $Q(5)$ are true.
For $n = 7$ the number $9 = 3 \cdot 3$ is not prime, so $Q(7)$ is false.
So $T_Q = \{3, 5\}$.
Truth sets turn a question about a predicate into a question about a set, which is often easier to answer.
Watch out: $n + 2$ need not lie in $D$, because the domain restricts only the variable $n$; so $Q(9)$ asks about $9$ and $11$, and it is a proposition.
