---
tag: RMH7ZQ2F40
kind: definition
name: Borel hierarchy
msc: ["03E15", "54H05", "28A05"]
defines: 4P4Z4ZGXCY
uses: [584GXXY73M, 0YSCSX5YZC, 0WQXY32Q8D]
sources:
  - url: https://en.wikipedia.org/wiki/Borel_hierarchy
---

## Definition

Let $X$ be a [[Polish space|584GXXY73M]], and let $\omega_1$ be the first uncountable [[ordinal|0YSCSX5YZC]].
Define classes of subsets of $X$ by recursion on $\alpha$ with $1 \le \alpha < \omega_1$:

1. $\Sigma^0_1$ is the class of open subsets of $X$.
2. For $\alpha \ge 1$, $\Pi^0_\alpha$ is the class of complements $X \setminus A$ of sets $A$ in $\Sigma^0_\alpha$.
3. For $\alpha > 1$, $\Sigma^0_\alpha$ is the class of countable unions $\bigcup_{n} A_n$ with each $A_n$ in $\Pi^0_{\beta_n}$ for some $\beta_n < \alpha$.
4. For $\alpha \ge 1$, $\Delta^0_\alpha = \Sigma^0_\alpha \cap \Pi^0_\alpha$.

This system of classes is the *Borel hierarchy* of $X$.

## Remarks

The class $\Pi^0_1$ is the class of closed sets, $\Sigma^0_2$ is the class of $F_\sigma$ sets, and $\Pi^0_2$ is the class of $G_\delta$ sets.
In $X = \R$, the set $\Q$ is in $\Sigma^0_2$, as the countable union of the closed sets $\set{q}$.
It is not in $\Pi^0_2$, since by the Baire category theorem a dense $G_\delta$ subset of $\R$ is uncountable.
Every class satisfies $\Sigma^0_\alpha \cup \Pi^0_\alpha \subseteq \Delta^0_{\alpha + 1}$, and the union of all the classes $\Sigma^0_\alpha$ is the [[Borel sigma-algebra|0WQXY32Q8D]] of $X$.
A non-example: an analytic set that is not Borel lies in no class of the hierarchy.
If $X$ is uncountable, then $\Sigma^0_\alpha \neq \Pi^0_\alpha$ for every $\alpha$, so the hierarchy does not collapse.
The same definition works in any metrizable space; metrizability is used to show that closed sets are $G_\delta$ sets.
