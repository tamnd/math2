---
tag: BND6A96S3D
kind: definition
name: Heyting algebra
msc: ["06D20", "03G10", "03B20"]
defines: NG943XNQWH
uses: [0QV2JS9RJ3, 0HM0HQCK6N, 0XADJKM699, 0CQHFPGJ45, 02BH3MCBQB, 0RZH6W98HK]
sources:
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
---

## Definition

A *Heyting algebra* is a structure $(H, \wedge, \vee, \to, 0, 1)$ such that:

1. $(H, \wedge, \vee, 0, 1)$ is a bounded lattice, with [[partial order|0QV2JS9RJ3]] $a \le b$ if and only if $a \wedge b = a$, least element $0$ and greatest element $1$.
2. $\to$ is a binary operation on $H$.
3. For all $a, b, c \in H$, $c \le (a \to b)$ if and only if $c \wedge a \le b$.

The *pseudocomplement* of $a$ is $\neg a = a \to 0$.

## Remarks

Clause 3 says that $a \to b$ is the largest element $c$ with $c \wedge a \le b$, so $\to$ is determined by the lattice.

Example: let $X$ be a [[topological space|0CQHFPGJ45]] and let $H$ be the set of its [[open sets|02BH3MCBQB]], with $\wedge = \cap$, $\vee = \cup$, $0 = \emptyset$, $1 = X$, and $U \to V$ the [[interior|0RZH6W98HK]] of $(X \setminus U) \cup V$.
For an open set $W$, the inclusion $W \subseteq (X \setminus U) \cup V$ holds if and only if $W \cap U \subseteq V$.
Since $W$ is open, the first inclusion holds if and only if $W$ lies in the interior; this is clause 3.

Non-example: the five-element lattice $M_3$ has a least element, a greatest element and three pairwise incomparable elements between them.
It is a bounded lattice but carries no operation $\to$ satisfying clause 3.
Indeed, every Heyting algebra is a [[distributive lattice|0HM0HQCK6N]], and $M_3$ is not distributive.

A [[Boolean algebra|0XADJKM699]] is a Heyting algebra with $a \to b = \neg a \vee b$, and a Heyting algebra is Boolean if and only if $a \vee \neg a = 1$ for all $a$.
Every finite distributive lattice is a Heyting algebra.
