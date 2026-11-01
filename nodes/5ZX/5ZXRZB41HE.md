---
tag: 5ZXRZB41HE
kind: definition
name: Characteristic of a field
msc: ["12E99", 13A99]
defines: 1ZB13N78XW
uses: [0QA8CHH8MG, 0P7CH1CND5]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_(algebra)
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]] with unit element $1$.
For a positive integer $n$, write $n \cdot 1 = 1 + 1 + \dots + 1$, with $n$ terms.
If $n \cdot 1 = 0$ for some positive integer $n$, the characteristic $\operatorname{char} K$ is the least such $n$.
Otherwise $\operatorname{char} K = 0$.

## Remarks

This is the [[characteristic of a ring|0P7CH1CND5]] applied to $K$.
Since a field is an integral domain, the [[characteristic is zero or a prime|00758QM6JJ]].
Example: in $\F_5$, $5 \cdot 1 = 0$ and $n \cdot 1 \ne 0$ for $1 \le n \le 4$, so $\operatorname{char} \F_5 = 5$.
Non-example of positive characteristic: in $\Q$, $n \cdot 1 = n \ne 0$ for every $n \ge 1$, so no positive $n$ works and $\operatorname{char} \Q = 0$.
The [[prime subfield|0VPFBAY7MW]] of $K$ is isomorphic to $\Q$ if $\operatorname{char} K = 0$ and to $\F_p$ if $\operatorname{char} K = p$.
If $\operatorname{char} K = p > 0$, then $(a + b)^p = a^p + b^p$ for all $a, b \in K$, which gives the [[Frobenius endomorphism|0GHDDVAH8P]].

## Explanations

### L1 human

The characteristic counts how many ones you must add to reach zero.
In the usual number fields you never reach zero, and the characteristic is $0$.
In a finite field you always reach zero, after a prime number of steps.
