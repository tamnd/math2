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

1. Lemma. If $a$ and $b$ are positive integers and $a \mid b$, then $a \le b$.
2. Proof of the lemma. Write $b = ak$ with $k$ an integer. Since $a > 0$ and $b > 0$, the integer $k = b/a$ is positive, so $k \ge 1$.
3. Multiply $k \ge 1$ by $a > 0$: $b = ak \ge a$. This proves the lemma.
4. ($a \le b$) Apply the lemma to $a \mid b$.
5. ($b \le a$) Apply the lemma to $b \mid a$, with the roles of $a$ and $b$ exchanged.
6. The order $\le$ on the integers is antisymmetric, so $a \le b$ and $b \le a$ give $a = b$.

A check with numbers: $6 \mid 12$ gives $6 \le 12$, and $12 \nmid 6$, so the hypothesis $b \mid a$ fails for $a = 6$ and $b = 12$, as it must.

## Remarks

1. The example proves that divisibility is antisymmetric on the positive integers. With reflexivity ($a \mid a$) and transitivity ($a \mid b$ and $b \mid c$ give $a \mid c$), it shows that divisibility is a [[partial order|0QV2JS9RJ3]] on the positive integers.
2. The proof transfers antisymmetry from one order to another: the lemma says that $a \mid b$ implies $a \le b$, and $\le$ is already known to be antisymmetric.
3. The hypothesis "positive" is used in step 2. Without it the result fails, as [[mutual divisibility of integers does not give equality|WRN90EH74V]] shows.
4. On the natural numbers with $0$ the result still holds: $0 \mid b$ forces $b = 0$, so if one of the numbers is $0$, both are.
5. A typical use is the uniqueness of the greatest common divisor: two positive greatest common divisors divide each other, so they are equal.

## Explanations

### L1 human

If $a$ divides $b$, then $b$ is $a$ times a whole number, so $b$ is at least as big as $a$ when both are positive.
If also $b$ divides $a$, then $a$ is at least as big as $b$.
A number cannot be both bigger and smaller than another number, so the two numbers are equal.
For instance, if a number divides $15$ and $15$ divides it, then the number is $15$.

### L2 human

We use the example to prove that $\gcd(a, b) = \gcd(b, a - b)$ for positive integers $a > b$.

1. Let $d = \gcd(a, b)$ and $e = \gcd(b, a - b)$. Both are positive.
2. The number $d$ divides $a$ and $b$, so it divides $a - b$. So $d$ is a common divisor of $b$ and $a - b$, and $d \mid e$ by the property of the greatest common divisor.
3. The number $e$ divides $b$ and $a - b$, so it divides $(a - b) + b = a$. So $e$ is a common divisor of $a$ and $b$, and $e \mid d$.
4. By the example, $d \mid e$ and $e \mid d$ give $d = e$.

The typical use is the proof that two numbers defined in different ways are equal, when each one divides the other.
A trap is to use the example for integers that can be negative, where it fails.
