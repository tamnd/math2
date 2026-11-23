---
tag: XNPJK6B921
kind: statement
role: theorem
name: Finite model property of K, T, D, K4, S4, B and S5
msc: ["03B45", "03B25"]
topics: [SKY7AQFG1V]
audience: grad
uses: [3NT8RCA6HE, FXTCKYR3AQ, T99DK51S0W, 6ZZSHAKG5F, E87G6ZTMTN, G8VGTW9P4F]
about: [3NT8RCA6HE, 6ZZSHAKG5F]
proofs: [521829K9P0]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Finite model property
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on filtrations and decidability
---

## Statement

Let $\Lambda$ be one of $\mathsf{K}$, $\mathsf{T} = \mathsf{KT}$, $\mathsf{D} = \mathsf{KD}$, $\mathsf{K4}$, $\mathsf{S4} = \mathsf{KT4}$, $\mathsf{B} = \mathsf{KTB}$ and $\mathsf{S5} = \mathsf{KT5}$, and let $\mathsf{C}$ be its frame class in [[the completeness theorem|FXTCKYR3AQ]].
Let $\varphi$ be a [[modal formula|G8VGTW9P4F]] with $n$ subformulas.

1. If $\Lambda \nvdash \varphi$, then $\varphi$ fails at some world of a model on a frame of $\mathsf{C}$ with at most $2^n$ worlds.
2. So $\Lambda = \operatorname{Log}(\mathsf{C}_{\mathrm{fin}})$, and $\Lambda$ has the [[finite model property|3NT8RCA6HE]] with the bound $f(n) = 2^n$.
3. So $\Lambda$ is decidable: $\Lambda \vdash \varphi$ holds if and only if $\varphi$ is valid on every frame of $\mathsf{C}$ with at most $2^n$ worlds.

The proof is in [[the proof of the finite model property|521829K9P0]].

## Remarks

### Why each hypothesis is needed

The choice of filtration depends on $\Lambda$.
For $\mathsf{K4}$ and $\mathsf{S4}$ the smallest filtration can leave the frame class, as [[the transitive example|V0J3A9Q4SY]] shows, so the proof uses the transitive filtration.

The bound counts the subformulas of $\varphi$ because the filtration is taken through that set, which is closed under subformulas.
A smaller set breaks [[the filtration theorem|T99DK51S0W]].

The theorem is about these seven logics.
Other normal logics can lack the FMP, as on the [[finite model property|3NT8RCA6HE]] page.

### What it gives you

Each of the seven logics is decidable, which also follows from [[Harrop's theorem|VSYQ1AZ9G7]].
A non-theorem has a countermodel that a program can find by listing the frames of $\mathsf{C}$ with at most $2^n$ worlds, as in [[the Harrop search|XQ8W9DEBD2]] and [[the countermodel for axiom 4|VK1RP97KKY]].
$\mathsf{S4}$ is the logic of finite preorders, so it is also the logic of finite topological spaces, as on [[the S4 page|N60RVXSA5W]].

### The converse

The converse of part 1 is soundness: a formula that fails on a frame of $\mathsf{C}$ is not a theorem, because each frame of $\mathsf{C}$ validates $\Lambda$.
So part 3 is an exact test.

### Generalizations

The same proof works for every combination of $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$ for which a suitable filtration exists, for example $\mathsf{KD45}$.
Sharper bounds hold for some of the logics: $\mathsf{S5}$ needs at most $1 + m$ worlds, where $m$ is the number of boxed subformulas, as on [[the S5 page|VC3A2VWXND]].
For $\mathsf{K}$, a countermodel can be chosen as a tree whose depth is at most the modal depth of $\varphi$, which leads to the PSPACE bound of [[the complexity theorem|1P2B0C7CQ4]].

## History

McKinsey proved the decidability of $\mathsf{S4}$ in 1941 with finite algebras.
Segerberg's An Essay in Classical Modal Logic of 1971 proved the FMP of these and many other logics by filtration.

## Explanations

### L1 human

For these seven logics, every statement that cannot be proved fails in a finite network of worlds.
The network is small: its size is at most two to the power of the number of parts of the statement.
So a computer can decide each question by checking all small networks.

### L2 human

We decide whether $\mathsf{T} \vdash \lozenge\square p \to \square p$.
By the theorem, if a countermodel exists, then one exists on a small reflexive frame, so we try small reflexive frames first.
Take worlds $w$ and $v$ with $w R v$, $w R w$ and $v R v$, and with $p$ true at $v$ only.
At $v$, $\square p$ is true, since $v$ sees only $v$.
At $w$, $\square p$ is false, since $w$ sees itself and $p$ is false at $w$, while $\lozenge\square p$ is true, since $w$ sees $v$.
So the formula fails at $w$ on a reflexive frame with 2 worlds, and $\mathsf{T} \nvdash \lozenge\square p \to \square p$.
Watch out: the search must range over frames of the class, here reflexive frames, and not over all frames.

### L3 human

The bound $2^n$ gives a nondeterministic exponential time algorithm, which is far from optimal.
By [[the complexity theorem|1P2B0C7CQ4]], satisfiability is PSPACE-complete for $\mathsf{K}$, $\mathsf{T}$ and $\mathsf{S4}$, and for $\mathsf{D}$ and $\mathsf{K4}$ as well, while it is NP-complete for $\mathsf{S5}$.
For the PSPACE-complete logics the exponential bound cannot be replaced by a polynomial one unless NP equals PSPACE, because polynomial countermodels would put satisfiability in NP.
