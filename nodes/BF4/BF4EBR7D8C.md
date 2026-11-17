---
tag: BF4EBR7D8C
kind: example
name: Z has infinite index in Q
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
instance_of: [0DTXBQPA2S]
uses: [0X1JXT47GA, 03DEH43F4H, 0DTXBQPA2S, 0C4JS9RF5M, 3C53TD]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Examples
  - book: isbn:9781305657960
    locator: Chapter 7
---

## Example

Let $G = (\mathbb{Q}, +)$ be the rational numbers with addition.
Let $H = \mathbb{Z}$ be the [[integers|0C4JS9RF5M]].
We show that the [[index|0DTXBQPA2S]] $[\mathbb{Q} : \mathbb{Z}]$ is infinite.

1. The set $\mathbb{Z}$ is a [[subgroup|0X1JXT47GA]] of $\mathbb{Q}$. It contains $0$, and sums and negatives of integers are integers.
2. Two [[left cosets|03DEH43F4H]] $a + \mathbb{Z}$ and $b + \mathbb{Z}$ are equal if and only if $a - b \in \mathbb{Z}$.
3. For each integer $m \geq 1$, consider the coset $\frac{1}{m} + \mathbb{Z}$.
4. Let $1 \leq m < k$ be integers. Then $0 < \frac{1}{m} - \frac{1}{k} < \frac{1}{m} \leq 1$. So $\frac{1}{m} - \frac{1}{k}$ is not an integer.
5. By steps 2 and 4, the cosets $\frac{1}{m} + \mathbb{Z}$ for $m = 1, 2, 3, \ldots$ are pairwise distinct.
6. Thus $\mathbb{Z}$ has infinitely many cosets in $\mathbb{Q}$, and $[\mathbb{Q} : \mathbb{Z}]$ is infinite.

## Remarks

Each coset $a + \mathbb{Z}$ contains exactly one number in the interval $[0, 1)$, namely $a - \lfloor a \rfloor$.
So the cosets are in bijection with $\mathbb{Q} \cap [0, 1)$, and the index is countably infinite.
If we replace $\mathbb{Q}$ by $\mathbb{R}$, the cosets of $\mathbb{Z}$ are in bijection with $[0, 1)$ in the same way, so $[\mathbb{R} : \mathbb{Z}]$ is uncountable.

The example shows that a subgroup can have infinite index even when both groups are countable.
In fact, the only subgroup of finite index in $\mathbb{Q}$ is $\mathbb{Q}$ itself.
The proof has three steps.
Let $K$ be a subgroup of finite index $n$.
The group $\mathbb{Q}$ is abelian, so $K$ is normal, and $\mathbb{Q}/K$ is a group of order $n$.
By [[Lagrange's theorem|3C53TD]], the order of each coset $x + K$ divides $n$, so $nx \in K$ for each $x \in \mathbb{Q}$.
Each $y \in \mathbb{Q}$ is equal to $nx$ for $x = y / n$, so $y \in K$, and $K = \mathbb{Q}$.

## Explanations

### L1 human

Two fractions are in the same coset when they differ by a whole number.
For example, $\frac{1}{2}$ and $\frac{5}{2}$ are in the same coset, because they differ by $2$.
The fractions $\frac{1}{2}$, $\frac{1}{3}$, $\frac{1}{4}$, and so on, are all in different cosets.
This list does not end, so there are infinitely many cosets.

### L2 human

We decide which of the numbers $\frac{1}{3}$, $\frac{7}{3}$ and $\frac{2}{3}$ lie in the same coset of $\mathbb{Z}$.

1. We compute $\frac{7}{3} - \frac{1}{3} = 2$, an integer. So $\frac{7}{3} + \mathbb{Z} = \frac{1}{3} + \mathbb{Z}$.
2. We compute $\frac{2}{3} - \frac{1}{3} = \frac{1}{3}$, not an integer. So $\frac{2}{3} + \mathbb{Z} \neq \frac{1}{3} + \mathbb{Z}$.
3. The representatives in $[0, 1)$ are $\frac{1}{3}$, $\frac{1}{3}$ and $\frac{2}{3}$, which confirms steps 1 and 2.

The typical use is to study the group $\mathbb{Q}/\mathbb{Z}$, the rational numbers modulo $1$, in which each element has finite order.
A trap is to compare the sizes of the sets.
The sets $\mathbb{Z}$ and $\mathbb{Q}$ have the same cardinality, but the index is infinite.
