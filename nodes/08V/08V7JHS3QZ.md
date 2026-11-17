---
tag: 08V7JHS3QZ
kind: statement
role: theorem
name: Order of an element divides the order of the group
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
about: [0WE2NHZJ7B, 0B85S2V2DR]
uses: [G5S1M9, 0WE2NHZJ7B, 0B85S2V2DR, 08ABT85339, 031M8HX7DA, 3C53TD]
formal:
  - system: lean4
    library: mathlib
    decl: orderOf_dvd_natCard
    match: stronger
    adapter: Math2.Match.orderOf_dvd
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
    locator: Applications
  - book: isbn:9780471433347
    locator: Section 3.2
  - book: isbn:9781305657960
    locator: Chapter 7
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] and let $g \in G$.
Then the [[order|0WE2NHZJ7B]] of $g$ divides the [[order|0B85S2V2DR]] $|G|$ of $G$.

## Remarks

### Why each hypothesis is needed

- The group $G$ must be finite. In $(\mathbb{Z}, +)$, the element $1$ has infinite order, and $|\mathbb{Z}|$ is not a natural number.
- In an infinite group, the orders of the elements of finite order need not have a common bound. In $(\mathbb{Q}/\mathbb{Z}, +)$, the coset $\frac{1}{n} + \mathbb{Z}$ has order $n$, for each $n \geq 1$.

### Consequences

- [[$g^{|G|} = e$ for each $g \in G$|0ZEPNS9BXK]]. With the units modulo $n$, this gives [[Fermat's little theorem|0M25PRN3WQ]] and [[Euler's theorem|0VC4DVE7DQ]].
- [[A group of prime order is cyclic|05MM4EK4SA]], because each element other than $e$ has order $p$.
- The [[exponent|0ZDW0H0VX4]] of $G$, the least common multiple of the orders of its elements, divides $|G|$.
- In a group of order $10$, each element has order $1$, $2$, $5$ or $10$.

### Converse

The converse asks: for each divisor $d$ of $|G|$, is there an element of order $d$?
This is false.
The [[Klein four-group|0PMRQJVTME]] has order $4$, but each element other than $e$ has order $2$.
The group $S_3$ has order $6$, but [[it has no element of order 6|Y20PEX049W]].
A partial converse is [[Cauchy's theorem|0JM7PA288B]]: if a prime $p$ divides $|G|$, then $G$ has an element of order $p$.

### Generalizations

- Let $G$ be any group, finite or infinite. If $g$ lies in a finite subgroup $H$ of $G$, then the order of $g$ divides $|H|$. The same proof applies, with $H$ in place of $G$.
- If a finite group $G$ acts on a set $X$, the size of each orbit of $\langle g \rangle$ on $X$ divides the order of $g$. This follows from the orbit-stabiliser theorem for $\langle g \rangle$.

## History

In 1801, Gauss proved the case of the nonzero residues modulo a prime $p$: the order of each residue divides $p - 1$.

## Explanations

### L1 human

Take an element of a finite group and multiply it by itself again and again.
After some steps you come back to the identity.
The number of steps is the order of the element.
The powers of the element form a small group inside the big group, with as many members as the order.
The size of such a small group always divides the size of the big group.
So in a group of $6$ elements, the order of each element is $1$, $2$, $3$ or $6$.

### L2 human

We check the theorem in the [[group of units|0F8X8ZRQ53]] $(\mathbb{Z}/7\mathbb{Z})^\times = \{1, 2, 3, 4, 5, 6\}$, which has order $6$.

1. Take $g = 2$. The powers are $2^1 = 2$, $2^2 = 4$ and $2^3 = 8 \equiv 1 \pmod 7$.
2. So the order of $2$ is $3$, and $3$ divides $6$.
3. Take $g = 3$. The powers are $3, 2, 6, 4, 5, 1$, because each power is $3$ times the previous one modulo $7$.
4. So the order of $3$ is $6$, and $6$ divides $6$.
5. Take $g = 6$. Then $6^2 = 36 \equiv 1 \pmod 7$, so the order of $6$ is $2$.

The typical use is to restrict the possible orders of elements.
For example, a group of order $15$ has no element of order $2$, because $2$ does not divide $15$.

A trap is to read the converse into the theorem.
The theorem does not say that each divisor of $|G|$ is the order of an element.

### L3 human

The theorem is Lagrange's theorem for the [[cyclic subgroup|08ABT85339]] $\langle g \rangle$.
In the language of group actions, $\langle g \rangle$ acts on $G$ by left multiplication, and each orbit is a right coset $\langle g \rangle x$ with $\operatorname{ord}(g)$ elements.
The stronger statement in Lean's Mathlib, `orderOf_dvd_natCard`, also covers infinite groups, because there $|G|$ is read as $0$, and each integer divides $0$.
The orders of the elements do not determine the group.
The group $(\mathbb{Z}/3\mathbb{Z})^3$ and the Heisenberg group of upper unitriangular $3 \times 3$ matrices over $\mathbb{F}_3$ both have order $27$.
In both groups, each of the $26$ elements other than $e$ has order $3$, but only the first group is abelian.
