---
tag: QC1D2SRDFX
kind: proof
name: Proof that convergence in probability implies convergence in distribution
msc: [60F05]
proves: 0EPTDZPJ83
uses: [0EFDDXTVD6, 0JDAQHWA9N, 0MXMS3AE13, 0EGSEE9J9R]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_of_convergence_of_random_variables
    locator: Convergence in probability implies convergence in distribution
---

## Proof

We sandwich $F_n(x)$ between values of $F$ near $x$.

1. Let $F, F_1, F_2, \dots$ be the [[cumulative distribution functions|0MXMS3AE13]] of $X, X_1, X_2, \dots$. Fix a point $x \in \R$ at which $F$ is continuous, and fix $\varepsilon > 0$.
2. Claim: $\set{X_n \le x} \subseteq \set{X \le x + \varepsilon} \cup \set{\abs{X_n - X} > \varepsilon}$. If $X_n \le x$ and $X > x + \varepsilon$, then $X - X_n > \varepsilon$.
3. By step 2 and [[Boole's inequality|0EGSEE9J9R]], $F_n(x) \le F(x + \varepsilon) + P(\abs{X_n - X} > \varepsilon)$.
4. Claim: $\set{X \le x - \varepsilon} \subseteq \set{X_n \le x} \cup \set{\abs{X_n - X} > \varepsilon}$. If $X \le x - \varepsilon$ and $X_n > x$, then $X_n - X > \varepsilon$.
5. By step 4 and Boole's inequality, $F(x - \varepsilon) \le F_n(x) + P(\abs{X_n - X} > \varepsilon)$.
6. By [[convergence in probability|0EFDDXTVD6]], $P(\abs{X_n - X} > \varepsilon) \to 0$ as $n \to \infty$.
7. Steps 3, 5 and 6 give $F(x - \varepsilon) \le \liminf_{n} F_n(x) \le \limsup_{n} F_n(x) \le F(x + \varepsilon)$.
8. Step 7 holds for every $\varepsilon > 0$. Since $F$ is continuous at $x$, $F(x - \varepsilon) \to F(x)$ and $F(x + \varepsilon) \to F(x)$ as $\varepsilon \to 0^+$.
9. So $\liminf_n F_n(x) = \limsup_n F_n(x) = F(x)$, that is, $F_n(x) \to F(x)$.
10. This holds at every continuity point $x$ of $F$. So $X_n \to X$ [[in distribution|0JDAQHWA9N]].

## Idea

If $X_n$ is within $\varepsilon$ of $X$ with high probability, then the event $X_n \le x$ is squeezed between $X \le x - \varepsilon$ and $X \le x + \varepsilon$, up to a small error. At a continuity point of $F$, both bounds come together as $\varepsilon$ shrinks.
