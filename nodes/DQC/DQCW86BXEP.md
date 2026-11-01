---
tag: DQCW86BXEP
kind: definition
name: Subnormal subgroup
msc: [20D35, "20E15"]
defines: FKTQ1WBMKM
uses: [0X1JXT47GA, 0CB0DX5BVV]
sources:
  - url: https://en.wikipedia.org/wiki/Subnormal_subgroup
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
The subgroup $H$ is *subnormal* in $G$ when there are subgroups $H_0, H_1, \dots, H_n$ of $G$ with these properties.
First, $H_0 = H$ and $H_n = G$.
Second, $H_{i-1}$ is a [[normal subgroup|0CB0DX5BVV]] of $H_i$ for $1 \le i \le n$.
In symbols, $H = H_0 \trianglelefteq H_1 \trianglelefteq \cdots \trianglelefteq H_n = G$.

## Remarks

One writes $H \trianglelefteq\trianglelefteq G$.
The least such $n$ is the defect of $H$ in $G$; the subgroups of defect at most $1$ are the normal subgroups.
Example: in the alternating group $A_4$, let $V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ and $H = \{e, (1\,2)(3\,4)\}$.
Then $H \trianglelefteq V$ because $V$ is abelian, and $V \trianglelefteq A_4$, so $H$ is subnormal of defect $2$; it is not normal, since conjugation by $(1\,2\,3)$ sends $(1\,2)(3\,4)$ to $(2\,3)(1\,4)$.
Non-example: in the symmetric group $S_3$, the subgroup $H = \{e, (1\,2)\}$ is not subnormal.
The only subgroups of $S_3$ that contain $H$ are $H$ and $S_3$.
So a chain from $H$ to $S_3$ must contain a step $H \trianglelefteq S_3$, but $H$ is not normal in $S_3$.
In a [[nilpotent group|0Q7MMQHC1P]] every subgroup is subnormal.

## Explanations

### L1 human

A subgroup is subnormal when you can climb from it to the whole group by a ladder in which each rung is normal in the next one.
