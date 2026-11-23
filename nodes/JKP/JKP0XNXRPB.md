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

The Herbrand universe of a signature is the set of its closed terms, built up from the constants by the function symbols.

Let $L$ be a [[signature|WDVVEYD6AT]] that contains at least one constant symbol; if $L$ has none, we replace $L$ by $L \cup \{ c_0 \}$ for a new constant symbol $c_0$.
We define sets of closed [[terms|6D3WA7N2W4]] by [[recursion|AM4GQQMZ3C]] on $k \in \mathbb{N}$.
The set $H_0$ is the set of constant symbols of $L$, and
$$H_{k+1} = H_k \cup \{ f(t_1, \ldots, t_n) : f \text{ is an } n\text{-ary function symbol of } L \text{ and } t_1, \ldots, t_n \in H_k \}.$$
The Herbrand universe of $L$ is
$$H(L) = \bigcup_{k \in \mathbb{N}} H_k.$$
The Herbrand base of $L$ is the set $B(L)$ of atomic formulas $R(t_1, \ldots, t_n)$, where $R$ is an $n$-ary relation symbol of $L$ and $t_1, \ldots, t_n \in H(L)$.

## Notation

$H(L)$ is also written $H_L$ or $U_L$, and $B(L)$ is also written $B_L$.
The elements of $H(L)$ are the closed terms, or ground terms, of $L$, and the elements of $B(L)$ are the ground atoms.

## Remarks

The added constant $c_0$ is there for one reason: a signature without constants has no closed terms, as [[the signature with one unary function symbol|5Y0RH5JH4T]] shows, and a structure needs a nonempty domain.
The added constant does not change which sets of $L$-sentences have models, since $c_0$ can name any element of a model.

The recursion gives exactly the terms without variables.
Each $H_k$ contains only closed terms, by induction on $k$.
Conversely, a closed term of height $k$ lies in $H_k$, by induction on the term.
The union over all $k$ is needed, because a term of large height appears only at a late level.

For example, take $L = \{ a, s, P \}$ with $s$ a unary function symbol and $P$ a unary relation symbol.
Then $H_0 = \{ a \}$, $H_1 = \{ a, s(a) \}$ and, in general, $H_k = \{ s^j(a) : 0 \leq j \leq k \}$, where $s^j(a)$ is $a$ with $j$ copies of $s$ in front.
So $H(L) = \{ s^j(a) : j \in \mathbb{N} \}$, and $B(L) = \{ P(s^j(a)) : j \in \mathbb{N} \}$.

The equality symbol is a logical symbol and not a relation symbol of $L$, so $B(L)$ contains no equations.
The concept page [[Herbrand universe|NFW38QJ3A7]] gives more examples and the main properties.

## Explanations

### L1 human

Start with the constant names, then apply each function symbol to names that you already have, and repeat forever.
With one name $a$ and one symbol $s$, you get $a$, then $s(a)$, then $s(s(a))$, and so on.
The Herbrand universe is everything you get this way.

### L2 human

A typical use is to list the ground instances of a universal sentence.
For $L = \{ a, s, P \}$ and the sentence $\forall x \, (P(x) \to P(s(x)))$, we replace $x$ by each element $s^j(a)$ of $H(L)$:
$$P(s^j(a)) \to P(s^{j+1}(a)) \qquad (j = 0, 1, 2, \ldots).$$
Each instance is built from two atoms of $B(L)$.
Watch out: the relation symbol $P$ never enters $H(L)$, because $P(a)$ is a formula and not a term.
