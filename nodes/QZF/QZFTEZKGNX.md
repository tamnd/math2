---
tag: QZFTEZKGNX
kind: definition
name: Locally presentable category
msc: [18C35]
defines: PZHDNJ2J73
uses: [FC8C0V4TFZ, BJS1CGTKQ5, 13ZV2F8JAR]
sources:
  - url: https://en.wikipedia.org/wiki/Accessible_category
---

## Definition

Let $\lambda$ be a [[regular cardinal|13ZV2F8JAR]] and let $\mathcal{C}$ be a locally small category.
The category $\mathcal{C}$ is *locally $\lambda$-presentable* if both conditions hold.

1. $\mathcal{C}$ is $\lambda$-[[accessible|FC8C0V4TFZ]].
2. $\mathcal{C}$ has all small [[colimits|BJS1CGTKQ5]].

The category $\mathcal{C}$ is *locally presentable* if it is locally $\lambda$-presentable for some regular cardinal $\lambda$.

## Remarks

Equivalently, $\mathcal{C}$ is cocomplete and has a set $S$ of $\lambda$-presentable objects such that every object is a $\lambda$-filtered colimit of objects of $S$.
For $\lambda = \aleph_0$ one says locally finitely presentable.

Example: the category of sets is locally finitely presentable.
It is cocomplete, and it is finitely accessible because every set is the filtered colimit of its finite subsets, which are finitely presentable.

Non-example: the category of fields and field homomorphisms is accessible but not locally presentable.
It has no initial object, which is the colimit of the empty diagram.
An initial field would map to both $\Q$ and $\F_2$, but a field homomorphism preserves the characteristic.
So clause 2 fails.

A locally presentable category is also complete, well-powered and co-well-powered.
