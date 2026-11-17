---
tag: MBPSRTCW23
kind: example
name: The sum 1 + 2 + ... + n in sigma notation
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
instance_of: [QKEX4PD029]
uses: [QKEX4PD029, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Summation
    locator: lead section
---

## Example

We write the sum of the first $n$ positive integers in two notations and compare them.
The ellipsis form is
$$1 + 2 + \cdots + n,$$
and the sigma form is
$$\sum_{k=1}^{n} k.$$

1. The ellipsis form lists the first terms and the last term. The reader must guess the rule "add $1$ each time" from the terms $1$ and $2$.
2. The sigma form states the rule. The index $k$ runs through the integers from $1$ to $n$, and the term for each $k$ is $k$ itself.
3. The index $k$ is a bound variable. So $\sum_{k=1}^{n} k$ and $\sum_{j=1}^{n} j$ are the same sum, but $n$ is free and fixes the length of the sum.
4. For $n = 4$ both forms give $1 + 2 + 3 + 4 = 10$.
5. For $n = 1$ the ellipsis form "$1 + 2 + \cdots + 1$" reads badly, but the sigma form gives the single term $1$ without trouble.
6. For $n = 0$ the sigma form is the empty sum, which is $0$ by convention, while the ellipsis form has no sensible reading.
7. The closed form is $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$. For $n = 4$ it gives $\frac{4 \cdot 5}{2} = 10$, and for $n = 100$ it gives $\frac{100 \cdot 101}{2} = 5050$.

## Remarks

The example shows that the sigma form states the rule of the terms, while the ellipsis form leaves the rule to the reader.
The sigma form also handles the small cases $n = 1$ and $n = 0$ correctly.
If the term $k$ is changed to $k^2$, the sum becomes $\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}$; for $n = 4$ this gives $1 + 4 + 9 + 16 = 30 = \frac{4 \cdot 5 \cdot 9}{6}$.
A proof of either closed form uses [[mathematical induction|0ASJVEFA9J]], and the notation makes the induction step $\sum_{k=1}^{n+1} k = \sum_{k=1}^{n} k + (n + 1)$ easy to write.

## Explanations

### L1 human

Adding $1 + 2 + 3 + 4$ gives $10$.
To say "add all whole numbers from $1$ up to some number $n$", we can write $1 + 2 + \cdots + n$ with dots in the middle.
The sign $\Sigma$, a Greek capital S for "sum", says the same thing more exactly.
Under the sign we write where the counting starts, above it where it stops, and to the right what we add each time.

### L2 human

We compute $\sum_{k=3}^{6} (2k + 1)$ and rewrite it with a new index.

1. The index $k$ takes the values $3, 4, 5, 6$.
2. The terms are $7, 9, 11, 13$, so the sum is $40$.
3. Put $j = k - 2$. Then $j$ runs from $1$ to $4$, and $2k + 1 = 2j + 5$.
4. So the sum is $\sum_{j=1}^{4} (2j + 5) = 2 \cdot 10 + 4 \cdot 5 = 40$, the same value.

The typical use of a shift of index is to bring a sum to a form with a known closed formula.
A trap: when the index shifts, both limits and the term must change together.
