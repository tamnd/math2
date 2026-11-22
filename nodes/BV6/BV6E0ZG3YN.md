---
tag: BV6E0ZG3YN
kind: example
name: Definition of an even integer
msc: ["00A35", "11A05"]
topics: [BP0WAF23HB]
audience: school
instance_of: [8ZCZ3HW91Z]
uses: [8ZCZ3HW91Z, 0C4JS9RF5M, 0CHQKZFK5S]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_(mathematics)
    locator: lead section
---

## Example

Here is the definition.
Let $n$ be an [[integer|0C4JS9RF5M]].
We say that $n$ is *even* if there is an integer $k$ with $n = 2k$, and *odd* if there is an integer $k$ with $n = 2k + 1$.
We check that this is a [[mathematical definition|8ZCZ3HW91Z]] and then use it on four numbers.

1. The definiendum is the word "even".
   The definiens is the condition "there is an integer $k$ with $n = 2k$".
2. The definiens uses only known terms: integers, multiplication by $2$, equality and "there is".
   It does not use the word "even", so it is not circular.
3. The "if" is read as "if and only if".
   So every even integer has the form $2k$, and proofs may use that form.
4. The number $0$ is even, because $0 = 2 \cdot 0$ and $0$ is an integer.
5. The number $-6$ is even, because $-6 = 2 \cdot (-3)$ and $-3$ is an integer.
6. The number $7$ is not even.
   For $k \le 3$ we get $2k \le 6$, and for $k \ge 4$ we get $2k \ge 8$, so $2k \neq 7$ for every integer $k$.
7. The number $7$ is odd, because $7 = 2 \cdot 3 + 1$.

## Remarks

The definition decides the borderline cases that everyday language leaves open.
Many people hesitate over $0$ and over negative numbers, but steps 4 and 5 settle them with one multiplication each.

The definition does not say that each integer is exactly one of even and odd.
That is a theorem, and it follows from the [[division algorithm|0CHQKZFK5S]] with divisor $2$: every $n$ is $2q + r$ with exactly one $r \in \{0, 1\}$.

The words "integer $k$" carry the whole meaning.
If $k$ could be any rational number, then every rational $q$ would be "even", since $q = 2 \cdot \tfrac{q}{2}$.
If we replace $2$ by an integer $m$, the same form defines "$n$ is a multiple of $m$".
For $m = 1$ every integer is a multiple, and for $m = 0$ only $0$ is.

Mathlib states the definition as $a = r + r$ for some $r$, which says the same thing because $r + r = 2r$.

## Explanations

### L1 human

A number is even when it splits into two equal whole parts.
So $10$ is even, because it is $5$ and $5$.
The rule also covers $0$, which is $0$ and $0$, and $-4$, which is $-2$ and $-2$.
The number $9$ is not even: $4$ and $4$ make $8$, and $5$ and $5$ make $10$, so no whole number fits.

### L2 human

We prove from the definition that the square of an even integer is even.

1. Let $n$ be an even integer.
2. By the definition there is an integer $k$ with $n = 2k$.
3. Square and factor:
   $$n^2 = 4k^2 = 2 \cdot (2k^2).$$
4. The number $2k^2$ is an integer, because products of integers are integers.
5. So $n^2$ is two times an integer, and $n^2$ is even by the definition.

Check: $n = 6$ gives $k = 3$, and $36 = 2 \cdot 18$ with $2k^2 = 18$.
This is the usual pattern: unfold "even" into $2k$, calculate, and fold the result back.
Watch out for the converse "if $n^2$ is even, then $n$ is even".
It is true, but this unfolding does not prove it, because $n^2 = 2j$ gives no formula for $n$.
The contrapositive works: if $n = 2k + 1$, then $n^2 = 2(2k^2 + 2k) + 1$ is odd.
