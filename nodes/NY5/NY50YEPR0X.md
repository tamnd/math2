---
tag: NY50YEPR0X
kind: definition
name: Projective hierarchy
msc: ["03E15", "54H05"]
defines: 8DZTNVTGY2
uses: [584GXXY73M, P2WS16HKD7, 3RWWZYPAFV]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_hierarchy
---

## Definition

Let $\mathcal{N} = \N^\N$ be the [[Baire space|P2WS16HKD7]].
For each [[Polish space|584GXXY73M]] $X$, define classes of subsets of $X$ by recursion on $n \ge 1$:

1. $\Sigma^1_1$ is the class of [[analytic subsets|3RWWZYPAFV]] of $X$.
2. $\Pi^1_n$ is the class of complements $X \setminus A$ of sets $A$ in $\Sigma^1_n$.
3. $\Sigma^1_{n+1}$ is the class of projections $\set{x \in X : \exists y \in \mathcal{N} \, (x, y) \in C}$ of sets $C \subseteq X \times \mathcal{N}$ in the class $\Pi^1_n$ of the Polish space $X \times \mathcal{N}$.
4. $\Delta^1_n = \Sigma^1_n \cap \Pi^1_n$.

A subset of $X$ is *projective* if it lies in $\Sigma^1_n$ for some $n$.
This system of classes is the *projective hierarchy*.

## Remarks

The coanalytic sets form $\Pi^1_1$, and by Suslin's theorem $\Delta^1_1$ is the class of Borel sets.
Example: the set of $x \in \set{0, 1}^{\N \times \N}$ that code a well-order of $\N$ is in $\Pi^1_1$ but not in $\Sigma^1_1$.
Non-example by counting: there are only $2^{\aleph_0}$ projective subsets of $\R$, and $2^{2^{\aleph_0}}$ subsets in all, so some subset of $\R$ is not projective.
Each class $\Sigma^1_n$ and $\Pi^1_n$ is closed under countable unions, countable intersections and preimages by continuous maps, and $\Sigma^1_n \cup \Pi^1_n \subseteq \Delta^1_{n+1}$.
If $X$ is uncountable, then $\Sigma^1_n \neq \Pi^1_n$ for every $n$.
The lightface version, defined with recursive codes instead of arbitrary parameters, is part of the [[analytical hierarchy|M6JGF4TPM6]].
