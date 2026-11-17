---
tag: D8CYAZ8S9T
kind: example
name: Quantifying an open sentence gives a statement
msc: ["97E40"]
topics: [WMY13MXY3W]
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
We make three [[mathematical statements|S9MHMRAX88]] from $P(x)$, and we find the truth value of each.

1. Substitution. Put $x = 2$. Then $2^2 - 5 \cdot 2 + 6 = 4 - 10 + 6 = 0$. So the statement $P(2)$ is true.
2. Substitution. Put $x = 0$. Then $0^2 - 5 \cdot 0 + 6 = 6 \neq 0$. So the statement $P(0)$ is false.
3. The [[existential quantifier|0MSRQHCNN9]]. The statement "there is a real number $x$ with $x^2 - 5x + 6 = 0$" is true, because step 1 gives such an $x$.
4. The [[universal quantifier|0GHS47PDAQ]]. The statement "for every real number $x$, $x^2 - 5x + 6 = 0$" is false, because step 2 gives an $x$ for which $P(x)$ is false.

In each case, the variable $x$ no longer waits for a value: it has one, or a quantifier binds it.
So each result is a statement, while $P(x)$ itself is not.

## Remarks

The example shows the two ways to close an open sentence: substitution and quantification.
The factorization $x^2 - 5x + 6 = (x - 2)(x - 3)$ shows that $P(x)$ is true exactly for $x = 2$ and $x = 3$.

The set of values changes the truth values.
If $x$ ranges over the integers from $4$ to $10$, then "there is $x$ with $P(x)$" is false, because $2$ and $3$ are not in the range.
If we replace $P(x)$ by "$x^2 - 5x + 6 \geq -\tfrac{1}{4}$", then the universal statement becomes true over $\mathbb{R}$, because $x^2 - 5x + 6 = (x - \tfrac{5}{2})^2 - \tfrac{1}{4}$.

## Explanations

### L1 human

The sentence "a number times itself is $9$" is not true or false by itself.
We must know which number is meant.
For the number $3$ it is true, and for the number $4$ it is false.
"Some number times itself is $9$" is a full claim, and it is true, because $3$ works.
"Every number times itself is $9$" is also a full claim, and it is false, because $4$ fails.

### L2 human

We close the open sentence $Q(n)$: "$n^2 + n$ is even", where $n$ is an integer.

1. $Q(5)$: $25 + 5 = 30$ is even, so $Q(5)$ is true.
2. "There is an integer $n$ with $Q(n)$" is true, by step 1.
3. "For every integer $n$, $Q(n)$" is also true. The number $n^2 + n = n(n + 1)$ is a product of two consecutive integers, and one of them is even.

The typical use is in reading a theorem: we find each variable and the quantifier or the value that closes it.

A trap: in step 3, checking many values of $n$ does not prove the universal statement.
The proof needs the reason that holds for every $n$.
