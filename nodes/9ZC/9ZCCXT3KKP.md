---
tag: 9ZCCXT3KKP
kind: statement
role: theorem
name: Nash–Moser theorem
msc: [58C15, 47J07, 35A01]
uses: [3GAA614673, 06EH97V2A7, M218MWZ62X]
about: [3GAA614673]
sources:
  - url: https://en.wikipedia.org/wiki/Nash%E2%80%93Moser_theorem
same_as:
  wikidata: Q6967039
  wikipedia: Nash–Moser theorem
---

## Statement

A *graded* [[Fréchet space|3GAA614673]] is a Fréchet space $F$ with a fixed increasing sequence of seminorms $\norm{\cdot}_0 \le \norm{\cdot}_1 \le \norm{\cdot}_2 \le \cdots$ that defines its topology.
Let $F$ and $G$ be graded Fréchet spaces and let $U \subseteq F$ be open.
A continuous map $P \colon U \to G$ is *tame* if each point of $U$ has a neighbourhood $V$ with this property.
There are integers $r, b \ge 0$ and constants $C_n$ with $\norm{P(f)}_n \le C_n(1 + \norm{f}_{n+r})$ for all $f \in V$ and all $n \ge b$.
It is *smooth tame* if it is smooth and all its derivatives are tame.
A graded Fréchet space is *tame* if it is a tame direct summand of a space of exponentially decreasing sequences in a Banach space.
For a compact manifold $M$, the space $C^\infty(M)$ graded by the $C^n$ norms is tame.

Let $F$ and $G$ be tame Fréchet spaces, let $U \subseteq F$ be open, and let $P \colon U \to G$ be a smooth tame map.
Suppose that for every $f \in U$ the [[derivative|06EH97V2A7]] $DP(f) \colon F \to G$ is bijective, and that the family of inverses $VP \colon U \times G \to F$, $VP(f, k) = DP(f)^{-1} k$, is a smooth tame map.
Then $P$ is locally invertible: each $f_0 \in U$ has an open neighbourhood $U_0$ such that $P(U_0)$ is open and $P \colon U_0 \to P(U_0)$ is a bijection.
Moreover, each such local inverse is a smooth tame map.

## Remarks

This is the form of the theorem given by Hamilton; Nash introduced the method to prove his embedding theorem for Riemannian manifolds, and Moser developed it as an abstract iteration.
The [[inverse function theorem in Banach spaces|M218MWZ62X]] does not apply, because in typical applications $DP(f)^{-1}$ loses derivatives: it maps $C^{n+r}$ data only to $C^{n}$ solutions.
The proof runs a Newton iteration $f_{j+1} = f_j - S_j\, VP(f_j, P(f_j) - g)$, where $S_j$ are smoothing operators that cut off high frequencies.
The quadratic convergence of Newton's method beats the loss of derivatives, and the tame estimates make this precise.

Example: in Kolmogorov–Arnold–Moser theory and in isometric embeddings of Riemannian manifolds, the linearised equations lose derivatives.
There the theorem gives solutions of the nonlinear equations near a known one.

## Explanations

### L1 human

The usual inverse function theorem says that if the derivative of a map is invertible, then the map itself is invertible near the point.
For maps between spaces of smooth functions this can fail when the inverse of the derivative makes functions rougher.
The Nash–Moser theorem restores the conclusion when every map involved obeys polynomial-type bounds that lose only a fixed number of derivatives.

### L2 human

The theorem is a tool for nonlinear PDEs whose linearisation is solvable only with a loss of derivatives, such as small divisor problems and isometric embeddings.
To apply it, one first checks that the nonlinear map is smooth tame, which is usually routine for differential operators.
One then checks that the linearised problem is solvable at every point near the base point, with tame estimates.
The second check is the real work, and it is often done with energy estimates or with Fourier analysis.
