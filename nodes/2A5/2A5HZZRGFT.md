---
tag: 2A5HZZRGFT
kind: statement
role: theorem
name: Malgrange preparation theorem
msc: [58K40, 58K20, "26E10"]
uses: [0V33BNKZ9S, 49JSD49P7X, 7SWSRGDT4A]
about: [7SWSRGDT4A]
sources:
  - url: https://en.wikipedia.org/wiki/Malgrange_preparation_theorem
same_as:
  wikidata: Q6743217
  wikipedia: Malgrange preparation theorem
---

## Statement

Let $F(t, x)$ be a real-valued [[smooth function|0V33BNKZ9S]] on a neighbourhood of $(0, 0)$ in $\R \times \R^n$.
Let $k \ge 1$, and assume that
$$F(0, 0) = \partial_t F(0, 0) = \cdots = \partial_t^{k-1} F(0, 0) = 0, \qquad \partial_t^k F(0, 0) \ne 0.$$
Then there are smooth functions $q(t, x)$ near $(0, 0)$ with $q(0, 0) \ne 0$, and $a_0(x), \ldots, a_{k-1}(x)$ near $0 \in \R^n$ with $a_i(0) = 0$, such that near $(0, 0)$
$$q(t, x) \, F(t, x) = t^k + a_{k-1}(x) \, t^{k-1} + \cdots + a_1(x) \, t + a_0(x).$$

## Remarks

This is the smooth analogue of the [[Weierstrass preparation theorem|49JSD49P7X]] for holomorphic functions.
The hypothesis says that $t \mapsto F(t, 0)$ vanishes to order exactly $k$ at $0$.
It is necessary: since $q(0, 0) \ne 0$ and $a_i(0) = 0$, the function $F(t, 0)$ vanishes at $t = 0$ to the same order as $t^k$.
In the smooth case the proof is much harder than in the holomorphic case, because there is no Cauchy integral formula.
Unlike the holomorphic case, the factorisation need not be unique.
A closely related form is the division theorem: every smooth $G$ near $(0, 0)$ can be written as $G = Q F + \sum_{i < k} r_i(x) t^i$ with smooth $Q$ and $r_i$.
Mather gave a form for modules of [[germs|7SWSRGDT4A]].
Let $\varphi \colon (\R^n, 0) \to (\R^p, 0)$ be a smooth map germ, and let $A$ be a finitely generated module over the ring $\mathcal{E}_n$ of smooth germs on $\R^n$.
Let $\mathfrak{m}_p$ be the maximal ideal of the ring $\mathcal{E}_p$ of smooth germs on $\R^p$.
Then $A$ is finitely generated over $\mathcal{E}_p$ through $\varphi$ if and only if $A / \varphi^*(\mathfrak{m}_p) A$ is a finite-dimensional real vector space.
Example: for $F(t, x) = t^2 - x$ the theorem holds with $q = 1$, $a_1 = 0$ and $a_0(x) = -x$.

## Explanations

### L1 human

Near a point where a smooth function of $t$ vanishes to order $k$, the theorem says that the function behaves like a polynomial of degree $k$ in $t$.
The coefficients of this polynomial depend smoothly on the remaining variables.
So questions about the zeros of a smooth function reduce to questions about the roots of a polynomial.

### L2 human

The preparation theorem is the main algebraic tool of the local theory of smooth maps.
In Mather's module form it turns infinitesimal conditions into finite-dimensional linear algebra.
It is used to prove that [[infinitesimal stability implies stability|T6BK8Q8PK8]], and results on finite determinacy and versal unfoldings.
