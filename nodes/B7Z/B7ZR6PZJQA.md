---
tag: B7ZR6PZJQA
kind: example
name: The Prüfer group has no finite exponent
msc: ["20F50", "20K10"]
topics: [BAVE5RN4EE]
audience: ug2
not_instance_of:
  - target: 0ZDW0H0VX4
    note: every element has finite order, but the element orders are not bounded, so no positive integer n gives nx = 0 for every element x
instance_of: [JZNQTTMG58]
uses: [F0XAMM2PPS, 0ZDW0H0VX4, 0WE2NHZJ7B, JZNQTTMG58, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Prüfer_group
  - url: https://en.wikipedia.org/wiki/Torsion_group
    locator: lead section
---

## Example

Let $p$ be a [[prime|01826KMG2H]], and let $\mathbb{Z}(p^\infty) = \{m/p^k + \mathbb{Z} : m \in \mathbb{Z},\ k \geq 0\}$ be the [[Prüfer group|F0XAMM2PPS]], a subgroup of $\mathbb{Q}/\mathbb{Z}$ under addition.
We show that each element has finite [[order|0WE2NHZJ7B]], but the group has no finite [[exponent|0ZDW0H0VX4]].

1. Each element has finite order. For $x = m/p^k + \mathbb{Z}$, we have $p^k x = m + \mathbb{Z} = 0$. So the order of $x$ divides $p^k$.
2. For each $k \geq 1$, the element $x_k = 1/p^k + \mathbb{Z}$ has order exactly $p^k$. If $1 \leq j < p^k$, then $j x_k = j/p^k + \mathbb{Z}$, and $0 < j/p^k < 1$, so $j/p^k$ is not an integer and $j x_k \neq 0$.
3. Suppose, for a contradiction, that $n \geq 1$ satisfies $nx = 0$ for every $x \in \mathbb{Z}(p^\infty)$.
4. Choose $k$ with $p^k > n$. This is possible because $p^k \geq 2^k > k$ for all $k \geq 1$, so $k = n$ works.
5. Then $1 \leq n < p^k$, so $n x_k \neq 0$ by step 2. This contradicts step 3.
6. So no positive integer $n$ satisfies $nx = 0$ for all $x$, and $\mathbb{Z}(p^\infty)$ has infinite exponent.

## Remarks

By step 1, $\mathbb{Z}(p^\infty)$ is a [[torsion group|JZNQTTMG58]]: every element has finite order.
So a torsion group need not have finite exponent.
The reason is that the element orders $p, p^2, p^3, \ldots$ are not bounded, so they have no common multiple.
A group has finite exponent exactly when it is torsion and the orders of its elements are bounded.
The group $\mathbb{Q}/\mathbb{Z}$ contains $\mathbb{Z}(p^\infty)$, so it also has infinite exponent.
Each finitely generated subgroup of $\mathbb{Z}(p^\infty)$ is cyclic of order $p^k$ for some $k$, so it has finite exponent.

## Explanations

### L1 human

Think of the rotations of a circle by $1/2$ of a turn, by $1/4$ of a turn, by $1/8$ of a turn, and so on, for $p = 2$.
Each such rotation, repeated often enough, gives a whole number of turns: $1/8$ of a turn needs $8$ repetitions.
But there is no single number of repetitions that works for all of them.
For any number $n$, a rotation by a fine enough fraction of a turn, such as $1/2^n$, needs more than $n$ repetitions.

### L2 human

We test the candidate $n = 12$ for $p = 2$.

1. The elements $1/2 + \mathbb{Z}$ and $1/4 + \mathbb{Z}$ satisfy $12x = 0$, because $12/2 = 6$ and $12/4 = 3$ are integers.
2. The element $1/8 + \mathbb{Z}$ gives $12/8 + \mathbb{Z} = 3/2 + \mathbb{Z} = 1/2 + \mathbb{Z} \neq 0$.
3. So $12$ is not an exponent, and the element $1/16 + \mathbb{Z}$ also fails, since $12/16 = 3/4$ is not an integer.

The typical use of this example is to separate "every element has finite order" from "the group has finite exponent".
A trap: a common bound on the element orders is needed, and a bound for each element is not enough.
