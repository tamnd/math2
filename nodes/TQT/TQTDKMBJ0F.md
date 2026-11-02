---
tag: TQTDKMBJ0F
kind: definition
name: Reverse mathematics
msc: [03B30, 03F35]
defines: 7SQS69T17R
uses: [DC60FYCSPM]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
---

## Definition

Let $\mathsf{RCA}_0$ be the subsystem of [[second-order arithmetic|DC60FYCSPM]] with the basic axioms, induction for $\Sigma^0_1$ formulas, and comprehension for $\Delta^0_1$ formulas.
A sentence $\tau$ of second-order arithmetic is *equivalent over* $\mathsf{RCA}_0$ to a subsystem $S$ if:

1. $S$ proves $\tau$;
2. $\mathsf{RCA}_0 + \tau$ proves every axiom of $S$.

*Reverse mathematics* is the study of which theorems of ordinary mathematics are provable in which subsystems of second-order arithmetic.
In particular, it studies equivalences over $\mathsf{RCA}_0$.

## Remarks

The big five subsystems are $\mathsf{RCA}_0$, $\mathsf{WKL}_0$ (adds weak König's lemma), $\mathsf{ACA}_0$ (arithmetical comprehension), $\mathsf{ATR}_0$ (arithmetical transfinite recursion) and $\Pi^1_1\text{-}\mathsf{CA}_0$ ($\Pi^1_1$ comprehension), each stronger than the one before.

Example: the Bolzano–Weierstrass theorem for sequences in $[0,1]$ is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
The Heine–Borel theorem for countable covers of $[0,1]$ by open intervals is equivalent to $\mathsf{WKL}_0$ over $\mathsf{RCA}_0$.

Non-example: weak König's lemma is provable in $\mathsf{ACA}_0$ but not equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
Clause 2 fails, because $\mathsf{WKL}_0$ does not prove arithmetical comprehension.

The models of $\mathsf{RCA}_0$ with the standard natural numbers include the one whose sets are the computable sets, so $\mathsf{RCA}_0$ corresponds to computable mathematics.
