---
tag: ~e0bed6c8
kind: definition
name: Ultrapower
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: grad
defines: ~93a646cd
uses: [VFPGADHJYA, J64Y3JC0RE, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Ultrapower
---

## Definition

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] with nonempty domain $M$, let $I$ be a nonempty set, and let $\mathcal{U}$ be an [[ultrafilter|J64Y3JC0RE]] on $I$.
The *ultrapower* of $\mathcal{M}$ by $\mathcal{U}$ is the [[ultraproduct|VFPGADHJYA]] $\mathcal{M}^I / \mathcal{U} = \prod_{i \in I} \mathcal{M} / \mathcal{U}$, in which every factor is $\mathcal{M}$.
So its elements are the classes $[f]$ of functions $f : I \to M$ under $f \sim_{\mathcal{U}} g \iff \set{i : f(i) = g(i)} \in \mathcal{U}$.
For $m \in M$ let $c_m : I \to M$ be the constant function with value $m$.
The *diagonal embedding* is the map $d : M \to M^I / \mathcal{U}$, $d(m) = [c_m]$.

## Notation

Common notations are $\mathcal{M}^I / \mathcal{U}$, $\prod_{\mathcal{U}} \mathcal{M}$, $\mathcal{M}^{\mathcal{U}}$ and, in set theory, $\operatorname{Ult}(\mathcal{M}, \mathcal{U})$.
The diagonal embedding is also written $\delta$ or $j$, and $d(m)$ is often identified with $m$.

## Remarks

The relation $\sim_{\mathcal{U}}$ and the interpretations are well defined, as for every ultraproduct.
In an ultrapower, an $n$-ary relation $R$ holds of $[f_1], \dots, [f_n]$ when $\set{i : R^{\mathcal{M}}(f_1(i), \dots, f_n(i))} \in \mathcal{U}$.
So $R(d(m_1), \dots, d(m_n))$ holds exactly when $R^{\mathcal{M}}(m_1, \dots, m_n)$ holds, since the truth set is $I$ or $\emptyset$.

Example: for $\mathcal{M} = (\N, <)$ and a nonprincipal $\mathcal{U}$ on $\N$, the class of the identity function is greater than $d(n)$ for every $n$.

Non-example: for the Fréchet filter $F$ on $\N$, the structure $(\N, <)^{\N} / F$ is a reduced power, not an ultrapower, and its order is not linear.

## Explanations

### L1 human

An ultrapower is built from many copies of one structure.
Its elements are infinite lists of elements of the structure, and two lists count as equal when they agree at "most" positions.
Each old element $m$ sits inside as the list $m, m, m, \dots$.

### L2 human

Let $\mathcal{M} = (\set{0, 1}, \le)$ and let $\mathcal{U}$ be any ultrafilter on $\N$.

1. A function $f : \N \to \set{0, 1}$ is $0$ on $Z = f^{-1}(0)$ and $1$ on $\N \setminus Z$.
2. Exactly one of $Z$ and $\N \setminus Z$ lies in $\mathcal{U}$.
3. In the first case $[f] = d(0)$, and in the second case $[f] = d(1)$.
4. So the ultrapower has exactly two elements, and $d$ is an isomorphism.

The typical use is to see the old structure inside the new one through $d$.
The trap is to expect new elements from a finite structure: an ultrapower of a finite structure is isomorphic to it.
