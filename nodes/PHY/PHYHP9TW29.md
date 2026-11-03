---
tag: PHYHP9TW29
kind: statement
role: theorem
name: Plancherel theorem for spherical functions
msc: ["43A90", "22E30", "43A85"]
uses: [XJS07AJ50Y, T2EB8R9HEV, VY0HXD3GC4, BKZNC76RC8, A6MQCW28KZ, JGCQX7ESVE, AYN9675FTS, 0V33BNKZ9S]
about: [E06PG40SVD, BKZNC76RC8]
sources:
  - url: https://en.wikipedia.org/wiki/Plancherel_theorem_for_spherical_functions
same_as:
  wikidata: Q11573495
  wikipedia: Plancherel theorem for spherical functions
---

## Statement

Let $G$ be a connected noncompact [[semisimple Lie group|XJS07AJ50Y]] with finite centre, and $K$ a [[maximal compact subgroup|T2EB8R9HEV]].
Let $G = K A N$ be an Iwasawa decomposition, with $\mathfrak a$ the Lie algebra of $A$.
Let $W$ be the Weyl group of the restricted roots, of order $\abs{W}$.
Let $\varphi_\lambda$, for $\lambda \in \mathfrak a^*_\C$, be the [[spherical functions|BKZNC76RC8]] given by [[Harish-Chandra's formula|A6MQCW28KZ]], let $\hat f(\lambda) = \int_G f(g) \varphi_{-\lambda}(g) \, dg$ be the [[spherical transform|JGCQX7ESVE]], and let $c$ be the [[Harish-Chandra c-function|AYN9675FTS]].
Then, for a suitable normalization of the [[Haar measure|VY0HXD3GC4]] $dg$ on $G$ and of the Lebesgue measure $d\lambda$ on $\mathfrak a^*$:

1. For every [[smooth|0V33BNKZ9S]] bi-$K$-invariant function $f$ with compact support on $G$ and every $g \in G$,
$$f(g) = \frac{1}{\abs{W}} \int_{\mathfrak a^*} \hat f(\lambda) \, \varphi_\lambda(g) \, \abs{c(\lambda)}^{-2} \, d\lambda.$$
2. For every such $f$,
$$\int_G \abs{f(g)}^2 \, dg = \frac{1}{\abs{W}} \int_{\mathfrak a^*} \abs{\hat f(\lambda)}^2 \, \abs{c(\lambda)}^{-2} \, d\lambda.$$
3. The map $f \mapsto \hat f$ extends to a unitary isomorphism from the space of bi-$K$-invariant functions in $L^2(G)$ onto the space of $W$-invariant functions in $L^2(\mathfrak a^*, \abs{W}^{-1} \abs{c(\lambda)}^{-2} \, d\lambda)$.

## Remarks

The theorem is due to Harish-Chandra.
The density $\abs{c(\lambda)}^{-2}$ comes from the asymptotics $\varphi_\lambda(\exp t H) \approx \sum_{w \in W} c(w \lambda) e^{(i w \lambda - \rho)(t H)}$ as $t \to \infty$, which compare $\varphi_\lambda$ with plane waves on $A$.
Only real $\lambda$ occur, so only the spherical unitary principal series contributes; the complementary series and the trivial representation have Plancherel measure zero.
The [[Gindikin–Karpelevich formula|5N2F22Y6AH]] gives $c$ as a product of Gamma function quotients, which makes the density explicit.

Example: for $G = \mathrm{SL}(2, \R)$ write $\lambda = s \rho$ with $s \in \R$.
Then $\abs{c(s \rho)}^{-2} = \tfrac{\pi s}{2} \tanh\big(\tfrac{\pi s}{2}\big)$, so the inversion formula on the hyperbolic plane uses the density $s \tanh(\pi s / 2)$ up to a constant.

## Explanations

### L1 human

On the line, a function can be rebuilt from its Fourier transform, and its energy equals the energy of the transform.
The same holds for radial functions on a symmetric space such as the hyperbolic plane, with spherical functions in place of exponentials.
The difference is a weight, $\abs{c(\lambda)}^{-2}$, that says how much each frequency counts.

### L2 human

This is the bi-$K$-invariant part of the full [[Harish-Chandra Plancherel theorem|N137YA7RGS]].
It extends to all of $L^2(G / K)$ through the [[Helgason Fourier transform|K533EAPKKY]], with the same density.
Its companion for compactly supported functions is the [[Paley–Wiener theorem for symmetric spaces|QA8BFW2QS4]], which describes the image of $\hat f$.
