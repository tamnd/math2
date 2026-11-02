---
tag: TMBCW25DZ4
kind: definition
name: Scott continuity
msc: [06B35, 68Q55]
defines: C6GAHS1Z2P
uses: [0QV2JS9RJ3, D9RY4667K6, 0R3H5PANRQ, 0A7KV2WB7A, ZR8A03FV67, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Scott_continuity
---

## Definition

Let $P$ and $Q$ be [[partially ordered sets|0QV2JS9RJ3]].
A map $f \colon P \to Q$ is *Scott-continuous* if it satisfies the following.
For every [[directed subset|D9RY4667K6]] $D \subseteq P$ with a [[supremum|0R3H5PANRQ]] $\bigvee D$ in $P$, the image $f(D)$ has a supremum in $Q$ and
$$f\left(\bigvee D\right) = \bigvee f(D).$$

## Remarks

A Scott-continuous map is [[monotone|0A7KV2WB7A]]: if $x \le y$, apply the definition to $D = \set{x, y}$, whose supremum is $y$, to get $f(x) \le f(y)$.
A map $f$ is Scott-continuous if and only if it is [[continuous|0X3WGX95FE]] for the [[Scott topologies|ZR8A03FV67]] on $P$ and $Q$.
Example: on the power set of $\N$, the map $A \mapsto A \cup \set{0}$; the image of the union of a directed family $D$ is $\bigcup_{A \in D} (A \cup \set{0})$.
Non-example: on the power set of $\N$, let $f(A) = \N$ if $A$ is infinite and $f(A) = \varnothing$ if $A$ is finite.
This map is monotone but not Scott-continuous.
The finite sets $\set{0, \ldots, n}$ form a directed family with union $\N$, and $f(\N) = \N \ne \varnothing = \bigvee_n f(\set{0, \ldots, n})$.
