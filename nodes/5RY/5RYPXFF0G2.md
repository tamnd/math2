---
tag: 5RYPXFF0G2
kind: statement
role: theorem
name: Pudlák's lower bound for cutting planes
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [KKCX2HQP2K, 59GJCM8C66, 0BYX1D7C2E, 2XH5VDJ426]
about: [KKCX2HQP2K, 59GJCM8C66]
proofs: [R3MZGB0KY8]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Feasible interpolation
history:
  first_stated: "1997"
  notes: "Pavel Pudlák, Lower bounds for resolution and cutting plane proofs and monotone computations, Journal of Symbolic Logic 62(3), 1997."
---

## Statement

Cutting planes needs exponentially many lines to prove that a graph with a $k$-clique cannot be colored with $k - 1$ colors.

Take one variable $p_{uv}$ for each pair $u < v$ in $\{1, \dots, n\}$, so that a $0$-$1$ assignment $a$ is a graph $G_a$ on $n$ vertices.
The *clique-coloring formulas* are two systems of lines, each with the Boolean axioms $0 \leq y \leq 1$ for its variables.

1. $\mathrm{Clique}^n_k(p, q)$ has the lines $\sum_{u=1}^n q_u \geq k$ and $p_{uv} - q_u - q_v \geq -1$ for all $u < v$.
2. $\mathrm{Color}^n_{k-1}(p, r)$ has the lines $\sum_{c=1}^{k-1} r_{u,c} \geq 1$ for each $u$, and $-p_{uv} - r_{u,c} - r_{v,c} \geq -2$ for all $u < v$ and colors $c$.

For $n = 3$ and $k = 3$ the first system says that $G_a$ is a triangle, the second that $G_a$ has a proper $2$-coloring, and no graph does both.
In general $\mathrm{Clique}^n_k(a, q)$ has a $0$-$1$ solution exactly when $G_a$ has a [[clique|0BYX1D7C2E]] with $k$ vertices, and $\mathrm{Color}^n_{k-1}(a, r)$ has one exactly when $G_a$ is $(k-1)$-colorable.
So the union of the two systems has no $0$-$1$ solution.

**Theorem (Pudlák).** Let $k = \lfloor (n / \log_2 n)^{2/3} / 8 \rfloor$, and let $n$ be large enough that $k \geq 2$.

1. Let $f$ be a monotone Boolean function of $p$ with $f(a) = 0$ when $G_a$ is $(k-1)$-colorable and $f(a) = 1$ when $G_a$ has a $k$-clique.
   Every monotone real circuit that computes $f$ has size $2^{\Omega((n / \log n)^{1/3})}$.
2. Every [[cutting-planes refutation|KKCX2HQP2K]] of $\mathrm{Clique}^n_k(p, q) \cup \mathrm{Color}^n_{k-1}(p, r)$ has length $2^{\Omega((n / \log n)^{1/3})}$.

## Remarks

### The measure and the circuits

The measure in part 2 is length, the number of lines, with no bound on the size of the coefficients.
So the bound holds even for refutations whose numbers have exponentially many bits.

A *monotone real circuit* has real inputs, and each gate computes a function $\mathbb{R} \to \mathbb{R}$ or $\mathbb{R}^2 \to \mathbb{R}$ that is non-decreasing in each argument.
It computes a Boolean function $f$ when its output equals $f$ at every $0$-$1$ input, and its size is its number of gates.
Real gates such as $x \mapsto \lceil x/m \rceil$ and $(x, y) \mapsto 3x + 5y$ are allowed, and they are exactly what the lines of cutting planes need.

### Why each hypothesis is needed

The gates must be monotone.
Tardos built a function of the required kind, from the Lovász theta function, that general Boolean circuits compute in polynomial size.
So part 1 fails for circuits with negation, and the proof uses monotonicity at every gate.

The variables $p$ must have non-positive coefficients in every line of $\mathrm{Color}$, in the $\geq$ form.
This sign condition is the hypothesis of monotone interpolation, and it makes the interpolating circuit monotone.
Without it interpolation still gives a circuit, but no strong lower bound is known for general circuits.

The value of $k$ is the one for which Pudlák proved the circuit bound, and we state no bounds for other values.

### What it gives you

Cutting planes is not polynomially bounded, and this holds with no unproved assumption.
Compare [[Frege systems|J2BAR09TPF]], for which the same question is open.
The bound is a lower bound for cutting planes only: Frege systems p-simulate cutting planes, and no superpolynomial lower bound for Frege is known.

### The converse

Interpolation goes from proofs to circuits, and not back.
A small monotone real circuit that separates two systems gives no short refutation of their union.

### Generalizations

Haken and Cook proved exponential lower bounds for monotone real circuits independently of Pudlák.
The method applies to every pair $A(p, q)$, $B(p, r)$ in which $p$ has coefficients of one sign in $B$ and whose separating functions need large monotone real circuits.

## History

Pavel Pudlák proved the theorem in 1997, in the Journal of Symbolic Logic.
Earlier lower bounds covered only restricted forms of cutting planes: tree-like refutations (Impagliazzo, Pitassi and Urquhart, 1994) and refutations with small coefficients (Bonet, Pitassi and Raz, 1997).
Pudlák's theorem was the first exponential lower bound for general cutting-planes refutations.

## Explanations

### L1 human

Some graphs have a large group of vertices that are all joined to each other, a clique.
Other graphs can be colored with few colors so that joined vertices get different colors.
No graph has both a clique of $k$ vertices and a coloring with $k - 1$ colors, since two clique vertices would share a color.
Pudlák showed that every cutting-planes proof of this fact must be very long.
The reason is that a short proof would give a small circuit that tells the two kinds of graphs apart, and such small circuits do not exist.

### L2 human

The [[proof|R3MZGB0KY8]] follows the pattern of [[feasible interpolation|59GJCM8C66]] in four moves.

1. A cutting-planes refutation with $L$ lines gives a monotone real circuit with at most $L + 1$ gates.
2. The circuit outputs $1$ on graphs with a $k$-clique and $0$ on $(k-1)$-colorable graphs.
3. Part 1 says that every such circuit has size $2^{\Omega((n/\log n)^{1/3})}$.
4. So $L + 1$ is at least this size.

The typical use is to turn a circuit lower bound into a proof lower bound.
Watch out: the circuits must be real circuits, because the lines carry integers.
The bound of [[Razborov|2XH5VDJ426]] for Boolean monotone circuits does not cover them, and Pudlák had to extend it.

### L3 human

The theorem is the main example of monotone feasible interpolation for a system that is not a subsystem of resolution.
The proof splits every line into a clique part and a coloring part, and the right side of the coloring part is a monotone function of $p$.
For [[extended Frege|5YSE04SHFH]], Krajíček and Pudlák showed in 1998 that feasible interpolation fails if RSA is secure, so this route to lower bounds closes for strong systems.
