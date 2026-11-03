---
tag: D3RW9XZVBQ
kind: definition
name: Tame symbol
msc: [19F15, 19C20]
defines: NPAX5HQFFQ
uses: [04C5ZBG1WT, A2KKZAV29W, MGM3CNJW9V, NJ3APQ8BHH]
sources:
  - url: https://en.wikipedia.org/wiki/Symbol_(number_theory)
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] with a [[discrete valuation|A2KKZAV29W]] $v \colon F^\times \to \Z$.
Let $\mathcal{O} = \set{x \in F : x = 0 \text{ or } v(x) \ge 0}$ be its [[valuation ring|MGM3CNJW9V]], with maximal ideal $\mathfrak{m}$ and [[residue field|NJ3APQ8BHH]] $k = \mathcal{O}/\mathfrak{m}$.
For $a, b \in F^\times$, the element
$$u(a, b) = (-1)^{v(a) v(b)} \, \frac{a^{v(b)}}{b^{v(a)}}$$
has valuation $0$, so it is a unit of $\mathcal{O}$.
The *tame symbol* of $a$ and $b$ is its residue
$$(a, b)_v = u(a, b) \bmod \mathfrak{m} \in k^\times.$$

## Remarks

The tame symbol is a Steinberg symbol: it is multiplicative in each variable, and $(a, 1 - a)_v = 1$ for $a \ne 0, 1$.
So it induces a homomorphism $\partial_v \colon K_2(F) \to k^\times$.
If $a$ and $b$ are both units of $\mathcal{O}$, then $(a, b)_v = 1$.
Some authors use the inverse of this element; the two conventions differ by a sign in additive notation.

Example: $F = \Q$, $v = v_p$ the $p$-adic valuation, and $k = \F_p$.
For an integer $u$ prime to $p$, $v_p(p) = 1$ and $v_p(u) = 0$, so $(p, u)_p = u^{-1} \bmod p$.

Non-example: the map $(a, b) \mapsto a^{v(b)} b^{-v(a)} \bmod \mathfrak{m}$, without the sign, is multiplicative in each variable but is not a Steinberg symbol in general.
For $F = \Q$, an odd prime $p$ and $a = 1/p$, one has $1 - a = (p - 1)/p$ and $v_p(a) = v_p(1 - a) = -1$.
The map without the sign gives $a^{-1}(1 - a) = p - 1 \equiv -1 \pmod p$, which is not $1$; the sign $(-1)^{1}$ corrects it to $1$.
