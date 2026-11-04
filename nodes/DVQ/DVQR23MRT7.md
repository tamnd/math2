---
tag: DVQR23MRT7
kind: proof
name: Proof that the degree of a constructible number is a power of two
msc: [12F05]
proves: 0SSSM1D475
uses: [0FMN2MN7TM, 0PN9WMRWT7, 07QY5RPFBR, 0MA5B744K3, 0GK1WB9R98, 06K7SARZKR, 0N5QW9K7MH, 0A7KJ68XHT, 0DFYTNZ6AM]
sources:
  - url: https://en.wikipedia.org/wiki/Constructible_number
    locator: Algebraic properties
---

## Proof

1. Call a finite chain of subfields $\Q = F_0 \subseteq F_1 \subseteq \dots \subseteq F_m$ of $\C$ a square-root tower if, for each $j$, [[$F_j = F_{j-1}(s_j)$|0MA5B744K3]] for some $s_j \in \C$ with $s_j^2 \in F_{j-1}$. The case $m = 0$ is allowed.
2. Let $T$ be the set of the complex numbers that lie in the top field $F_m$ of some square-root tower.
3. In a square-root tower, $s_j$ is a root of $x^2 - s_j^2 \in F_{j-1}[x]$. So its [[minimal polynomial|0GK1WB9R98]] over $F_{j-1}$ [[divides|06K7SARZKR]] this polynomial and has degree $1$ or $2$.
4. By the [[degree of a simple extension|0N5QW9K7MH]], $[F_j : F_{j-1}] \in \set{1, 2}$. By the [[tower law|0A7KJ68XHT]], $[F_m : \Q]$ is a product of $1$s and $2$s, so it is a power of $2$.
5. Let $z, w \in T$, with towers $(F_j)_{j \le m}$ built from $s_1, \dots, s_m$ and $(G_j)_{j \le l}$ built from $t_1, \dots, t_l$.
6. Extend the first tower by $F_{m+j} = F_{m+j-1}(t_j)$ for $1 \le j \le l$. By induction on $j$, $G_j \subseteq F_{m+j}$: indeed $G_j = G_{j-1}(t_j)$, and $F_{m+j}$ contains $G_{j-1}$ and $t_j$.
7. So $t_j^2 \in G_{j-1} \subseteq F_{m+j-1}$, and the extended chain is a square-root tower. Its top field contains $z$ and $w$.
8. That top field is a field. So $z + w$, $-z$, $zw$, and $z^{-1}$ for $z \neq 0$, lie in it and hence in $T$. Also $\Q \subseteq T$, from the tower with $m = 0$. So $T$ is a [[subfield|07QY5RPFBR]] of $\C$.
9. Let $z \in T$ lie in the top field $F_m$ of a tower, and let $s \in \C$ with $s^2 = z$. Then $F_{m+1} = F_m(s)$ extends the tower, so $s \in T$. So $T$ is closed under square roots.
10. The [[constructible numbers|0FMN2MN7TM]] form the [[smallest subfield of $\C$ closed under square roots|0PN9WMRWT7]]. By steps 8 and 9, every constructible number lies in $T$.
11. Let $z$ be constructible. By step 10, $z \in F_m$ for some square-root tower, and $[F_m : \Q] = 2^e$ for some $e \ge 0$ by step 4.
12. So $F_m / \Q$ is finite, hence [[algebraic|0DFYTNZ6AM]], and $z$ is algebraic over $\Q$.
13. Since $\Q \subseteq \Q(z) \subseteq F_m$, the tower law gives $2^e = [F_m : \Q(z)] \cdot [\Q(z) : \Q]$. So $[\Q(z) : \Q]$ divides $2^e$.
14. By unique factorisation, a positive divisor of $2^e$ is $2^r$ for some $r$ with $0 \le r \le e$. So $[\Q(z) : \Q] = 2^r$.

## Idea

The numbers reachable from $\Q$ by adjoining square roots one at a time form a field closed under square roots, so they contain all constructible numbers. Each adjunction at most doubles the degree. So a constructible number sits in a field of degree $2^e$, and its own degree divides $2^e$.
