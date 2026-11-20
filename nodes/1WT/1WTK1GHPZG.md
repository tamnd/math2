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

We first prove an extension fact, used in parts 3 and 5.

*Extension fact.* Let $Y$ be a subspace of $V$ and let $\psi \colon Y \to F$ be linear.
Then $\psi = g|_Y$ for some $g \in V^*$.

1. Choose a basis $C$ of $Y$. It is [[linearly independent|0CRMGPAH83]] in $V$, so it [[extends to a basis|0M4SXE5WW3]] $D \supseteq C$ of $V$.
2. By the [[theorem on maps determined by a basis|0R8X9XA83A]], there is $g \in V^*$ with $g(c) = \psi(c)$ for $c \in C$ and $g(d) = 0$ for $d \in D \setminus C$.
3. Then $g|_Y$ and $\psi$ are linear and agree on the basis $C$ of $Y$, so $g|_Y = \psi$.

*Part 1.*

4. $0 \in U^0$. If $f, g \in U^0$ and $a, b \in F$, then $(af + bg)(u) = a f(u) + b g(u) = 0$ for $u \in U$. So $U^0$ is a subspace.
5. Every form vanishes at $0$, so $\set{0}^0 = V^*$. A form that vanishes on $V$ is the zero form, so $V^0 = \set{0}$.

*Part 3.*

6. If $u \in U$ and $f \in U^0$, then $f(u) = 0$. So $U \subseteq (U^0)_0$.
7. Let $v \in V \setminus U$. Define $\psi$ on $Y = U + Fv$ by $\psi(u + av) = a$. This is well defined, since $u + av = u' + a'v$ with $a \ne a'$ would put $v$ in $U$.
8. $\psi$ is linear and vanishes on $U$. By the extension fact, $\psi = g|_Y$ for some $g \in V^*$.
9. Then $g \in U^0$ and $g(v) = 1 \ne 0$. So $v \notin (U^0)_0$, and $(U^0)_0 \subseteq U$.
10. If $U^0 = W^0$, then $U = (U^0)_0 = (W^0)_0 = W$. So $U \mapsto U^0$ is injective.

*Part 2.*

11. If $U \subseteq W$ and $f \in W^0$, then $f$ vanishes on $W$, hence on $U$. So $W^0 \subseteq U^0$.
12. Conversely, let $W^0 \subseteq U^0$. If $v \in (U^0)_0$, then $v$ is killed by every $f \in U^0$, hence by every $f \in W^0$. So $(U^0)_0 \subseteq (W^0)_0$.
13. By part 3, this says $U \subseteq W$.

*Part 4.*

14. $U \subseteq U + W$ and $W \subseteq U + W$, so part 2 gives $(U + W)^0 \subseteq U^0 \cap W^0$.
15. Let $f \in U^0 \cap W^0$. Then $f(u + w) = f(u) + f(w) = 0$ for $u \in U$, $w \in W$. So $f \in (U + W)^0$.

*Part 5.*

16. Let $f \in U^0$ and $g \in W^0$. On $U \cap W$, both vanish, so $f + g \in (U \cap W)^0$. Hence $U^0 + W^0 \subseteq (U \cap W)^0$.
17. Conversely, let $\varphi \in (U \cap W)^0$. Define $\psi$ on $U + W$ by $\psi(u + w) = \varphi(w)$, for $u \in U$, $w \in W$.
18. $\psi$ is well defined. If $u + w = u' + w'$, then $w - w' = u' - u \in U \cap W$. So $\varphi(w) - \varphi(w') = \varphi(w - w') = 0$.
19. $\psi$ is linear, because $\varphi$ is linear. By the extension fact, $\psi = g|_{U + W}$ for some $g \in V^*$.
20. For $u \in U$, we get $g(u) = \psi(u + 0) = \varphi(0) = 0$. So $g \in U^0$.
21. For $w \in W$, we get $g(w) = \psi(0 + w) = \varphi(w)$. So $\varphi - g \in W^0$.
22. Hence $\varphi = g + (\varphi - g) \in U^0 + W^0$.

*Part 6.*

23. Let $\dim V = n$ be finite, and let $X$ be a subspace of $V^*$. Then $X \subseteq (X_0)^0$, by the definition of $X_0$.
24. Let $\operatorname{ev} \colon V \to V^{**}$ be the evaluation map. Then $v \in X_0$ exactly when $\operatorname{ev}(v)$ vanishes on $X$, that is, $\operatorname{ev}(X_0) = X^0 \cap \operatorname{ev}(V)$.
25. $\operatorname{ev}$ is an isomorphism, by the theorem on the [[double dual|0ZJM9D7NPS]]. So $\operatorname{ev}(X_0) = X^0$, the annihilator of $X$ in $V^{**}$, and $\dim X_0 = \dim X^0$.
26. By the [[dimension of the annihilator|06Q1EFVH0Q]] for $X \subseteq V^*$, $\dim X^0 = n - \dim X$. So $\dim X_0 = n - \dim X$.
27. Again by that theorem, $\dim (X_0)^0 = n - \dim X_0 = \dim X$.
28. By step 23 and the theorem on the [[dimension of a subspace|0QW084460E]], $X = (X_0)^0$. So $U \mapsto U^0$ is onto, with inverse $X \mapsto X_0$.
29. It is injective by part 3, and it reverses inclusions by part 2.

## Idea

Parts 1, 2 and 4 follow from the definitions.
Parts 3 and 5 need forms with given values on a subspace, and the extension of a basis gives them.
Part 6 needs a count of dimensions, which only works in finite dimension.

## Variants

- In finite dimension, part 5 follows from part 4 by duality. Apply part 4 in $V^*$ to $U^0$ and $W^0$, and use the bijection of part 6.
- In finite dimension, step 17 to step 22 can be replaced by a dimension count: both sides of part 5 have dimension $n - \dim(U \cap W)$, by the Grassmann formula.
