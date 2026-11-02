---
tag: 46ESFR9MSE
kind: definition
name: Ample line bundle
msc: [14C20]
defines: RRK8P6TXG2
uses: [ND6XEY68P4, 7JCF2TE3V5, 56RXEJ8Z6S, V93Y0XYPZD]
sources:
  - url: https://en.wikipedia.org/wiki/Ample_line_bundle
---

## Definition

Let $X$ be a [[Noetherian scheme|ND6XEY68P4]] and let $\mathcal{L}$ be an [[invertible sheaf|7JCF2TE3V5]] on $X$.
Let $\mathcal{F}$ be a sheaf of $\mathcal{O}_X$-modules.
It is *globally generated* if for every $x \in X$ the images of $H^0(X, \mathcal{F})$ generate the stalk $\mathcal{F}_x$ as an $\mathcal{O}_{X,x}$-module.
The sheaf $\mathcal{L}$ is *ample* if the following holds for every [[coherent sheaf|56RXEJ8Z6S]] $\mathcal{F}$ on $X$.
There is an integer $n_0$ such that $\mathcal{F} \otimes \mathcal{L}^{\otimes n}$ is globally generated for all $n \ge n_0$.

## Remarks

If $X$ is of finite type over a Noetherian ring $A$, then $\mathcal{L}$ is ample if and only if $\mathcal{L}^{\otimes m}$ is very ample over $\operatorname{Spec} A$ for some $m \ge 1$.
Here very ample means $\mathcal{L}^{\otimes m} \cong i^*\mathcal{O}(1)$ for an immersion $i \colon X \to \mathbb{P}^N_A$.

Example: on $X = \mathbb{P}^n_k$ the [[twisting sheaf|V93Y0XYPZD]] $\mathcal{O}(1)$ is ample.
By a theorem of Serre, every coherent $\mathcal{F}$ on $\mathbb{P}^n_k$ has $\mathcal{F}(n)$ globally generated for $n$ large.

Non-example: on $\mathbb{P}^1_k$, $\mathcal{L} = \mathcal{O}(-1)$ is not ample.
Take $\mathcal{F} = \mathcal{O}_X$: then $\mathcal{L}^{\otimes n} = \mathcal{O}(-n)$ has no nonzero global sections for $n \ge 1$, so it is not globally generated.

Ampleness is preserved by positive tensor powers, and $\mathcal{L}$ is ample if and only if $\mathcal{L}^{\otimes m}$ is ample for one $m \ge 1$.
