---
tag: ARHWX7H5BN
kind: example
name: The even numbers are not almost all natural numbers
msc: ["00A35", "11B05"]
topics: [Z2WNQ1DNTX]
audience: ug1
not_instance_of:
  - target: N1XSAXCQY3
    note: the exceptions, the odd numbers, are infinite and have natural density one half, so the claim fails in the cofinite and in the density sense
uses: [N1XSAXCQY3, 0MWKJ44V5A, RVG9Z8NYA6, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_density
    locator: Properties and examples
  - url: https://en.wikipedia.org/wiki/Almost_all
    locator: Meaning in number theory
---

## Example

Let $E = \{0, 2, 4, 6, \ldots\}$ be the set of even [[natural numbers|0MWKJ44V5A]].
We show that the claim "almost all natural numbers are even" is false in the cofinite sense and in the density sense of [[almost all|N1XSAXCQY3]].
The exceptions are the odd natural numbers, $O = \{1, 3, 5, \ldots\}$.

1. The set $O$ is infinite, because the numbers $2k + 1$ for $k \in \mathbb{N}$ are distinct and odd.
   So the claim fails in the cofinite sense.
2. For $n \in \mathbb{N}$, the even numbers in $\{0, 1, \ldots, n\}$ are $0, 2, \ldots, 2\lfloor n/2 \rfloor$, so there are $\lfloor n/2 \rfloor + 1$ of them.
   For example, $n = 9$ gives the $5$ numbers $0, 2, 4, 6, 8$, and $\lfloor 9/2 \rfloor + 1 = 5$.
3. The share of even numbers is $(\lfloor n/2 \rfloor + 1)/(n + 1)$.
   Since $n/2 - 1 < \lfloor n/2 \rfloor \le n/2$, the share lies between two bounds:
   $$\frac{n}{2(n + 1)} < \frac{\lfloor n/2 \rfloor + 1}{n + 1} \le \frac{n + 2}{2(n + 1)}.$$
4. Both bounds tend to $\tfrac{1}{2}$, so $E$ has [[natural density|RVG9Z8NYA6]] $\tfrac{1}{2}$.
5. Then $O$ has density $1 - \tfrac{1}{2} = \tfrac{1}{2}$.
   The exceptions do not have density zero, so the claim fails in the density sense.

## Remarks

The example shows that an infinite set of exceptions can be too large for "almost all", even when the good cases are also infinite.

In the countable sense the claim is true but empty.
Every subset of $\mathbb{N}$ is [[countable|01TQB88H4C]], so in that sense every property holds for almost all natural numbers.
This is why the countable sense is used only on uncountable sets such as $\mathbb{R}$.

Change the property and the answer can change.
"Almost all natural numbers are not divisible by $10$" is still false, because the multiples of $10$ are infinite and have density $\tfrac{1}{10}$.
"Almost all natural numbers are not perfect squares" is true in the density sense and still false in the cofinite sense.

## Explanations

### L1 human

Half of the numbers are even and half are odd: $0, 2, 4$ are even, and $1, 3, 5$ are odd.
For "almost all numbers are even" to be true, the odd numbers would have to be a tiny part of all numbers.
But from $0$ to $100$ there are $50$ odd numbers among $101$ numbers, and the share stays close to one half forever.
So the odd numbers are not a tiny part, and the claim is false.

### L2 human

How does the density change with the step of the progression?
Take the multiples of $3$.
In $\{0, 1, \ldots, n\}$ they are $0, 3, \ldots, 3\lfloor n/3 \rfloor$, so there are $\lfloor n/3 \rfloor + 1$ of them.
The bounds $n/3 - 1 < \lfloor n/3 \rfloor \le n/3$ show that the share $(\lfloor n/3 \rfloor + 1)/(n + 1)$ tends to $\tfrac{1}{3}$.
So the numbers not divisible by $3$ have density $\tfrac{2}{3}$, and they are not almost all natural numbers either.
Check at $n = 29$: there are $10$ multiples of $3$ among $30$ numbers.

The typical use is a quick test: a nonempty set given by a congruence condition modulo $m$ has positive density, so its complement is never almost all of $\mathbb{N}$.
Watch out: infinitely many exceptions do not by themselves make "almost all" false in the density sense, since the squares are infinite and still have density zero.
