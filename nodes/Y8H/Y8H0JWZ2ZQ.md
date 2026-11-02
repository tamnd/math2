---
tag: Y8H0JWZ2ZQ
kind: definition
name: Brauer–Manin obstruction
msc: [14G05, 14F22, 11G35]
defines: XDWF0HW2QN
uses: [MWBDFS2KJ5, BEW48TA9WZ, SEH68BA1QQ, EMAR4X3W8D, BEKCEYHCHX, SWJYG87QQH, W168DS966V]
sources:
  - url: https://en.wikipedia.org/wiki/Manin_obstruction
---

## Definition

Let $k$ be an [[algebraic number field|MWBDFS2KJ5]] with [[adele ring|SEH68BA1QQ]] $\mathbb{A}_k$, and for each place $v$ let $k_v$ be the [[completion|W168DS966V]] of $k$ at $v$.
Let $X$ be a smooth projective geometrically integral variety over $k$, and let $\operatorname{Br} X = H^2_{\text{ét}}(X, \mathbb{G}_m)$ be its [[Brauer group|BEW48TA9WZ]].
For each place $v$ let $\operatorname{inv}_v \colon \operatorname{Br} k_v \to \Q/\Z$ be the local invariant map of [[class field theory|BEKCEYHCHX]].
For $\alpha \in \operatorname{Br} X$ and $P \in X(k_v)$ let $\alpha(P) \in \operatorname{Br} k_v$ be the pullback of $\alpha$ along $P$.
The *Brauer–Manin set* is
$$X(\mathbb{A}_k)^{\operatorname{Br}} = \set{(P_v)_v \in X(\mathbb{A}_k) : \textstyle\sum_v \operatorname{inv}_v \alpha(P_v) = 0 \text{ for all } \alpha \in \operatorname{Br} X}.$$
There is a *Brauer–Manin obstruction to the Hasse principle* for $X$ if $X(\mathbb{A}_k) \neq \emptyset$ and $X(\mathbb{A}_k)^{\operatorname{Br}} = \emptyset$.

## Remarks

Since $X$ is projective, $X(\mathbb{A}_k) = \prod_v X(k_v)$.
For fixed $\alpha$, the term $\operatorname{inv}_v \alpha(P_v)$ is $0$ for all but finitely many $v$, so the sum is finite.
The reciprocity law says that $\sum_v \operatorname{inv}_v \beta = 0$ for every $\beta \in \operatorname{Br} k$.
Applied to $\beta = \alpha(P)$ for a [[rational point|SWJYG87QQH]] $P \in X(k)$, it gives the inclusion
$$X(k) \subseteq X(\mathbb{A}_k)^{\operatorname{Br}} \subseteq X(\mathbb{A}_k).$$
So a Brauer–Manin obstruction implies $X(k) = \emptyset$ although $X$ has points over every $k_v$.

Example: suppose that $\operatorname{Br} X$ is the image of $\operatorname{Br} k$, as when $X$ is a projective space.
Then the sum vanishes for every adelic point by reciprocity, so $X(\mathbb{A}_k)^{\operatorname{Br}} = X(\mathbb{A}_k)$ and there is no obstruction.
Non-example of a sufficient test: Skorobogatov constructed a surface with $X(\mathbb{A}_k)^{\operatorname{Br}} \ne \emptyset$ and $X(k) = \emptyset$, so the Brauer–Manin obstruction does not explain all failures of the Hasse principle.
