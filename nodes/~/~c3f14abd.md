---
tag: ~c3f14abd
kind: proof
name: Proof of the Kechris-Pestov-Todorcevic correspondence
msc: ["03C15", "05D10", "22F50"]
topics: [ZS8X8KS54R]
audience: research
proves: ~d7362f14
uses: [HJVRBDQSGG, ~7468669e, ~8398d787, 0QPHW703PV, 0S1FJ8VEX9, 01EY3VR7ZD, 0X3WGX95FE, FVGB8ZP67B]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_Ramsey_theory
    locator: The Kechris–Pestov–Todorčević correspondence
---

## Proof

A *copy* of $A$ is a substructure of $F$ isomorphic to $A$.
For finite $A \subseteq F$, $G_A$ is the pointwise stabilizer; these subgroups form a base at the identity.

### Step A: cosets and copies

1. Every $A \in \mathcal{K}$ is rigid, since a linear order has no nontrivial automorphism.
2. Map $g G_A \mapsto g(A)$. It is well defined, and onto the copies of $A$ by [[ultrahomogeneity|~7468669e]].
3. If $g(A) = h(A)$, then $h^{-1} g$ restricts to an automorphism of $A$, which is the identity. So $g G_A = h G_A$.

### Step B: finite and infinite Ramsey

4. Claim: $\mathcal{K}$ is Ramsey if and only if the following holds. For all $A \le B$ in $\mathcal{K}$ and all $k$, every $k$-coloring of copies of $A$ in $F$ is constant on the copies inside some copy of $B$.
5. If $\mathcal{K}$ is Ramsey, embed the witness $C$ into $F$ and restrict the coloring.
6. Conversely, write $F = \bigcup_n C_n$ with $C_n$ finite and increasing. If $\mathcal{K}$ is not Ramsey, no $C_n$ is a witness.
7. So the bad colorings of the $C_n$ form an infinite finitely branching tree under restriction.
8. König's lemma gives a branch, a bad coloring of all of $F$, a contradiction.

### Step C: Ramsey implies a fixed point

9. Let $G$ act continuously on a compact Hausdorff $X$, and fix $x_0 \in X$.
10. For finite $S \subseteq G$, [[continuous|0X3WGX95FE]] $f_1, \dots, f_m \colon X \to \R$ and $\varepsilon > 0$, let $C(S, \bar f, \varepsilon)$ be the set of $x$ with $\lvert f_i(sx) - f_i(x) \rvert \le \varepsilon$ for all $s, i$.
11. These sets are closed, and a finite intersection of them contains another one of them.
12. If each is nonempty, [[compactness|0QPHW703PV]] gives $x^*$ in all of them, so $f(s x^*) = f(x^*)$ for all $s \in G$ and continuous $f$.
13. Continuous functions separate points of $X$, by [[Urysohn's lemma|01EY3VR7ZD]], so $x^*$ is a fixed point.

### Step C, continued: nonemptiness

14. Let $u_i(g) = f_i(g x_0)$. By compactness of $X$, some $G_A$ satisfies $\lvert u_i(vg) - u_i(g) \rvert < \varepsilon/3$ for $v \in G_A$, all $g$.
15. Pick $r_{A'}$ with $r_{A'}(A) = A'$ for each copy $A'$. Color $A'$ by the cube of side $\varepsilon/3$ containing $(u_i(r_{A'}^{-1}))_i$.
16. The $f_i$ are bounded, so there are finitely many colors.
17. Let $B \supseteq A \cup \bigcup_{s \in S} s^{-1}(A)$ be finite. Step B gives a copy of $B$ on which the coloring is constant.
18. By ultrahomogeneity this copy is $g(B)$ for some $g \in G$.
19. Then $g(A)$ and $g s^{-1}(A)$ have the same color. Step 14 moves each representative within $\varepsilon/3$ of $g^{-1}$ and $s g^{-1}$.
20. So $x = g^{-1} x_0$ satisfies $\lvert f_i(sx) - f_i(x) \rvert \le \varepsilon$, and $C(S, \bar f, \varepsilon) \ne \emptyset$.

### Step D: a fixed point implies Ramsey

21. Suppose $\mathcal{K}$ is not Ramsey. Step B gives a coloring $c_0$ of copies of $A$ in $F$ with no monochromatic copy of $B$.
22. $G$ acts on the compact space $\set{1, \dots, k}^{\text{copies of } A}$ by $(g c)(A') = c(g^{-1} A')$. Let $Y$ be the orbit closure of $c_0$.
23. A fixed point $c \in Y$ is constant, since $G$ is transitive on copies of $A$.
24. $c$ agrees with some $g c_0$ on the finitely many copies inside $B$. So $c_0$ is constant on copies inside $g^{-1}(B)$, a [[contradiction|0J0XBKG64S]].

## Idea

Copies of $A$ are cosets of $G_A$, so colorings of copies are functions on $G / G_A$.
The Ramsey property makes such functions almost constant on translates of a finite set, which is what a fixed point needs.

## Variants

The same argument, with "copies" replaced by embeddings, proves the version for classes of rigid structures without a named order.
