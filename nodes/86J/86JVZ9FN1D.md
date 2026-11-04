---
tag: 86JVZ9FN1D
kind: proof
name: Proof of the uniqueness of the algebraic closure
msc: [12F05]
proves: 01VQ7C4FTB
uses: [0QA8CHH8MG, 0MCXX29HWY, 09EYMKMSB9, 0NPW1DWECM, 02SJG1HC32, 07QY5RPFBR, 0MA5B744K3, 0GGE0Z0JQ1, 0GK1WB9R98, 0NFEG48RDR, 00EHX6FWC0, 0DQMDSVSXJ, 0AAHE7GEW6, 0DQG39K2NH, 0QKVE1GD9A, 095ZHQ7WCJ, 09J6KGT65G, 0ZMYX7GMH0, 0ZN39QDTP9, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 04RXTQA5ZA, 0TZEEFTNCC, 0J0XBKG64S, 09N7DZ7SDB, 0K3MWA7DMC, 0ASJVEFA9J]
methods: [0J0XBKG64S, 0ASJVEFA9J]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Theorem 6.6
---

## Proof

Let $L$ and $L'$ be [[algebraic closures|0MCXX29HWY]] of the [[field|0QA8CHH8MG]] $K$. First we extend embeddings by one element.

1. Let $E$ be a [[subfield|07QY5RPFBR]] of $L$ containing $K$, and $\varphi \colon E \to L'$ a [[ring homomorphism|0GGE0Z0JQ1]] with $\varphi(c) = c$ for $c \in K$. Let $\alpha \in L$.
2. Since $L/K$ is [[algebraic|09EYMKMSB9]], some nonzero $g \in K[x]$ has $g(\alpha) = 0$. As $K \subseteq E$, $\alpha$ is [[algebraic|0NPW1DWECM]] over $E$.
3. Let $m$ be the [[minimal polynomial|0GK1WB9R98]] of $\alpha$ over $E$. It is [[irreducible|0NFEG48RDR]] in $E[x]$, so $\deg m \ge 1$.
4. Let $\varphi m \in L'[x]$ be the polynomial obtained by applying $\varphi$ to the coefficients of $m$. It is monic of degree $\deg m \ge 1$.
5. Since $L'$ is [[algebraically closed|02SJG1HC32]], $\varphi m$ has a [[root|00EHX6FWC0]] $\beta \in L'$.
6. By the [[universal property of the polynomial ring|0DQMDSVSXJ]], $\psi \colon E[x] \to L'$, $h \mapsto (\varphi h)(\beta)$, is a ring homomorphism. Its [[kernel|0AAHE7GEW6]] contains $m$, so it contains $(m)$.
7. The kernel is not $E[x]$, since $\psi(1) = 1$. The ring $E[x]$ is a [[Euclidean domain|0DQG39K2NH]], hence a [[PID|0QKVE1GD9A]].
8. Since $m$ is irreducible, $(m)$ is a [[maximal ideal|09J6KGT65G]] by the [[theorem on principal ideal domains|095ZHQ7WCJ]]. So the kernel of $\psi$ equals $(m)$.
9. By the [[first isomorphism theorem|0ZMYX7GMH0]], $h + (m) \mapsto (\varphi h)(\beta)$ is an injective ring homomorphism $E[x]/(m) \to L'$.
10. By the [[structure of simple extensions|0ZN39QDTP9]], $h(\alpha) \mapsto h + (m)$ is a ring isomorphism $E(\alpha) \to E[x]/(m)$, where $E(\alpha)$ is the [[generated field|0MA5B744K3]].
11. Composing, $\varphi' \colon E(\alpha) \to L'$, $h(\alpha) \mapsto (\varphi h)(\beta)$, is a ring homomorphism. On constants $h = c \in E$ it gives $\varphi(c)$, so $\varphi'$ extends $\varphi$.

Now we apply Zorn's lemma.

12. Let $P$ be the set of pairs $(E, \varphi)$ as in Step 1. Write $(E_1, \varphi_1) \le (E_2, \varphi_2)$ when $E_1 \subseteq E_2$ and $\varphi_2$ restricts to $\varphi_1$ on $E_1$.
13. This relation is reflexive, antisymmetric and transitive, so $P$ is a [[partially ordered set|011C29Q1S1]]. It is nonempty, since it contains $K$ with its inclusion map into $L'$.
14. Let $C$ be a [[chain|0GP9ASVQ1X]] in $P$. If $C$ is empty, then $K$ with its inclusion map is an [[upper bound|0H5J02P8S9]]. Assume $C$ is nonempty, and let $U$ be the union of the fields $E$ with $(E, \varphi) \in C$.
15. Any two elements of $U$ lie in a common $E$ from $C$, since $C$ is a chain. So $U$ is a subfield of $L$ containing $K$.
16. For $u \in U$, set $\varphi_U(u) = \varphi(u)$ for any $(E, \varphi) \in C$ with $u \in E$. Two such pairs are comparable, so $\varphi_U(u)$ does not depend on the pair.
17. Any two elements of $U$ lie in one $E$ from $C$, so $\varphi_U$ preserves sums and products. So $(U, \varphi_U) \in P$, and it is an upper bound of $C$.
18. By [[Zorn's lemma|04RXTQA5ZA]], $P$ has a [[maximal element|0TZEEFTNCC]] $(E, \sigma)$.
19. Suppose $E \ne L$, for [[contradiction|0J0XBKG64S]], and pick $\alpha \in L \setminus E$. Steps 1 to 11 give $(E(\alpha), \sigma') \in P$ above $(E, \sigma)$ and different from it. This contradicts maximality, so $E = L$.

Finally we show that $\sigma \colon L \to L'$ is an isomorphism.

20. The map $\sigma$ is [[injective|09N7DZ7SDB]], so it is a ring isomorphism from $L$ onto the subfield $\sigma(L)$ of $L'$. Also $\sigma(c) = c$ for every $c \in K$.
21. The field $\sigma(L)$ is algebraically closed. Indeed, let $g \in \sigma(L)[x]$ with $\deg g \ge 1$. Applying $\sigma^{-1}$ to its coefficients gives $g_0 \in L[x]$ of the same degree.
22. Then $g_0$ has a root $r \in L$, and applying $\sigma$ to $g_0(r) = 0$ gives $g(\sigma(r)) = 0$.
23. Every nonzero $q \in \sigma(L)[x]$ is a product of a constant and factors $x - c_j$ with $c_j \in \sigma(L)$. This follows by [[induction|0ASJVEFA9J]] on $\deg q$ from Steps 21 and 22 and the [[factor theorem|0K3MWA7DMC]].
24. Let $b \in L'$. Since $L'/K$ is algebraic, $b$ has a minimal polynomial $m_b \in K[x]$, and $K \subseteq \sigma(L)$.
25. By Step 23, $m_b = \prod_j (x - c_j)$ with $c_j \in \sigma(L)$, since $m_b$ is monic. Evaluating at $b$ in the field $L'$ gives $\prod_j (b - c_j) = 0$.
26. So $b = c_j$ for some $j$, and $b \in \sigma(L)$. Thus $\sigma$ is surjective, and $\sigma \colon L \to L'$ is a ring isomorphism fixing $K$.

## Idea

An embedding of a subfield of $L$ into $L'$ over $K$ extends to one more element, by sending it to a root of the image of its minimal polynomial. Zorn's lemma gives an embedding of all of $L$. Its image is algebraically closed, and every element of $L'$ is a root of a polynomial that splits over the image, so the embedding is onto.
