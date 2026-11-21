---
tag: J6ZSWZ0CC1
kind: definition
name: Universal model
msc: ["03C50"]
topics: [Z772KEC9BY]
audience: grad
defines: F30ZVR4AD5
uses: [983GZBQYT4, P3B1V182N4, CGH8C8EA9N, 0EBACQFAZW, 4NJS7W57VK, XXM7GN1C92, RMTZ5J64FX, 8R31F7BQGY]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Definition

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] with domain $M$, and let $\kappa$ be an infinite [[cardinal|0EBACQFAZW]].

1. $\mathcal{M}$ is *$\kappa$-universal* if for every $L$-structure $\mathcal{N}$ with $\mathcal{N} \equiv \mathcal{M}$ and $\abs{N} < \kappa$ there is an [[elementary embedding|CGH8C8EA9N]] $g : \mathcal{N} \to \mathcal{M}$.
2. $\mathcal{M}$ is *universal* if it is $\abs{M}^+$-universal.

Here $\mathcal{N} \equiv \mathcal{M}$ means that the two structures are [[elementarily equivalent|P3B1V182N4]].

## Notation

Some sources use "$\kappa$-universal" for the condition with $\abs{N} \le \kappa$.

## Remarks

The main page of the idea is [[universal model|F30ZVR4AD5]].
We prove that a countable [[homogeneous|4NJS7W57VK]] and universal structure $\mathcal{M}$ in a countable language is [[saturated|RMTZ5J64FX]].

1. Let $A \subseteq M$ be finite and let $p \in S_1(A)$.
2. By [[realizing types|8R31F7BQGY]], some countable $\mathcal{N} \succeq \mathcal{M}$ has an element $b$ that realizes $p$.
3. By universality, there is an elementary embedding $g : \mathcal{N} \to \mathcal{M}$.
4. The map $h : g(A) \to A$ with $h(g(a)) = a$ is partial elementary in $\mathcal{M}$, since $g$ is elementary and $\mathcal{M} \preceq \mathcal{N}$.
5. By homogeneity, $h$ extends to a partial elementary map $h'$ with $g(b)$ in its domain. Let $c = h'(g(b))$.
6. For $\varphi(x, \bar{a}) \in p$: $\mathcal{N} \models \varphi(b, \bar{a})$, so $\mathcal{M} \models \varphi(g(b), g(\bar{a}))$, so $\mathcal{M} \models \varphi(c, \bar{a})$. So $c$ realizes $p$.

Example: $(\Q, <)$ is universal, by Cantor's theorem.

Non-example: the field $\overline{\Q}$ is not universal; see [[the algebraic numbers are not saturated|9JGR3GXPMK]].

## Explanations

### L1 human

A universal structure contains a faithful copy of every structure of the same theory that is not larger.

### L2 human

To prove that $\mathcal{M}$ is not universal, find a model $\mathcal{N} \equiv \mathcal{M}$ with $\abs{N} \le \abs{M}$ that realizes a type over $\emptyset$ omitted in $\mathcal{M}$.

1. An elementary embedding preserves the type of each element.
2. So the image of a realization in $\mathcal{N}$ would realize the same type in $\mathcal{M}$.

The trap is to use ordinary embeddings, which preserve only quantifier-free formulas.
