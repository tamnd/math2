---
tag: 8WJPSS7TE9
kind: example
name: The even integers form a subgroup of the integers
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
instance_of: [0X1JXT47GA, 0CB0DX5BVV]
uses: [0C4JS9RF5M, 0BSCJA5G53, 0X1JXT47GA, 0CB0DX5BVV]
sources:
  - url: https://en.wikipedia.org/wiki/Subgroup
    locator: Other examples
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] with addition, and let $2\mathbb{Z} = \{2k : k \in \mathbb{Z}\}$ be the set of even integers.
We check the three conditions of a [[subgroup|0X1JXT47GA]].

1. Identity: $0 = 2 \cdot 0$, so $0 \in 2\mathbb{Z}$.
2. Closure: let $2k, 2l \in 2\mathbb{Z}$. Then $2k + 2l = 2(k + l)$, and $k + l \in \mathbb{Z}$. So $2k + 2l \in 2\mathbb{Z}$.
3. Inverses: let $2k \in 2\mathbb{Z}$. Its inverse in $G$ is $-2k = 2(-k)$, and $-k \in \mathbb{Z}$. So $-2k \in 2\mathbb{Z}$.
4. By steps 1 to 3, $2\mathbb{Z}$ is a subgroup of $\mathbb{Z}$.
5. Normality: $G$ is abelian, so $g + 2\mathbb{Z} = 2\mathbb{Z} + g$ for each $g \in \mathbb{Z}$. Thus $2\mathbb{Z}$ is [[normal|0CB0DX5BVV]] in $G$.

## Remarks

The example is the first case of a proper nontrivial subgroup of $\mathbb{Z}$.
If we replace $2$ by any integer $n \geq 0$, the same three steps show that $n\mathbb{Z}$ is a subgroup of $\mathbb{Z}$.
For $n = 0$ we get the trivial subgroup $\{0\}$, and for $n = 1$ we get $\mathbb{Z}$ itself.
By [[the classification of the subgroups of the integers|0SRATCFF1W]], every subgroup of $\mathbb{Z}$ is $n\mathbb{Z}$ for exactly one $n \geq 0$.
For an integer $a$, the coset $a + 2\mathbb{Z}$ is the set $\{a + h : h \in 2\mathbb{Z}\}$.
There are two cosets, $2\mathbb{Z}$ and $1 + 2\mathbb{Z}$, so the [[index|0DTXBQPA2S]] of $2\mathbb{Z}$ in $\mathbb{Z}$ is $2$.
The set $1 + 2\mathbb{Z}$ of odd integers is [[not a subgroup|VN9H9H74KN]].

## Explanations

### L1 human

The even numbers are $\ldots, -4, -2, 0, 2, 4, \ldots$.
Zero is even.
If we add two even numbers, we get an even number, for example $4 + 6 = 10$.
If we change the sign of an even number, it stays even.
So the even numbers form a group of their own inside the integers.

### L2 human

We check the conditions on concrete elements and then in general.

1. Take $a = 6$ and $b = -14$. Then $a + b = -8 = 2 \cdot (-4)$ and $-a = -6 = 2 \cdot (-3)$ are even.
2. In general, the even integers are the multiples of $2$, and sums and negatives of multiples of $2$ are multiples of $2$.

The typical use of this example is as a model: a subgroup of $\mathbb{Z}$ is the set of multiples of one number.
A trap: the set $\{0, 2, 4, 6, \ldots\}$ of nonnegative even integers is not a subgroup, because $-2$ is missing.
