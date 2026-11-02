---
tag: 6JBE71PZWA
kind: definition
name: Semiconjugacy and factor map
msc: [37B02, 37C15]
defines: AEXJNRBASV
uses: [0CQHFPGJ45, 0X3WGX95FE, 01RVCMSN5N, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_conjugacy
---

## Definition

Let $X$ and $Y$ be [[topological spaces|0CQHFPGJ45]], and let $f \colon X \to X$ and $g \colon Y \to Y$ be [[continuous maps|0X3WGX95FE]].
A *semiconjugacy* from $f$ to $g$ is a continuous [[surjective|01RVCMSN5N]] map $h \colon X \to Y$ such that
$$h \circ f = g \circ h,$$
where $\circ$ is [[composition|0THBK9V825]].
Then $h$ is called a *factor map*, the system $(Y, g)$ is a *factor* of $(X, f)$, and $(X, f)$ is an *extension* of $(Y, g)$.

## Remarks

Some authors use the word semiconjugacy without the surjectivity condition and say factor map only when $h$ is onto.
If $h$ is moreover a homeomorphism, it is a topological conjugacy.
The relation gives $h \circ f^n = g^n \circ h$, so $h$ maps the orbit of $x$ onto the orbit of $h(x)$, and periodic points of $f$ to periodic points of $g$.

Example: let $\Sigma = \set{0, 1}^{\N}$ with the product topology, let $\sigma$ be the shift $(\sigma x)_i = x_{i+1}$, and let $g(y) = 2y \bmod 1$ on the circle $\R / \Z$.
The map $h(x) = \sum_{i \ge 0} x_i 2^{-i-1} \bmod 1$ is continuous and onto, since every number in $[0, 1]$ has a binary expansion.
One has $h(\sigma x) = \sum_{i \ge 0} x_{i+1} 2^{-i-1} = 2 h(x) - x_0$, which equals $2 h(x)$ modulo $1$, so $h \circ \sigma = g \circ h$.
This $h$ is not injective, since $(1, 0, 0, \dots)$ and $(0, 1, 1, \dots)$ have the same image.

Non-example: the inclusion $h \colon \set{0} \to \R$ satisfies $h \circ f = g \circ h$ for $f = \id$ and $g(y) = y/2$, but it is not surjective, so it is not a factor map.
