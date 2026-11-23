---
tag: R3MZGB0KY8
kind: proof
name: Proof structure of Pudlák's lower bound by monotone interpolation
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
proves: 5RYPXFF0G2
uses: [KKCX2HQP2K, 59GJCM8C66, 2XH5VDJ426, 0BYX1D7C2E]
methods: [0NTF6DMVAP, 0J0XBKG64S, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Feasible interpolation
---

## Proof

We turn a short cutting-planes refutation into a small monotone real circuit, and then a circuit lower bound, which we cite, bounds the number of lines.
We write $A = \mathrm{Clique}^n_k(p, q)$ and $B = \mathrm{Color}^n_{k-1}(p, r)$, as in the statement.
Part 1 of the theorem, the circuit bound, is cited without proof.
The interpolation lemma is proved below.

### The signs of the shared variables

1. In the $\geq$ form, the lines of $A$ are $\sum_u q_u \geq k$, the lines $p_{uv} - q_u - q_v \geq -1$, and Boolean axioms.
   So $p$ has non-negative coefficients in $A$.
2. The lines of $B$ are $\sum_c r_{u,c} \geq 1$, the lines $-p_{uv} - r_{u,c} - r_{v,c} \geq -2$, and Boolean axioms.
   So $p$ has non-positive coefficients in $B$, and each line of $B$ contains at most one variable of $p$.
3. We count the Boolean axioms $p_{uv} \geq 0$ and $-p_{uv} \geq -1$ as lines of $A$, since they contain no $r$.

### The interpolation lemma: two numbers per line

Fix a $0$-$1$ assignment $a$ of $p$, and let $\pi$ be a refutation of $A \cup B$ with $L$ lines.
Write each line of $\pi$ as $b^{\mathsf T} q + c^{\mathsf T} r + d^{\mathsf T} p \geq \gamma$.
By induction along $\pi$ we attach integers $D_1(a)$ and $D_2(a)$ to each line, with three properties.

- (i) Every $0$-$1$ solution $q$ of $A(a, q)$ satisfies $b^{\mathsf T} q \geq D_1(a)$.
- (ii) Every $0$-$1$ solution $r$ of $B(a, r)$ satisfies $c^{\mathsf T} r \geq D_2(a)$.
- (iii) $D_1(a) + D_2(a) \geq \gamma - d^{\mathsf T} a$.

4. A line of $A$ has $c = 0$, and we put $D_1 = \gamma - d^{\mathsf T} a$ and $D_2 = 0$.
   Property (i) is the line itself at $p = a$, and (ii) and (iii) hold with equality.
5. A line of $B$ has $b = 0$, and we put $D_1 = 0$ and $D_2 = \gamma - d^{\mathsf T} a$.
   Since $d \leq 0$, the number $D_2$ is a non-decreasing function of $a$.
6. For a linear combination with weights $\alpha, \beta \geq 0$, we put $D_i = \alpha D_i' + \beta D_i''$, where $D_i'$ and $D_i''$ belong to the premises.
   The three properties follow by adding those of the premises with non-negative weights.
7. For a division by $m$, every entry of $b$, $c$ and $d$ is divisible by $m$, and we put $D_i = \lceil D_i' / m \rceil$.
   Property (ii) holds because $(c/m)^{\mathsf T} r$ is an integer that is at least $D_2'/m$, and (i) holds in the same way.
8. For (iii) after a division, $\lceil D_1'/m \rceil + \lceil D_2'/m \rceil$ is an integer that is at least $(\gamma - d^{\mathsf T} a)/m$.
   So it is at least $\lceil \gamma/m \rceil - (d/m)^{\mathsf T} a$, because $(d/m)^{\mathsf T} a$ is an integer.

### The interpolant

9. The last line $0 \geq 1$ has $b = c = d = 0$ and $\gamma = 1$, so (iii) gives $D_1(a) + D_2(a) \geq 1$.
10. Put $I(a) = 1$ when $D_2(a) \geq 1$, and $I(a) = 0$ otherwise.
11. If $I(a) = 1$, then by (ii) at the last line every solution of $B(a, r)$ satisfies $0 \geq D_2(a) \geq 1$, so $B(a, r)$ has no solution.
12. If $I(a) = 0$, then $D_2(a) \leq 0$, so $D_1(a) \geq 1$, and by (i) the system $A(a, q)$ has no solution.

### The circuit

13. We compute $D_2$ with one gate per line.
   A line of $B$ whose only $p$-variable is $p_e$, with coefficient $d_e \leq 0$, gets the gate $x \mapsto \gamma + \lvert d_e \rvert x$ on the input $a_e$.
   A line of $B$ without $p$ gets the constant $\gamma$, and a line of $A$ gets the constant $0$.
14. A combination gets the gate $(x, y) \mapsto \alpha x + \beta y$, and a division gets $x \mapsto \lceil x/m \rceil$.
   One output gate computes $x \mapsto 1$ if $x \geq 1$ and $x \mapsto 0$ otherwise.
15. Each gate is non-decreasing, because $\alpha, \beta, \lvert d_e \rvert \geq 0$ and $m \geq 1$.
   So we get a monotone real circuit with at most $L + 1$ gates that computes $I$.

### Conclusion

16. If $G_a$ has a $k$-clique, then $A(a, q)$ has a solution, so $I(a) \neq 0$ by step 12, and $I(a) = 1$.
17. If $G_a$ is $(k-1)$-colorable, then $B(a, r)$ has a solution, so $I(a) \neq 1$ by step 11, and $I(a) = 0$.
18. A composition of non-decreasing functions is non-decreasing, so $I$ is a monotone Boolean function with the two properties of $f$ in part 1.
19. Part 1, which Pudlák proved by extending the approximation method of [[Razborov's monotone circuit bound|2XH5VDJ426]] to real gates, gives $L + 1 \geq 2^{\Omega((n/\log n)^{1/3})}$.

So every cutting-planes refutation of the clique-coloring formulas has length $2^{\Omega((n/\log n)^{1/3})}$, which is part 2.

## Idea

Every line of the refutation is split into a clique part and a coloring part, and we follow a lower bound for each part through the refutation.
At the end the two bounds add up to at least $1$, so one of the two parts has become a contradiction, and the coloring bound tells us which.
That bound is computed by one monotone real gate per line, because the coloring lines have non-positive coefficients on $p$.
A lower bound for monotone real circuits then bounds the number of lines.

## Variants

The same argument gives lower bounds for [[resolution|6JSH907W5R]], where the circuit is a monotone Boolean circuit.
See [[the interpolation theorem for resolution|YHGCN7BBEP]] and [[its application to clique-coloring|F8GJ402PH2]].
For resolution, [[Razborov's bound|2XH5VDJ426]] for Boolean monotone circuits is enough, and real gates are not needed.

When an axiom of $B$ contains several variables of $p$, step 13 needs one more addition gate for each extra variable, and the gate count grows by the number of those occurrences.
Haken and Cook proved lower bounds for monotone real circuits independently, and their bound can replace part 1.
