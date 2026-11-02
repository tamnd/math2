---
tag: VFPGADHJYA
kind: definition
name: Ultraproduct
msc: [03C20]
defines: AX9Q86GB8M
uses: [J64Y3JC0RE, 983GZBQYT4, WDVVEYD6AT, 09CEDJYBKP, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], let $I$ be a nonempty set, and let $\mathcal{U}$ be an [[ultrafilter|J64Y3JC0RE]] on $I$.
For each $i \in I$ let $M_i$ be an [[$L$-structure|983GZBQYT4]] with nonempty domain.
Let $P = \prod_{i \in I} M_i$ be the [[Cartesian product|09CEDJYBKP]] of the domains.
For $a, b \in P$ write $a \sim_{\mathcal{U}} b$ when $\set{i \in I : a(i) = b(i)} \in \mathcal{U}$; this is an [[equivalence relation|0G8VEZ3WTK]] on $P$, and $[a]$ denotes the class of $a$.
The *ultraproduct* $\prod_{i \in I} M_i / \mathcal{U}$ is the $L$-structure with domain $P / {\sim_{\mathcal{U}}}$ and the following interpretations:

1. for an $n$-ary function symbol $f$, $f([a_1], \dots, [a_n]) = [b]$, where $b(i) = f^{M_i}(a_1(i), \dots, a_n(i))$;
2. for an $n$-ary relation symbol $R$, $R([a_1], \dots, [a_n])$ holds if and only if $\set{i \in I : (a_1(i), \dots, a_n(i)) \in R^{M_i}} \in \mathcal{U}$;
3. for a constant symbol $c$, its value is $[b]$, where $b(i) = c^{M_i}$.

If all $M_i$ equal one structure $M$, the ultraproduct is called the *ultrapower* $M^I / \mathcal{U}$.

## Remarks

The interpretations do not depend on the chosen representatives, because $\mathcal{U}$ is closed under finite intersections and supersets.

Example: let $\mathcal{U}$ be a non-principal ultrafilter on $\N$ and let $M_i = \R$ for all $i$.
The ultrapower $\R^{\N} / \mathcal{U}$ is the ordered field of [[hyperreal numbers|421QMTFG9T]].
The class of $a = (0, 1, 2, 3, \dots)$ is larger than the class of each constant sequence $(r, r, r, \dots)$, since $\set{i : i > r}$ is cofinite and so lies in $\mathcal{U}$.

Non-example: replace $\mathcal{U}$ by the Fréchet filter $\mathcal{F}$ of cofinite subsets of $\N$, which is a filter but not an ultrafilter.
The same construction gives a ring $\R^{\N} / \mathcal{F}$, but it is not a field.
The classes of $(1, 0, 1, 0, \dots)$ and $(0, 1, 0, 1, \dots)$ are both nonzero, because neither sequence is zero on a cofinite set, but their product is the class of $0$.

If $\mathcal{U}$ is the principal ultrafilter at $i_0 \in I$, the ultraproduct is isomorphic to $M_{i_0}$.
