---
tag: HZ9VYPSH98
kind: proof
name: Width proof of Urquhart's theorem
msc: ["03F20", "05C50"]
topics: [CBAF7J051K]
audience: research
proves: HF1GHVRDSD
uses: [JXTCC6KXNG, GWDGRPAQSM, 6JSH907W5R, 8D74S641EK]
methods: [0J0XBKG64S, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
---

## Proof

We find a clause in the refutation that depends on a medium-sized set of vertices, show that it mentions every edge leaving that set, and then apply the size-width relation.
Let $G = (V, E)$, $N$, $d$ and $\chi$ be as in the statement.
For a set $U \subseteq V$, write $\mathrm{PAR}_U$ for the conjunction of the parity constraints of the vertices in $U$.

### Part 1: a clause of medium complexity

1. *Every proper subset is satisfiable.*
   Let $U \ne V$, fix $v_0 \in V \setminus U$, and start with any assignment.
   For each vertex $u \in U$ whose constraint fails, flip the edges of a path from $u$ to $v_0$.
   Flipping a path changes the parity at its two ends only, so after these flips every constraint in $U$ holds.
2. *A measure.* For a clause $C$, let $\mu(C)$ be the least $\lvert U \rvert$ such that $\mathrm{PAR}_U$ implies $C$.
3. A clause of the constraint of $v$ is implied by $\mathrm{PAR}_{\{v\}}$, so $\mu(C) \le 1$ for every axiom $C$.
4. $\square$ is implied by $\mathrm{PAR}_V$, since $T(G, \chi)$ is unsatisfiable.
   It is not implied by $\mathrm{PAR}_U$ for $U \ne V$, by step 1, so $\mu(\square) = N$.
5. Let $C$ be the resolvent of $A$ and $B$, with $\mathrm{PAR}_{U_A} \models A$ and $\mathrm{PAR}_{U_B} \models B$.
   Then $\mathrm{PAR}_{U_A \cup U_B} \models C$, so $\mu(C) \le \mu(A) + \mu(B)$.
6. Let $\pi$ be a refutation, and let $C$ be the first clause of $\pi$ with $\mu(C) \ge N/3$.
   It is not an axiom, since $N/3 > 1$ for $N \ge 4$.
   Its premises have $\mu < N/3$, so $\mu(C) < 2N/3$ by step 5.
7. Choose $U$ with $\lvert U \rvert = \mu(C)$ and $\mathrm{PAR}_U \models C$.
   Then $N/3 \le \lvert U \rvert < 2N/3$.

### Part 1, boundary edges occur in the clause

8. Let $e = \{u, w\}$ be an edge with $u \in U$ and $w \notin U$.
   By the minimality of $U$, $\mathrm{PAR}_{U \setminus \{u\}}$ does not imply $C$.
   So some assignment $\alpha$ satisfies every constraint of $U \setminus \{u\}$ and falsifies $C$.
9. $\alpha$ falsifies the constraint of $u$, since otherwise it satisfies $\mathrm{PAR}_U$ and hence $C$.
10. Let $\alpha'$ be $\alpha$ with $x_e$ flipped, so the parity changes at $u$ and $w$ only.
    Then $\alpha'$ satisfies the constraint of $u$, and the other constraints of $U$ still hold, since $w \notin U$.
    So $\alpha'$ satisfies $\mathrm{PAR}_U$ and hence $C$.
11. $\alpha$ and $\alpha'$ differ only in $x_e$, and they give $C$ different values, so $x_e$ occurs in $C$.
12. By steps 8 to 11, $C$ contains a literal for each edge of $E(U, V \setminus U)$.
    So $w(C) \ge e(G)$, and $w(\pi) \ge e(G)$, which proves part 1.

### Part 2: size

13. The formula $T(G, \chi)$ has $\lvert E \rvert = dN/2$ variables, and its clauses have width $d$.
14. We apply the [[size-width relation|GWDGRPAQSM]] for general resolution, with $n = dN/2$, $w(F) = d$ and $w(F \vdash \square) \ge e(G) \ge d + 1$.
    It gives at least $\exp\bigl((e(G) - d - 1)^2/(8 \cdot dN/2)\bigr)$ clauses.
15. Since $8 \cdot dN/2 = 4dN$, this is the bound of part 2.

### The corollary

16. If $e(G_N) \ge \varepsilon N$ and $N \ge 2(d + 1)/\varepsilon$, then $e(G_N) - d - 1 \ge \varepsilon N/2$.
17. So the bound is at least $\exp\bigl(\varepsilon^2 N^2/(16 d N)\bigr) = \exp\bigl(\varepsilon^2 N/(16 d)\bigr)$.
    This is $2^{\Omega(N)}$, since $d$ and $\varepsilon$ are constants.

$\blacksquare$

## Idea

A clause in the middle of a refutation summarizes the constraints of a medium-sized set $U$ of vertices.
It must mention every edge that leaves $U$, because flipping such an edge moves a parity violation out of $U$.
On an expander, every medium-sized set has many leaving edges, so some clause is wide, and wide refutations are long.
The step where students slip is step 6.
The clause must be the first one with $\mu \ge N/3$, so that $\mu$ is also below $2N/3$, and both bounds are needed for the expansion to apply.

## Variants

Urquhart's original proof of 1987 used a direct counting argument on the refutation, without width.
The same measure $\mu$, with the pigeons in place of the vertices, gives the clause with a wide monotone transform in the [[proof of Haken's theorem|8D74S641EK]].
