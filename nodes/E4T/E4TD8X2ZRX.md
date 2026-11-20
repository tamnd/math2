---
tag: E4TD8X2ZRX
kind: statement
role: theorem
name: The diagonal embedding into an ultrapower is elementary
aliases: [diagonal-embedding-is-elementary]
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: grad
about: [5ZVJK0V0GF, CGH8C8EA9N]
uses: [WBWC47Y5SK, AGYBSTD7BG, CGH8C8EA9N, J64Y3JC0RE]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Ultrapower
  - book: isbn:9780387987606
---

## Statement

Let $\mathcal{M}$ be an $L$-structure with nonempty domain $M$, let $\mathcal{U}$ be an [[ultrafilter|J64Y3JC0RE]] on a nonempty set $I$, and let $d : \mathcal{M} \to \mathcal{M}^I / \mathcal{U}$ be the [[diagonal embedding|WBWC47Y5SK]].

1. $d$ is an [[elementary embedding|CGH8C8EA9N]]: for every $L$-formula $\varphi(x_1, \dots, x_n)$ and $m_1, \dots, m_n \in M$, $\mathcal{M} \models \varphi(m_1, \dots, m_n)$ if and only if $\mathcal{M}^I / \mathcal{U} \models \varphi(d(m_1), \dots, d(m_n))$.
2. In particular $\mathcal{M} \equiv \mathcal{M}^I / \mathcal{U}$.
3. If $M$ is finite or $\mathcal{U}$ is principal, then $d$ is surjective.
4. If $M$ is infinite and $\mathcal{U}$ is *countably incomplete*, meaning that some sets $X_0 \supseteq X_1 \supseteq \dots$ in $\mathcal{U}$ have empty intersection, then $d$ is not surjective.

## Remarks

### Why each hypothesis is needed

- $\mathcal{U}$ must be an ultrafilter. For the Fréchet filter on $\N$, the diagonal map $\R \to \R^{\N} / F$ is an embedding of rings, but not elementary: $\R$ is a field and $\R^{\N} / F$ is not.
- In part 4, countable incompleteness is needed. If $\mathcal{U}$ is principal, $d$ is an isomorphism by part 3.
- In part 4, $M$ must be infinite, by part 3.

### Consequences

- Every infinite structure has a proper elementary extension, namely an ultrapower over a nonprincipal ultrafilter on $\N$; such an ultrafilter is countably incomplete, with $X_n = \set{k : k \ge n}$.
- $\N$ has an elementary extension with an element above every standard number; see [[this example|5B6GQKKDMG]].
- If $\mathcal{N}$ elementarily embeds in an ultrapower of $\mathcal{M}$, then $\mathcal{N} \equiv \mathcal{M}$, which is the easy half of [[Frayne's theorem|QPX9HG9BH4]].

### Converse

Part 1 has a converse in the form of Frayne's theorem: $\mathcal{N} \equiv \mathcal{M}$ holds if and only if $\mathcal{N}$ embeds elementarily into some ultrapower of $\mathcal{M}$.
An elementary embedding $\mathcal{M} \to \mathcal{N}$ need not be the diagonal embedding into an ultrapower: a countable proper elementary extension of $\N$ is not an ultrapower of $\N$, by [[this non-example|WAENF6VDJZ]].

### Generalizations

- The same proof shows that $d$ is elementary for $L_{\kappa\kappa}$ when $\mathcal{U}$ is $\kappa$-complete.
- For a filter $F$, the diagonal map into the reduced power $\mathcal{M}^I / F$ preserves Horn formulas.

## History

Part 1 follows at once from Łoś's theorem of 1955.
Parts 3 and 4 belong to the theory of ultrapowers that was developed in the early 1960s.

## Explanations

### L1 human

Every element of a structure appears in its ultrapower as a constant list.
A statement about some elements is true in the old structure exactly when it is true about their constant lists in the ultrapower.
So the old structure sits inside the ultrapower without any change in its first-order properties.

### L2 human

Take $\mathcal{M} = (\Z, <)$ and a nonprincipal $\mathcal{U}$ on $\N$.

1. The formula $\varphi(x, y)$: "$x < y$ and no $z$ satisfies $x < z < y$".
2. In $\Z$, $\varphi(3, 4)$ holds. By part 1, $\varphi(d(3), d(4))$ holds in the ultrapower, so nothing lies between $d(3)$ and $d(4)$.
3. The class $[f]$ with $f(i) = i$ satisfies $[f] > d(m)$ for every $m$, since $\set{i : i > m}$ is cofinite.
4. So $d$ is not surjective, in line with part 4.

The typical use is to prove that a structure has a proper elementary extension.
The trap is to think that the new elements also lie between old ones: here they lie above all of $d(\Z)$ or below it.

### L3 human

The theorem says that $d$ is a morphism in the category of $L$-structures and elementary embeddings.
In set theory, the analogous map $j : V \to \operatorname{Ult}(V, \mathcal{U})$ is elementary by the same argument, and for countably complete $\mathcal{U}$ it leads to measurable cardinals.
In nonstandard analysis, the elementarity of $d$ is the [[transfer principle|GXG80SQ66Z]].
