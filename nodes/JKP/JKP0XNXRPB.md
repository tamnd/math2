---
tag: JKP0XNXRPB
kind: definition
name: Herbrand universe
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
defines: NFW38QJ3A7
uses: [6D3WA7N2W4, WDVVEYD6AT, AM4GQQMZ3C]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]] that contains at least one constant symbol; if $L$ has none, replace $L$ by $L \cup \set{c_0}$ for a new constant symbol $c_0$.
Define sets of closed [[terms|6D3WA7N2W4]] by [[recursion|AM4GQQMZ3C]] on $k \in \N$:

- $H_0$ is the set of constant symbols of $L$;
- $H_{k+1} = H_k \cup \set{f(t_1, \ldots, t_n) : f \text{ is an } n\text{-ary function symbol of } L \text{ and } t_1, \ldots, t_n \in H_k}$.

The Herbrand universe of $L$ is $H(L) = \bigcup_{k \in \N} H_k$.
The Herbrand base of $L$ is the set $B(L)$ of atomic formulas $R(t_1, \ldots, t_n)$ with $R$ an $n$-ary relation symbol of $L$ and $t_1, \ldots, t_n \in H(L)$.

## Notation

$H(L)$ is also written $H_L$ or $U_L$, and $B(L)$ is also written $B_L$.
The elements of $H(L)$ are the closed terms, or ground terms, of $L$.

## Remarks

$H(L)$ is exactly the set of terms of $L$ without variables: each $H_k$ consists of closed terms, and each closed term of height $k$ lies in $H_k$, by induction on terms.
The equality symbol is not a relation symbol of $L$, so $B(L)$ contains no equations.
The concept page [[Herbrand universe|NFW38QJ3A7]] gives examples and properties.

## Explanations

### L1 human

Start with the constant names, then apply each function symbol to names that you already have, and repeat forever.
The Herbrand universe is everything you get this way.

### L2 human

We compute the definition for $L = \set{a, s, P}$, with $s$ unary and $P$ unary.

1. $H_0 = \set{a}$.
2. $H_1 = \set{a, s(a)}$, and $H_2 = \set{a, s(a), s(s(a))}$.
3. In general $H_k = \set{s^j(a) : 0 \leq j \leq k}$, where $s^j(a)$ is $a$ with $j$ copies of $s$ in front.
4. So $H(L) = \set{s^j(a) : j \in \N}$ and $B(L) = \set{P(s^j(a)) : j \in \N}$.

The typical use is to list the ground instances of a universal sentence, such as $P(s^j(a)) \to P(s^{j+1}(a))$ for $\forall x \, (P(x) \to P(s(x)))$.
A trap is to put the relation symbol $P$ into $H(L)$; relation symbols form atoms of $B(L)$, not terms.
