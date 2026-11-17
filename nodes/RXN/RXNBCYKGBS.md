---
tag: RXNBCYKGBS
kind: example
name: An infinite direct product of copies of Z/2 has exponent 2
msc: ["20F50", "20K10"]
topics: [BAVE5RN4EE]
audience: ug2
instance_of: [0ZDW0H0VX4, DZSZ8ZS554]
uses: [0ZDW0H0VX4, 00HF4RJ5QN, 03VFZ2WETT, DZSZ8ZS554, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_abelian_group
---

## Example

Let $G = \prod_{i \geq 1} \mathbb{Z}/2\mathbb{Z}$ be the [[direct product|00HF4RJ5QN]] of countably many copies of the [[integers modulo 2|03VFZ2WETT]].
Its elements are the sequences $(a_1, a_2, a_3, \ldots)$ with each $a_i \in \{0, 1\}$, and we add two sequences term by term modulo $2$.
We show that $G$ is infinite and has [[exponent|0ZDW0H0VX4]] $2$.

1. $G$ is a group: the sum of two sequences is a sequence, the zero sequence is the identity, and each $a$ is its own inverse, because $a_i + a_i = 0$ in $\mathbb{Z}/2\mathbb{Z}$.
2. $G$ is infinite. For each $k \geq 1$, let $u_k$ be the sequence with $1$ in position $k$ and $0$ in all other positions. The elements $u_1, u_2, u_3, \ldots$ are pairwise distinct.
3. Every $a \in G$ satisfies $2a = a + a = (2a_1, 2a_2, \ldots) = (0, 0, \ldots) = 0$.
4. The exponent is not $1$, because $u_1 \neq 0$, so $1 \cdot u_1 \neq 0$.
5. By steps 3 and 4, the least positive integer $n$ with $na = 0$ for all $a \in G$ is $n = 2$. So $\exp(G) = 2$.

## Remarks

The example shows that a group of finite exponent can be infinite.
Each nonzero element has order $2$, so $G$ is an [[elementary abelian group|DZSZ8ZS554]] and a [[vector space|000AYPA9AJ]] over $\mathbb{F}_2$, of infinite dimension.
The subgroup of sequences with only finitely many nonzero terms, the direct sum $\bigoplus_{i \geq 1} \mathbb{Z}/2\mathbb{Z}$, also has exponent $2$ and is countable.
The group $G$ is not finitely generated.
If $g_1, \ldots, g_r$ generate a subgroup $H$, then each element of $H$ is a sum $c_1 g_1 + \cdots + c_r g_r$ with $c_i \in \{0, 1\}$, so $|H| \leq 2^r$.
The same argument shows that a finitely generated abelian group of finite exponent is finite.
So the [[Burnside problem|XWEMJ7T2XV]] has a positive answer for abelian groups.

## Explanations

### L1 human

Imagine an infinite row of light switches, each one on or off.
An element of the group is a choice of switches to flip.
If we do the same choice of flips twice, every switch returns to where it was.
So doing any element twice gives back the start, although the group has infinitely many elements.

### L2 human

We compare $G$ with a finite group of the same exponent.

1. The [[Klein four-group|0PMRQJVTME]] $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ has order $4$ and exponent $2$.
2. The group $G$ contains the Klein four-group as the set of sequences that are $0$ after position $2$.
3. More generally, $G$ contains a copy of $(\mathbb{Z}/2\mathbb{Z})^k$ for every $k$, so the orders of its finite subgroups are not bounded.

The typical use of this example is as a test case: a statement about groups of finite exponent must hold here, and this group is infinite and not cyclic.
A trap: finite exponent does not imply finite order, and it does not imply finitely generated.
