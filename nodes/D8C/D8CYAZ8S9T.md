---
tag: D8CYAZ8S9T
kind: example
name: Quantifying an open sentence gives a statement
msc: ["97E40"]
topics: [WMY13MXY3W, PM1AYWABA7]
audience: school
instance_of: [0ZGC7ZESYN]
uses: [S9MHMRAX88, 0GHS47PDAQ, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
---

## Example

Let $P(x)$ be the open sentence "$x^2 - 5x + 6 = 0$", where $x$ is a real number.
It is not yet true or false, because $x$ has no value.
We make four [[mathematical statements|S9MHMRAX88]] from it, two by putting in a value and two by adding a quantifier.

1. Put $x = 2$.
   Then
   $$2^2 - 5 \cdot 2 + 6 = 4 - 10 + 6 = 0,$$
   so the statement $P(2)$ is true.
2. Put $x = 0$.
   Then $0^2 - 5 \cdot 0 + 6 = 6 \ne 0$, so the statement $P(0)$ is false.
3. Add the [[existential quantifier|0MSRQHCNN9]]: "there is a real number $x$ with $x^2 - 5x + 6 = 0$".
   This statement is true, because step 1 gives such an $x$.
4. Add the [[universal quantifier|0GHS47PDAQ]]: "for every real number $x$, $x^2 - 5x + 6 = 0$".
   This statement is false, because step 2 gives an $x$ for which $P(x)$ fails.

In each case the variable no longer waits for a value: either it has one, or a quantifier binds it.
So each result is a statement, while $P(x)$ itself is not.

## Remarks

The example shows the two ways to close an open sentence, substitution and quantification.
The factorization tells the whole story of $P(x)$:
$$x^2 - 5x + 6 = (x - 2)(x - 3),$$
so $P(x)$ is true exactly for $x = 2$ and $x = 3$.
Check: $(x - 2)(x - 3) = x^2 - 3x - 2x + 6 = x^2 - 5x + 6$.

The set over which $x$ ranges changes the truth values.
If $x$ ranges over the integers from $4$ to $10$, then "there is $x$ with $P(x)$" is false, because neither $2$ nor $3$ is in the range.
If we change the open sentence to "$x^2 - 5x + 6 \ge -\tfrac{1}{4}$", then the universal statement becomes true over $\mathbb{R}$, because
$$x^2 - 5x + 6 = \left(x - \tfrac{5}{2}\right)^2 - \tfrac{1}{4} \ge -\tfrac{1}{4}.$$

## Explanations

### L1 human

The sentence "a number times itself is $9$" is not true or false by itself.
We must know which number is meant.
For the number $3$ it is true, and for the number $4$ it is false.
"Some number times itself is $9$" is a full claim, and it is true, because $3$ works.
"Every number times itself is $9$" is also a full claim, and it is false, because $4$ fails.

### L2 human

Close the open sentence $Q(n)$: "$n^2 + n$ is even", where $n$ is an integer.
Putting in $n = 5$ gives $25 + 5 = 30$, which is even, so $Q(5)$ is true.
So "there is an integer $n$ with $Q(n)$" is true as well.
The universal statement "for every integer $n$, $Q(n)$" is also true, and the reason covers every $n$ at once:
$$n^2 + n = n(n + 1),$$
a product of two consecutive integers, and one of two consecutive integers is even.
Watch out: checking many values of $n$ would not prove the universal statement.
What proves it is a reason that holds for every $n$, and finding each variable and the quantifier that closes it is the first step in reading any theorem.
