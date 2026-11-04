---
tag: 4YDQC8KBV0
kind: proof
name: Proof of the Jordan–Hölder theorem by induction on the length
msc: ["20E15", 20D30]
proves: 0E088ZP533
uses: [0NB8VPB93V, 096HN851YZ, 0C093D1T4M, 0W77CVBCHQ, 0YYWCNTPWR, 0PPP2J2DJV, 0S9ZVZ34MD, 0ZTGMDNVTB, 085PND4KNT]
sources:
  - url: https://www.isa-afp.org/browser_info/current/AFP/Jordan_Hoelder/document.pdf
---

## Proof

We argue by strong induction on the length $n$ of the first series.

1. Let $(X_1, \dots, X_n)$ and $(Y_1, \dots, Y_m)$ be finite lists of groups. Call them equivalent when $n = m$ and there is a suitable permutation $\sigma$ of $\{1, \dots, n\}$. It must make $X_i$ [[isomorphic|085PND4KNT]] to $Y_{\sigma(i)}$ for each $i$.
2. This relation is symmetric and transitive: invert or compose the permutations and the isomorphisms. A reordering of a list is equivalent to it. If two lists are equivalent, then they stay equivalent after the same group is added at the end of both.
3. For a [[composition series|0NB8VPB93V]], the factor list is $(G_1/G_0, \dots, G_n/G_{n-1})$. Let $P(n)$ be the following claim. For every group $G$, a composition series of length $n$ and any composition series of $G$ have equivalent factor lists. This is the theorem.
4. Each factor $G_i/G_{i-1}$ is [[simple|0C093D1T4M]], so it is not trivial and $G_{i-1} \neq G_i$. Hence a composition series has length $0$ exactly when $G = \{e\}$.
5. Base case $n = 0$. Then $G = \{e\}$, so by step 4 also $m = 0$. Two empty lists are equivalent.
6. Let $n \geq 1$ and assume $P(n')$ for all $n' < n$. By step 4, $G \neq \{e\}$ and $m \geq 1$. Let $A = G_{n-1}$ and $B = H_{m-1}$. Both are [[normal|0W77CVBCHQ]] in $G$, and $G/A$ and $G/B$ are simple.
7. Case $A = B$. The series $G_0, \dots, G_{n-1}$ and $H_0, \dots, H_{m-1}$ are composition series of $A$, the first of length $n - 1$. By $P(n-1)$, their factor lists are equivalent. Adding $G/A = G/B$ to both and using step 2 proves the claim in this case.
8. Case $A \neq B$. By the [[second isomorphism theorem|0PPP2J2DJV]], $AB$ is a subgroup of $G$. It is normal in $G$, because $g(ab)g^{-1} = (gag^{-1})(gbg^{-1})$ for $g \in G$, $a \in A$ and $b \in B$.
9. By the [[correspondence theorem|0S9ZVZ34MD]], $AB/A$ is a normal subgroup of the simple group $G/A$. So $AB/A$ is trivial or equal to $G/A$. By the bijection in that theorem, $AB = A$ or $AB = G$.
10. Suppose $AB = A$, so $B \subseteq A$. As in step 9, $A/B$ is normal in the simple group $G/B$, so $A = B$ or $A = G$. But $A \neq B$, and $A \neq G$ because $G/A$ is not trivial. So $AB = G$.
11. Let $D = A \cap B$. By the second isomorphism theorem with $S = A$ and $N = B$, $D$ is normal in $A$ and $A/D \cong AB/B = G/B$. In the same way, $D$ is normal in $B$ and $B/D \cong G/A$. So $A/D$ and $B/D$ are simple.
12. We build a composition series of $D$. For $0 \leq i \leq n-1$, let $D_i = D \cap G_i$, a subgroup by [[this result|0ZTGMDNVTB]]. Then $D_0 = \{e\}$ and $D_{n-1} = D \cap A = D$.
13. Fix $1 \leq i \leq n-1$. Apply the second isomorphism theorem in the group $G_i$, with $S = D_i$ and the normal subgroup $N = G_{i-1}$. Since $D_i \cap G_{i-1} = D_{i-1}$, we get $D_{i-1} \trianglelefteq D_i$ and $D_i/D_{i-1} \cong D_i G_{i-1}/G_{i-1}$.
14. The subgroup $D_i$ is normal in $G_i$. Indeed, for $x \in G_i \subseteq A$ we have $xDx^{-1} = D$, since $D \trianglelefteq A$, and $xG_ix^{-1} = G_i$.
15. As in step 8, $D_i G_{i-1}$ is then a normal subgroup of $G_i$ that contains $G_{i-1}$. By the correspondence theorem, $D_i G_{i-1}/G_{i-1}$ is normal in the simple group $G_i/G_{i-1}$, so it is trivial or all of $G_i/G_{i-1}$.
16. By steps 13 and 15, each factor $D_i/D_{i-1}$ is trivial or simple. Delete each $D_i$ with $D_i = D_{i-1}$. What remains is a composition series of $D$ of some length $k$, with a factor list $L$.
17. Adding $A$ on top gives a composition series of $A$ of length $k + 1$, with factor list $(L, A/D)$, by step 11. The series $G_0, \dots, G_{n-1}$ is a composition series of $A$ of length $n - 1$.
18. By $P(n-1)$ in the group $A$, the lists $(G_1/G_0, \dots, G_{n-1}/G_{n-2})$ and $(L, A/D)$ are equivalent. In particular, $k + 1 = n - 1$.
19. Adding $B$ on top of the series of $D$ gives a composition series of $B$ of length $k + 1 = n - 1$, with factor list $(L, B/D)$. The series $H_0, \dots, H_{m-1}$ is another composition series of $B$.
20. By $P(n-1)$ in the group $B$, the lists $(L, B/D)$ and $(H_1/H_0, \dots, H_{m-1}/H_{m-2})$ are equivalent. In particular, $m - 1 = n - 1$, so $m = n$.
21. By steps 2, 11 and 18, the factor list of the $G_i$ is equivalent to $(L, A/D, G/A)$, hence to $(L, G/B, G/A)$.
22. By steps 2, 11 and 20, the factor list of the $H_j$ is equivalent to $(L, B/D, G/B)$, hence to $(L, G/A, G/B)$.
23. The lists in steps 21 and 22 differ only by the order of the last two entries. By step 2, the two factor lists are equivalent. So $n = m$, and there is a permutation $\sigma$ with $G_i/G_{i-1} \cong H_{\sigma(i)}/H_{\sigma(i)-1}$ for each $i$.

## Idea

Compare the two maximal normal subgroups $A$ and $B$ just below $G$. If they are equal, the induction hypothesis applies to $A$ directly. If not, their intersection $D$ is a common maximal normal subgroup of both, with $A/D \cong G/B$ and $B/D \cong G/A$. One series of $D$ then links the two series of $G$, and the two top factors simply swap places.
