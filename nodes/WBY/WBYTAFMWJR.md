---
tag: WBYTAFMWJR
kind: definition
name: Commutator theory
msc: [08A30, 08B10]
defines: 6DSWPHSWQW
uses: [DCSXXT4SER, N9M2N27END]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_algebra
---

## Definition

Let $A$ be an algebra and let $\alpha$, $\beta$, $\delta$ be [[congruences|DCSXXT4SER]] of $A$.
The congruence $\alpha$ *centralizes* $\beta$ *modulo* $\delta$, written $C(\alpha, \beta; \delta)$, if the following holds.
For every $n \ge 1$, every $(n+1)$-ary [[term operation|N9M2N27END]] $t$ of $A$, every pair $(a, b) \in \alpha$ and all tuples $\bar{c} = (c_1, \dots, c_n)$ and $\bar{d} = (d_1, \dots, d_n)$ with $(c_i, d_i) \in \beta$ for each $i$:
$$t(a, \bar{c}) \mathrel{\delta} t(a, \bar{d}) \implies t(b, \bar{c}) \mathrel{\delta} t(b, \bar{d}).$$
The *commutator* $[\alpha, \beta]$ is the least congruence $\delta$ of $A$ such that $C(\alpha, \beta; \delta)$.

## Remarks

The least such $\delta$ exists: $C(\alpha, \beta; 1_A)$ holds for the full congruence $1_A$, and if $C(\alpha, \beta; \delta_i)$ holds for every $i$, then $C(\alpha, \beta; \bigcap_i \delta_i)$ holds.
The definition is often called the term condition, and this commutator the term-condition commutator.
Example: in a group $G$, let $\alpha$ and $\beta$ be the congruences of normal subgroups $M$ and $N$.
Then $[\alpha, \beta]$ is the congruence of the commutator subgroup $[M, N]$.
In particular $[1_G, 1_G]$ is the congruence of the [[commutator subgroup|0ASGSTXSBW]] of $G$.
Non-example of $C(1_G, 1_G; 0_G)$: let $G$ be a nonabelian group with $b c \ne c b$, and let $t(x, y) = x y x^{-1} y^{-1}$.
With $a = e$, $\bar{c} = c$ and $\bar{d} = e$, both $t(e, c)$ and $t(e, e)$ equal $e$, but $t(b, c) = b c b^{-1} c^{-1} \ne e = t(b, e)$.
In a congruence-modular variety the commutator is symmetric, $[\alpha, \beta] = [\beta, \alpha]$, and $[\alpha, \beta] \le \alpha \wedge \beta$.

## Explanations

### L1 human

The commutator of two congruences is the smallest congruence that makes them commute with each other inside all term operations.
