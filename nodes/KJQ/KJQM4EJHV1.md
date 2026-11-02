---
tag: KJQM4EJHV1
kind: definition
name: Projective morphism
msc: [14A15]
defines: Z5G47MQ99B
uses: [JXRKH6P1Z4, WWRWYSJDET, 1DZMT4S9FB, A39XQHCVNW, ZT9A6JK8QF, 9537RKBZPP]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_algebraic_geometry
---

## Definition

Let $Y$ be a scheme and let $n \ge 0$ be an integer.
Let $\mathbb{P}^n_{\Z} = \operatorname{Proj} \Z[x_0, \dots, x_n]$ be [[projective space|ZT9A6JK8QF]] over $\Z$, given by the [[Proj construction|A39XQHCVNW]].
Let $\mathbb{P}^n_Y = \mathbb{P}^n_{\Z} \times_{\operatorname{Spec} \Z} Y$ be the [[fiber product|1DZMT4S9FB]], with projection $p \colon \mathbb{P}^n_Y \to Y$.
A [[morphism of schemes|JXRKH6P1Z4]] $f \colon X \to Y$ is *projective* if $f = p \circ i$ for some $n \ge 0$ and some [[closed immersion|WWRWYSJDET]] $i \colon X \to \mathbb{P}^n_Y$.

## Remarks

For a field $k$ and a homogeneous polynomial $F \in k[x_0, x_1, x_2]$ of positive degree, the curve $X = V(F) \subseteq \mathbb{P}^2_k$ is projective over $\operatorname{Spec} k$.
Indeed, $X \to \mathbb{P}^2_k$ is a closed immersion and $\mathbb{P}^2_k \to \operatorname{Spec} k$ is the projection $p$.
The affine line $\mathbb{A}^1_k \to \operatorname{Spec} k$ is not projective.
A projective morphism is [[proper|9537RKBZPP]], and $\mathbb{A}^1_k$ is not proper over $k$.
This is the definition in Hartshorne's textbook.
In EGA the definition is more general: $X$ is a closed subscheme of the projective bundle of a quasi-coherent $\mathcal{O}_Y$-module of finite type.
The two definitions agree when $Y$ is affine.
