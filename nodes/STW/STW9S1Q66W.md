---
tag: STW9S1Q66W
kind: definition
name: Inductive dimension
msc: [54F45]
defines: MKS9H497AM
uses: [0CQHFPGJ45, 05D5EGMFYV, 02BH3MCBQB, 0ZCK8DQYN1]
sources:
  - url: https://en.wikipedia.org/wiki/Inductive_dimension
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]], and write $\partial V$ for the [[boundary|05D5EGMFYV]] of a set $V \subseteq X$.
The *small inductive dimension* $\operatorname{ind} X$ is defined by induction on $n \ge -1$:

1. $\operatorname{ind} X = -1$ if and only if $X = \emptyset$.
2. For $n \ge 0$, $\operatorname{ind} X \le n$ if for every point $x \in X$ and every [[open set|02BH3MCBQB]] $U$ with $x \in U$ there is an open set $V$ with $x \in V \subseteq U$ and $\operatorname{ind} \partial V \le n - 1$.
3. $\operatorname{ind} X = n$ if $\operatorname{ind} X \le n$ and not $\operatorname{ind} X \le n - 1$; and $\operatorname{ind} X = \infty$ if $\operatorname{ind} X \le n$ holds for no $n$.

The *large inductive dimension* $\operatorname{Ind} X$ is defined in the same way, with a new clause 2.
For $n \ge 0$, $\operatorname{Ind} X \le n$ if for every [[closed set|0ZCK8DQYN1]] $A$ and every open set $U \supseteq A$ there is an open set $V$ with $A \subseteq V \subseteq U$ and $\operatorname{Ind} \partial V \le n - 1$.
Here the boundary $\partial V$ carries the subspace topology.

## Remarks

The rational numbers $\Q$ have $\operatorname{ind} \Q = 0$.
Given $x \in U$, choose irrational numbers $a < x < b$ with $(a, b) \cap \Q \subseteq U$; then $V = (a, b) \cap \Q$ is open and closed in $\Q$, so $\partial V = \emptyset$.
The real line has $\operatorname{ind} \R = 1$.
Small open intervals have a two-point boundary, which has dimension $0$, so $\operatorname{ind} \R \le 1$.
But $\operatorname{ind} \R \le 0$ fails: a nonempty open set $V \neq \R$ has nonempty boundary, because $\R$ is connected.
For separable metric spaces, $\operatorname{ind} X = \operatorname{Ind} X = \dim X$, where $\dim$ is the [[Lebesgue covering dimension|A3W7RGXXK9]].

## Explanations

### L1 human

A space has inductive dimension at most $n$ when small pieces of it can be cut out by walls of dimension at most $n - 1$.
