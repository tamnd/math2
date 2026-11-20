---
tag: AGYBSTD7BG
kind: statement
role: theorem
name: Łoś's theorem
aliases: [los-theorem, fundamental-theorem-of-ultraproducts]
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: ug2
about: [AX9Q86GB8M]
uses: [AX9Q86GB8M, VFPGADHJYA, J64Y3JC0RE, HYJ10AF6RT]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Ultraproduct.sentence_realize
    match: weaker
history:
  first_stated: "Jerzy Łoś, 1955"
sources:
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Łoś's theorem
  - url: https://en.wikipedia.org/wiki/Jerzy_Łoś
    locator: lead section
  - book: isbn:9780387987606
close_to:
  - system: wikidata
    id: Q1535225
    note: The item is on ultraproducts in general. Node AX9Q86GB8M holds the same_as link.
---

## Statement

Let $L$ be a signature, let $\mathcal{U}$ be an [[ultrafilter|J64Y3JC0RE]] on a nonempty set $I$, and let $(\mathcal{M}_i)_{i \in I}$ be $L$-structures with nonempty domains $M_i$.
Let $\mathcal{M} = \prod_{i \in I} \mathcal{M}_i / \mathcal{U}$ be their [[ultraproduct|AX9Q86GB8M]], and write $[a]$ for the class of $a \in \prod_{i \in I} M_i$.
Let $\varphi(x_1, \dots, x_n)$ be a first-order $L$-[[formula|HYJ10AF6RT]], and let $a_1, \dots, a_n \in \prod_{i \in I} M_i$.
Then
$$\mathcal{M} \models \varphi([a_1], \dots, [a_n]) \iff \set{i \in I : \mathcal{M}_i \models \varphi(a_1(i), \dots, a_n(i))} \in \mathcal{U}.$$
In particular, an $L$-sentence $\sigma$ holds in $\mathcal{M}$ if and only if $\set{i \in I : \mathcal{M}_i \models \sigma} \in \mathcal{U}$.

## Remarks

### Why each hypothesis is needed

- $\mathcal{U}$ must be an ultrafilter. For the [[Fréchet filter|QN98V7NMCD]] on $\N$, the field axioms hold in each factor $\R$ and fail in $\R^{\N}$ modulo the filter; see [[this example|7TJPSD6H5P]].
- $\varphi$ must be first-order. An ultraproduct of finite sets over a nonprincipal ultrafilter is infinite, so "the domain is finite" is not kept; see [[this example|V4090YNR6F]].
- The domains must be nonempty, or the product of the domains is empty.
- The proof uses the [[axiom of choice|0HTGB13FE2]] at the existential step. If each $M_i$ carries a given well-order, the least witness can be taken, and choice is not needed there.

### Consequences

- If every $\mathcal{M}_i$ is a model of a theory $T$, so is $\mathcal{M}$; ultraproducts of groups, fields or ordered fields are again of the same kind.
- The [[diagonal embedding into an ultrapower is elementary|E4TD8X2ZRX]].
- The [[compactness theorem|1NR3HAWG9D]] follows by an [[ultraproduct construction|EY09JT7270]].
- A class closed under elementary equivalence and ultraproducts is [[axiomatizable|4HNAJQQ8Z0]].
- For the hyperreals, the theorem is the [[transfer principle|GXG80SQ66Z]].
- If a sentence holds in algebraically closed fields of characteristic $p$ for infinitely many $p$, then it holds in some ultraproduct of them, which is algebraically closed of characteristic $0$. This is one form of the [[Lefschetz principle|SKTMN14X5P]].

### Converse

The theorem is already an equivalence.
It also characterizes ultrafilters among filters: if $F$ is a filter and neither $X$ nor $I \setminus X$ lies in $F$, take each $\mathcal{M}_i = \set{0, 1}$ with constants $0$ and $1$.
The sentence $\forall x \, (x = 0 \lor x = 1)$ holds in every factor, and the class of the indicator function of $X$ is neither $0$ nor $1$ in the reduced product.

### Generalizations

- For a filter, [[Horn formulas are preserved by reduced products|8RRECJJM3G]], and the [[Feferman-Vaught theorem|RYMZZ2AWFT]] computes truth in reduced products from the quotient Boolean algebra.
- For a $\kappa$-complete ultrafilter, the theorem holds for the infinitary logic $L_{\kappa\kappa}$; this is the basis of the theory of [[measurable cardinals|AKBWT323RQ]].
- In continuous logic, ultraproducts of metric structures such as Banach spaces satisfy a Łoś theorem for continuous formulas.
- Mathlib states the theorem for sentences as `FirstOrder.Language.Ultraproduct.sentence_realize`. The version for formulas follows by naming the elements $[a_k]$ with new constants.

## History

Jerzy Łoś stated and proved the theorem in 1955, in a paper that introduced ultraproducts of general structures.
In the following decade, Frayne, Morel, Scott and Keisler developed the theory of ultraproducts and used it to study elementary equivalence.
The [[proof by induction on formulas|REAJ3C5Q24]] is the standard proof.

## Explanations

### L1 human

An ultraproduct glues many structures into one, and an ultrafilter decides which sets of pieces count as "most" pieces.
Łoś's theorem says that a first-order statement is true in the glued structure exactly when it is true in most of the pieces.
For example, in each system of numbers modulo a prime $p$, adding $p$ ones gives $0$.
For a fixed number such as $7$, the statement "adding $7$ ones gives a nonzero result" is true in all pieces except one.
So it is true in the glued structure.

### L2 human

For each prime $p$, let $\mathcal{M}_p$ be an algebraic closure of $\F_p$, a countable field.
Let $\mathcal{U}$ be a nonprincipal ultrafilter on the primes and $K = \prod_p \mathcal{M}_p / \mathcal{U}$.

1. For each $n \ge 1$, the sentence "every monic polynomial of degree $n$ has a root" holds in every $\mathcal{M}_p$. By the theorem it holds in $K$, so $K$ is algebraically closed.
2. For a prime $q$, the sentence "$q \cdot 1 \neq 0$" holds for all $p \neq q$, a set in $\mathcal{U}$. So $K$ has characteristic $0$.
3. $K$ has $2^{\aleph_0}$ elements, since a nonprincipal ultraproduct of countably many countably infinite sets has this size.
4. By Steinitz's theorem, algebraically closed fields of characteristic $0$ and the same uncountable size are isomorphic, so $K \cong \C$.

The typical use is to transfer one sentence at a time from the factors.
The trap is to transfer an infinite set of sentences as if it were one: "characteristic $p$ for some $p$" is not kept.

### L3 human

Łoś's theorem says that the ultraproduct is a limit of the factors in the sense of first-order truth: the truth value of $\varphi$ is the limit of its truth values along $\mathcal{U}$.
In topological terms, $\mathcal{U}$ is a point of the Stone-Čech compactification $\beta I$, and the ultraproduct evaluates each formula at that point.
The same pattern gives [[ultralimits|3R9GQGFHP5]] in metric geometry and ultraproducts of Banach spaces in analysis.
Within model theory, the theorem is the base of the results that describe elementary equivalence by ultrapowers, such as [[Frayne's theorem|QPX9HG9BH4]] and the [[Keisler-Shelah theorem|A37HPCKCE2]].
