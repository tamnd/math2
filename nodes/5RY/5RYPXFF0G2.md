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

Let $2 \leq k \leq n$.
Take one variable $p_{uv}$ for each pair $u < v$ of vertices in $\set{1, \dots, n}$.
A $0$-$1$ assignment $a$ of them is the graph $G_a$ on $\set{1, \dots, n}$ with the edges $\set{u, v}$ for which $a_{uv} = 1$.

The *clique-colouring formulas* are two systems of integer linear inequalities, each with the Boolean axioms $0 \leq y \leq 1$ for its variables.

1. $\mathrm{Clique}^n_k(p, q)$ has the variables $p$ and $q_1, \dots, q_n$, and the lines $\sum_{u=1}^n q_u \geq k$ and $p_{uv} - q_u - q_v \geq -1$ for all $u < v$.
2. $\mathrm{Colour}^n_{k-1}(p, r)$ has the variables $p$ and $r_{u,c}$ for $u \leq n$ and $c \leq k - 1$, and the lines $\sum_{c=1}^{k-1} r_{u,c} \geq 1$ for each $u$ and $-p_{uv} - r_{u,c} - r_{v,c} \geq -2$ for all $u < v$ and all $c$.

For each $a$, $\mathrm{Clique}^n_k(a, q)$ has a $0$-$1$ solution exactly when $G_a$ has a [[clique|0BYX1D7C2E]] with $k$ vertices, and $\mathrm{Colour}^n_{k-1}(a, r)$ has one exactly when $G_a$ is $(k-1)$-colourable.
A graph with a $k$-clique is not $(k-1)$-colourable, so the union of the systems has no $0$-$1$ solution.

A *monotone real circuit* is a circuit whose inputs are real numbers and whose gates compute functions $\mathbb{R} \to \mathbb{R}$ or $\mathbb{R}^2 \to \mathbb{R}$ that are non-decreasing in each argument.
It computes a Boolean function $f$ when it has the value of $f$ at every $0$-$1$ input.
Its size is its number of gates.

**Theorem (Pudlák).** Let $k = \floor{(n / \log_2 n)^{2/3} / 8}$, and assume that $n$ is large enough that $k \geq 2$.

1. Let $f$ be a monotone Boolean function of the variables $p$ such that $f(a) = 0$ for every $(k-1)$-colourable graph $G_a$ and $f(a) = 1$ for every graph $G_a$ with a $k$-clique. Then every monotone real circuit that computes $f$ has size $2^{\Omega((n / \log n)^{1/3})}$.
2. Every [[cutting-planes refutation|KKCX2HQP2K]] of $\mathrm{Clique}^n_k(p, q) \cup \mathrm{Colour}^n_{k-1}(p, r)$ has length $2^{\Omega((n / \log n)^{1/3})}$.

## Remarks

The measure in part 2 is the length, the number of lines, with no bound on the size of the coefficients.

### Why each hypothesis is needed

- **Monotone gates.** Part 1 is false for unrestricted circuits in a strong sense: no superpolynomial lower bound for general Boolean circuits is known for any function in NP. The proof uses monotonicity at every gate.
- **The signs of $p$.** In the $\geq$ form, $p$ has non-positive coefficients in every line of $\mathrm{Colour}$. This is the hypothesis of the monotone interpolation lemma for CP, and it makes the interpolant monotone. Without it, interpolation still gives a circuit, but no exponential lower bound is known for general circuits.
- **The value of $k$.** The theorem is stated for this $k$, which enters the parameters of the approximation argument. We do not state the bounds for other values of $k$.

### Consequences

- CP is not polynomially bounded. This is an unconditional result, in contrast with the open question whether [[Frege systems|J2BAR09TPF]] are polynomially bounded.
- The bound is on the number of lines, so large coefficients do not help.
- The theorem is a lower bound for CP only. It says nothing about stronger systems: Frege systems p-simulate CP, and no superpolynomial lower bound for Frege is known.

### Converse

Interpolation goes from proofs to circuits, and not back.
A small monotone real circuit that separates two systems gives no short CP refutation of their union.

### Generalizations

Haken and Cook proved exponential lower bounds for monotone real circuits independently of Pudlák.
The same method applies to every pair $A(p, q)$, $B(p, r)$ in which $p$ has coefficients of one sign in $B$ and whose separating functions need large monotone real circuits.

## History

Pavel Pudlák proved the theorem in *Lower bounds for resolution and cutting plane proofs and monotone computations*, Journal of Symbolic Logic 62(3), 1997.
Before this, Impagliazzo, Pitassi and Urquhart (1994) had lower bounds for tree-like CP, and Bonet, Pitassi and Raz (1997) had lower bounds for CP with small coefficients.
Pudlák's result was the first exponential lower bound for general CP refutations.

## Explanations

### L1 human

Some graphs have a large group of vertices that are all joined to each other, a clique.
Other graphs can be coloured with few colours so that joined vertices get different colours.
No graph has both a clique of $k$ vertices and a colouring with $k - 1$ colours.
Pudlák showed that any cutting-planes proof of this fact must be very long.
The reason is that a short proof would give a small circuit that tells the two kinds of graphs apart, and such small circuits do not exist.

### L2 human

The proof follows the pattern of [[feasible interpolation|59GJCM8C66]].

1. A CP refutation with $L$ lines gives a monotone real circuit with $O(L)$ gates.
2. The circuit outputs $1$ on graphs with a $k$-clique and $0$ on $(k-1)$-colourable graphs.
3. Part 1 says that every such circuit has size $2^{\Omega((n/\log n)^{1/3})}$.
4. So $L$ is at least this size, up to a constant factor.

A typical use is to transfer a circuit lower bound to a proof lower bound.
A trap: the circuits are real circuits, not Boolean circuits, because the lines of CP carry integers; the lower bound of [[Razborov|2XH5VDJ426]] for Boolean monotone circuits is not enough.

### L3 human

The theorem is the main example of monotone feasible interpolation for a system that is not a subsystem of resolution.
Its proof splits every line of the refutation into a part about the clique and a part about the colouring, and the right side of the colouring part is a monotone function of $p$.
For [[extended Frege|5YSE04SHFH]] there is no feasible interpolation under cryptographic assumptions, so this route to lower bounds is closed for strong systems.
