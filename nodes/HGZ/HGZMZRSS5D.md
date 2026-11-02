---
tag: HGZMZRSS5D
kind: statement
role: theorem
name: Docquier–Grauert theorem
msc: ["32E10", "32E40", 32T05]
uses: [HMCD0JBFST, JSGWAN2RJV, FF2P7ER3QT]
about: [HMCD0JBFST]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Statement

Let $X$ be a [[Stein manifold|HMCD0JBFST]] and let $D \subseteq X$ be an open subset.
Suppose that $D$ is locally Stein in $X$.
This means that every point $p \in \partial D$ has an open neighbourhood $U$ in $X$ such that $U \cap D$ is Stein.
Then $D$ is a Stein manifold.

## Remarks

For $X = \C^n$ this is Oka's solution of the Levi problem: a locally pseudoconvex domain in $\C^n$ is a domain of holomorphy.
The proof follows the same pattern.
Using that $X$ embeds in some $\C^N$ and has a holomorphic retraction from a neighbourhood, one builds a distance-to-the-boundary function $\delta$ on $D$.
The local Stein condition makes $-\log \delta$ [[plurisubharmonic|FF2P7ER3QT]] near $\partial D$.
Adding a strictly plurisubharmonic exhaustion of $X$ gives a plurisubharmonic exhaustion function of $D$, and Grauert's solution of the Levi problem then shows that $D$ is Stein.
The same holds for unbranched Riemann domains spread over a Stein manifold, which is the form in which Docquier and Grauert proved it.
Example: if $D_1, D_2$ are Stein open subsets of $X$, then $D_1 \cap D_2$ is locally Stein, hence Stein.
The hypothesis that $X$ is Stein cannot be dropped.
If $X$ is the Riemann sphere and $D = X$, then $\partial D$ is empty, so $D$ is locally Stein, but $D$ is compact and not Stein.

## Explanations

### L1 human

Being Stein is a global property of a complex manifold, roughly saying that it has many holomorphic functions.
The theorem says that, inside a Stein manifold, it is enough to check this property near each boundary point of an open set.
A local test at the boundary then gives a global conclusion.

### L2 human

The theorem shows that the class of Stein open sets of a Stein manifold is described by a local boundary condition, pseudoconvexity, just as for domains in $\C^n$.
It is used to prove that intersections, and suitable unions and limits, of Stein domains are Stein.
It reduces many questions on Stein manifolds to the case of domains in $\C^n$ through the embedding theorem.
