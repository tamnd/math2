---
tag: KZASF579JE
kind: example
name: Increasing sequences in a dense linear order are indiscernible
msc: ["03C30", "03C10", "06A05"]
topics: [W9CHA4PD9H]
audience: grad
instance_of: [6EG0ZK1YBX, RQS808ZC8T]
uses: [4016QKAHFB, 2W4S2H4VYA, E52RM0KX94, 7FDDXV3JK7, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Indiscernibles
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 5
---

## Example

Let $\mathcal{M} = (M, <)$ be a model of the [[theory of dense linear orders without endpoints|2W4S2H4VYA]], for example $(\Q, <)$ or $(\R, <)$.
Let $(I, <)$ be a [[linear order|0FRXBVVR03]], and let $(a_i)_{i \in I}$ be strictly increasing: $i < j$ implies $a_i < a_j$.
We show that $(a_i)_{i \in I}$ is an [[order-indiscernible sequence|4016QKAHFB]] over $\emptyset$, and that it is not an indiscernible set.

1. By [[quantifier elimination for dense linear orders|E52RM0KX94]], every formula $\varphi(x_1, \dots, x_n)$ is equivalent in $\mathcal{M}$ to a quantifier-free formula $\psi(x_1, \dots, x_n)$.
2. The formula $\psi$ is a Boolean combination of atomic formulas $x_k < x_l$ and $x_k = x_l$, with $1 \le k, l \le n$. The signature has no constants, so no other atomic formulas occur.
3. Let $i_1 < \dots < i_n$ in $I$. Then $a_{i_k} < a_{i_l}$ holds exactly when $k < l$, and $a_{i_k} = a_{i_l}$ holds exactly when $k = l$, because the sequence is strictly increasing.
4. So the truth value of each atomic formula at $(a_{i_1}, \dots, a_{i_n})$ depends only on $k$ and $l$, not on the indices. The same then holds for the Boolean combination $\psi$, and for $\varphi$.
5. Hence all increasing $n$-tuples of the sequence satisfy the same formulas, which is order-indiscernibility.
6. If $I$ has two elements $i < j$, the formula $x_1 < x_2$ holds at $(a_i, a_j)$ and fails at $(a_j, a_i)$. So the sequence is not an indiscernible set.

## Remarks

The example shows that the order of the indices can be visible to the formulas.
Over a set of parameters $A \subseteq M$ the sequence stays indiscernible when each element of $A$ lies below all members or above all members.
For instance, $a_n = n$ for $n \ge 1$ in $(\Q, <)$ is indiscernible over $\set{0}$ and not over $\set{3/2}$, since $x_1 < 3/2$ holds at $a_1$ and fails at $a_2$.
For $(\Q, <)$ itself, the identity map indexed by $(\Q, <)$ is an indiscernible sequence, and it is a first instance of [[generalized indiscernibles|RQS808ZC8T]] indexed by an ordered structure.
A sequence that is not monotone, such as $0, 2, 1, 3$, is not indiscernible, since $x_1 < x_2$ holds at $(0, 2)$ and fails at $(2, 1)$.
A strictly decreasing sequence is also indiscernible, by the same steps with $<$ reversed.

## Explanations

### L1 human

Take the numbers $1, 2, 3, 4, \dots$ inside the rational numbers, and use only the order to describe them.
The pair $1, 2$ and the pair $5, 17$ look the same: in both, the first number is smaller, and between them there are always more rationals.
So every statement in the language of order that is true about $1$ and $2$ is also true about $5$ and $17$.
But $2, 1$ looks different from $1, 2$, so the order of the members matters.

### L2 human

We check the pairs directly for the formula $\varphi(x_1, x_2) := \exists z \, (x_1 < z \wedge z < x_2)$, with $a_n = n$ in $(\Q, <)$.

1. At $(a_1, a_2) = (1, 2)$ the witness $z = 3/2$ shows that $\varphi$ holds.
2. At $(a_5, a_{17}) = (5, 17)$ the witness $z = 6$ shows that $\varphi$ holds.
3. Quantifier elimination replaces $\varphi$ by $x_1 < x_2$, because the order is dense. This matches steps 1 to 4 of the example.

The typical use is as the model case of an indiscernible sequence: in many theories with an order, indiscernible sequences look like this one.
The trap is to think that a parameter outside the sequence is harmless; a parameter between two members separates them.
