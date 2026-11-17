---
tag: EDZN6B9AWQ
kind: proof
name: Proof of the Kirby–Paris hydra theorem by ordinal assignment
msc: ["03F30", "03F15", "05C05"]
topics: [T6FK1E7GJ1]
audience: grad
proves: C028FF4TWM
uses: [0C9J6W2A8A, 0YSCSX5YZC, 6GD30FGYDZ, KT50SMH3EC, 0F1D6PK9RZ, 0ZHQMQ2C1N, Z742YPHPNS]
methods: [TP3GC5J08D, 0EFYCFHYFG, 12MQ2NJ29A, 0WCP0PVET6, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Hydra_game
    locator: Kirby–Paris and Buchholz hydras
---

## Proof

We use the rules of the [[Kirby-Paris hydra|C028FF4TWM]] game.
All ordinals are below [[epsilon nought|KT50SMH3EC]] $\varepsilon_0$ and are written in [[Cantor normal form|6GD30FGYDZ]] as a sum $\omega^{\gamma_1} + \cdots + \omega^{\gamma_j}$ with $\gamma_1 \ge \cdots \ge \gamma_j$.
So an ordinal is a finite list of exponents in nonincreasing order, and a coefficient $c$ is the exponent repeated $c$ times.

**Natural sums.**

1. The *natural sum* $\alpha \# \beta$ is the ordinal whose list of exponents is the union of the two lists, with repetitions kept, sorted in nonincreasing order.
2. The natural sum is commutative and associative, because the union of lists of exponents is commutative and associative.
3. Two ordinals are compared at the largest exponent where the numbers of occurrences differ. The one with more occurrences is larger.
4. If $\beta < \beta'$, then $\alpha \# \beta < \alpha \# \beta'$. Indeed $\alpha$ adds the same number of occurrences of each exponent to both, so the comparison of step 3 does not change.
5. The natural sum of $c$ copies of $\omega^\beta$ is $\omega^\beta c$. For every finite $c$, $\omega^\beta c < \omega^{\beta+1}$, by step 3 at the exponent $\beta + 1$.
6. If $\beta < \beta'$, then $\omega^\beta < \omega^{\beta'}$, by step 3. Also $\alpha \# \omega^0 = \alpha + 1$.

**The ordinal of a hydra.**

1. For a node $v$ with children $u_1, \dots, u_j$, define $o(v) = \omega^{o(u_1)} \# \cdots \# \omega^{o(u_j)}$, and $o(v) = 0$ for a leaf. This is a definition by [[structural induction|12MQ2NJ29A]] on the tree.
2. The ordinal of a hydra is $o(r)$ for its root $r$. By step 2 of the natural sums, it does not depend on the order of the children.
3. The value is below $\varepsilon_0$: if all $o(u_i) < \varepsilon_0$, then all $\omega^{o(u_i)} < \varepsilon_0$, and a natural sum of ordinals below $\varepsilon_0$ is below $\varepsilon_0$.
4. The hydra is dead if and only if $o(r) = 0$, because only a root with no children has the empty natural sum.

**Each step lowers the ordinal.**
Let Hercules cut the head $h$ with parent $p$ at step $n$, with $N_n \ge 0$ new copies.
Let $p'$ be the node $p$ after the removal of $h$, and let $\beta = o(p')$.

1. The head $h$ is a leaf, so it adds the term $\omega^0$ to $o(p)$. By step 6 of the natural sums, $o(p) = \beta + 1$.
2. Case 1: $p$ is the root. The ordinal of the hydra changes from $\beta + 1$ to $\beta$, so it decreases.
3. Case 2: $p$ has a parent $g$. Write $o(g) = \delta \# \omega^{o(p)} = \delta \# \omega^{\beta+1}$, where $\delta$ comes from the other children of $g$.
4. After the step, $g$ has the child $p'$ and $N_n$ copies of it, so its new value is $\delta \# \omega^\beta (N_n + 1)$, by step 5 of the natural sums.
5. Since $\omega^\beta (N_n + 1) < \omega^{\beta+1}$, step 4 of the natural sums gives that the value of $g$ strictly decreases.
6. Let $a$ be an ancestor of $g$, and let $u$ be its child on the path to $g$. Then $o(a) = \delta_a \# \omega^{o(u)}$, where $\delta_a$ does not change.
7. If $o(u)$ strictly decreases, then $\omega^{o(u)}$ strictly decreases by step 6 of the natural sums, and so $o(a)$ strictly decreases by step 4.
8. Going up the path from $g$ to the root with step 7, the ordinal $o(r)$ of the hydra strictly decreases.
9. Nodes outside this path keep their values, because their subtrees do not change.

**Part 1: every battle ends.**

1. Fix a hydra and a strategy, and let $\alpha_n$ be the ordinal of the hydra after step $n$.
2. While the hydra is alive, $\alpha_{n+1} < \alpha_n$, by the previous part. This holds for every choice of $N_n$.
3. If the battle never ended, $\alpha_0 > \alpha_1 > \alpha_2 > \cdots$ would be an infinite strictly decreasing sequence of ordinals.
4. This contradicts the [[well-ordering|0F1D6PK9RZ]] of the ordinals. So the hydra is dead after finitely many steps.

**Part 4: a proof in $\mathsf{PA}$ plus transfinite induction up to $\varepsilon_0$.**

1. Code hydras as finite trees and ordinals below $\varepsilon_0$ as their normal forms. The map $o$ and the standard battle are then primitive recursive.
2. The computations above are inductions over finite trees and lists, so $\mathsf{PA}$ proves them.
3. Let $\varphi(\alpha)$ say: every hydra with ordinal $\alpha$, met at any step $n$ of the standard battle, dies after finitely many further steps.
4. If $\varphi(\beta)$ holds for all $\beta < \alpha$, then $\varphi(\alpha)$ holds, because the next step reaches a smaller ordinal or the hydra is dead.
5. [[Transfinite induction|0ZHQMQ2C1N]] up to $\varepsilon_0$ for $\varphi$ gives $\varphi(\alpha)$ for every $\alpha < \varepsilon_0$, and this is part 4.

**Parts 2 and 3: unprovability in $\mathsf{PA}$.**

1. **Cited lemma** (Kirby and Paris 1982). The function $\mathrm{Hydra}$ eventually dominates every function that $\mathsf{PA}$ proves total. This is part 2, and we do not prove it here.
2. Suppose that $\mathsf{PA}$ proves that the standard battle kills every hydra. The standard battle is primitive recursive, so $\mathsf{PA}$ proves that $\mathrm{Hydra}$ is total.
3. Then $\mathsf{PA}$ also proves that $k \mapsto \mathrm{Hydra}(k) + 1$ is total.
4. The cited lemma gives $\mathrm{Hydra}(k) > \mathrm{Hydra}(k) + 1$ for all large $k$, which is false. So $\mathsf{PA}$ does not prove that the standard battle kills every hydra.
5. The standard strategy is given by one Turing machine $e_0$, and $\mathsf{PA}$ proves that $e_0$ always gives a legal move.
6. If $\mathsf{PA}$ proved that every recursive strategy kills every hydra, it would prove this for $e_0$, against step 4. This proves part 3.

## Idea

Each hydra gets an ordinal below $\varepsilon_0$: a node is worth the natural sum of $\omega$ to the values of its children.
Cutting a head turns one term $\omega^{\beta+1}$ at the grandparent into finitely many terms $\omega^\beta$, which is smaller however many copies grow.
The ordinals strictly decrease, so the battle ends; the unprovability comes from the growth of the length of the battle.

## Variants

- Kirby and Paris proved part 2 with non-standard models of $\mathsf{PA}$, as for [[Goodstein's theorem|XQMNJF241J]].
- One can also compare the standard battle with the [[Hardy hierarchy|X8RKXQASR9]] and then use the bound on the [[provably total functions|Z742YPHPNS]] of $\mathsf{PA}$.
- The same ordinal argument, with labels and collapsing functions, proves the termination of the [[Buchholz hydra|9APRFM0G7F]].
