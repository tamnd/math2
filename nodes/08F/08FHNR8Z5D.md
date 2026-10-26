---
tag: 08FHNR8Z5D
kind: definition
name: Group of units of a monoid
msc: [20M10]
defines: 0FJ90Y9926
uses: [0R47MAD57S, 0BRHKKP333]
sources:
  - url: https://en.wikipedia.org/wiki/Unit_(ring_theory)
    locator: Group of units
---

## Definition

Let $(M, \ast, e)$ be a [[monoid|0N6R902FG1]].
An element $u \in M$ is a unit when it has a two-sided [[inverse|0ZNZH0EXFX]], that is, an element $v \in M$ with $u \ast v = v \ast u = e$.
The group of units of $M$ is the set $M^\times$ of the units of $M$, with the operation $\ast$ restricted to $M^\times$.
It is a [[group|G5S1M9]] with identity $e$.

## Remarks

The units of the monoid $(\mathbb{Z}, \cdot)$ are $1$ and $-1$.
The units of the monoid of $n \times n$ real matrices under multiplication are the invertible matrices, and they form the general linear group $\mathrm{GL}_n(\mathbb{R})$.
For a ring $R$, the group of units $R^\times$ is the group of units of the monoid $(R, \cdot)$.

## Explanations

### L1 human

In a monoid, some elements can be undone and others cannot.
The elements that can be undone are the units.
The units alone form a group, because products and inverses of units are units.
