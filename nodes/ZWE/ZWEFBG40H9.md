---
tag: ZWEFBG40H9
kind: conjecture
name: Birch and Swinnerton-Dyer conjecture
msc: [11G40, 11G05, 14G10]
uses: [427N6S6QQW, P7V1BQJPSS, BZHGKN6Q3K, CS1NVJBZMH, BK9WBMF56G, 0ZXZ82FTX2]
about: [427N6S6QQW]
sources:
  - url: https://en.wikipedia.org/wiki/Birch_and_Swinnerton-Dyer_conjecture
same_as:
  wikidata: Q527863
  wikipedia: Birch and Swinnerton-Dyer conjecture
history:
  posed_by: "Bryan Birch and Peter Swinnerton-Dyer"
  first_stated: "1965"
---

## Statement

Let $E$ be an [[elliptic curve|427N6S6QQW]] over $\Q$ with conductor $N$.
For a prime $p \nmid N$, let $a_p = p + 1 - \#\tilde{E}(\F_p)$, where $\tilde{E}$ is the reduction of $E$ modulo $p$.
For $p \mid N$, let $a_p$ be $1$, $-1$ or $0$ when the reduction of $E$ at $p$ is split multiplicative, non-split multiplicative or additive.
Let
$$L(E, s) = \prod_{p \nmid N} \left(1 - a_p p^{-s} + p^{1 - 2s}\right)^{-1} \prod_{p \mid N} \left(1 - a_p p^{-s}\right)^{-1},$$
which converges for $\mathrm{Re}(s) > 3/2$ and extends to an entire function of $s$ by the [[modularity theorem|CS1NVJBZMH]].
Let $r$ be the rank of the finitely generated abelian group $E(\Q)$ of [[rational points|P7V1BQJPSS]].
Then $L(E, s)$ has a zero of order exactly $r$ at $s = 1$.

## Remarks

The refined form of the conjecture predicts the leading coefficient.
$$\lim_{s \to 1} \frac{L(E, s)}{(s - 1)^r} = \frac{\Omega_E \cdot \mathrm{Reg}_E \cdot \#\text{Ш}(E/\Q) \cdot \prod_{p \mid N} c_p}{(\# E(\Q)_{\mathrm{tors}})^2},$$
where $\Omega_E$ is the real period, $\mathrm{Reg}_E$ the regulator of the canonical height pairing, $\text{Ш}(E/\Q)$ the [[Tate–Shafarevich group|BK9WBMF56G]] (conjectured to be finite), and $c_p$ the Tamagawa numbers.
Status: the conjecture is open; it is one of the Clay Millennium Prize Problems.
Known results: if the order of vanishing of $L(E, s)$ at $s = 1$ is $0$ or $1$, then the rank equals it and $\text{Ш}(E/\Q)$ is finite.
This follows from the [[Gross–Zagier theorem|BX558DTV2D]] together with the work of Kolyvagin.
Coates and Wiles had earlier proved that if $E$ has [[complex multiplication|D3HEJTVY7G]] and $L(E, 1) \ne 0$, then $E(\Q)$ is finite.
Birch and Swinnerton-Dyer formulated the conjecture in the 1960s after computer experiments on the products $\prod_{p \le x} \#\tilde{E}(\F_p)/p$.

## Explanations

### L1 human

The rank measures how many independent rational points an elliptic curve has, but it is hard to compute.
The $L$-function packs together the numbers of points of the curve modulo every prime.
The conjecture says that the rank can be read off from the $L$-function: it is the order of its zero at $s = 1$.
Heuristically, a curve with many rational points tends to have many points modulo $p$, which pushes the Euler product toward zero at $s = 1$.
