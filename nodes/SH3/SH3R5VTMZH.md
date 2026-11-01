---
tag: SH3R5VTMZH
kind: statement
role: proposition
name: Cayley–Hamilton theorem for modules
msc: [13C05, 15A24]
uses: [0310REJJY8, 05QY1VEBYD, 096Z9MP2ME, 0J7H0YBFDJ]
about: [05QY1VEBYD, 0J7H0YBFDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley–Hamilton_theorem
---

## Statement

Let $R$ be a [[commutative ring|0310REJJY8]], let $I$ be an [[ideal|096Z9MP2ME]] of $R$, and let $M$ be an $R$-module [[generated|05QY1VEBYD]] by $n$ elements.
Let $\varphi \colon M \to M$ be an $R$-linear [[endomorphism|0J7H0YBFDJ]] with $\varphi(M) \subseteq IM$.
Then there are elements $a_1, \ldots, a_n \in R$ with $a_i \in I^i$ for each $i$ such that
$$\varphi^n + a_1 \varphi^{n-1} + \cdots + a_{n-1} \varphi + a_n \id_M = 0.$$

## Remarks

Let $x_1, \ldots, x_n$ generate $M$ and write $\varphi(x_i) = \sum_j a_{ij} x_j$ with $a_{ij} \in I$.
View $M$ as a module over $R[t]$ with $t$ acting as $\varphi$.
The matrix $B = t I_n - (a_{ij})$ kills the column vector $(x_1, \ldots, x_n)$; multiplying by the [[adjugate|07W9H8QF38]] of $B$ shows that $\det B$ kills every $x_j$, hence all of $M$.
Expanding $\det B$ gives the polynomial, and its coefficient of $t^{n-i}$ is a sum of products of $i$ entries in $I$.
For $I = R$ and $M = R^n$, with $\varphi$ given by a matrix $A$, one recovers the [[Cayley–Hamilton theorem|0F765KFC2J]] $p_A(A) = 0$.

## Explanations

### L1 human

Every endomorphism of a finite-dimensional vector space satisfies its characteristic polynomial.
This result says the same thing for any finitely generated module over a commutative ring.
It adds a bonus: if the map pushes $M$ into $IM$, the coefficients of the polynomial lie in powers of $I$.

### L2 human

This is the engine behind the [[determinant trick|A8HRT9H3XA]] and hence behind [[Nakayama's lemma|15JHBYR6KH]].
Taking $\varphi = \id_M$ when $IM = M$ gives an element $1 + a_1 + \cdots + a_n$ with $a_i \in I$ that annihilates $M$.
It is also the standard tool to prove that an element is integral.
If $x$ lies in a ring $S \supseteq R$ and $M$ is a faithful $R[x]$-module that is finitely generated over $R$, then $x$ satisfies a monic polynomial over $R$.
