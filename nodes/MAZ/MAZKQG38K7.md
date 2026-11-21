---
tag: MAZKQG38K7
kind: proof
name: Proof of the existence of existentially closed models by chains
msc: ["03C25"]
topics: [1A9JSC5YG8]
audience: grad
proves: 9DCXP1F8V1
uses: [60HQMM380F, K0PXB1979D, 484M0TZ1S7, C9494XYEMN, 8WZF9SBP39]
methods: [01XM7JEKHY, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraically_closed_group
    locator: Known results
  - book: isbn:9780521587136
---

## Proof

Let $T$, $L$, $\kappa$ and $M$ be as in the statement, and let $\lambda = \abs{M} + \kappa$.
All models below are models of $T$, and "existential formula" means an existential formula with parameters.

### One round

Let $A$ be a model of $T$ of size at most $\lambda$.
We build a model $A^* \supseteq A$ of size at most $\lambda$ such that: if an existential formula $\varphi$ with parameters in $A$ is true in some model $B \supseteq A^*$, then $\varphi$ is true in $A^*$.

1. There are at most $\lambda$ existential formulas with parameters in $A$. List them as $(\varphi_\alpha)_{\alpha < \lambda}$.
2. Put $A_0 = A$. At a limit stage $\delta$, let $A_\delta = \bigcup_{\alpha < \delta} A_\alpha$, which is a model since $T$ is [[inductive|K0PXB1979D]].
3. At stage $\alpha + 1$: if some model $B \supseteq A_\alpha$ satisfies $\varphi_\alpha$, choose such a $B$ and a witness $\bar b$ for $\varphi_\alpha$ in $B$.
4. By the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]], there is an [[elementary substructure|8WZF9SBP39]] $A_{\alpha + 1} \preceq B$ of size at most $\lambda$ that contains $A_\alpha$ and $\bar b$. It is a model of $T$, and $\varphi_\alpha$ is true in it.
5. If no such $B$ exists, put $A_{\alpha + 1} = A_\alpha$.
6. Let $A^* = \bigcup_{\alpha < \lambda} A_\alpha$. It is a model of $T$, since $T$ is inductive, and its size is at most $\lambda \cdot \lambda = \lambda$.
7. Let $\varphi = \varphi_\alpha$ be true in some model $B \supseteq A^*$. Then $B \supseteq A_\alpha$, so the condition of step 3 held at stage $\alpha + 1$, and $\varphi_\alpha$ is true in $A_{\alpha + 1}$.
8. Existential formulas go up from a substructure to a larger structure, by [[this result|C9494XYEMN]]. So $\varphi$ is true in $A^*$.

### Many rounds

1. Put $M_0 = M$ and $M_{n + 1} = (M_n)^*$ for each $n \in \N$. This is a chain of models of size at most $\lambda$.
2. Let $N = \bigcup_n M_n$. It is a model of $T$, since $T$ is inductive, and $\abs{N} \le \lambda$.
3. Let $B \supseteq N$ be a model, and let $\varphi$ be an existential formula with parameters $\bar a$ in $N$ that is true in $B$.
4. The tuple $\bar a$ is finite, so $\bar a$ lies in some $M_n$. Since $B \supseteq M_{n+1} = (M_n)^*$, the first part gives that $\varphi$ is true in $M_{n+1}$.
5. Existential formulas go up, so $\varphi$ is true in $N$.
6. So $N$ is an [[existentially closed model|60HQMM380F]] of $T$, $M \subseteq N$, and $\abs{N} \le \abs{M} + \kappa$.

## Idea

Each round solves, in some extension, every existential formula over the current model that can be solved at all.
Inductivity keeps the unions of the chains inside the class of models, and the Löwenheim-Skolem theorem keeps the size small.
After $\omega$ rounds every finite set of parameters lies in a model whose next round has solved all its formulas.

## Variants

When $L$ and $M$ are countable, the proof can be organized as one chain of length $\omega$, with a list of all pairs (stage, formula) of order type $\omega$.
For groups, step 3 can use explicit amalgamated free products and HNN extensions in place of an arbitrary $B$, which gives the classical embedding of every group into an algebraically closed group.
