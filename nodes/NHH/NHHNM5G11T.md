---
tag: NHHNM5G11T
kind: proof
name: Proof of Zorn's lemma
msc: ["03E25"]
proves: 04RXTQA5ZA
sources:
  - wikipedia: en:51442@r1364256157
    locator: Zorn's lemma, section Example applications > A proof of Tychonoff's theorem
    note: adopted
    mention: wikipedia://en/51442#G4L4
    sections: [Proof]
---

## Proof

Zorn's lemma implies the ultrafilter lemma, which in turn implies [[Tychonoff's theorem|0JTRSJKCFB]] (together with the axiom of choice). However, it is also possible to prove Tychonoff's theorem directly from Zorn's lemma as follows (by using an ultrafilter implicitly).

Let $X_i$ be a family of [[compact spaces|0QPHW703PV]], not necessarily Hausdorff. We shall show that a family $F$ of closed subsets of $X := \prod_i X_i$ with the [[finite intersection property|00BWV5CKCF]] has nonempty intersection. Let $P$ be the collection of all the families of subsets of $X$ with the finite intersection property (not necessarily closed subsets). We let $P$ be ordered by set inclusion. If $C \subset P$ is a chain, then clearly the union of $C$ has the finite intersection property; so, the union is in $P$. Thus, by Zorn's lemma, there is a maximal element $M$ in $P$ containing $F$. We shall show that the intersection of all the closed sets in $M$ has nonempty intersection; *a fortiori*, $F$ has nonempty intersection.

For each finite subset $M' \subset M$, since $\cap M'$ is nonempty, $\cap p_i(M')$ is nonempty for the projection $p_i : X \to X_i.$ Thus, for each $i$, the set

$$N_i := \left \{ \overline{p_i(A)} \mid A \in M \right \}$$

has nonempty intersection since it has the finite intersection property and $X_i$ is compact. We note

1. If $M' \subset M$ is a finite subset, $\cap M'$ is in $M$.
1. For an open set $U_i$ intersecting $\cap N_i$, we have $p_i^{-1}(U_i)$ is in $M$.

Indeed, (1) holds since $M = M \cup \{ \cap M' \}$ by maximality, as the set on the right has the finite intersection property. Similarly, for a finite subset $M' \subset M$, since $A = \cap M'$ is in $M$, $U_i \cap p_i(A) \ne \emptyset$ or $p_i^{-1}(U_i) \cap A \ne \emptyset$. Thus, the set $M \cup \{ p_i^{-1}(U_i) \}$ has the finite intersection property and (2) follows by the maximality of $M$.

Now, by the axiom of choice, we can find an element $m$ in $\prod_i (\cap N_i)$. We claim this $m$ is in each closed set $A$ in $M$. Since $A$ is closed, it is enough to show $m$ is in the closure of $A$; i.e., each basic neighborhood of $m$ intersects $A$. A basic neighborhood of $m$ has the form $\cap_{j=1}^r p_{i_j}^{-1}(U_{i_j})$. But by the property (2) above, we have $\left \{ A, p_{i_j}^{-1}(U_{i_j}) \mid j = 1, \dots, r \right \} \subset M$, which gives the claim by the finite intersection property. $\square$
