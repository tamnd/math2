---
tag: P9V296DEAX
kind: proof
name: Proof of the existence of a complementary subspace by Zorn's lemma
msc: ["15A03", "03E25"]
topics: [QHKTJ89V6S]
audience: ug2
proves: 0P9T8WHNMH
methods: [0J0XBKG64S]
uses: [04RXTQA5ZA, 04C3BAHV03, 0EPTJA5QV4, 0V33SPH7RR, 0RMKABS2S5]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_subspace
    locator: Algebraic direct sum
  - url: https://en.wikipedia.org/wiki/Zorn%27s_lemma
    locator: Example applications
---

## Proof

1. Let $\mathcal{S}$ be the set of [[subspaces|0EPTJA5QV4]] $W$ of $V$ with $U \cap W = \{0\}$, ordered by inclusion. It is not empty, since $\{0\} \in \mathcal{S}$.
2. Let $\mathcal{C} \subseteq \mathcal{S}$ be a nonempty chain, and let $W^* = \bigcup_{W \in \mathcal{C}} W$.
3. $W^*$ is a subspace. It contains $0$. If $x, y \in W^*$, then $x \in W_1$ and $y \in W_2$ for some $W_1, W_2 \in \mathcal{C}$. As $\mathcal{C}$ is a chain, one of them contains the other, say $W_1 \subseteq W_2$. Then $x + y$ and $a x$ lie in $W_2 \subseteq W^*$.
4. $U \cap W^* = \{0\}$: a vector of $U \cap W^*$ lies in $U \cap W$ for some $W \in \mathcal{C}$, so it is $0$.
5. So $W^* \in \mathcal{S}$ is an upper bound of $\mathcal{C}$. By [[Zorn's lemma|04RXTQA5ZA]], $\mathcal{S}$ has a maximal element $W$.
6. We have $U \cap W = \{0\}$, since $W \in \mathcal{S}$. It remains to show $U + W = V$, the [[sum|0RMKABS2S5]].
7. Suppose, for a contradiction, that there is $v \in V$ with $v \notin U + W$. Let $W' = W + F v$.
8. Let $x \in U \cap W'$, so $x = w + a v$ with $w \in W$ and $a \in F$.
9. If $a \ne 0$, then $v = a^{-1}(x - w) \in U + W$, a contradiction. Here we use that $F$ is a field.
10. So $a = 0$, and $x = w \in U \cap W = \{0\}$. Hence the [[intersection|0V33SPH7RR]] $U \cap W'$ is $\{0\}$, and $W' \in \mathcal{S}$.
11. Also $v \in W'$ and $v \notin W$, since $v \notin U + W$. So $W \subsetneq W'$, which contradicts the maximality of $W$.
12. Hence $U + W = V$, and $W$ is a [[complement|04C3BAHV03]] of $U$.
13. For the dimension formula in finite dimension: a basis of $U$ together with a basis of $W$ is a basis of $V = U \oplus W$, so $\dim V = \dim U + \dim W$.

## Idea

Take a subspace that is as large as possible among those that avoid $U$.
If it missed some direction $v$, adding $v$ would give a larger subspace that still avoids $U$.

## Variants

- The [[proof by extending a basis|K653S85P27]] gives the same result through a basis of $V$.
- In finite dimension, Zorn's lemma is not needed: start from $W = \{0\}$ and add vectors $v \notin U + W$ one at a time, as in steps 7 to 10. The dimension of $W$ increases each time, so the process stops after at most $\dim V - \dim U$ steps.
