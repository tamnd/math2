---
tag: 8YQJQXQHVE
kind: statement
role: theorem
name: Nash embedding theorems
msc: [53C42, 53B20]
uses: [7CBT4SM83Y, Q61VFHCH2J]
about: [7CBT4SM83Y]
sources:
  - url: https://en.wikipedia.org/wiki/Nash_embedding_theorems
same_as:
  wikidata: Q1306092
  wikipedia: Nash embedding theorems
---

## Statement

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] of dimension $m$.
Write $\ip{\cdot}{\cdot}$ for the Euclidean inner product on $\R^n$.
An *isometric embedding* of $(M, g)$ into $\R^n$ is an embedding $f \colon M \to \R^n$ with $\ip{df_p(v)}{df_p(w)} = g_p(v, w)$ for all $p \in M$ and $v, w \in T_pM$.

1. ($C^1$ theorem, Nash and Kuiper.) Let $n \ge m + 1$ and let $f \colon M \to \R^n$ be a smooth embedding that is short, that is $\abs{df_p(v)}^2 < g_p(v, v)$ for all $p$ and all nonzero $v \in T_pM$. Then for every $\varepsilon > 0$ there is a $C^1$ embedding $\tilde f \colon M \to \R^n$ that is isometric for $g$ and satisfies $\abs{\tilde f(p) - f(p)} < \varepsilon$ for all $p \in M$.
2. ($C^k$ theorem, Nash.) Let $3 \le k \le \infty$ and let $g$ be of class $C^k$. Then $(M, g)$ has an isometric embedding of class $C^k$ into $\R^n$. Here $n = m(3m + 11)/2$ if $M$ is compact, and $n = m(m + 1)(3m + 11)/2$ otherwise.

## Remarks

Part 2 is proved by solving the nonlinear system $f^*\ip{\cdot}{\cdot} = g$ with an iteration that combines Newton's method with smoothing operators, the Nash–Moser technique.
Part 1 is proved by convex integration: one adds many small fast oscillations that increase lengths in a controlled way.
An example of part 1: the flat square torus $\R^2 / \Z^2$ has a $C^1$ isometric embedding into $\R^3$.
It has no $C^2$ isometric embedding there, because a compact surface in $\R^3$ has a point of positive [[Gaussian curvature|SQVQ5DQT6W]], while the flat torus has curvature $0$.
So the low codimension in part 1 really needs the low regularity $C^1$.
Nash proved part 1 with $n \ge m + 2$, and Kuiper extended it to $n \ge m + 1$.

## Explanations

### L1 human

Every abstract curved space described by a Riemannian metric can be realised as a surface inside some ordinary Euclidean space, with lengths measured in the usual way.
So the abstract definition of a Riemannian manifold gives nothing new compared with curved submanifolds of $\R^n$.
If one allows the surface to be only once differentiable, very little room is needed, and strange crumpled embeddings appear.

### L2 human

The [[Whitney embedding theorem|2GSRBDT96M]] embeds a manifold in $\R^{2m}$ but ignores the metric; Nash's theorems make the embedding respect the metric at the cost of more dimensions or less smoothness.
The $C^1$ theorem is an early instance of the h-principle: a short embedding can be deformed into an isometric one by arbitrarily small moves.
The bounds on $n$ in part 2 have been lowered by later work, but the existence statement is what is used in practice.
