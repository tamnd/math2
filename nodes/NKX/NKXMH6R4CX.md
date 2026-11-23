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

We prove part 1 with the tree of Erdős and Rado, and part 2 with a computable coloring that defeats every set computable from the halting set.
Parts 3 and 4 use one construction of $\omega$-models, which rests on two cited theorems.

### Part 1: the Erdős-Rado tree

We argue in $\mathsf{ACA}_0$ and fix a coloring $c$ of pairs.

1. We place the numbers $1, 2, 3, \ldots$ in a tree with root $0$, one at a time.
   To place $n$, start at the root, and at a node $x$ move to a child $y$ of $x$ with $c(x, y) = c(x, n)$ if there is one; otherwise make $n$ a new child of $x$ and stop.
2. Each move goes to a node $y < n$, so the walk stops after at most $n$ moves.
   So the parent function $n \mapsto p(n)$ is defined by primitive recursion from $c$, and it exists already in $\mathsf{RCA}_0$.
3. Let $T$ be the set of sequences $(x_0, \ldots, x_k)$ with $x_0 = 0$ and $p(x_{i+1}) = x_i$ for all $i < k$.
   It exists by $\Delta^0_1$ comprehension, and it is closed under initial segments.
4. Each number $n$ is the last entry of some sequence in $T$, so $T$ is infinite.
5. A node $x$ has at most two children, because step 1 never adds a second child $y$ with the same color $c(x, y)$.
   So $T$ is finitely branching.
6. By [[König's lemma|3P2J5NWCM1]], which holds in $\mathsf{ACA}_0$, $T$ has a path $g$.
   Write $x_i = g(i)$; children are larger than parents, so $x_0 < x_1 < x_2 < \cdots$.
7. Let $i < j$.
   When $x_j$ was placed, its walk passed through $x_i$ and moved to the child $x_{i+1}$, so $c(x_i, x_j) = c(x_i, x_{i+1})$, which we call $d_i$.
8. The function $i \mapsto d_i$ exists by $\Delta^0_1$ comprehension.
   By the [[infinite pigeonhole principle in RCA0|9EB4DXQMWK]], there is $d \in \{0, 1\}$ with $I = \{i : d_i = d\}$ infinite.
9. Let $H = \{x_i : i \in I\}$.
   Since $g(i) \ge i$, we have $m \in H$ if and only if $\exists i \le m \, (g(i) = m \wedge i \in I)$, so $H$ exists, and it is infinite.
10. For $x_i < x_j$ in $H$, step 7 gives $c(x_i, x_j) = d_i = d$.
    So $H$ is an infinite homogeneous set.

### Part 2: a coloring that defeats the halting set

11. For $e$ and $s$, let $A_{e,s} = \{x < s : \Phi_{e,s}^{\emptyset'_s}(x) \downarrow = 1\}$, where $\emptyset'_s$ is the part of the halting set enumerated by stage $s$.
    These finite sets are computable uniformly in $e$ and $s$.
12. If $\Phi_e^{\emptyset'}$ is the characteristic function of a set $A_e$, then for each $x$ we have $A_{e,s}(x) = A_e(x)$ for all large $s$.
    This is the limit lemma, which we cite.
13. We define $c(x, s)$ for all $x < s$ at stage $s$.
    For $e = 0, 1, \ldots, s - 1$ in turn, if $A_{e,s}$ has at least $2e + 2$ elements, let $u_e < v_e$ be the two least among its first $2e + 2$ elements that no $e' < e$ has chosen, and put $c(u_e, s) = 0$ and $c(v_e, s) = 1$.
14. The indices $e' < e$ choose at most $2e$ elements in total, so two free elements remain.
    Put $c(x, s) = 0$ for every other $x < s$; then $c$ is computable.
15. Let $A_e = \Phi_e^{\emptyset'}$ be infinite, and let $a$ be its $(2e + 2)$-th element.
    By step 12 there is $s_0 > \max(a, e)$ with $A_{e,s} \cap [0, a] = A_e \cap [0, a]$ for all $s \ge s_0$.
16. Take $s \ge s_0$ with $s \in A_e$.
    At stage $s$ the first $2e + 2$ elements of $A_{e,s}$ are those of $A_e$, so $u_e, v_e \in A_e$, with $c(u_e, s) = 0$ and $c(v_e, s) = 1$.
17. So $A_e$ is not homogeneous, and $c$ has no infinite homogeneous set $H \le_T \emptyset'$.

### Part 2, the model

18. Let $(\mathbb{N}, \mathcal{S})$ be the [[ω-model of WKL0 with only low sets|8B045KSKW5]].
    Each $Z \in \mathcal{S}$ is [[low|DKQG0X84D9]], so $Z \le_T Z' \le_T \emptyset'$.
19. The coloring $c$ is computable, so $c \in \mathcal{S}$, and by step 17 no infinite homogeneous set for $c$ is in $\mathcal{S}$.
20. The formula "$H$ is infinite and homogeneous for $c$" is arithmetical, so it means the same in $(\mathbb{N}, \mathcal{S})$ as in the true model.
    So $\mathrm{RT}^2_2$ fails in a model of $\mathsf{WKL}_0$, and by the [[soundness theorem|4A84VHDTHV]] $\mathsf{WKL}_0 \nvdash \mathrm{RT}^2_2$.

### Parts 3 and 4: models that avoid a class

Let $\mathcal{B}$ be a class of sets that is closed upward under $\le_T$, with $\emptyset \notin \mathcal{B}$.
We say that $\mathrm{RT}^2_2$ *avoids* $\mathcal{B}$ if for every $X \notin \mathcal{B}$ and every coloring $c \le_T X$ there is an infinite homogeneous $H$ with $X \oplus H \notin \mathcal{B}$.

21. Suppose that $\mathrm{RT}^2_2$ avoids $\mathcal{B}$, and put $X_0 = \emptyset$.
    For $n = \langle e, m \rangle$, where $m \le n$, if $\Phi_e^{X_m}$ is a coloring of pairs, choose $H$ by avoidance for $X_n$ and this coloring and put $X_{n+1} = X_n \oplus H$; otherwise put $X_{n+1} = X_n$.
22. By induction on $n$, no $X_n$ is in $\mathcal{B}$.
    Let $\mathcal{S} = \{Z : Z \le_T X_n \text{ for some } n\}$; it is a Turing ideal, so $(\mathbb{N}, \mathcal{S})$ is a model of $\mathsf{RCA}_0$ by the [[characterization of ω-models|Y6D27XJT3H]], and no member of $\mathcal{S}$ is in $\mathcal{B}$ because $\mathcal{B}$ is closed upward.
23. A coloring in $\mathcal{S}$ is $\Phi_e^{X_m}$ for some $e$ and $m$, and at stage $\langle e, m \rangle$ an infinite homogeneous set for it entered $\mathcal{S}$.
    As in step 20, $(\mathbb{N}, \mathcal{S})$ is a model of $\mathsf{RCA}_0 + \mathrm{RT}^2_2$.

### Part 3: avoiding the halting set

24. Let $\mathcal{B} = \{Z : \emptyset' \le_T Z\}$.
    Seetapun's cone avoidance theorem, which we cite, says: if $C \not\le_T X$ and $c \le_T X$ is a coloring of pairs, then some infinite homogeneous $H$ has $C \not\le_T X \oplus H$.
    With $C = \emptyset'$ this says that $\mathrm{RT}^2_2$ avoids $\mathcal{B}$.
25. Steps 21 to 23 give an $\omega$-model of $\mathsf{RCA}_0 + \mathrm{RT}^2_2$ that does not contain the [[jump|60P2XWY5QX]] $\emptyset'$.
26. Every $\omega$-model of $\mathsf{ACA}_0$ contains $\emptyset'$, by arithmetical comprehension for the $\Sigma^0_1$ formula "program $e$ halts on input $e$".
    So the model is not a model of $\mathsf{ACA}_0$, and by soundness $\mathsf{RCA}_0 + \mathrm{RT}^2_2 \nvdash \mathsf{ACA}_0$.

### Part 4: avoiding separating sets

27. Let $A = \{e : \varphi_e(e) = 0\}$ and $B = \{e : \varphi_e(e) = 1\}$, and let $\mathcal{B}$ be the class of sets that compute a set $C$ with $A \subseteq C$ and $C \cap B = \emptyset$.
    It is closed upward, and $\emptyset \notin \mathcal{B}$ because no computable set separates $A$ from $B$, as the [[computable sets example|F5T3F7E0H1]] shows.
28. A set lies in $\mathcal{B}$ if and only if it has PA degree, and Liu's theorem says that $\mathrm{RT}^2_2$ avoids the class of sets of PA degree.
    We cite both facts, and together they say that $\mathrm{RT}^2_2$ avoids $\mathcal{B}$.
29. Steps 21 to 23 give an $\omega$-model of $\mathsf{RCA}_0 + \mathrm{RT}^2_2$ with no member in $\mathcal{B}$.
30. The Kleene tree of the same example is computable, so it lies in every $\omega$-model of $\mathsf{RCA}_0$, and each of its paths gives a set that separates $A$ from $B$.
    So every $\omega$-model of $\mathsf{WKL}_0$ has a member in $\mathcal{B}$.
31. So the model of step 29 is not a model of $\mathsf{WKL}_0$, and by soundness $\mathsf{RCA}_0 + \mathrm{RT}^2_2 \nvdash \mathsf{WKL}_0$.

## Idea

The positive part is a greedy construction.
Each new number walks down a tree, following its colors with the earlier numbers, so that along any branch the color of a pair depends only on the smaller element.
A branch exists by König's lemma, and then the one-dimensional pigeonhole principle finishes the proof.
The negative parts each build an $\omega$-model.
For part 2, a single computable coloring kills every candidate homogeneous set that the halting set computes, and a model of $\mathsf{WKL}_0$ with only low sets has no other candidates.
For parts 3 and 4, homogeneous sets are added one at a time, and each new set is chosen to stay away from a fixed kind of information: the halting set, or a separating set for $A$ and $B$.

## Variants

Jockusch's construction gives more than part 2 needs: a computable coloring of pairs with no infinite $\Sigma^0_2$ homogeneous set.
He also showed that every computable coloring of pairs has an infinite $\Pi^0_2$ homogeneous set, so the bound is sharp.
Cholak, Jockusch and Slaman gave a second route to part 3.
They showed that every computable coloring of pairs has an infinite homogeneous set $H$ with $H'' \le_T \emptyset''$, that is, a low$_2$ set.
Iterated, this gives an $\omega$-model of $\mathsf{RCA}_0 + \mathrm{RT}^2_2$ whose sets are all low$_2$, and $\emptyset'$ is not low$_2$, so the model omits it.
