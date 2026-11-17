---
tag: NKXMH6R4CX
kind: proof
name: Proof of the reverse mathematics of Ramsey's theorem for pairs
msc: ["03B30", "05D10", "03D80"]
topics: [BY8AAFN7C5]
audience: grad
proves: ZT5KV6KJ3E
uses: [3P2J5NWCM1, 9EB4DXQMWK, 8B045KSKW5, F5T3F7E0H1, Y6D27XJT3H, DKQG0X84D9, 60P2XWY5QX, 4A84VHDTHV]
methods: [0NTF6DMVAP, V2H30SA654, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Ramsey%27s_theorem
    locator: Reverse mathematics
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
---

## Proof

Part 1: $\mathsf{ACA}_0$ proves $\mathrm{RT}^2_2$.
The proof uses the tree of Erdős and Rado.

1. Let $c$ be a coloring of pairs. Place the numbers $1, 2, 3, \ldots$ in a tree with root $0$, one at a time. To place $n$, start at the root. At a node $x$, if $x$ has a child $y$ with $c(x, y) = c(x, n)$, move to $y$. Otherwise, make $n$ a new child of $x$ and stop.
2. Each step moves to a node $y < n$, so the walk stops after at most $n$ steps. So the parent function $n \mapsto p(n)$ is defined by course-of-values recursion from $c$, and it exists in $\mathsf{RCA}_0$.
3. Let $T$ be the set of sequences $(x_0, x_1, \ldots, x_k)$ with $x_0 = 0$ and $p(x_{i+1}) = x_i$ for all $i < k$. $T$ exists by $\Delta^0_1$ comprehension, and it is closed under initial segments.
4. Each number $n$ is the last entry of some sequence in $T$, so $T$ is infinite.
5. A node $x$ has at most two children, one with $c(x, y) = 0$ and one with $c(x, y) = 1$, because step 1 never adds a second child of the same color. So $T$ is finitely branching.
6. By [[König's lemma|3P2J5NWCM1]], which holds in $\mathsf{ACA}_0$, $T$ has a path $g$. Write $x_i = g(i)$. Children are larger than parents, so $x_0 < x_1 < x_2 < \cdots$.
7. Let $i < j$. When $x_j$ was placed, its walk passed through $x_i$ and moved to the child $x_{i+1}$. So $c(x_i, x_j) = c(x_i, x_{i+1})$. Call this color $d_i$.
8. The function $i \mapsto d_i$ exists by $\Delta^0_1$ comprehension. By the [[infinite pigeonhole principle in RCA0|9EB4DXQMWK]], there are $d \in \set{0, 1}$ and an infinite set $I = \set{i : d_i = d}$.
9. Let $H = \set{x_i : i \in I}$. Since $g$ is increasing, $m \in H$ if and only if $\exists i \le m\, (g(i) = m \wedge i \in I)$, so $H$ exists and it is infinite.
10. For $x_i < x_j$ in $H$, step 7 gives $c(x_i, x_j) = d_i = d$. So $H$ is homogeneous.

Part 2: $\mathsf{WKL}_0$ does not prove $\mathrm{RT}^2_2$.

11. For each $e$ and $s$, let $A_{e,s} = \set{x < s : \Phi_{e,s}^{\emptyset'_s}(x) \downarrow = 1}$, where $\emptyset'_s$ is the part of the halting set enumerated by stage $s$. The sets $A_{e,s}$ are computable uniformly in $e$ and $s$.
12. If $\Phi_e^{\emptyset'}$ is the characteristic function of a set $A_e$, then for each $x$, $A_{e,s}(x) = A_e(x)$ for all large $s$, by the use principle. This is the limit lemma, and it is cited without proof.
13. Define $c(x, s)$ for $x < s$ at stage $s$. For $e = 0, 1, \ldots, s - 1$ in turn, look at the first $2e + 2$ elements of $A_{e,s}$. If there are at least $2e + 2$, choose the two least of them that no $e' < e$ has chosen at stage $s$. Call them $u_e < v_e$, and put $c(u_e, s) = 0$ and $c(v_e, s) = 1$.
14. The indices $e' < e$ choose at most $2e$ elements in total, so two free elements always remain. The chosen elements are distinct, so step 13 is consistent. Put $c(x, s) = 0$ for every other $x < s$. Then $c$ is computable.
15. Let $A_e$ be an infinite set with $A_e = \Phi_e^{\emptyset'}$. Let $a$ be its $(2e + 2)$-th element. By step 12, there is $s_0 > \max(a, e)$ with $A_{e,s} \cap [0, a] = A_e \cap [0, a]$ for $s \ge s_0$.
16. Take $s \ge s_0$ with $s \in A_e$. At stage $s$, the first $2e + 2$ elements of $A_{e,s}$ are those of $A_e$, so $u_e, v_e \in A_e$, with $c(u_e, s) = 0$ and $c(v_e, s) = 1$.
17. So the pairs $\set{u_e, s}$ and $\set{v_e, s}$ in $[A_e]^2$ have different colors, and $A_e$ is not homogeneous. Thus $c$ has no infinite homogeneous set $H \le_T \emptyset'$.
18. Let $(\N, \mathcal{S})$ be the [[ω-model of WKL0 with only low sets|8B045KSKW5]]. Each $Z \in \mathcal{S}$ is [[low|DKQG0X84D9]], so $Z \le_T Z' \le_T \emptyset'$.
19. The coloring $c$ is computable, so $c \in \mathcal{S}$. By step 17, no infinite homogeneous set for $c$ is in $\mathcal{S}$.
20. The formula "$H$ is infinite and homogeneous for $c$" is arithmetical, so its meaning in $(\N, \mathcal{S})$ is the true one. So $\mathrm{RT}^2_2$ fails in a model of $\mathsf{WKL}_0$, and by the [[soundness theorem|4A84VHDTHV]] $\mathsf{WKL}_0 \nvdash \mathrm{RT}^2_2$.

Parts 3 and 4 use one construction of $\omega$-models.
Let $\mathcal{B}$ be a class of sets closed upward under $\le_T$, with $\emptyset \notin \mathcal{B}$.
Say that $\mathrm{RT}^2_2$ *avoids* $\mathcal{B}$ if: for every $X \notin \mathcal{B}$ and every coloring $c \le_T X$, there is an infinite homogeneous $H$ with $X \oplus H \notin \mathcal{B}$.

21. Suppose that $\mathrm{RT}^2_2$ avoids $\mathcal{B}$. Let $X_0 = \emptyset$. For $n = \langle e, m \rangle$, with $m \le n$: if $\Phi_e^{X_m}$ is a coloring of pairs, choose $H$ by avoidance for $X_n$ and this coloring, and put $X_{n+1} = X_n \oplus H$. Otherwise put $X_{n+1} = X_n$.
22. By induction, no $X_n$ is in $\mathcal{B}$. Let $\mathcal{S} = \set{Z : Z \le_T X_n \text{ for some } n}$. It is a Turing ideal, so $(\N, \mathcal{S})$ is a model of $\mathsf{RCA}_0$ by the [[characterization of ω-models|Y6D27XJT3H]]. No set of $\mathcal{S}$ is in $\mathcal{B}$, since $\mathcal{B}$ is closed upward.
23. A coloring in $\mathcal{S}$ is $\Phi_e^{X_m}$ for some $e$ and $m$. At stage $n = \langle e, m \rangle$ an infinite homogeneous set entered $\mathcal{S}$. As in step 20, $(\N, \mathcal{S})$ is a model of $\mathsf{RCA}_0 + \mathrm{RT}^2_2$.

Part 3: $\mathsf{RCA}_0 + \mathrm{RT}^2_2 \nvdash \mathsf{ACA}_0$.

24. Let $\mathcal{B} = \set{Z : \emptyset' \le_T Z}$. Seetapun's cone avoidance theorem says that $\mathrm{RT}^2_2$ avoids the cone above every noncomputable set, so it avoids $\mathcal{B}$. This theorem is cited without proof.
25. Steps 21 to 23 give an $\omega$-model of $\mathsf{RCA}_0 + \mathrm{RT}^2_2$ that does not contain the [[jump|60P2XWY5QX]] $\emptyset'$ of $\emptyset$.
26. Every $\omega$-model of $\mathsf{ACA}_0$ contains $\emptyset'$, by arithmetical comprehension for the $\Sigma^0_1$ formula "program $e$ halts on input $e$". So the model is not a model of $\mathsf{ACA}_0$.

Part 4: $\mathsf{RCA}_0 + \mathrm{RT}^2_2 \nvdash \mathsf{WKL}_0$.

27. Let $A$ and $B$ be the disjoint computably enumerable sets of the [[computable sets example|F5T3F7E0H1]], and let $\mathcal{B}$ be the class of sets that compute a set $C$ with $A \subseteq C$ and $C \cap B = \emptyset$. It is closed upward, and $\emptyset \notin \mathcal{B}$ by step 5 of that example.
28. Liu's theorem says that $\mathrm{RT}^2_2$ avoids the class of sets of PA degree. A set is of PA degree if and only if it computes a set that separates $A$ from $B$, so $\mathrm{RT}^2_2$ avoids $\mathcal{B}$. Both facts are cited without proof.
29. Steps 21 to 23 give an $\omega$-model of $\mathsf{RCA}_0 + \mathrm{RT}^2_2$ with no set in $\mathcal{B}$.
30. The Kleene tree $T$ of that example is computable, so it is in every $\omega$-model of $\mathsf{RCA}_0$. In a model of $\mathsf{WKL}_0$ it has a path $P$, and $\set{e : P(e) = 1}$ separates $A$ from $B$ by steps 9 and 10 of that example. So every $\omega$-model of $\mathsf{WKL}_0$ has a set in $\mathcal{B}$.
31. So the model of step 29 is not a model of $\mathsf{WKL}_0$. By soundness, $\mathsf{RCA}_0 + \mathrm{RT}^2_2 \nvdash \mathsf{WKL}_0$.

## Idea

The positive part uses a greedy construction: each number goes down a binary tree, along its colors with earlier numbers.
A path through this tree is a sequence on which the color of a pair depends only on its smaller element.
The negative parts each build an $\omega$-model.
For part 2, a computable coloring kills every homogeneous set that is computable from the halting set, while a model of $\mathsf{WKL}_0$ can have only such sets.
For parts 3 and 4, homogeneous sets are added one at a time, and each new set avoids a fixed kind of information: the halting set, or a separating set for $A$ and $B$.

## Variants

Jockusch's construction gives more: a computable coloring of pairs with no infinite $\Sigma^0_2$ homogeneous set.
Jockusch also showed that every computable coloring of pairs has an infinite $\Pi^0_2$ homogeneous set.
