---
tag: 1WTK1GHPZG
kind: proof
name: Proof of the properties of annihilators
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: Z71CEX564V
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0R6M158SQ9, 0M4SXE5WW3, 0R8X9XA83A, 0CRMGPAH83, 0ZJM9D7NPS, 06Q1EFVH0Q, 0QW084460E]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Quotient spaces and annihilators
---

## Proof

We first show that a form on a subspace extends to all of $V$, and then we prove the six parts of the [[lemma|Z71CEX564V]] in the order 1, 3, 2, 4, 5, 6.

*Extension fact.* Let $Y$ be a subspace of $V$ and let $\psi \colon Y \to F$ be linear. Then $\psi = g|_Y$ for some $g \in V^*$.

1. Choose a basis $C$ of $Y$. It is [[linearly independent|0CRMGPAH83]] in $V$, so it [[extends to a basis|0M4SXE5WW3]] $D \supseteq C$ of $V$.
2. A linear map may take any values on a basis, by the [[theorem on maps determined by a basis|0R8X9XA83A]]. So there is $g \in V^*$ with $g(c) = \psi(c)$ for $c \in C$ and $g(d) = 0$ for $d \in D \setminus C$.
3. The maps $g|_Y$ and $\psi$ are linear and agree on the basis $C$ of $Y$, so $g|_Y = \psi$.

*Part 1.*

4. The zero form vanishes on $U$, so $0 \in U^0$. If $f, g \in U^0$ and $a, b \in F$, then $(af + bg)(u) = a f(u) + b g(u) = 0$ for every $u \in U$. So $U^0$ is a subspace.
5. Every form vanishes at $0$, so $\{0\}^0 = V^*$. A form that vanishes at every vector of $V$ is the zero form, so $V^0 = \{0\}$.

*Part 3.*

6. If $u \in U$ and $f \in U^0$, then $f(u) = 0$ by the definition of $U^0$. So $U \subseteq (U^0)_0$.
7. For the reverse inclusion, let $v \in V$ with $v \notin U$, and put $Y = U + Fv$. Every element of $Y$ is $u + av$ with $u \in U$ and $a \in F$, and $a$ is unique: if $u + av = u' + a'v$ with $a \ne a'$, then $v = (u' - u)/(a - a')$ lies in $U$.
8. So $\psi(u + av) = a$ defines a map $Y \to F$. It is linear and vanishes on $U$. By the extension fact, $\psi = g|_Y$ for some $g \in V^*$.
9. Then $g \in U^0$ and $g(v) = \psi(v) = 1 \ne 0$. So $v \notin (U^0)_0$, and this proves $(U^0)_0 \subseteq U$.
10. If $U^0 = W^0$, then $U = (U^0)_0 = (W^0)_0 = W$. So $U \mapsto U^0$ is injective.

*Part 2.*

11. Let $U \subseteq W$ and $f \in W^0$. Then $f$ vanishes on $W$, hence on $U$, so $f \in U^0$. This gives $W^0 \subseteq U^0$.
12. Conversely, let $W^0 \subseteq U^0$, and let $v \in (U^0)_0$. Then every $f \in U^0$ kills $v$, so in particular every $f \in W^0$ kills $v$, and $v \in (W^0)_0$.
13. So $(U^0)_0 \subseteq (W^0)_0$, and part 3 turns this into $U \subseteq W$.

*Part 4.*

14. Since $U \subseteq U + W$ and $W \subseteq U + W$, part 2 gives $(U + W)^0 \subseteq U^0$ and $(U + W)^0 \subseteq W^0$.
15. Conversely, let $f \in U^0 \cap W^0$. For $u \in U$ and $w \in W$ we get $f(u + w) = f(u) + f(w) = 0$, so $f \in (U + W)^0$.

*Part 5.*

16. Let $f \in U^0$ and $g \in W^0$. Both vanish on $U \cap W$, so $f + g \in (U \cap W)^0$. This gives $U^0 + W^0 \subseteq (U \cap W)^0$.
17. Conversely, let $\varphi \in (U \cap W)^0$. We try to define $\psi$ on $U + W$ by $\psi(u + w) = \varphi(w)$ for $u \in U$ and $w \in W$.
18. This is well defined. If $u + w = u' + w'$, then $w - w' = u' - u$ lies in $U \cap W$, so $\varphi(w) - \varphi(w') = \varphi(w - w') = 0$.
19. The map $\psi$ is linear because $\varphi$ is linear. By the extension fact, $\psi = g|_{U + W}$ for some $g \in V^*$.
20. For $u \in U$, we get $g(u) = \psi(u + 0) = \varphi(0) = 0$. So $g \in U^0$.
21. For $w \in W$, we get $g(w) = \psi(0 + w) = \varphi(w)$. So $\varphi - g$ vanishes on $W$, that is, $\varphi - g \in W^0$.
22. Hence $\varphi = g + (\varphi - g)$ lies in $U^0 + W^0$.

*Part 6.* Let $\dim V = n$ be finite, and let $X$ be a subspace of $V^*$.

23. Every $f \in X$ vanishes on $X_0$ by the definition of $X_0$, so $X \subseteq (X_0)^0$.
24. Let $\operatorname{ev} \colon V \to V^{**}$ be the evaluation map, $\operatorname{ev}(v)(f) = f(v)$. A vector $v$ lies in $X_0$ exactly when $\operatorname{ev}(v)$ vanishes on $X$, that is, when $\operatorname{ev}(v)$ lies in the annihilator $X^0 \subseteq V^{**}$.
25. The map $\operatorname{ev}$ is an isomorphism in finite dimension, by the theorem on the [[double dual|0ZJM9D7NPS]]. So $\operatorname{ev}$ maps $X_0$ onto $X^0$, and $\dim X_0 = \dim X^0$.
26. The [[dimension of the annihilator|06Q1EFVH0Q]], applied to $X$ inside the $n$-dimensional space $V^*$, gives $\dim X^0 = n - \dim X$. So $\dim X_0 = n - \dim X$.
27. The same theorem, applied to $X_0$ inside $V$, gives $\dim (X_0)^0 = n - \dim X_0 = \dim X$.
28. So $X$ is a subspace of $(X_0)^0$ of the same finite dimension, and the theorem on the [[dimension of a subspace|0QW084460E]] gives $X = (X_0)^0$.
29. Hence every subspace of $V^*$ is an annihilator, so $U \mapsto U^0$ is onto, and $X \mapsto X_0$ is its inverse by step 28 and part 3. It reverses inclusions by part 2.

## Idea

Parts 1, 2 and 4 come straight from the definitions, once part 3 is known.
Parts 3 and 5 need forms with prescribed values on a subspace, and the extension of a basis produces them.
In part 3 the prescribed form separates a vector from the subspace, and in part 5 it splits a form on $U \cap W$ into a piece that kills $U$ and a piece that kills $W$.
Part 6 is a count of dimensions, and it is the only part that needs $V$ to be finite-dimensional.

## Variants

In finite dimension, part 5 follows from part 4 by duality.
Apply part 4 in $V^*$ to the subspaces $U^0$ and $W^0$, carry the result back to $V$ with the evaluation map, and use the bijection of part 6.

In finite dimension one can also count dimensions in part 5.
Put $u = \dim U$ and $w = \dim W$.
The [[Grassmann formula|06HTJNCMPA]] in $V^*$ and part 4 give the first equality below, and the Grassmann formula in $V$ gives the second:
$$\dim(U^0 + W^0) = (n - u) + (n - w) - (n - \dim(U + W)) = n - \dim(U \cap W),$$
which is $\dim (U \cap W)^0$.
Since step 16 gives one inclusion, the two subspaces are equal.

In infinite dimension the extension of a basis, and so the whole proof of parts 3 and 5, rests on the existence of bases, which uses the [[axiom of choice|0HTGB13FE2]].
