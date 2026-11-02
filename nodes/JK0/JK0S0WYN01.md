---
tag: JK0S0WYN01
kind: definition
name: Proper morphism
msc: [14A15]
defines: 9537RKBZPP
uses: [JXRKH6P1Z4, X30G4V7VAJ, AHTE5DVX61, W0B0BBAH35, QZN6P7AG33]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_morphism
---

## Definition

Let $f \colon X \to Y$ be a [[morphism of schemes|JXRKH6P1Z4]].
The morphism $f$ is *proper* if it satisfies the following three conditions.

1. $f$ is [[separated|X30G4V7VAJ]].
2. $f$ is [[of finite type|AHTE5DVX61]].
3. $f$ is [[universally closed|W0B0BBAH35]].

## Remarks

Let $k$ be a field.
The structure morphism $\mathbb{P}^n_k \to \operatorname{Spec} k$ of projective $n$-space is proper.
It is separated and of finite type, and it is universally closed by the main theorem of elimination theory, which can also be derived from the [[valuative criterion|QZN6P7AG33]].
The structure morphism $\mathbb{A}^1_k \to \operatorname{Spec} k$ is separated and of finite type but not proper.
After base change along $\mathbb{A}^1_k \to \operatorname{Spec} k$ it becomes the projection $\mathbb{A}^2_k \to \mathbb{A}^1_k$, $(x, y) \mapsto x$.
This projection maps the closed curve $xy = 1$ onto $\mathbb{A}^1_k \setminus \set{0}$, which is not closed, so clause 3 fails.
Closed immersions and finite morphisms are proper, and proper morphisms are stable under composition and base change.
