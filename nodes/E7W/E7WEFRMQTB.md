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

Start with $0$ and allow only addition: you never leave $0$, so the first ordinal you miss is $1$.
Now allow the name $1$ as well, and sums of it give every natural number, so the first ordinal you miss is $\omega$.
Buchholz writes these two facts as $\psi_0(0) = 1$ and $\psi_0(1) = \omega$, and his functions $\psi_\nu$ turn this game of naming into a notation for very large countable ordinals.

Let $\Omega_0 = 1$, and for $0 < \nu \le \omega$ let $\Omega_\nu = \aleph_\nu$, the $\nu$-th uncountable [[cardinal|0EBACQFAZW]], seen as an initial ordinal.
For $\nu \le \omega$ and an [[ordinal|0YSCSX5YZC]] $\alpha$, let $C_\nu(\alpha)$ be the least set that contains every ordinal below $\Omega_\nu$, is closed under addition, and contains $\psi_\mu(\xi)$ for each $\mu \le \omega$ and each $\xi \in C_\nu(\alpha)$ with $\xi < \alpha$.
Then
$$\psi_\nu(\alpha) = \min \{ \gamma : \gamma \notin C_\nu(\alpha) \}.$$
The definition is a recursion on $\alpha$, simultaneous for all $\nu \le \omega$.

## Motivation

A [[collapsing function|8S6CT4TMB7]] with one uncountable ordinal $\Omega$ reaches the [[Bachmann-Howard ordinal|QH3ENXFRSV]], the ordinal of $\mathrm{ID}_1$, and no further.
The [[theories of iterated inductive definitions|5VNT564Y2W]] $\mathrm{ID}_\nu$ and the [[Π¹₁-comprehension|2MGJJTSRFD]] systems need a tower of large ordinals.
In Buchholz's system each level $\Omega_{\nu + 1}$ is collapsed into the level below by $\psi_\nu$, and $\psi_0$ brings everything down to countable ordinals.

Buchholz saw that closure under addition and under the functions $\psi_\mu$ is enough.
Multiplication and powers come for free, because $\psi_0$ produces the powers of $\omega$ by itself: $\psi_0(\alpha) = \omega^\alpha$ for $\alpha \le \varepsilon_0$.
So the definition is shorter than the earlier $\theta$ functions of Feferman, and the comparison of terms is a simple recursive procedure.
The system names every ordinal below $\psi_0(\varepsilon_{\Omega_\omega + 1})$, the [[Takeuti-Feferman-Buchholz ordinal|NZWRK062WQ]].

## Notation

We write $\Omega$ for $\Omega_1$, and many papers write $\psi$ for $\psi_0$.
The closure set is often built in stages $C^0_\nu(\alpha) \subseteq C^1_\nu(\alpha) \subseteq \dots$, where $C^0_\nu(\alpha)$ is the set of ordinals below $\Omega_\nu$ and each stage adds sums and allowed values of $\psi$.
Some authors extend the index $\nu$ beyond $\omega$; we keep $\nu \le \omega$, as in Buchholz's paper.

Watch out: the letter $\psi$ names different functions in different systems.
In the Wikipedia system of [[collapsing functions|8S6CT4TMB7]], which has exponentiation as an operation, $\psi(\Omega) = \zeta_0$.
In Buchholz's system, $\psi_0(\Omega) = \varepsilon_0$.
Every value below is a value of Buchholz's $\psi_\nu$.

## Remarks

### The first values

The [[small values of ψ₀|TZHC9KJBWF]] follow the opening pattern.
With $1 = \psi_0(0)$ and $\omega = \psi_0(1)$ available, $C_0(2)$ contains all sums of $1$ and $\omega$, which are the ordinals below $\omega^2$, so $\psi_0(2) = \omega^2$.
In general $\psi_0(\alpha) = \omega^\alpha$ for $\alpha \le \varepsilon_0$.
After that the function is stuck at $\varepsilon_0$ up to $\Omega$, because no countable argument at or above $\varepsilon_0$ can be named.
The name $\Omega = \psi_1(0)$ breaks the deadlock, and
$$\psi_0(\Omega) = \varepsilon_0, \qquad \psi_0(\Omega + 1) = \omega^{\varepsilon_0 + 1} = \varepsilon_0 \cdot \omega.$$

### Climbing with $\Omega$

Arguments between $\Omega$ and $\Omega \cdot 2$ list the ordinals between $\varepsilon_0$ and $\varepsilon_1$, and the next landmark is [[ψ₀(Ω·2) = ε₁|T01DYDHV4C]].
The higher functions behave the same way one level up.
For example, $\psi_1(1) = \Omega \cdot \omega = \omega^{\Omega + 1}$, because $C_1(1)$ contains every countable ordinal and $\Omega = \psi_1(0)$, hence every $\Omega \cdot n + \beta$, and nothing in between.
The Wikipedia article on the functions gives the landmarks
$$\psi_0(\Omega^2) = \zeta_0, \qquad \psi_0(\Omega^\Omega) = \Gamma_0, \qquad \psi_0(\varepsilon_{\Omega + 1}) = \psi_0(\Omega_2),$$
where $\Gamma_0$ is the [[Feferman-Schütte ordinal|CNN7BK5YAW]] and the last value is the Bachmann-Howard ordinal.
Higher up, $\psi_0(\Omega_\omega)$ is the ordinal of $\Pi^1_1\text{-}\mathrm{CA}_0$, and $\psi_0(\varepsilon_{\Omega_\omega + 1})$ is the ordinal of $\Pi^1_1\text{-}\mathrm{CA}_0 + \mathrm{BI}$ and of $\mathrm{ID}_{<\omega}$.

### The rules you can use

Each $\psi_\nu(0)$ is $\Omega_\nu$, because $C_\nu(0)$ is the set of ordinals below $\Omega_\nu$, and that set is closed under addition, since $\Omega_\nu$ is $1$ or an infinite cardinal.
Each value is at least $\Omega_\nu$, and for $\nu < \omega$ it is below $\Omega_{\nu + 1}$, because $C_\nu(\alpha)$ has at most $\aleph_\nu$ members.
Each value $\rho = \psi_\nu(\alpha)$ is [[additively indecomposable|7TFCZSVX5R]]: if $\beta, \gamma < \rho$ had $\beta + \gamma \ge \rho$, then $\rho = \beta + \delta$ with $\delta \le \gamma$, and $\rho$ would be in $C_\nu(\alpha)$.
Each $\psi_\nu$ is weakly increasing, since $\alpha \le \alpha'$ gives $C_\nu(\alpha) \subseteq C_\nu(\alpha')$.
By the Wikipedia article, $\psi_\nu(\alpha) = \omega^{\Omega_\nu + \alpha}$ for $\nu \ge 1$ and $\alpha < \varepsilon_{\Omega_\nu + 1}$.

### Terms and their order

Every nonzero member of $C_0(\varepsilon_{\Omega_\omega + 1})$ is a sum $\psi_{\nu_1}(\beta_1) + \dots + \psi_{\nu_k}(\beta_k)$ of non-increasing summands with $\beta_i \in C_{\nu_i}(\beta_i)$.
Buchholz turned these sums into a set $\mathrm{OT}$ of finite terms with a primitive recursive order.
On arguments with $\beta \in C_\nu(\beta)$ the function $\psi_\nu$ is strictly increasing, so two terms compare by comparing their arguments.

### What it is not

[[ψ₀ is not a normal function|2MY5GMPJP5]]: it fails strict monotonicity, since $\psi_0(\varepsilon_0) = \psi_0(\Omega) = \varepsilon_0$.
If we drop the levels $\Omega_\nu$ with $\nu \ge 1$, the function is $\omega^\alpha$ up to $\varepsilon_0$ and then constant, because large arguments cannot be named.
The [[Veblen function|JQFAE9S2F4]] is not of this kind: it names $\varepsilon_0$ as $\varphi_1(0)$ by a fixed point from below, while Buchholz names it as $\psi_0(\Omega)$ by a collapse from above.

### Watch out

Do not compare terms of two systems: $\psi_0(\Omega \cdot 2) = \varepsilon_1$ here, but $\psi(\Omega \cdot 2) = \zeta_1$ in the Wikipedia system with exponentiation.
Do not set $\Omega_0 = 0$.
Then $C_0(\alpha)$ would be empty for every $\alpha$, since a value of $\psi$ needs a named argument, and $\psi_0$ would be constantly $0$.
Finally, the useful arguments of $\psi_0$ are uncountable, such as $\Omega$, $\Omega_2$ or $\varepsilon_{\Omega_\omega + 1}$.

### History and a question

Wilfried Buchholz introduced the functions in "A new system of proof-theoretic ordinal functions", Annals of Pure and Applied Logic 32 (1986), and compared them there with Feferman's $\theta$ functions.
They became a standard tool for the ordinals of $\mathrm{ID}_\nu$ and of $\Pi^1_1$-comprehension, and their terms label the [[Buchholz hydra|9APRFM0G7F]].

Try it: compute $\psi_0(\omega)$.
The values $\psi_0(n) = \omega^n$ are available for every natural $n$, their sums give every ordinal below $\omega^\omega$, and $\omega^\omega$ itself is missed, so $\psi_0(\omega) = \omega^\omega$.

## Explanations

### L1 human

Buchholz's functions give names to very large countable ordinals.
There is a tower of larger and larger infinities $\Omega_1, \Omega_2, \dots$, and each function $\psi_\nu$ turns expressions with these infinities into ordinals of level $\nu$.
The only operations allowed are addition and the functions $\psi$ themselves.
For example, $\psi_0(1) = \omega$, the first infinite ordinal, and $\psi_0(2) = \omega^2$.
The expression $\psi_0(\Omega)$ names $\varepsilon_0$, the ordinal that measures the strength of ordinary arithmetic.

### L2 human

We compute $\psi_0(3)$.
The set $C_0(3)$ contains $0$, and it contains $\psi_0(0) = 1$, $\psi_0(1) = \omega$ and $\psi_0(2) = \omega^2$, since $0, 1, 2$ are named and below $3$.
It also contains $\psi_\mu(\xi)$ for $\mu \ge 1$, but these are uncountable, and sums with them stay uncountable.
Sums of $1$, $\omega$ and $\omega^2$ give exactly the ordinals
$$\omega^2 \cdot a + \omega \cdot b + c, \qquad a, b, c \in \mathbb{N},$$
which are the ordinals below $\omega^3$.
No value $\psi_0(\xi)$ with $\xi \ge 3$ is allowed, so $\psi_0(3) = \omega^3$.

The typical use is a well-ordering proof in [[ordinal analysis|C5E5TG8PGP]]: a theory proves the well-foundedness of each initial segment below a term such as $\psi_0(\Omega_\omega)$, and the term measures its strength.
The condition $\xi < \alpha$ is what keeps the definition from being circular.

### L3 human

Buchholz's system is the simplest member of a family of collapsing functions indexed by regular cardinals.
In proof theory the cardinal $\Omega_{\nu + 1}$ can be read as the $(\nu + 1)$-th admissible ordinal above $\omega$, and $\psi_\nu$ mirrors the collapsing lemma for derivations with Buchholz's [[Ω-rule|5C4YBXQV15]].
Replacing the countable tower by an inaccessible, a Mahlo or a weakly compact cardinal gives the systems of Rathjen, such as [[Rathjen's psi function|M7D1HEJQVH]], for stronger theories.
The terms of $\mathrm{OT}$ can be drawn as finite labeled trees, and the [[Buchholz hydra|9APRFM0G7F]] uses these trees for a combinatorial statement that $\Pi^1_1\text{-}\mathrm{CA}_0 + \mathrm{BI}$ does not prove.
