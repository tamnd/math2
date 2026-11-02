---
tag: 833XVEEZCJ
kind: statement
role: theorem
name: Kingman's subadditive ergodic theorem
msc: [37A30, 60F15, 28D05]
uses: [556WBDAHNP, 0NFPJVJJHX, X7GTF3D98F, RARTMA0ZEC, AZRPHS478B, J6NMBX3E55, 8A4GGX1MEY, NJ1FJSNK6A]
about: [556WBDAHNP]
sources:
  - url: https://en.wikipedia.org/wiki/Kingman%27s_subadditive_ergodic_theorem
same_as:
  wikidata: Q22906153
  wikipedia: Kingman's subadditive ergodic theorem
---

## Statement

Let $(X, \mathcal{A}, \mu)$ be a [[probability space|0NFPJVJJHX]] and let $T \colon X \to X$ be a [[measure-preserving transformation|556WBDAHNP]].
Let $(f_n)_{n \ge 1}$ be [[integrable|X7GTF3D98F]] functions $f_n \colon X \to \R$ that are subadditive along $T$:
$$f_{m+n} \le f_m + f_n \circ T^m \quad \text{almost everywhere, for all } m, n \ge 1.$$
Let $\gamma = \inf_{n \ge 1} \frac{1}{n} \int_X f_n \, d\mu$, an element of $[-\infty, \infty)$.
Then:

1. $f_n / n$ converges [[almost everywhere|RARTMA0ZEC]] to a function $g \colon X \to [-\infty, \infty)$ with $g \circ T = g$ almost everywhere;
2. $\int_X g \, d\mu = \gamma$, and if $\gamma > -\infty$, then $f_n / n \to g$ in $L^1(\mu)$;
3. if $T$ is [[ergodic|AZRPHS478B]], then $g = \gamma$ almost everywhere.

## Remarks

If $f_n = \sum_{k=0}^{n-1} f \circ T^k$ for an integrable $f$, then equality holds in the subadditivity condition, and the theorem reduces to [[Birkhoff's ergodic theorem|J6NMBX3E55]].
The integrals $a_n = \int_X f_n \, d\mu$ form a subadditive sequence, $a_{m+n} \le a_m + a_n$, so $a_n / n \to \gamma$ by [[Fekete's lemma|8A4GGX1MEY]]; the theorem is the pointwise version of this fact.
In the proof, the function $\liminf_n f_n / n$ is shown to be invariant.
A covering argument cuts a long orbit segment into blocks on which $f_k / k$ is close to this $\liminf$.
Subadditivity then bounds $f_N$ by the sum over the blocks.

Example: let $A \colon X \to GL_d(\R)$ be measurable with $\log^+ \norm{A}$ and $\log^+ \norm{A^{-1}}$ integrable, and let $f_n(x) = \log \norm{A(T^{n-1}(x)) \cdots A(T(x)) A(x)}$.
Submultiplicativity of the operator norm gives $f_{m+n} \le f_m + f_n \circ T^m$, and the two integrability conditions make each $f_n$ integrable.
For ergodic $T$, the theorem gives the almost sure limit of $f_n / n$, the top [[Lyapunov exponent|NJ1FJSNK6A]] of the matrix cocycle; this is the Furstenberg–Kesten theorem.

## Explanations

### L1 human

Sometimes the cost of a long journey is at most the cost of its first part plus the cost of the rest, as for the length of a shortest path.
The theorem says that, in a random environment that looks the same everywhere, the cost per unit of length of such a journey settles down to a limit.
For an ergodic environment this limit is a fixed number, the same for almost every starting point.

### L2 human

Kingman proved the theorem in 1968.
It extends Birkhoff's theorem from additive to subadditive sequences.
It is the main tool for the existence of Lyapunov exponents, as in the Furstenberg–Kesten theorem and in the proof of the Oseledets multiplicative ergodic theorem.
Another standard use is the time constant of first-passage percolation, where travel times between points are subadditive but not additive.
