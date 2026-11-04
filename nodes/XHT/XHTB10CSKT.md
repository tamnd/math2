---
tag: XHTB10CSKT
kind: proof
name: Proof of the comparability of cardinals from Zorn's lemma
msc: ["03E10"]
proves: 0YBHSJMN3J
uses: [04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC, 0PVG1CRAJN, 0XHDTE5YMZ, 05GK32H72H, 01GTP8M5RG]
sources:
  - url: https://andrescaicedo.wordpress.com/2014/09/26/comparability-of-cardinals-from-zorns-lemma/
---

## Proof

We apply Zorn's lemma to the partial injections from $A$ to $B$.

1. Let $A$ and $B$ be sets. A partial injection is an [[injective function|0PVG1CRAJN]] $p \colon D \to B$ with $D \subseteq A$. We view $p$ as its set of pairs $\{(a, p(a)) : a \in D\}$.
2. Let $Q$ be the set of partial injections, ordered by inclusion $\subseteq$. This is a [[partial order|011C29Q1S1]]. The empty function lies in $Q$, so $Q$ is nonempty.
3. Let $K$ be a [[chain|0GP9ASVQ1X]] of $Q$. If $K$ is empty, the empty function is an [[upper bound|0H5J02P8S9]] of $K$.
4. Let $K$ be nonempty, and let $q = \bigcup_{p \in K} p$ be the [[union|05GK32H72H]] of these sets of pairs.
5. Let $(a, b), (a', b') \in q$, with $(a, b) \in p$ and $(a', b') \in p'$ for $p, p' \in K$. Since $K$ is a chain, both pairs lie in one member $r \in K$, the larger of $p$ and $p'$.
6. If $a = a'$, then $b = b'$, since $r$ is a [[function|0XHDTE5YMZ]]. If $b = b'$, then $a = a'$, since $r$ is injective.
7. By step 6, $q$ is an injective function from a subset of $A$ to $B$. So $q \in Q$, and $q$ is an upper bound of $K$.
8. By [[Zorn's lemma|04RXTQA5ZA]], $Q$ has a [[maximal element|0TZEEFTNCC]] $m \colon D \to B$. Let $E = m(D)$ be its image.
9. Suppose that $D \neq A$ and $E \neq B$. Pick $a \in A \setminus D$ and $b \in B \setminus E$.
10. Then $m \cup \{(a, b)\}$ is a function on $D \cup \{a\}$, and it is injective, because $b \notin E$. It lies in $Q$ and strictly contains $m$, contradicting maximality.
11. So $D = A$ or $E = B$. If $D = A$, then $m \colon A \to B$ is injective.
12. If $E = B$, then $m \colon D \to B$ is a bijection. Its inverse $m^{-1} \colon B \to D \subseteq A$ is an injective function from $B$ to $A$.
13. So there is an injection from $A$ to $B$ or from $B$ to $A$. By the [[order of cardinals|01GTP8M5RG]], $|A| \le |B|$ or $|B| \le |A|$.

## Idea

Build an injection from $A$ to $B$ as far as possible. Zorn's lemma gives one that cannot be extended. It cannot be extended only if it has used up all of $A$ or all of $B$, and each case gives an injection in one direction.
