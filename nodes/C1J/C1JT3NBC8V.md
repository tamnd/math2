---
tag: C1JT3NBC8V
kind: example
name: The diagonal argument does not prove the rationals uncountable
msc: ["00A35", "03E10"]
topics: [T6QQ749DM5]
audience: ug1
instance_of: [D8A1K052XV]
uses: [D8A1K052XV, 0XCH8QVDCQ, 0DS9KWFDK2, 0518MM6BE1]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
    locator: Uncountable set
  - url: https://en.wikipedia.org/wiki/Countable_set
    locator: lead section
---

## Example

A student adapts [[Cantor's diagonal argument|0XCH8QVDCQ]] to the rational numbers in $(0, 1)$.
The conclusion is false, so some step must fail; find it before reading on.

1. Assume that $q_1, q_2, q_3, \ldots$ lists all rational numbers in $(0, 1)$.
2. Write each $q_n$ as a decimal $0.d_{n1} d_{n2} d_{n3} \ldots$.
3. Let $e_n = 5$ if $d_{nn} \neq 5$, and $e_n = 4$ if $d_{nn} = 5$, and let $x = 0.e_1 e_2 e_3 \ldots$.
4. Then $x$ differs from each $q_n$ in the $n$th digit, so $x$ is not in the list.
5. So the list misses a rational number, and the rationals in $(0, 1)$ are uncountable.

[[The rationals are countable|0DS9KWFDK2]], so a list as in step 1 exists, and the argument [[proves too much|D8A1K052XV]].
Steps 1 to 4 are valid: the digits of $x$ are all $4$ or $5$, so $x$ has only one decimal expansion, and it differs from each $q_n$.
Step 5 is the failure, because it assumes that $x$ is rational, and nothing proves that.
In fact $x$ is irrational: a rational $x$ would lie in $(0, 1)$ and so equal some $q_n$, against step 4.

The correct conclusion is weaker and true: every list of rationals in $(0, 1)$ misses some irrational number.
In the proof that [[the reals are uncountable|0518MM6BE1]], the same $x$ only has to be a real number in $(0, 1)$, which every such decimal is, and that is why the argument works there.

## Remarks

The way to catch this error is to test an argument on a case where the answer is known.
The diagonal construction always produces a number outside the list, and the argument succeeds exactly when that number is guaranteed to lie in the set being listed.
For the reals the guarantee holds, and for the rationals it fails.

## Explanations

### L1 human

Cantor's trick builds a new decimal number that differs from every number on a given list.
For a list of all real numbers between $0$ and $1$, that is a contradiction, because the new number is a real number too.
For a list of all fractions, it is no contradiction, because the new number need not be a fraction.
The trick shows only that the new number is missing, and a missing irrational number does not hurt a list of fractions.

### L2 human

We run the construction on a list that begins $q_1 = 0.5000\ldots$, $q_2 = 0.333\ldots$ and $q_3 = 0.666\ldots$.
The diagonal digits are $5$, $3$ and $6$, so $e_1 = 4$, $e_2 = 5$, $e_3 = 5$, and $x$ begins $0.455$.
Check that $x \neq q_m$ for every $m$: the $m$th digits $e_m$ and $d_{mm}$ differ, and $x$ has no second decimal expansion because its digits are only $4$ and $5$.
If the list contains all rationals in $(0, 1)$, this shows that $x$ is irrational.

The typical use of this reasoning is to read the diagonal argument as the construction of an element outside a list, and then to ask in which set that element lies.
Watch out for a step that is valid for one set and silently reused for another, here "$x$ belongs to the set".
