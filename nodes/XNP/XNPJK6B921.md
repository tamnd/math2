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

Let $\Lambda$ be one of $\mathsf{K}$, $\mathsf{T}$, $\mathsf{D}$, $\mathsf{K4}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$, and let $\mathsf{C}$ be its frame class in [[the completeness theorem|FXTCKYR3AQ]].
Let $\varphi$ be a [[modal formula|G8VGTW9P4F]] with $n = |\operatorname{Sub}(\varphi)|$.

1. If $\Lambda \nvdash \varphi$, then $\varphi$ fails at some world of a model on a frame of $\mathsf{C}$ with at most $2^n$ worlds.
2. So $\Lambda = \operatorname{Log}(\mathsf{C}_{\mathrm{fin}})$, and $\Lambda$ has the [[finite model property|3NT8RCA6HE]] with the bound $f(n) = 2^n$.
3. So $\Lambda$ is decidable: $\Lambda \vdash \varphi$ if and only if $\varphi$ is valid on every frame of $\mathsf{C}$ with at most $2^n$ worlds.

The proof is in [[the proof of the finite model property|521829K9P0]].

## Remarks

### Why each hypothesis is needed

1. The choice of filtration depends on $\Lambda$. For $\mathsf{K4}$ and $\mathsf{S4}$ the smallest filtration can leave the frame class, see [[the transitive example|V0J3A9Q4SY]], so the proof uses the transitive filtration.
2. The bound uses $\operatorname{Sub}(\varphi)$, a set closed under subformulas; a smaller set breaks [[the filtration theorem|T99DK51S0W]].
3. The theorem is about these seven logics; other logics can lack the FMP, see [[finite model property|3NT8RCA6HE]].

### Consequences

1. Each of the seven logics is decidable, also by [[Harrop's theorem|VSYQ1AZ9G7]].
2. A non-theorem has a countermodel that a program can find by listing the frames of $\mathsf{C}$ up to $2^n$ worlds. See [[the Harrop search|XQ8W9DEBD2]] and [[the countermodel for axiom 4|VK1RP97KKY]].
3. $\mathsf{S4}$ is the logic of finite preorders, so it is also the logic of finite topological spaces, see [[S4|N60RVXSA5W]].

### Generalizations

1. The same proof works for every combination of $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$ for which a suitable filtration exists, for example $\mathsf{KD45}$.
2. Sharper bounds hold: $\mathsf{S5}$ needs at most $1 + m$ worlds, where $m$ is the number of boxed subformulas, see [[S5|VC3A2VWXND]].
3. For $\mathsf{K}$, a countermodel can be chosen as a tree of depth at most the modal depth of $\varphi$. This leads to the PSPACE bound of [[the complexity theorem|1P2B0C7CQ4]].

## History

McKinsey proved the decidability of $\mathsf{S4}$ in 1941 by finite algebras.
Lemmon and Segerberg proved the FMP of the basic logics by filtration in the 1960s.
Segerberg's An essay in classical modal logic of 1971 collects the results.

## Explanations

### L1 human

For these seven logics, every statement that cannot be proved fails in a finite network of worlds.
The network is small: its size is at most two to the power of the number of parts of the statement.
So a computer can decide each question by checking all small networks.

### L2 human

We decide whether $\mathsf{T} \vdash \lozenge\square p \to \square p$.

1. By the theorem, if a countermodel exists, then one exists on a reflexive frame with at most $2^n$ worlds. So we try small reflexive frames first.
2. Try the reflexive frame $w R v$, $w R w$, $v R v$, with $p$ true at $v$ only.
3. At $v$, $\square p$ is true, since $v$ sees only $v$. At $w$, $\square p$ is false, since $w$ sees itself and $p$ is false at $w$.
4. At $w$, $\lozenge\square p$ is true, since $w$ sees $v$.
5. So the formula fails at $w$ on a reflexive frame with 2 worlds, and $\mathsf{T} \nvdash \lozenge\square p \to \square p$.

The typical use is to replace a search for derivations by a finite search for countermodels.
A trap: the search must range over frames of the class, here reflexive frames, not over all frames.

### L3 human

The bound $2^n$ gives a nondeterministic exponential time algorithm, which is far from optimal.
By [[the complexity theorem|1P2B0C7CQ4]], satisfiability is PSPACE-complete for $\mathsf{K}$, $\mathsf{T}$, $\mathsf{D}$, $\mathsf{K4}$ and $\mathsf{S4}$, and NP-complete for $\mathsf{S5}$.
For these five logics the exponential bound cannot be replaced by a polynomial one unless NP equals PSPACE.
The reason is that polynomial countermodels would put satisfiability in NP.
