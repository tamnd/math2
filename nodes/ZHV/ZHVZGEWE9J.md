---
tag: ZHVZGEWE9J
kind: example
name: The universal statement that n^2 is at most 2^n for every natural number n is false
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0GHS47PDAQ]
uses: [0GHS47PDAQ, 0B88PQTJ66, 0ED72CTBNP, 0ASJVEFA9J, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_quantification
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Counterexample
    locator: lead section
---

## Example

Let $\mathbb{N} = \{0, 1, 2, \dots\}$ be the set of [[natural numbers|0MWKJ44V5A]].
Consider the [[universal statement|0B88PQTJ66]] $\forall n \in \mathbb{N} \; (n^2 \le 2^n)$.
We show that it is false, and that it becomes true when the domain is restricted to $n \ge 4$.

1. A universal statement is false when at least one element of the domain fails the predicate.
2. Compute the first values: $(n, n^2, 2^n)$ is $(0, 0, 1)$, $(1, 1, 2)$, $(2, 4, 4)$, $(3, 9, 8)$, $(4, 16, 16)$, $(5, 25, 32)$.
3. For $n = 3$, $n^2 = 9$ and $2^n = 8$, and $9 > 8$. So $n = 3$ fails the predicate.
4. So $n = 3$ is a [[counterexample|0ED72CTBNP]], and the statement is false.

Now consider $\forall n \in \mathbb{N} \; (n \ge 4 \to n^2 \le 2^n)$.
We prove it by [[induction|0ASJVEFA9J]] on $n \ge 4$.

5. Base case: $4^2 = 16 = 2^4$.
6. For $n \ge 3$, we have $n^2 - 2n - 1 = (n - 1)^2 - 2 \ge 4 - 2 > 0$, so $2n + 1 < n^2$.
7. Induction step: assume $n \ge 4$ and $n^2 \le 2^n$. Then $(n + 1)^2 = n^2 + 2n + 1 < n^2 + n^2 = 2n^2 \le 2 \cdot 2^n = 2^{n + 1}$, by step 6 and the assumption.
8. So the restricted statement is true for every $n \ge 4$.

## Remarks

The example shows that one failure is enough to make a universal statement false, even when the predicate holds for all other elements.
Here the predicate holds for $n = 0, 1, 2$ and for every $n \ge 4$, and it fails only at $n = 3$.

The truth value depends on the domain.
On $\{0, 1, 2\}$ the statement is true, on $\{0, 1, 2, 3\}$ it is false, and on $\{n \in \mathbb{N} \mid n \ge 4\}$ it is true.
The negation of the original statement is the existential statement $\exists n \in \mathbb{N} \; (n^2 > 2^n)$, and the witness $n = 3$ proves it.

## Explanations

### L1 human

Compare the square of a number with the power of $2$: $0$ and $1$, $1$ and $2$, $4$ and $4$, $9$ and $8$, $16$ and $16$, $25$ and $32$.
The square is at most the power for every number in the list except $3$.
So "for every number, the square is at most the power of $2$" is false, because of the single number $3$.
From $4$ on, the power of $2$ doubles at each step and stays ahead.

### L2 human

We decide whether $\forall n \in \mathbb{N} \; (n^2 + n + 11 \text{ is prime})$ is true.

1. For $n = 0, 1, 2, 3$ the values are $11$, $13$, $17$, $23$, all prime.
2. For $n = 10$ the value is $100 + 10 + 11 = 121 = 11 \cdot 11$, which is not prime.
3. So $n = 10$ is a counterexample, and the statement is false.

The typical use of a counterexample is to show that a pattern seen in small cases is not a theorem.
A trap is to stop the search early: the first nine values of $n$ give primes, and a search up to $n = 9$ finds no counterexample.
