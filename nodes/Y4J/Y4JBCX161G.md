---
tag: Y4JBCX161G
kind: definition
name: Non-atomic measure
msc: [28A12]
defines: SV96KN4WR9
uses: [P15VQS5DJ9, PR11BZQQPG, 0ACRGYNHSR]
sources:
  - url: https://en.wikipedia.org/wiki/Atom_(measure_theory)
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
An *atom* of $\mu$ is a set $A \in \Sigma$ with $\mu(A) > 0$ such that for every $B \in \Sigma$ with $B \subseteq A$, either $\mu(B) = 0$ or $\mu(A \setminus B) = 0$.
The [[measure|PR11BZQQPG]] $\mu$ is *non-atomic*, or *atomless*, if it has no atoms.

## Remarks

Lebesgue measure $\lambda$ on $\R$ is non-atomic.
If $\lambda(A) > 0$, the function $t \mapsto \lambda(A \cap (-\infty, t])$ is continuous and increases from $0$ to $\lambda(A)$.
So there is $t$ with $B = A \cap (-\infty, t]$ such that $\lambda(B) > 0$ and $\lambda(A \setminus B) > 0$.
The [[Dirac measure|0ACRGYNHSR]] $\delta_x$ is not non-atomic, since $\set{x}$ is an atom: its only measurable subsets are $\varnothing$ and $\set{x}$.
Some authors define an atom by the condition that every measurable $B \subseteq A$ has $\mu(B) = 0$ or $\mu(B) = \mu(A)$.
For sets $A$ of finite measure the two conditions agree.
