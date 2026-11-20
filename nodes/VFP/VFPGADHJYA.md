---
tag: VFPGADHJYA
kind: definition
name: Ultraproduct
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: ug2
defines: AX9Q86GB8M
uses: [J64Y3JC0RE, 983GZBQYT4, WDVVEYD6AT, 09CEDJYBKP, 0G8VEZ3WTK, 84XXPH6XJ8]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Definition
  - book: isbn:9780387987606
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], let $I$ be a nonempty set, and let $\mathcal{U}$ be an [[ultrafilter|J64Y3JC0RE]] on $I$.
For each $i \in I$ let $\mathcal{M}_i$ be an $L$-[[structure|983GZBQYT4]] with nonempty domain $M_i$.
Let $P = \prod_{i \in I} M_i$ be the [[Cartesian product|09CEDJYBKP]] of the domains.
For $a, b \in P$ write $a \sim_{\mathcal{U}} b$ when $\set{i \in I : a(i) = b(i)} \in \mathcal{U}$, and let $[a]$ be the class of $a$.
The *ultraproduct* $\prod_{i \in I} \mathcal{M}_i / \mathcal{U}$ is the $L$-structure with domain $P / {\sim_{\mathcal{U}}}$ and these interpretations.

1. For an $n$-ary function symbol $f$: $f([a_1], \dots, [a_n]) = [b]$, where $b(i) = f^{\mathcal{M}_i}(a_1(i), \dots, a_n(i))$.
2. For an $n$-ary relation symbol $R$: $R([a_1], \dots, [a_n])$ holds when $\set{i \in I : (a_1(i), \dots, a_n(i)) \in R^{\mathcal{M}_i}} \in \mathcal{U}$.
3. For a constant symbol $c$: its value is $[b]$, where $b(i) = c^{\mathcal{M}_i}$.

If all $\mathcal{M}_i$ equal one structure $\mathcal{M}$, the ultraproduct is the *ultrapower* $\mathcal{M}^I / \mathcal{U}$.

## Notation

Other common forms are $\prod_{\mathcal{U}} \mathcal{M}_i$ and $\prod \mathcal{M}_i / D$; Chang and Keisler write $D$ for the ultrafilter.
The class $[a]$ is also written $[a]_{\mathcal{U}}$ or $a / \mathcal{U}$.
The construction is the [[reduced product|84XXPH6XJ8]] for a filter that happens to be an ultrafilter.

## Remarks

We check that $\sim_{\mathcal{U}}$ is an [[equivalence relation|0G8VEZ3WTK]] and that the clauses do not depend on the representatives.

1. Reflexivity: $\set{i : a(i) = a(i)} = I$, and $I \in \mathcal{U}$.
2. Symmetry: the set $\set{i : a(i) = b(i)}$ does not change when $a$ and $b$ are exchanged.
3. Transitivity: $\set{i : a(i) = c(i)}$ contains $\set{i : a(i) = b(i)} \cap \set{i : b(i) = c(i)}$; an ultrafilter is closed under intersections and supersets.
4. Clauses 1 and 2: if $a_k \sim_{\mathcal{U}} a'_k$ for each $k$, the two computations agree on the intersection of the agreement sets, which lies in $\mathcal{U}$.

Example: for a nonprincipal ultrafilter $\mathcal{U}$ on $\N$, the ultrapower $\R^{\N} / \mathcal{U}$ of the ordered field $\R$ is a field of [[hyperreal numbers|421QMTFG9T]].
The class of $(0, 1, 2, \dots)$ is larger than the class of each constant sequence $(r, r, \dots)$, since $\set{i : i > r}$ is cofinite and lies in $\mathcal{U}$.

Non-example: for the [[Fréchet filter|QN98V7NMCD]] $F$ of cofinite subsets of $\N$, the same construction gives the ring $\R^{\N} / F$, which is not a field.
The classes of $(1, 0, 1, 0, \dots)$ and $(0, 1, 0, 1, \dots)$ are both nonzero, but their product is $0$.

If $\mathcal{U}$ is the principal ultrafilter at $i_0 \in I$, the map $[a] \mapsto a(i_0)$ is an isomorphism onto $\mathcal{M}_{i_0}$.

## Explanations

### L1 human

We line up one structure for each index and take all lists with one entry from each.
An ultrafilter tells us, for every set of positions, whether it is "most" positions or not.
Two lists are equal when they agree at most positions.
A relation holds between lists when it holds at most positions.

### L2 human

Let $\mathcal{U}$ be a nonprincipal ultrafilter on $\N$, and work in the ultrapower $\Z^{\N} / \mathcal{U}$ of the ring $\Z$.

1. Let $a = (0, 1, 0, 1, \dots)$. The set of even numbers or the set of odd numbers lies in $\mathcal{U}$, but not both.
2. If the evens lie in $\mathcal{U}$, then $a$ agrees with $0$ there, so $[a] = 0$.
3. If the odds lie in $\mathcal{U}$, then $a$ agrees with $1$ there, so $[a] = 1$.
4. In both cases $[a] \cdot [a] = [a]$, which agrees with $a(i)^2 = a(i)$ for every $i$.

The typical use is to compute in the ultraproduct by computing in the factors.
The trap is that we cannot say which case of step 1 holds; a nonprincipal ultrafilter is obtained by the axiom of choice and has no explicit description.
