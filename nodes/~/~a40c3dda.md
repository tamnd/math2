---
tag: ~a40c3dda
kind: proof
name: Proof of the Jankov-de Jongh theorem by quotients and p-morphisms
msc: ["03B55", "06D20"]
topics: [38EQ20GR7M]
audience: research
proves: ~6e548f0e
uses: [~be90dd8c, BND6A96S3D, TYYS649FAJ, ~11b532e9, ~32a20f35, AJNZJD8442]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - arxiv: 1407.5823v1
    locator: Section 1.3, Proposition 1.6
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 5.3, Theorem 95
---

## Proof

Let $s = s_A$ and $\delta = \delta(A)$, as in [[the definition|~be90dd8c]].
For elements $x, y$ of a Heyting algebra, write $x \leftrightarrow y = (x \to y) \wedge (y \to x)$.
Then $x \leftrightarrow y = 1$ iff $x = y$.

*Part 1, the direction from right to left.*

1. Assume $A \in \mathbf{SH}(B)$. Then there are a surjective homomorphism $g \colon B \to C$ and an injective homomorphism $e \colon A \to C$.
2. Define a valuation $u$ in $C$ by $u(p_a) = e(a)$.
3. Each conjunct of $\delta$ gets value $1$ under $u$. For example $u(p_{a \wedge b}) = e(a \wedge b) = e(a) \wedge e(b) = u(p_a \wedge p_b)$, and the same holds for $\vee$, $\to$ and $\neg$. So $u(\delta) = 1$.
4. Since $s \neq 1$ and $e$ is injective, $u(p_s) = e(s) \neq e(1) = 1$. So $u(\chi(A)) = 1 \to e(s) = e(s) \neq 1$.
5. For each variable $p$ choose $b_p \in B$ with $g(b_p) = u(p)$, and let $v(p) = b_p$. Since $g$ is a homomorphism, $g(v(\varphi)) = u(\varphi)$ for every formula $\varphi$, by induction on $\varphi$.
6. If $v(\chi(A)) = 1$, then $u(\chi(A)) = g(1) = 1$, contradicting step 4. So $\chi(A)$ is not valid in $B$.

*Part 1, the direction from left to right.*

7. Assume $v$ is a valuation in $B$ with $v(\chi(A)) \neq 1$. Let $d = v(\delta)$. Then $d \to v(p_s) \neq 1$, that is $d \not\leq v(p_s)$.
8. Let $\mathord{\downarrow} d = \set{x \in B : x \leq d}$, with the order of $B$, bottom $0$, top $d$ and $x \to_d y = (x \to y) \wedge d$. For $x, y, z \leq d$ we have $z \leq (x \to y) \wedge d$ iff $z \wedge x \leq y$. So $\mathord{\downarrow} d$ is a [[Heyting algebra|BND6A96S3D]].
9. Let $\pi(x) = x \wedge d$. By distributivity $\pi$ preserves $\wedge$ and $\vee$, and $\pi(0) = 0$, $\pi(1) = d$, and $\pi$ is onto.
10. $\pi$ preserves $\to$. For $z \leq d$ we have $z \leq ((x \wedge d) \to (y \wedge d)) \wedge d$ iff $z \wedge x \leq y \wedge d$ iff $z \wedge x \leq y$ iff $z \leq (x \to y) \wedge d$. So $\pi(x) \to_d \pi(y) = \pi(x \to y)$.
11. If $d \leq x \leftrightarrow y$, then $\pi(x) = \pi(y)$. Indeed $d \leq x \to y$ gives $d \wedge x \leq y$, so $d \wedge x \leq d \wedge y$, and symmetrically.
12. Define $e \colon A \to \mathord{\downarrow} d$ by $e(a) = \pi(v(p_a))$.
13. Since $d \leq v(p_{a \wedge b} \leftrightarrow p_a \wedge p_b)$, step 11 gives $e(a \wedge b) = \pi(v(p_a) \wedge v(p_b)) = e(a) \wedge e(b)$, using step 9.
14. In the same way, steps 9 to 11 give $e(a \vee b) = e(a) \vee e(b)$, $e(a \to b) = e(a) \to_d e(b)$ and $e(\neg a) = e(a) \to_d 0$.
15. Then $e(1) = e(a \to a) = d$ for any $a$, and $e(0) = e(\neg 1) = d \to_d 0 = 0$. So $e$ is a homomorphism of Heyting algebras.
16. Suppose $e(a) = e(b)$ with $a \neq b$. Let $c = a \leftrightarrow b$ in $A$. Then $c \neq 1$ and $e(c) = e(a) \leftrightarrow_d e(b) = d$.
17. Every element of the finite algebra $A$ other than $1$ lies below a coatom, and $s$ is the only coatom. So $c \leq s$, and $d = e(c) \leq e(s) \leq d$.
18. But $e(s) = v(p_s) \wedge d$, and $v(p_s) \wedge d = d$ would mean $d \leq v(p_s)$, against step 7. So $e$ is injective.
19. Hence $A$ is isomorphic to the subalgebra $e[A]$ of $\mathord{\downarrow} d$, a homomorphic image of $B$. So $A \in \mathbf{SH}(B)$.

*Part 2, the direction from right to left.* Let $r$ be the root of $F$, so $s = F \setminus \set{r}$ in $\mathrm{Up}(F)$.

20. Let $H$ be a generated subframe of $G$ and $f \colon H \to F$ a surjective p-morphism.
21. For each up-set $U$ of $F$, put $V(p_U) = f^{-1}[U]$. It is an up-set of $H$ because $f$ is monotone, and of $G$ because $H$ is an up-set.
22. The map $U \mapsto f^{-1}[U]$ preserves $\cap$, $\cup$ and $\emptyset$. It also preserves $\Rightarrow$, the implication of up-sets, in two halves.
    - If $y \notin f^{-1}[U] \Rightarrow f^{-1}[W]$, some $y' \geq y$ has $f(y') \in U \setminus W$. Since $f(y') \geq f(y)$, we get $f(y) \notin U \Rightarrow W$.
    - If $f(y) \notin U \Rightarrow W$, some $x \geq f(y)$ lies in $U \setminus W$. The p-morphism condition gives $y' \geq y$ with $f(y') = x$, so $y \notin f^{-1}[U] \Rightarrow f^{-1}[W]$.
23. Truth at worlds of $H$ depends only on worlds of $H$, by the [[Kripke clauses|~11b532e9]]. So by step 22 every conjunct of $\delta$ is true at every world of $H$.
24. Since $f$ is onto, some $w \in H$ has $f(w) = r$. Then $w \notin f^{-1}[s] = V(p_s)$, and $w \Vdash \delta$. So $w \nVdash \chi(F)$.

*Part 2, the direction from left to right.*

25. Assume $V$ is a valuation on $G$ and $w$ a world with $w \Vdash \delta$ and $w \nVdash p_s$. Let $H = \mathord{\uparrow} w$, a generated subframe.
26. By persistence $\delta$ is true at every world of $H$. Let $h(U) = V(p_U) \cap H$ for each up-set $U$ of $F$.
27. As in step 23, the conjuncts of $\delta$ give $h(U \cap W) = h(U) \cap h(W)$, $h(U \cup W) = h(U) \cup h(W)$ and $h(U \Rightarrow W) = h(U) \Rightarrow_H h(W)$. Also $h(F) = h(U \Rightarrow U) = H$, and $h(\emptyset) = h(F \Rightarrow \emptyset) = \emptyset$ by the conjunct for $\neg$.
28. For $y \in H$ let $U_y = \bigcap \set{U : y \in h(U)}$, a finite intersection of up-sets of $F$. By step 27, $y \in h(U_y)$, so $U_y \neq \emptyset$.
29. Let $x_1, \dots, x_k$ be the minimal elements of $U_y$. Then $U_y = \mathord{\uparrow} x_1 \cup \dots \cup \mathord{\uparrow} x_k$, so $y \in h(\mathord{\uparrow} x_i)$ for some $i$. Then $U_y \subseteq \mathord{\uparrow} x_i \subseteq U_y$.
30. Define $f(y) = x_i$, the least element of $U_y$. For every up-set $U$, $y \in h(U)$ iff $U_y \subseteq U$ iff $f(y) \in U$. So $h(U) = f^{-1}[U]$.
31. $f$ is monotone: if $y \leq y'$, then $y' \in h(U)$ whenever $y \in h(U)$, so $U_{y'} \subseteq U_y$ and $f(y') \geq f(y)$.
32. Let $f(y) \leq x$. Put $U = \mathord{\uparrow} x$ and $W = \mathord{\uparrow} x \setminus \set{x}$, both up-sets. A world $z$ lies in $U \Rightarrow W$ iff $x \notin \mathord{\uparrow} z$, so $U \Rightarrow W = F \setminus \mathord{\downarrow} x$.
33. Since $f(y) \in \mathord{\downarrow} x$, step 30 gives $y \notin h(U \Rightarrow W) = h(U) \Rightarrow_H h(W)$. So some $y' \geq y$ has $f(y') \in U \setminus W = \set{x}$. Thus $f$ is a p-morphism.
34. Since $w \notin h(s)$, $f(w) \notin F \setminus \set{r}$, so $f(w) = r$. By step 33 every $x \geq r$ is $f(y')$ for some $y' \geq w$. So $f \colon H \to F$ is onto, and $F \leq G$.

*Part 3.*

35. Let $L$ be a superintuitionistic logic with $\chi(A) \notin L$.
36. By item 4 of [[Heyting algebra semantics|~32a20f35]], $\mathrm{Log}(\mathbf{V}(L)) = L$. So some $B \in \mathbf{V}(L)$ does not validate $\chi(A)$.
37. By part 1, $A \in \mathbf{SH}(B)$. Since $\mathbf{V}(L)$ is a [[variety|AJNZJD8442]], it is closed under $\mathbf{S}$ and $\mathbf{H}$, so $A \in \mathbf{V}(L)$ and $L \subseteq \mathrm{Log}(A)$.
38. Both cannot hold: by part 1 with $B = A$, $\chi(A) \notin \mathrm{Log}(A)$. So $\chi(A) \in L$ excludes $L \subseteq \mathrm{Log}(A)$. $\blacksquare$

## Idea

A refutation of $\delta \to p_s$ makes $\delta$ hold at a value $d$ where $p_s$ fails.
Cutting $B$ down to $\mathord{\downarrow} d$ turns $\delta$ into "the map $a \mapsto p_a$ is a homomorphism".
The unique coatom then forces this homomorphism to be injective.
On frames, the same cut is the passage to the generated subframe $\mathord{\uparrow} w$, and the homomorphism is read off as a p-morphism.

## Variants

Bezhanishvili and de Jongh prove part 2 for frames with de Jongh formulas and the $n$-universal model, using that $\leq$ can be computed in either order of the two operations.
Citkin's version replaces finiteness by finite presentability and uses that every congruence is given by a filter.
For finite $G$ one can also derive part 2 from part 1 by the duality between finite frames and finite Heyting algebras; the direct argument above also covers infinite $G$.
