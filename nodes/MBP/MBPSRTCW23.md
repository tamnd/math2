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

A textbook writes "the sum $1 + 2 + \cdots + n$" in one line and "$\sum_{k=1}^{n} k$" in the next.
We read both forms of the sum of the first $n$ positive integers and compare them:
$$1 + 2 + \cdots + n \qquad \text{and} \qquad \sum_{k=1}^{n} k.$$

1. The ellipsis form lists the first terms and the last term.
   The reader must guess the rule "add $1$ each time" from the terms $1$ and $2$.
2. The sigma form states the rule.
   The index $k$ runs through the integers from $1$ to $n$, and the term for each $k$ is $k$ itself.
3. The index $k$ is a bound letter, so renaming it changes nothing:
   $$\sum_{k=1}^{n} k = \sum_{j=1}^{n} j.$$
   The letter $n$ is free, and it fixes the length of the sum.
4. For $n = 4$ both forms give the same value:
   $$1 + 2 + 3 + 4 = 10.$$
5. For $n = 1$ the ellipsis form "$1 + 2 + \cdots + 1$" reads badly, but the sigma form gives the single term $1$.
6. For $n = 0$ the sigma form is the empty sum, which is $0$ by convention, while the ellipsis form has no sensible reading.
7. The closed form is
   $$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}.$$
   For $n = 4$ it gives $\frac{4 \cdot 5}{2} = 10$, and for $n = 100$ it gives $\frac{100 \cdot 101}{2} = 5050$.

Check: the closed form at $n = 0$ gives $\frac{0 \cdot 1}{2} = 0$, the value of the empty sum.

## Remarks

The sigma form states the rule of the terms, while the ellipsis form leaves the rule to the reader.
For $1 + 2 + \cdots + n$ the guess is safe, because every reader shares the habit that the step is $1$.
The sigma form is also the one that behaves well at the small cases $n = 1$ and $n = 0$, which is where proofs by [[mathematical induction|0ASJVEFA9J]] start.

Change the term and the notation keeps up.
With $k^2$ in place of $k$ the closed form becomes
$$\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6},$$
and for $n = 4$ both sides give $1 + 4 + 9 + 16 = 30 = \frac{4 \cdot 5 \cdot 9}{6}$.
The sigma form also makes the induction step easy to write, since $\sum_{k=1}^{n+1} k = \sum_{k=1}^{n} k + (n + 1)$.

## Explanations

### L1 human

Adding $1 + 2 + 3 + 4$ gives $10$.
To say "add all whole numbers from $1$ up to some number $n$", we can write $1 + 2 + \cdots + n$ with dots in the middle.
The sign $\Sigma$, a Greek capital S for "sum", says the same thing more exactly.
Under the sign we write where the counting starts, above it where it stops, and to the right what we add each time.

### L2 human

Compute $\sum_{k=3}^{6} (2k + 1)$, and then rewrite it with a new index.
The index $k$ takes the values $3, 4, 5, 6$, so the terms are $7, 9, 11, 13$:
$$\sum_{k=3}^{6} (2k + 1) = 7 + 9 + 11 + 13 = 40.$$
Now put $j = k - 2$.
Then $j$ runs from $1$ to $4$, and $2k + 1 = 2(j + 2) + 1 = 2j + 5$, so
$$\sum_{j=1}^{4} (2j + 5) = 2(1 + 2 + 3 + 4) + 4 \cdot 5 = 20 + 20 = 40.$$
Check: both computations give $40$.
A shift of index brings a sum to a form with a known closed formula, here the formula for $1 + 2 + 3 + 4$.
Watch out: when the index shifts, both limits and the term must change together.
