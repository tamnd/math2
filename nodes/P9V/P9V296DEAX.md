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

We take a subspace that is maximal among those meeting $U$ only in $0$, and we show by contradiction that it already fills the rest of $V$.

1. Let $\mathcal{S}$ be the set of [[subspaces|0EPTJA5QV4]] $W$ of $V$ with $U \cap W = \{0\}$, ordered by inclusion.
   It is not empty, since $\{0\} \in \mathcal{S}$.
2. Let $\mathcal{C} \subseteq \mathcal{S}$ be a nonempty chain, and let $W^* = \bigcup_{W \in \mathcal{C}} W$.
3. We show that $W^*$ is a subspace.
   It contains $0$, since each member of $\mathcal{C}$ does.
   If $x, y \in W^*$ and $a \in F$, then $x \in W_1$ and $y \in W_2$ for some $W_1, W_2 \in \mathcal{C}$.
   Since $\mathcal{C}$ is a chain, one of them contains the other, say $W_1 \subseteq W_2$.
   Then $x + y$ and $a x$ lie in the subspace $W_2$, so they lie in $W^*$.
4. A vector of $U \cap W^*$ lies in $U \cap W$ for some $W \in \mathcal{C}$, so it is $0$.
   Hence $U \cap W^* = \{0\}$.
5. So $W^* \in \mathcal{S}$, and it is an upper bound of $\mathcal{C}$.
   By [[Zorn's lemma|04RXTQA5ZA]], $\mathcal{S}$ has a maximal element $W$.
6. We have $U \cap W = \{0\}$, since $W \in \mathcal{S}$.
   It remains to show that the [[sum|0RMKABS2S5]] $U + W$ is $V$.
7. Suppose, for a contradiction, that some $v \in V$ is not in $U + W$, and let $W' = W + F v$.
8. Let $x \in U \cap W'$, and write $x = w + a v$ with $w \in W$ and $a \in F$.
9. If $a \ne 0$, then $v = a^{-1}(x - w)$, which lies in $U + W$ because $x \in U$ and $w \in W$.
   This contradicts the choice of $v$, so $a = 0$.
   Here we use that the nonzero scalar $a$ has an inverse in the field $F$.
10. With $a = 0$ we get $x = w \in U \cap W = \{0\}$.
    So the [[intersection|0V33SPH7RR]] $U \cap W'$ is $\{0\}$, and $W' \in \mathcal{S}$.
11. Also $v \in W'$, and $v \notin W$, since $v \notin U + W$.
    So $W \subsetneq W'$, which contradicts the maximality of $W$.
12. Hence $U + W = V$, and $W$ is a [[complement|04C3BAHV03]] of $U$.
13. For the dimension formula, let $V$ be finite-dimensional.
    A basis of $U$ followed by a basis of $W$ is a basis of $V = U \oplus W$, so $\dim V = \dim U + \dim W$.

## Idea

Look at all the subspaces that avoid $U$, and take one that is as large as possible.
If it missed some direction $v$ outside $U + W$, then adding $v$ would give a larger subspace that still avoids $U$.
Zorn's lemma is the tool that produces a largest one, because the union of a chain of subspaces that avoid $U$ is again such a subspace.

## Variants

The [[proof by extending a basis|K653S85P27]] reaches the same result through a basis of $V$ that extends a basis of $U$.
In infinite dimension it also needs Zorn's lemma, inside the theorem that a basis can be extended.

In finite dimension, Zorn's lemma is not needed.
Start from $W = \{0\}$, and while $U + W \ne V$, choose $v \notin U + W$ and replace $W$ by $W + F v$, as in steps 7 to 10.
Each step keeps $U \cap W = \{0\}$ and raises $\dim W$ by $1$, so the process stops after at most $\dim V - \dim U$ steps, and then $U + W = V$.
