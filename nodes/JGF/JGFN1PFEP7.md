---
tag: JGFN1PFEP7
kind: proof
name: Proof of the simplicity of the alternating group by three-cycles
msc: [20B30, 20D06]
proves: 0ARPRJQWZ2
uses: [0T13HM377F, 0W77CVBCHQ, 0KFZ0QX83G, 0YWDAZPRPQ, 07E6D8R4D6, 0V0E04DWX2, 0JEJJCB0EX, 0SK90238BH, 0ZKPH2BD1T, 0RG9SPQSWM]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/grouptheory/Ansimple.pdf
    locator: Section 6 and Lemma 2.2
---

## Proof

We show that a nontrivial normal subgroup contains a $3$-cycle, and then all $3$-cycles. Products in $S_n$ are composites of maps, and the right factor acts first.

1. Let $n \geq 5$ and let $N$ be a [[normal subgroup|0W77CVBCHQ]] of $A_n$ with $N \neq \{e\}$. We must show $N = A_n$.
2. Conjugation formula. Let $\rho \in S_n$ and let $c = (b_1\ \dots\ b_k)$ be a cycle in [[cycle notation|0ZKPH2BD1T]]. For each $i$, $\rho c \rho^{-1}(\rho(b_i)) = \rho(c(b_i))$, which is $\rho(b_{i+1})$, with $b_{k+1} = b_1$.
3. If $y$ is not among the $\rho(b_i)$, then $\rho^{-1}(y)$ is not among the $b_i$, so $c$ fixes it and $\rho c \rho^{-1}(y) = y$. Hence $\rho c \rho^{-1} = (\rho(b_1)\ \dots\ \rho(b_k))$.
4. For a product $c_1 \cdots c_r$, inserting $\rho^{-1} \rho$ between the factors gives $\rho c_1 \cdots c_r \rho^{-1} = (\rho c_1 \rho^{-1}) \cdots (\rho c_r \rho^{-1})$. If $\rho$ fixes every point moved by $c$, step 3 gives $\rho c \rho^{-1} = c$.
5. All $3$-cycles are conjugate in $A_n$. Let $(a\ b\ c)$ and $(a'\ b'\ c')$ be $3$-cycles. Choose $\rho \in S_n$ with $\rho(a) = a'$, $\rho(b) = b'$, $\rho(c) = c'$.
6. Such $\rho$ exists, because the complements of $\{a, b, c\}$ and $\{a', b', c'\}$ both have $n - 3$ elements, and any bijection between them extends the choice. By step 3, $\rho (a\ b\ c) \rho^{-1} = (a'\ b'\ c')$.
7. If $\rho$ is odd, choose distinct points $d, e$ outside $\{a, b, c\}$, which is possible since $n \geq 5$. Put $\rho' = \rho (d\ e)$.
8. By the [[sign homomorphism|0JEJJCB0EX]], $\rho'$ is even, so $\rho' \in A_n$. [[Disjoint cycles commute|07E6D8R4D6]], so $(d\ e)(a\ b\ c)(d\ e)^{-1} = (a\ b\ c)$, and $\rho' (a\ b\ c) \rho'^{-1} = (a'\ b'\ c')$.
9. Hence, if $N$ contains one $3$-cycle, normality gives all $3$-cycles in $N$. Since the [[$3$-cycles generate $A_n$|0KFZ0QX83G]], the [[generated subgroup|0RG9SPQSWM]] lies in $N$, so $N = A_n$.
10. It remains to find a $3$-cycle in $N$. Key fact: for $\sigma \in N$ and $\rho \in A_n$, normality gives $\rho \sigma \rho^{-1} \in N$. So $\pi = (\rho \sigma \rho^{-1}) \sigma^{-1} \in N$.
11. Pick $\sigma \in N$ with $\sigma \neq e$. By the [[disjoint cycle decomposition|0YWDAZPRPQ]], $\sigma$ is a product of disjoint cycles of length at least $2$, and there is at least one cycle.
12. In the cases below, $\sigma = c \tau$. Here $c$ is a product of listed cycles, which move the points of a set $S$, and $\tau$ is the product of the other cycles. Each $\rho$ used moves only points of $S$.
13. Then $\rho \sigma \rho^{-1} = (\rho c \rho^{-1}) \tau$ by step 4, and $\rho c \rho^{-1}$ moves only points of $S$. For $x \notin S$, $\sigma^{-1}(x) = \tau^{-1}(x) \notin S$, so $\pi(x) = \tau(\tau^{-1}(x)) = x$. So we only compute $\pi$ on $S$.
14. Case A: some cycle has length $r \geq 4$, say $\sigma = (a_1\ a_2\ \dots\ a_r) \tau$. Take $\rho = (a_1\ a_2\ a_3)$, which is even by the [[sign of a cycle|0V0E04DWX2]].
15. By step 3, $\rho \sigma \rho^{-1} = (a_2\ a_3\ a_1\ a_4\ \dots\ a_r) \tau$. On $S$, $\sigma^{-1}$ sends $a_1 \mapsto a_r$ and $a_j \mapsto a_{j-1}$ for $j \geq 2$.
16. So $\pi(a_1) = a_2$, $\pi(a_2) = a_4$, $\pi(a_3) = a_3$, $\pi(a_4) = a_1$, and $\pi(a_j) = a_j$ for $j \geq 5$. Thus $\pi = (a_1\ a_2\ a_4)$ is a $3$-cycle in $N$.
17. Case B: no cycle has length $4$ or more, and there are at least two $3$-cycles, say $\sigma = (a_1\ a_2\ a_3)(a_4\ a_5\ a_6) \tau$. Take $\rho = (a_1\ a_2\ a_4) \in A_n$.
18. By step 3, $\rho \sigma \rho^{-1} = (a_2\ a_4\ a_3)(a_1\ a_5\ a_6) \tau$. Computing on $S$ gives $\pi(a_1) = a_2$, $\pi(a_2) = a_5$, $\pi(a_5) = a_3$, $\pi(a_3) = a_4$, $\pi(a_4) = a_1$, $\pi(a_6) = a_6$.
19. So $\pi = (a_1\ a_2\ a_5\ a_3\ a_4)$ lies in $N$. Applying Case A to $\pi$ in place of $\sigma$ gives a $3$-cycle in $N$.
20. Case C: no cycle has length $4$ or more, and there is exactly one $3$-cycle. So $\sigma = (a_1\ a_2\ a_3) \tau$, where $\tau$ is a product of disjoint transpositions, possibly empty.
21. The factors commute, since [[disjoint cycles commute|07E6D8R4D6]], and each transposition squares to $e$. So $\sigma^2 = (a_1\ a_2\ a_3)^2 \tau^2 = (a_1\ a_3\ a_2)$, a $3$-cycle in $N$.
22. Case D: every cycle is a transposition. If there are $m$ of them, the [[definition of the sign|0SK90238BH]] gives $(-1)^m = 1$, because $\sigma \in A_n$ by the [[definition of $A_n$|0T13HM377F]].
23. So $m$ is even, and $m \geq 2$ since $\sigma \neq e$. Write $\sigma = (a_1\ a_2)(a_3\ a_4) \tau$ and take $\rho = (a_1\ a_2\ a_3) \in A_n$.
24. By step 3, $\rho \sigma \rho^{-1} = (a_2\ a_3)(a_1\ a_4) \tau$. Since $\sigma^{-1} = \sigma$, computing on $S$ gives $\pi = (a_1\ a_3)(a_2\ a_4) \in N$.
25. Since $n \geq 5$, choose $a_5 \notin \{a_1, a_2, a_3, a_4\}$ and let $\beta = (a_1\ a_3\ a_5) \in A_n$. By step 3, $\beta \pi \beta^{-1} = (a_3\ a_5)(a_2\ a_4) \in N$.
26. Then $\pi \beta \pi \beta^{-1} = (a_1\ a_3)(a_2\ a_4)(a_3\ a_5)(a_2\ a_4)$ lies in $N$. Swapping the disjoint factors $(a_3\ a_5)$ and $(a_2\ a_4)$ and cancelling $(a_2\ a_4)(a_2\ a_4) = e$ makes it $(a_1\ a_3)(a_3\ a_5)$.
27. Point by point, $(a_1\ a_3)(a_3\ a_5)$ sends $a_1 \mapsto a_3$, $a_3 \mapsto a_5$, $a_5 \mapsto a_1$. So it is the $3$-cycle $(a_1\ a_3\ a_5)$, and it lies in $N$.
28. Cases A to D cover every $\sigma \neq e$. Either some cycle has length at least $4$, or all lengths are $2$ or $3$. In the second case, the number of $3$-cycles is at least two, exactly one, or zero.
29. So $N$ contains a $3$-cycle, and $N = A_n$ by step 9. Hence the only normal subgroups of $A_n$ are $\{e\}$ and $A_n$.

## Idea

For $n \geq 5$ there is room to correct the parity of a conjugating permutation, so all $3$-cycles are conjugate inside $A_n$. A normal subgroup is closed under the commutator-like products $\rho \sigma \rho^{-1} \sigma^{-1}$. A good choice of the $3$-cycle $\rho$ makes this product a $3$-cycle, which then forces the whole group.
