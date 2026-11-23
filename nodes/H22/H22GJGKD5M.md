---
tag: H22GJGKD5M
kind: example
name: No two-valued truth table for the box gives the logic K
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: NGHWZ9Y7ZV
    note: a truth table reads the box from one truth value, with no worlds and no relation
  - target: CN7HK9K1B6
    note: a truth table reads the box from one truth value, not from the truth set of the formula
uses: [JS8W7PA6JK, NGHWZ9Y7ZV, CN7HK9K1B6, 05006AJ7DZ, G989VP2NGP, E87G6ZTMTN]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

Suppose that we read $\square$ by a unary truth function $f : \{ 0, 1 \} \to \{ 0, 1 \}$, so that the value of $\square\varphi$ is $f$ applied to the value of $\varphi$.
Call a formula $f$-valid when it gets the value $1$ under every assignment of values to the variables.
We show that for no $f$ is the set of $f$-valid formulas equal to the logic $\mathsf{K}$ of [[normal modal logic K|JS8W7PA6JK]].

1. There are $4$ functions $f$: the constant $0$, the constant $1$, the identity and the negation.
2. $\mathsf{K} \vdash \square\top$, by [[necessitation|G989VP2NGP]] from the [[tautology|05006AJ7DZ]] $\top$.
   The value of $\top$ is $1$, so $\square\top$ is $f$-valid only when $f(1) = 1$.
3. So the constant $0$ and the negation fail, because under them $\square\top$ gets the value $0$ although it is a theorem of $\mathsf{K}$.
4. Under the identity, $\square p \to p$ gets the value of $p \to p$, which is $1$, so $\square p \to p$ is $f$-valid.
5. But $\mathsf{K} \nvdash \square p \to p$.
   On one world without successors and with $V(p) = \varnothing$, $\square p$ is true and $p$ is false, and [[soundness|E87G6ZTMTN]] applies.
6. Under the constant $1$, $\square\bot$ gets the value $1$, so $\square\bot$ is $f$-valid.
7. But $\mathsf{K} \nvdash \square\bot$, because on one world $w$ with $w R w$ the formula $\square\bot$ is false at $w$.
8. So each of the $4$ choices either misses a theorem of $\mathsf{K}$ or adds a non-theorem.

## Remarks

The box of $\mathsf{K}$ is not truth-functional.
[[Kripke semantics|NGHWZ9Y7ZV]] solves this: the value of $\square\varphi$ at $w$ depends on the values of $\varphi$ at other worlds, the successors of $w$.
[[Neighborhood semantics|CN7HK9K1B6]] also makes the value depend on the whole truth set of $\varphi$, not on one truth value.

The two truth tables that respect necessitation describe the two frames with one world.
The identity is the reflexive point, and it gives the trivial logic, in which the box can be deleted.
The constant $1$ is the point with no successor, and it gives the verum logic, which contains $\square\bot$; see [[the trivial logic and the verum logic|5PZCVXYXDD]].
Both are sound for $\mathsf{K}$, and neither is complete for it.

More truth values do not help with Lewis's systems.
Dugundji proved in 1940 that none of the systems $\mathsf{S1}$ to $\mathsf{S5}$ is characterized by a finite matrix.

## Explanations

### L1 human

For "and" and "not", the truth of the whole is fixed by the truth of the parts.
For "necessarily", this is not so.
"Two plus two is four" and "it rains today" may both be true.
The first is necessary and the second is not.
So we cannot compute "necessarily $p$" from the truth value of $p$ alone.

### L2 human

Try $f$ equal to the identity on the formula $p \to \square p$.
Its value is that of $p \to p$, so it is $f$-valid.
On the frame with $W = \{ 1, 2 \}$ and $R = \{ (1, 2) \}$, put $V(p) = \{ 1 \}$.
Then $p$ is true at $1$ and $\square p$ is false at $1$, since $p$ fails at $2$, so $p \to \square p$ fails at $1$.
So the identity adds the non-theorem $p \to \square p$ as well.
The lesson is that an operator which is not truth-functional needs more than one point of evaluation, and that is the reason for possible worlds.
Watch out: a truth function can be sound for $\mathsf{K}$, as the identity is, without being complete for it.
