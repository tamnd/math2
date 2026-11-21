---
tag: E7WEFRMQTB
kind: concept
name: Buchholz psi functions
aliases: [buchholz-psi-function]
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: research
uses: [0YSCSX5YZC, KAEDCQ8RM6, 7TFCZSVX5R, 0EBACQFAZW, 8S6CT4TMB7, PQSHBKCE7V]
sources:
  - wikipedia: en:54183426@r1346942673
    locator: Buchholz psi functions
    note: adopted
    mention: wikipedia://en/54183426
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Explanation
  - url: https://en.wikipedia.org/wiki/Buchholz_psi_functions
    locator: Ordinal notation
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Table of ordinal analyses
same_as:
  wikidata: Q48996114
  wikipedia: Buchholz psi functions
inventory: [5SXQMWDD1X]
---

## Summary

Let $\Omega_0 = 1$, and for $0 < \nu \le \omega$ let $\Omega_\nu = \aleph_\nu$, the $\nu$-th uncountable [[cardinal|0EBACQFAZW]], seen as an initial ordinal.
For $\nu \le \omega$ and an [[ordinal|0YSCSX5YZC]] $\alpha$, let $C_\nu(\alpha)$ be the least set of ordinals that contains every ordinal below $\Omega_\nu$, is closed under ordinal addition, and contains $\psi_\mu(\xi)$ for each $\mu \le \omega$ and each $\xi \in C_\nu(\alpha)$ with $\xi < \alpha$.
Buchholz's function $\psi_\nu$ sends $\alpha$ to the least ordinal that is not in $C_\nu(\alpha)$.
The definition is a recursion on $\alpha$, simultaneous for all $\nu \le \omega$.
These [[collapsing functions|8S6CT4TMB7]] give a short notation system for the ordinals below $\psi_0(\varepsilon_{\Omega_\omega + 1})$, and this range contains the ordinals of $\mathrm{ID}_\nu$ and of $\Pi^1_1$-comprehension.

## Motivation

A single collapsing function with one uncountable ordinal $\Omega$ reaches the [[Bachmann-Howard ordinal|QH3ENXFRSV]], and no further.
The ordinals of stronger theories, such as the [[theories of iterated inductive definitions|5VNT564Y2W]] $\mathrm{ID}_\nu$, need a tower of large ordinals.
Each level $\Omega_{\nu + 1}$ is collapsed into the level below by $\psi_\nu$, and $\psi_0$ sends everything to countable ordinals.
Buchholz noticed that the closure under addition and under the functions $\psi_\mu$ is enough: multiplication and exponentiation come for free, because $\psi_\nu$ produces the powers of $\omega$ by itself.
This makes the definition shorter than the earlier $\theta$-functions of Feferman, and it makes the comparison of terms a simple recursive procedure.

## Notation

We write $C^0_\nu(\alpha) = \set{\beta : \beta < \Omega_\nu}$ and

$$C^{n+1}_\nu(\alpha) = C^n_\nu(\alpha) \cup \set{\beta + \gamma : \beta, \gamma \in C^n_\nu(\alpha)} \cup \set{\psi_\mu(\xi) : \xi \in C^n_\nu(\alpha), \ \xi < \alpha, \ \mu \le \omega}.$$

Then $C_\nu(\alpha) = \bigcup_{n < \omega} C^n_\nu(\alpha)$ and $\psi_\nu(\alpha) = \min \set{\gamma : \gamma \notin C_\nu(\alpha)}$.
We write $\Omega$ for $\Omega_1$, and $\psi$ without an index means $\psi_0$ in many papers.

Notation trap: the letter $\psi$ names different functions in different systems.
In the system of the page on [[collapsing functions|8S6CT4TMB7]], $\psi(\Omega) = \zeta_0$.
In Buchholz's system, $\psi_0(\Omega) = \varepsilon_0$.
Every value on this page is a value of Buchholz's $\psi_\nu$.
Some authors also extend the index $\nu$ beyond $\omega$; this page keeps $\nu \le \omega$, as in Buchholz's paper.

## Remarks

### Examples

- [[Small values of ψ₀|TZHC9KJBWF]]: $\psi_0(0) = 1$, $\psi_0(1) = \omega$, $\psi_0(\alpha) = \omega^\alpha$ for $\alpha \le \varepsilon_0$, and $\psi_0(\alpha) = \varepsilon_0$ for $\varepsilon_0 \le \alpha \le \Omega$. Also $\psi_\nu(0) = \Omega_\nu$ and $\psi_0(\Omega + 1) = \omega^{\varepsilon_0 + 1}$.
- [[The value ψ₀(Ω·2)|T01DYDHV4C]]: $\psi_0(\Omega \cdot 2) = \varepsilon_1$. In the system of the collapsing function page, the term $\psi(\Omega \cdot 2)$ is $\zeta_1$, a much larger ordinal.
- $\psi_1(1) = \Omega \cdot \omega = \omega^{\Omega + 1}$. The set $C_1(1)$ contains every countable ordinal and $\psi_1(0) = \Omega$, so it contains $\Omega \cdot n + \beta$ for countable $\beta$, and nothing in between.
- Values cited from the Wikipedia article (section "Explanation"): $\psi_0(\Omega^2) = \zeta_0$, $\psi_0(\Omega^\Omega) = \Gamma_0$, the [[Feferman-Schütte ordinal|CNN7BK5YAW]], and $\psi_0(\varepsilon_{\Omega + 1}) = \psi_0(\Omega_2)$, the [[Bachmann-Howard ordinal|QH3ENXFRSV]].
- Values cited from the Wikipedia article on ordinal analysis (section "Table of ordinal analyses"): $\psi_0(\Omega_\omega)$ is the ordinal of [[Π¹₁-comprehension|2MGJJTSRFD]] $\Pi^1_1\text{-}\mathrm{CA}_0$, and $\psi_0(\varepsilon_{\Omega_\omega + 1})$ is the [[Takeuti-Feferman-Buchholz ordinal|NZWRK062WQ]].

### Non-examples

- [[ψ₀ is not a normal function|2MY5GMPJP5]]: the condition that fails is strict monotonicity, because $\psi_0(\varepsilon_0) = \psi_0(\Omega) = \varepsilon_0$.
- Drop the cardinals $\Omega_\nu$ for $\nu \ge 1$ and keep only $\psi_0$. Then the values are $\omega^\alpha$ for $\alpha \le \varepsilon_0$, and the function is constant $\varepsilon_0$ after that. The condition that fails is the presence of an uncountable level: the large arguments cannot be named in the closure set.
- The [[Veblen function|JQFAE9S2F4]] is not of this kind. It names $\varepsilon_0$ as $\varphi_1(0)$ by a fixed point from below, while Buchholz names it as $\psi_0(\Omega)$ by a collapse from above.

### Basic properties

1. $\psi_\nu(0) = \Omega_\nu$. The set $C_\nu(0)$ is the set of ordinals below $\Omega_\nu$, and this set is closed under addition, because $\Omega_\nu$ is $1$ or an infinite cardinal. (For $\nu = 0$ the set is $\set{0}$.)
2. $\Omega_\nu \le \psi_\nu(\alpha)$, because $C_\nu(\alpha)$ contains every ordinal below $\Omega_\nu$.
3. $\psi_\nu(\alpha) < \Omega_{\nu + 1}$ for $\nu < \omega$. The set $C_\nu(\alpha)$ has cardinality at most $\aleph_\nu$, because each stage adds at most $\aleph_\nu$ elements. The set of ordinals below $\Omega_{\nu+1}$ is larger, so it is not contained in $C_\nu(\alpha)$.
4. Each value $\rho = \psi_\nu(\alpha)$ is [[additively indecomposable|7TFCZSVX5R]]. Let $\beta, \gamma < \rho$ and assume $\beta + \gamma \ge \rho$. Then $\rho = \beta + \delta$ with $\delta \le \gamma < \rho$, and $\beta, \delta \in C_\nu(\alpha)$ give $\rho \in C_\nu(\alpha)$, a contradiction.
5. Each $\psi_\nu$ is weakly increasing, because $\alpha \le \alpha'$ gives $C_\nu(\alpha) \subseteq C_\nu(\alpha')$.
6. Buchholz proved that $\psi_\nu(\alpha + 1)$ is the next additively indecomposable ordinal after $\psi_\nu(\alpha)$ when $\alpha \in C_\nu(\alpha)$, and that $\psi_\nu(\alpha) = \omega^{\Omega_\nu + \alpha}$ for $1 \le \nu$ and $\alpha < \varepsilon_{\Omega_\nu + 1}$ (Wikipedia, section "Properties").
7. Normal form. Every nonzero ordinal of $C_0(\varepsilon_{\Omega_\omega + 1})$ is a sum $\psi_{\nu_1}(\beta_1) + \dots + \psi_{\nu_k}(\beta_k)$ with non-increasing summands and $\beta_i \in C_{\nu_i}(\beta_i)$. Buchholz turned these sums into a set $\mathrm{OT}$ of terms with a primitive recursive order (Wikipedia, section "Ordinal notation").

### History

Wilfried Buchholz introduced the functions in "A new system of proof-theoretic ordinal functions", Annals of Pure and Applied Logic 32 (1986).
He showed that they give the same values as Feferman's $\theta$-functions at the points used in proof theory, for example $\psi_0(\varepsilon_{\Omega_\nu + 1}) = \theta_{\varepsilon_{\Omega_\nu + 1}}(0)$.
The functions became a standard tool for the ordinals of $\mathrm{ID}_\nu$ and of $\Pi^1_1$-comprehension, and Buchholz also used the notation for the [[Buchholz hydra|9APRFM0G7F]] game.

### Common errors

- Comparing terms of two systems. $\psi_0(\Omega)$ in Buchholz's system is $\varepsilon_0$, while $\psi(\Omega)$ in the system with exponentiation is $\zeta_0$.
- Forgetting that $\Omega_0 = 1$ and not $0$. With $\Omega_0 = 0$ the set $C_0(0)$ would be empty, and the value $\psi_0(0) = 0$ would break the pattern $\psi_0(\alpha) = \omega^\alpha$.
- Reading $\psi_0(\alpha)$ as defined only for countable $\alpha$. The useful arguments are uncountable ordinals such as $\Omega$, $\Omega_2$ or $\varepsilon_{\Omega_\omega + 1}$.

## Explanations

### L1 human

Buchholz's functions are a way to give names to very large countable ordinals.
There is a tower of larger and larger infinities $\Omega_1, \Omega_2, \dots$, and each function $\psi_\nu$ turns expressions with these infinities into ordinals of level $\nu$.
The only operations allowed are addition and the functions $\psi$ themselves.
For example, $\psi_0(1) = \omega$, the first infinite ordinal, and $\psi_0(2) = \omega^2$.
The expression $\psi_0(\Omega)$ names $\varepsilon_0$, the ordinal that measures the strength of ordinary arithmetic.

### L2 human

We compute $\psi_0(3)$.

1. $C_0(3)$ contains $0$ and is closed under addition.
2. It contains $\psi_0(0) = 1$, $\psi_0(1) = \omega$ and $\psi_0(2) = \omega^2$, because $0, 1, 2 \in C_0(3)$ and they are below $3$.
3. It also contains $\psi_\mu(0) = \Omega_\mu$ for $\mu \ge 1$, but these are uncountable, and sums with them stay uncountable.
4. Sums of $1$, $\omega$ and $\omega^2$ give exactly the ordinals $\omega^2 \cdot a + \omega \cdot b + c$ with natural numbers $a, b, c$, so every ordinal below $\omega^3$.
5. Values $\psi_\mu(\xi)$ with $\xi \ge 3$ are not allowed, so $\omega^3 \notin C_0(3)$ and $\psi_0(3) = \omega^3$.

The typical use is a [[well-ordering proof|C5E5TG8PGP]]: a theory proves the well-foundedness of every initial segment below a term such as $\psi_0(\Omega_\omega)$, and the term measures the strength of the theory.
The trap is to forget the condition $\xi < \alpha$: without it the definition is circular.

### L3 human

Buchholz's system is the simplest member of a family of collapsing functions indexed by regular cardinals.
In proof theory the cardinal $\Omega_{\nu + 1}$ stands for the $(\nu + 1)$-th admissible ordinal above $\omega$, and the collapse $\psi_\nu$ mirrors the collapsing lemma for derivations with the $\Omega_{\nu + 1}$-rule of [[local predicativity|5C4YBXQV15]].
Replacing the countable tower by an inaccessible cardinal, a Mahlo cardinal or a weakly compact cardinal gives the systems of Rathjen, for example [[Rathjen's psi function|M7D1HEJQVH]], and stronger theories.
The terms of $\mathrm{OT}$ can be drawn as finite labelled trees, and the [[Buchholz hydra|9APRFM0G7F]] uses these trees to give a combinatorial statement that strong subsystems of second-order arithmetic do not prove.
