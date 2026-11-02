---
tag: FPK5ZH7FKC
kind: definition
name: Unramified morphism
msc: [14A15, "14E22"]
defines: 1JQX6HD8E5
uses: [JXRKH6P1Z4, AHTE5DVX61, G51E8MW7J1, MZ02BKPHJA, 0WCX7NB4N7, 7HCFARHG7D]
sources:
  - url: https://en.wikipedia.org/wiki/Unramified_morphism
---

## Definition

Let $f \colon X \to Y$ be a [[morphism of schemes|JXRKH6P1Z4]] that is locally [[of finite type|AHTE5DVX61]].
For $x \in X$ and $y = f(x)$, let $\mathfrak{m}_x$ and $\mathfrak{m}_y$ be the maximal ideals of the [[local rings|MZ02BKPHJA]] $\mathcal{O}_{X,x}$ and $\mathcal{O}_{Y,y}$.
Let $\kappa(x)$ and $\kappa(y)$ be the [[residue fields|G51E8MW7J1]].
The morphism $f$ is *unramified at $x$* if the following two conditions hold.

1. $\mathfrak{m}_y \mathcal{O}_{X,x} = \mathfrak{m}_x$.
2. $\kappa(x)$ is a finite [[separable extension|0WCX7NB4N7]] of $\kappa(y)$.

The morphism $f$ is *unramified* if it is unramified at every point of $X$.

## Remarks

An open immersion or a closed immersion is unramified.
For a closed immersion, each $\mathcal{O}_{X,x}$ is a quotient of $\mathcal{O}_{Y,y}$, so both conditions hold with $\kappa(x) = \kappa(y)$.
For a field $k$ of characteristic not $2$, the map $\operatorname{Spec} k[t] \to \operatorname{Spec} k[s]$ given by $s \mapsto t^2$ is not unramified at $t = 0$.
There $\mathfrak{m}_y \mathcal{O}_{X,x} = (t^2)$, which is strictly smaller than $\mathfrak{m}_x = (t)$, so condition 1 fails.
For $f$ locally of finite type, $f$ is unramified exactly when the sheaf of relative [[Kähler differentials|7HCFARHG7D]] $\Omega_{X/Y}$ is zero.
Some authors, as in EGA, also require $f$ to be locally of finite presentation.
The ring version of this notion is an [[unramified morphism of rings|GY3QA6NH0E]].
