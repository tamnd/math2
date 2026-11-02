---
tag: 7ERFZS0NJJ
kind: definition
name: Finite morphism
msc: [14A15]
defines: N9C4X7XKE4
uses: [JXRKH6P1Z4, B3V3XJ2W8G, 05QY1VEBYD, 1NBACAEC2V, AFC6JMYWEH, H20P600HQS]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_morphism
---

## Definition

A [[morphism of schemes|JXRKH6P1Z4]] $f \colon X \to Y$ is *finite* if there is a cover of $Y$ by open [[affine|B3V3XJ2W8G]] subschemes $V_i = \operatorname{Spec} B_i$ such that, for each $i$:

1. $f^{-1}(V_i)$ is an affine scheme $\operatorname{Spec} A_i$;
2. $A_i$, made into a $B_i$-module by the ring map $B_i \to A_i$ of $f$, is a [[finitely generated module|05QY1VEBYD]].

## Remarks

If $f$ is finite, then clauses 1 and 2 hold for every open affine $V \subseteq Y$.
A morphism $\operatorname{Spec} A \to \operatorname{Spec} B$ is finite if and only if $B \to A$ is a [[finite morphism of rings|1NBACAEC2V]].
A finite morphism is [[affine|AFC6JMYWEH]] and of finite type.
Example: for a field $k$, the morphism $\mathbb{A}^1_k \to \mathbb{A}^1_k$ given by $k[x] \to k[t]$, $x \mapsto t^2$, is finite, since $k[t] = k[x] \cdot 1 + k[x] \cdot t$.
Non-example: the open immersion $\operatorname{Spec} k[x, x^{-1}] \to \operatorname{Spec} k[x]$ satisfies clause 1 but not clause 2.
If $k[x, x^{-1}]$ were a finite $k[x]$-module, then $x^{-1}$ would be integral over $k[x]$.
Since $k[x]$ is an [[integrally closed domain|H20P600HQS]], this would give $x^{-1} \in k[x]$, which is false.
