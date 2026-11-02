---
tag: JKXTT55WCV
kind: definition
name: End and coend
msc: [18A30, 18A23]
defines: W9QTFV0Z8D
uses: [A2DE66937D, DAMK8XE1FR, AFNE9C4NH6, 28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/End_(category_theory)
---

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be [[categories|A2DE66937D]], and let $S \colon \mathcal{C}^{\mathrm{op}} \times \mathcal{C} \to \mathcal{D}$ be a [[functor|28NQ0KRHD3]] on the [[product|AFNE9C4NH6]] of the [[opposite category|DAMK8XE1FR]] with $\mathcal{C}$.

A *wedge* to $S$ is an object $w$ of $\mathcal{D}$ with morphisms $e_c \colon w \to S(c, c)$ for all objects $c$.
They must satisfy $S(c, f) \circ e_c = S(f, c') \circ e_{c'}$ for every morphism $f \colon c \to c'$ of $\mathcal{C}$.
An *end* of $S$ is a wedge $(E, e)$ such that every wedge $(w, e')$ factors as $e'_c = e_c \circ u$ for a unique $u \colon w \to E$.

A *cowedge* from $S$ is an object $w$ with morphisms $\omega_c \colon S(c, c) \to w$.
They must satisfy $\omega_c \circ S(f, c) = \omega_{c'} \circ S(c', f)$ for every $f \colon c \to c'$.
A *coend* of $S$ is a cowedge $(E, \omega)$ such that every cowedge $(w, \omega')$ factors as $\omega'_c = u \circ \omega_c$ for a unique $u \colon E \to w$.

## Remarks

The end is written $\int_{c} S(c, c)$ and the coend $\int^{c} S(c, c)$.
Both are unique up to a unique isomorphism.
For $\mathcal{C}$ small and $\mathcal{D}$ complete, the end is the equalizer of two maps $\prod_c S(c, c) \rightrightarrows \prod_{f \colon c \to c'} S(c, c')$.

Example: let $F, G \colon \mathcal{C} \to \mathcal{E}$ be functors with $\mathcal{C}$ small and $\mathcal{E}$ locally small, and let $S(c, c') = \Hom_{\mathcal{E}}(F c, G c')$ in $\mathbf{Set}$.
A wedge from a one-point set is a family $\alpha_c \colon F c \to G c$ with $G f \circ \alpha_c = \alpha_{c'} \circ F f$, that is, a natural transformation.
So $\int_c \Hom(F c, G c)$ is the set of natural transformations $F \Rightarrow G$.

Non-example: in the same setting, the set $\prod_c \Hom(F c, G c)$ of all families, with its projections, is in general not a wedge.
The wedge condition would require every family $(\alpha_c)$ to be natural.
It fails as soon as some family has $G f \circ \alpha_c \neq \alpha_{c'} \circ F f$ for some $f \colon c \to c'$.
