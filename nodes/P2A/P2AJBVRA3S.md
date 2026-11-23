---
tag: P2AJBVRA3S
kind: example
name: Mutual divisibility of natural numbers gives equality
msc: ["00A35", "11A05"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [S3QADD13E9]
uses: [S3QADD13E9, 0PG2H7WKGG, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Antisymmetric_relation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Partially_ordered_set
    locator: lead section
---

## Example

Let $a$ and $b$ be positive integers with $a \mid b$ and $b \mid a$, where $\mid$ is [[divisibility|0PG2H7WKGG]].
We prove $a = b$ by [[equality by two inequalities|S3QADD13E9]] for the usual order $\le$.

1. Lemma: if $a$ and $b$ are positive integers and $a \mid b$, then $a \le b$.
2. Proof of the lemma: write $b = ak$ with $k$ an integer.
   Since $a > 0$ and $b > 0$, the integer $k = b/a$ is positive, so $k \ge 1$.
3. Multiply $k \ge 1$ by $a > 0$ to get $b = ak \ge a$, which proves the lemma.
4. ($a \le b$) Apply the lemma to $a \mid b$.
5. ($b \le a$) Apply the lemma to $b \mid a$, with the roles of $a$ and $b$ exchanged.
6. The order $\le$ on the integers is antisymmetric, so $a \le b$ and $b \le a$ give $a = b$.

Check: $6 \mid 12$ gives $6 \le 12$, and $12 \nmid 6$, so for $a = 6$ and $b = 12$ the hypothesis $b \mid a$ fails, as it must.

## Remarks

The example proves that divisibility is antisymmetric on the positive integers.
Together with $a \mid a$ and the rule that $a \mid b$ and $b \mid c$ give $a \mid c$, this makes divisibility a [[partial order|0QV2JS9RJ3]] there.
The proof borrows antisymmetry from a known order: the lemma says that $a \mid b$ implies $a \le b$, and $\le$ is already antisymmetric.

Positivity is used in step 2, and without it the result fails, as [[mutual divisibility of integers|WRN90EH74V]] shows with $2$ and $-2$.
If $0$ is allowed together with the positive integers, the result still holds, because $0 \mid b$ forces $b = 0$.
A typical use is the uniqueness of the greatest common divisor: two positive greatest common divisors divide each other, so they are equal.

## Explanations

### L1 human

If $a$ divides $b$, then $b$ is $a$ times a whole number, so $b$ is at least as big as $a$ when both are positive.
If $b$ also divides $a$, then $a$ is at least as big as $b$.
Neither can be bigger, so the two numbers are equal.
For instance, a number that divides $15$ and is divided by $15$ must be $15$.

### L2 human

We prove $\gcd(a, b) = \gcd(b, a - b)$ for positive integers $a > b$.

1. Let $d = \gcd(a, b)$ and $e = \gcd(b, a - b)$, both positive.
2. The number $d$ divides $a$ and $b$, so it divides $a - b$.
   So $d$ is a common divisor of $b$ and $a - b$, and therefore $d \mid e$.
3. The number $e$ divides $b$ and $a - b$, so it divides $(a - b) + b = a$.
   So $e$ is a common divisor of $a$ and $b$, and $e \mid d$.
4. By the example, $d \mid e$ and $e \mid d$ give $d = e$.

Check: $\gcd(12, 8) = 4$ and $\gcd(8, 4) = 4$.
This is the usual way to show that two numbers defined differently are equal.
Watch out: the result needs positive numbers, and it fails for integers of either sign.
