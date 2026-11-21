---
tag: 1T221XPKPJ
kind: example
name: The natural numbers in their order are not an indiscernible sequence
msc: ["03C30", "06A05"]
topics: [W9CHA4PD9H]
audience: grad
not_instance_of:
  - target: 6EG0ZK1YBX
    note: "the formula exists y (y < x) is false at 0 and true at 1"
uses: [4016QKAHFB, 0FRXBVVR03, HYJ10AF6RT, KZASF579JE]
sources:
  - url: https://en.wikipedia.org/wiki/Indiscernibles
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 5
---

## Example

Consider the structure $(\N, <)$ in the signature $\set{<}$, and the family $a_n = n$ indexed by $(\N, <)$.
We show that this family is not an [[order-indiscernible sequence|4016QKAHFB]] over $\emptyset$.

1. Let $\varphi(x)$ be the [[formula|HYJ10AF6RT]] $\exists y \, (y < x)$, in one free variable.
2. At $a_0 = 0$ the formula fails, because no natural number is smaller than $0$.
3. At $a_1 = 1$ the formula holds, with the witness $y = 0$.
4. The one-element tuples $(a_0)$ and $(a_1)$ are both increasing, so indiscernibility would force $\varphi$ to have the same truth value at both. It does not.

The same failure happens for every infinite subfamily $(a_n)_{n \in J}$ with $J \subseteq \N$.
Indeed, let $j_0 < j_1$ be the two least members of $J$; the formula $\exists y_1 \dots \exists y_{j_0+1} \, (y_1 < y_2 < \dots < y_{j_0+1} < x)$ is false at $j_0$ and true at $j_1$.

## Remarks

The failure comes from the elements of $\N$ being definable: each $n$ is the unique element with exactly $n$ elements below it.
In a structure where every element is definable without parameters, no infinite injective family is indiscernible.
The sequence $(n)_{n \ge 1}$ is indiscernible in $(\Q, <)$, as in [[the dense linear order example|KZASF579JE]], so the failure depends on the ambient structure and not on the sequence alone.
The elementary extension $\N + \Q \times \Z$ of $(\N, <)$, with one copy of $\Z$ for each rational in increasing order, does contain an infinite indiscernible sequence: choose one element in each of the copies indexed by $1, 2, 3, \dots$.
Order automorphisms of $\Q$, combined with shifts inside the copies, move any increasing tuple of these elements to any other.
This agrees with the existence theorem for indiscernibles, which gives them in some model of the theory and not in every model.

## Explanations

### L1 human

In the natural numbers, $0$ is special: it is the first one.
The number $1$ is not first, because $0$ comes before it.
So the question "is there a smaller number?" tells $0$ and $1$ apart, using only the order.
That is exactly what an indiscernible sequence does not allow.

### L2 human

The test for a non-example is to find one formula and two increasing tuples on which it disagrees.

1. Look for a definable property that only the first members have, such as "has no predecessor" or "has at most $k$ elements below it".
2. Here $\exists y \, (y < x)$ separates $0$ from $1$, with tuples of length $1$.
3. For the subfamily of even numbers the formula "at least one element lies below $x$" fails only at $0$, and the formula "at least three elements lie below $x$" separates $2$ from $4$.

The trap is to compare only tuples of length at least $2$; the definition includes tuples of length $1$, and these already require all members to have the same type.
