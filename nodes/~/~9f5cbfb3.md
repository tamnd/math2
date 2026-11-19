---
tag: ~9f5cbfb3
kind: proof
name: Proof of the Rieger-Nishimura theorem by the universal ladder
msc: ["03B55", "06D20"]
topics: [38EQ20GR7M]
audience: research
proves: ~791fc2d0
uses: [~11b532e9, ~ac029000]
methods: [0NTF6DMVAP, 0ASJVEFA9J, 12MQ2NJ29A, 0WCP0PVET6]
sources:
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 6.1 Subintuitionistic and Intermediate Logics
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Section 3.6, Definition 37 and Theorem 38
---

## Proof

*The ladder and its up-sets.*

1. Let $L$ be the [[Kripke model|~11b532e9]] with worlds $\mathbb{N}$, where $n \leq m$ means $m = n$ or $m \leq n - 2$, and $p$ true at $0$ only.
2. $\leq$ is reflexive. It is antisymmetric, since $m \leq n - 2$ and $n \leq m - 2$ cannot both hold. It is transitive, since $m \leq n - 2$ and $l \leq m - 2$ give $l \leq n - 2$. The set $\set{0}$ is an up-set, because $\mathord{\uparrow} 0 = \set{0}$.
3. For $n \geq 1$, $\mathord{\uparrow} n = \set{n} \cup I_{n-1}$; in particular $\mathord{\uparrow} 1 = \set{1}$. So $\mathord{\uparrow}(k + 1) = J_k$ for every $k \geq 0$.
4. Let $U$ be an up-set other than $\mathbb{N}$, and let $k$ be the least number not in $U$. Then $I_k \subseteq U$. If $m \in U$ and $m \geq k + 2$, then $k \leq m - 2$, so $k \in U$, which is false. So $U = I_k$ or $U = J_k$.
5. So the up-sets of $L$ are $I_k$, $J_k$ for $k \geq 0$, and $\mathbb{N}$. Write $T(\varphi)$ for the truth set of $\varphi$ in $L$; it is an up-set by persistence.

*Truth sets of the formulas.*

6. $T(F_0) = \emptyset = I_0$ and $T(F_\infty) = \mathbb{N}$. $T(F_1) = \set{0} = I_1$.
7. A world $n$ sees $0$ iff $n = 0$ or $n \geq 2$. So $T(F_2) = T(\neg p) = \set{1} = J_0$.
8. For $k \geq 0$: $I_{k+1} \cup J_k = I_{k+2}$, since $I_{k+1} = I_k \cup \set{k}$.
9. For $k \geq 0$: $I_{k+2} \Rightarrow I_{k+1} = J_{k+1}$, where $\Rightarrow$ is the implication of up-sets. A world $n$ lies in it iff no world above $n$ lies in $I_{k+2} \setminus I_{k+1} = \set{k + 1}$. By step 1, $n$ sees $k + 1$ iff $n = k + 1$ or $n \geq k + 3$. So the set is $I_{k+1} \cup \set{k + 2} = J_{k+1}$.
10. By induction on $n$, steps 6 to 9 give $T(F_{2n+1}) = I_{n+1}$ and $T(F_{2n+2}) = J_n$, that is $T(F_m) = t(F_m)$ for all $m$.
11. By step 5, every up-set of $L$ is $T(F_m)$ for exactly one $m$, since the sets $t(F_m)$ are pairwise distinct.

*Universality of the ladder.*

12. Let $M$ be a finite model and consider only the variable $p$. We define $f$ from the worlds of $M$ to $\mathbb{N}$, starting from the maximal worlds and going down. Assume $f$ is defined on all proper successors of $x$, with $f[\mathord{\uparrow} y] = \mathord{\uparrow} f(y)$ for each of them.
13. If $x \Vdash p$, put $f(x) = 0$. Every $y \geq x$ also has $f(y) = 0$, so $f[\mathord{\uparrow} x] = \set{0} = \mathord{\uparrow} 0$.
14. If $x \nVdash p$, let $U = \bigcup_{y > x} \mathord{\uparrow} f(y)$, a finite up-set, so $U \neq \mathbb{N}$. Let $k$ be the least number not in $U$, and put $f(x) = k + 1$.
15. By step 4, $I_k \subseteq U \subseteq J_k$. By step 3, $\mathord{\uparrow} f(x) = J_k = \set{k + 1} \cup I_k$. So $f[\mathord{\uparrow} x] = \set{k + 1} \cup U = \mathord{\uparrow} f(x)$. Also $p$ is false at $k + 1 \geq 1$.
16. So $f$ preserves $p$, is monotone, and satisfies the back condition: if $f(x) \leq m$, then $m = f(y)$ for some $y \geq x$.
17. Claim: $x \Vdash \varphi$ iff $f(x) \Vdash \varphi$ for every one-variable $\varphi$. Induction on $\varphi$: atoms by step 16, and $\bot$, $\wedge$, $\vee$ directly.
18. For $\varphi \to \psi$: if $x \nVdash \varphi \to \psi$, some $y \geq x$ forces $\varphi$ but not $\psi$, and then $f(y) \geq f(x)$ does too. If $f(x) \nVdash \varphi \to \psi$, some $m \geq f(x)$ forces $\varphi$ but not $\psi$. By step 16, $m = f(y)$ with $y \geq x$, and $y$ forces $\varphi$ but not $\psi$.

*Conclusion.*

19. Let $\varphi$ and $\psi$ be one-variable formulas with $T(\varphi) \subseteq T(\psi)$. In every finite model, step 17 gives $x \Vdash \varphi \to \psi$ at every world $x$.
20. By the finite model property in [[Kripke completeness|~ac029000]], $\mathsf{IPC} \vdash \varphi \to \psi$. Other variables of a countermodel play no role, since $\varphi \to \psi$ contains only $p$.
21. Conversely, if $\mathsf{IPC} \vdash \varphi \to \psi$, then $T(\varphi) \subseteq T(\psi)$, by soundness on the model $L$. This proves part 2, using step 10.
22. For part 1, let $\varphi$ have only the variable $p$. By step 11, $T(\varphi) = T(F_m)$ for some $m$. By steps 19 and 20 in both directions, $\mathsf{IPC} \vdash \varphi \leftrightarrow F_m$.
23. Part 3 follows from part 2, since the sets $t(F_m)$ are pairwise distinct. $\blacksquare$

## Idea

Every one-variable model can be folded onto the ladder by a p-morphism, so the ladder decides all one-variable equivalences.
The up-sets of the ladder are easy to list: initial segments, and initial segments with one extra point.
Nishimura's formulas hit these sets one by one, alternating a disjunction and an implication.

## Variants

An algebraic proof checks instead that the classes of the $F_m$ are closed under $\wedge$, $\vee$ and $\to$, using derivations in $\mathsf{IPC}$.
Bezhanishvili and de Jongh obtain the ladder as the 1-universal model and use the formulas $g_n$ and $f_n$.
