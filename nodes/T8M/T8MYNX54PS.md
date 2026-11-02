---
tag: T8MYNX54PS
kind: definition
name: Residuated mapping
msc: [06A15]
defines: V76Q9B6VS8
uses: [011C29Q1S1, 0WFF6AZPBP, TGW5NTV3AA]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_mapping
---

## Definition

Let $(P, \le)$ and $(Q, \le)$ be [[partially ordered sets|011C29Q1S1]].
A map $f \colon P \to Q$ is *residuated* when, for each $y \in Q$, the preimage $f^{-1}(\downarrow y)$ is a principal down-set $\downarrow x$ of $P$, for some $x \in P$.
Here $\downarrow y = \set{z : z \le y}$ is the [[principal down-set|TGW5NTV3AA]] of $y$.

## Remarks

A residuated map is [[monotone|0WFF6AZPBP]].
A map $f$ is residuated if and only if there is a map $g \colon Q \to P$ with $f(x) \le y \iff x \le g(y)$ for all $x \in P$ and $y \in Q$.
Then $g(y)$ is the greatest element of $f^{-1}(\downarrow y)$, and $g$ is called the *residual* of $f$.
For an integer $a > 0$, the map $x \mapsto a x$ on $\Z$ is residuated with residual $y \mapsto \lfloor y / a \rfloor$, since $a x \le y$ if and only if $x \le \lfloor y / a \rfloor$.
The map $f \colon \R \to \R$ with $f(x) = 0$ for $x < 0$ and $f(x) = 1$ for $x \ge 0$ is monotone but not residuated.
Indeed $f^{-1}(\downarrow 0) = (-\infty, 0)$ has no greatest element, so it is not a principal down-set.

## Explanations

### L1 human

A residuated map is one whose inequalities $f(x) \le y$ always have a largest solution $x$.
The largest solution, as a function of $y$, is the residual.
