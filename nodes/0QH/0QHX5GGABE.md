---
tag: 0QHX5GGABE
kind: definition
name: Affine map
msc: [51N10]
defines: 0JF0TVYGWT
uses: [09XNAPTJQ7]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_transformation
    locator: Definition
---

## Definition

Let $K$ be a field. Let $A$ be an [[affine space|09XNAPTJQ7]] over a $K$-vector space $V$, and let $B$ be an affine space over a $K$-vector space $W$.
A map $f : A \to B$ is an affine map if there is a linear map $L : V \to W$ such that
$$f(p + v) = f(p) + L(v) \quad \text{for each point } p \text{ of } A \text{ and each vector } v \text{ of } V.$$
The map $L$ is unique. It is the linear part of $f$, and it satisfies $L(q - p) = f(q) - f(p)$ for all points $p$ and $q$ of $A$.

## Remarks

The affine maps from $\mathbb{R}^n$ to $\mathbb{R}^m$ are the maps $x \mapsto M x + b$, with $M$ a real $m \times n$ matrix and $b$ a vector of $\mathbb{R}^m$.
An affine map keeps [[affine combinations|0KJH6SRFZK]]. In particular it sends [[midpoints|0S706JBZBG]] to midpoints.
An affine transformation is a bijective affine map from $A$ to itself. The affine transformations of $A$ form a group under composition.
Mathlib's `AffineMap` is this notion, with the linear part as a field of the structure.

## Explanations

### L1 human

An affine map is a linear map that may also shift the origin. In the plane, examples are rotations, stretches, shears and translations, and the compositions of these. A grid of squares goes to a grid of parallelograms.
