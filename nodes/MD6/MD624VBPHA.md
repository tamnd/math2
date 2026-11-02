---
tag: MD624VBPHA
kind: definition
name: Crystalline cohomology
msc: [14F30, 14G17]
defines: EVXCN06FW3
uses: [5A35TYZD02, EXKGG9X6J0, 9537RKBZPP, C9Z22J9SQE, NYE0Z94MME, DZB378CNCK, 13F5JZPDD0]
sources:
  - url: https://en.wikipedia.org/wiki/Crystalline_cohomology
---

## Definition

Let $k$ be a perfect field of characteristic $p > 0$, let $W = W(k)$ be its ring of [[Witt vectors|C9Z22J9SQE]], and let $W_n = W/p^n W$.
Let $X$ be a [[scheme|5A35TYZD02]] that is [[smooth|EXKGG9X6J0]] and [[proper|9537RKBZPP]] over $k$.
A *divided power structure* on an ideal $I$ of a ring is a family of maps $\gamma_m \colon I \to I$, $m \ge 1$, with the identities of $x \mapsto x^m/m!$.
The ideal $pW_n$ of $W_n$ has a canonical one.
The *crystalline site* $\mathrm{Cris}(X/W_n)$ is the [[site|NYE0Z94MME]] defined as follows.

1. Its objects are triples $(U, T, \delta)$ with $U \subset X$ Zariski open and $U \hookrightarrow T$ a closed immersion into a $W_n$-scheme $T$ with ideal $I$.
   Here $\delta$ is a divided power structure on $I$ compatible with the one on $pW_n$.
2. Its morphisms are pairs of compatible maps $U \to U'$ and $T \to T'$ that respect the divided powers.
3. Its coverings are the families $\set{(U_i, T_i, \delta_i) \to (U, T, \delta)}$ in which the maps $T_i \to T$ are open immersions that cover $T$.

The *structure sheaf* $\mathcal{O}_{X/W_n}$ sends $(U, T, \delta)$ to $\Gamma(T, \mathcal{O}_T)$.
The *crystalline cohomology* of $X$ is
$$H^i_{\mathrm{cris}}(X/W) = \varprojlim_n H^i\big(\mathrm{Cris}(X/W_n), \mathcal{O}_{X/W_n}\big),$$
an [[inverse limit|DZB378CNCK]] of sheaf cohomology groups on these sites.

## Remarks

Each $H^i_{\mathrm{cris}}(X/W)$ is a finitely generated $W$-module, and it vanishes for $i > 2 \dim X$.
If $\mathfrak{X}$ is a smooth proper scheme over $W$ with special fiber $X$, then $H^i_{\mathrm{cris}}(X/W) \cong H^i_{\mathrm{dR}}(\mathfrak{X}/W)$, the [[algebraic de Rham cohomology|13F5JZPDD0]] of the lift.
Example: for $X = \mathbb{P}^1_k$, the lift $\mathbb{P}^1_W$ gives $H^0_{\mathrm{cris}} \cong H^2_{\mathrm{cris}} \cong W$ and $H^1_{\mathrm{cris}} = 0$.
Non-example: replacing $W$ by $k$, that is, taking only $n = 1$, gives the de Rham cohomology $H^i_{\mathrm{dR}}(X/k)$.
This is a vector space over a field of characteristic $p$, so it cannot give coefficients in a field of characteristic $0$.
After tensoring with the fraction field $K$ of $W$, crystalline cohomology is a Weil cohomology theory, with the Frobenius of $X$ acting semilinearly.
