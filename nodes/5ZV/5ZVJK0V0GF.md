---
tag: 5ZVJK0V0GF
kind: concept
name: Ultrapower
aliases: [ultrapower-of-a-structure, diagonal-embedding]
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: grad
uses: [AX9Q86GB8M, AGYBSTD7BG, J64Y3JC0RE, CGH8C8EA9N]
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Ultrapower
  - book: isbn:9780387987606
---

## Summary

Let $\mathcal{M}$ be an $L$-structure with domain $M \neq \emptyset$, let $I$ be a nonempty set, and let $\mathcal{U}$ be an [[ultrafilter|J64Y3JC0RE]] on $I$.
The *ultrapower* $\mathcal{M}^I / \mathcal{U}$ is the [[ultraproduct|AX9Q86GB8M]] $\prod_{i \in I} \mathcal{M}_i / \mathcal{U}$ with $\mathcal{M}_i = \mathcal{M}$ for every $i$.
Its elements are the classes $[f]$ of functions $f : I \to M$, where $f$ and $g$ are identified when they agree on a set in $\mathcal{U}$.
The *diagonal embedding* $d : \mathcal{M} \to \mathcal{M}^I / \mathcal{U}$ sends $m$ to the class of the constant function with value $m$.
By [[Łoś's theorem|AGYBSTD7BG]], $d$ is an [[elementary embedding|CGH8C8EA9N]].
So ultrapowers give elementary extensions of a structure by an explicit algebraic construction, without compactness or syntax.

## Motivation

To find a nonstandard natural number, one needs a structure with the same first-order properties as $\N$ and an element above all standard numbers.
The compactness theorem gives such a structure, but not a concrete one.
The ultrapower gives a concrete one: the class of the identity function $n \mapsto n$ lies above every standard $n$.
More generally, the ultrapower collects "sequences of elements of $\mathcal{M}$" and treats them as new elements.
The ultrafilter makes this collection a model of the same theory, with $\mathcal{M}$ inside it as an elementary substructure.

## Notation

We write $\mathcal{M}^I / \mathcal{U}$, $\prod_{\mathcal{U}} \mathcal{M}$ or $\mathcal{M}^{\mathcal{U}}$, and $[f]$ or $[f]_{\mathcal{U}}$ for the class of $f$.
In set theory the ultrapower of the universe is written $\operatorname{Ult}(V, \mathcal{U})$, and the embedding is $j$.
The diagonal embedding is also written $\delta$, $\iota$ or $m \mapsto m^*$; in nonstandard analysis, ${}^*\R$ denotes an ultrapower of $\R$.
The formal construction is the [[definition of the ultrapower|WBWC47Y5SK]].

## Remarks

### Examples

- For a nonprincipal $\mathcal{U}$ on $\N$, the ultrapower of $(\N, +, \cdot, 0, 1, <)$ is a nonstandard model of true arithmetic; see [[this example|5B6GQKKDMG]].
- For a nonprincipal $\mathcal{U}$ on $\N$, the ultrapower of the ordered field $\R$ has infinitesimals; see [[this example|4W5HFEXSKT]].
- If $M$ is finite, $d$ is an isomorphism. A function $f : I \to M$ has finitely many fibers, which partition $I$, so one of them lies in $\mathcal{U}$, and $[f] = d(m)$.
- If $\mathcal{U}$ is principal at $i_0$, then $[f] \mapsto f(i_0)$ is the inverse of $d$, so the ultrapower is a copy of $\mathcal{M}$.
- The ultrapower $(\Q, <)^{\N} / \mathcal{U}$ for nonprincipal $\mathcal{U}$ is a dense linear order without endpoints, of size $2^{\aleph_0}$.

### Non-examples

- A countable nonstandard model of arithmetic is not an ultrapower of $\N$ over an ultrafilter on $\N$; see [[this non-example|WAENF6VDJZ]].
- The reduced power $\R^{\N} / F$ for the Fréchet filter $F$ is not an ultrapower, and the diagonal map into it is not elementary: $\R$ is a field and $\R^{\N} / F$ is not.

### Basic properties

- The [[diagonal embedding is elementary|E4TD8X2ZRX]], so $\mathcal{M} \equiv \mathcal{M}^I / \mathcal{U}$.
- If $M$ is infinite and $\mathcal{U}$ is countably incomplete, for example nonprincipal on $\N$, then $d$ is not surjective, and the ultrapower is a proper elementary extension.
- $\abs{\mathcal{M}^I / \mathcal{U}} \le \abs{M}^{\abs{I}}$.
- Iterated ultrapowers: an ultrapower of $\mathcal{M}^I / \mathcal{U}$ by $\mathcal{V}$ on $J$ is isomorphic to an ultrapower of $\mathcal{M}$ on $I \times J$. Iterating along the ordinals, with direct limits at limit stages, gives iterated ultrapowers.
- Keisler's limit ultrapowers are substructures of an ultrapower. Fix a filter $G$ on $I \times I$ and keep the classes $[f]$ whose kernel $\set{(i, j) : f(i) = f(j)}$ lies in $G$.
- A limit ultrapower contains $d(M)$ and is an elementary extension of $\mathcal{M}$: by the Tarski-Vaught test, a witness $g$ can be chosen as a function of the values of the parameters, so its kernel lies in $G$.
- Elementary equivalence is described by ultrapowers: see [[Frayne's theorem|QPX9HG9BH4]] and the [[Keisler-Shelah theorem|A37HPCKCE2]].

### History

Ultrapowers are the special case of Łoś's ultraproducts of 1955 with equal factors.
Keisler introduced limit ultrapowers and used ultrapowers to study elementary equivalence in the early 1960s.
Kunen used iterated ultrapowers of the set-theoretic universe in his work on measurable cardinals.

### Common errors

- To think that the ultrapower adds no elements; it adds new elements exactly when $M$ is infinite and $\mathcal{U}$ is suitably nonprincipal.
- To confuse $d(m)$ with an arbitrary function whose values are often $m$; $[f] = d(m)$ needs $f = m$ on a set in $\mathcal{U}$.
- To believe that the ultrapower keeps properties such as "well ordered" or "Archimedean"; these are not first-order.

## Explanations

### L1 human

Take one structure, such as the natural numbers, and form all infinite lists of its elements.
Two lists count as equal when they agree at "most" positions, in the sense of an ultrafilter.
Each ordinary number $n$ appears as the constant list $n, n, n, \dots$.
The list $0, 1, 2, 3, \dots$ is a new element, bigger than every ordinary number.
All first-order facts about the natural numbers remain true in this larger world.

### L2 human

Let $\mathcal{U}$ be nonprincipal on $\N$, and let ${}^*\N = \N^{\N} / \mathcal{U}$ with $+$, $\cdot$ and $<$.

1. For $n \in \N$, $d(n) = [(n, n, \dots)]$.
2. Let $\omega = [(0, 1, 2, \dots)]$. For each $n$, the set $\set{i : i > n}$ is cofinite, so it lies in $\mathcal{U}$.
3. So $\omega > d(n)$ for every $n$.
4. The sentence "every element other than $0$ has a predecessor" holds in $\N$, so it holds in ${}^*\N$ by Łoś's theorem.
5. The predecessor of $\omega$ is $[(0, 0, 1, 2, \dots)]$, and it is again above every $d(n)$.

The typical use is to produce elementary extensions with new elements of a desired kind.
The trap is to assume that ${}^*\N$ is well ordered: the elements above all $d(n)$ have no least one.

### L3 human

In set theory, if $\mathcal{U}$ is a countably complete ultrafilter on a measurable cardinal $\kappa$, then $\operatorname{Ult}(V, \mathcal{U})$ is well founded, and its collapse gives an elementary embedding $j : V \to M$ with critical point $\kappa$.
This is the link between ultrapowers and [[measurable cardinals|AKBWT323RQ]], and iterated ultrapowers are a basic tool of inner model theory.
In model theory, ultrapowers give the saturated models of [[saturation of ultraproducts|DYXQP8WS63]] and the order of [[Keisler's order|TD5D2G5PYP]].
In nonstandard analysis, the ultrapower of the full structure over $\R$ gives the [[transfer principle|GXG80SQ66Z]] in its usual form.
