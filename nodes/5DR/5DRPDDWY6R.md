---
tag: 5DRPDDWY6R
kind: proof
name: Proof of the law of total variance
msc: [60A10]
proves: 03BY5XTNA4
uses: [0YAMJRK04E, 0F1SN93KXE, 007QED3E0Y, 04RRB6HM00, 03PGHKAJG3, G2S6H789RG, BYNV84PF86, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_total_variance
    locator: Proof
---

## Proof

We split $X - E[X]$ into a part inside the groups and a part between the groups. Then we show that the cross term has mean $0$.

1. Let $\mathcal{G} = \sigma(Y)$, let $M = E[X \mid Y] = E[X \mid \mathcal{G}]$ be the [[conditional expectation|0YAMJRK04E]], and let $\mu = E[X]$. Since $E[X^2] < \infty$, $X$ is integrable, so $M$ exists.
2. Claim: $E[M W] = E[X W]$ for each bounded $\mathcal{G}$-measurable random variable $W$. For $W = 1_G$ with $G \in \mathcal{G}$, this is the defining property of $M$.
3. By [[linearity of expectation|0P7PTC8DDE]], the claim holds for each simple $\mathcal{G}$-measurable $W$. Such a $W$ is a finite linear combination of indicators of sets in $\mathcal{G}$.
4. Let $W$ be $\mathcal{G}$-measurable with $\abs{W} \le c$ for a constant $c$. Let $W_j = 2^{-j} \floor{2^j W}$ for $j \ge 1$. Each $W_j$ is $\mathcal{G}$-measurable and takes finitely many values, so it is simple.
5. We have $\abs{W_j - W} \le 2^{-j}$ and $\abs{W_j} \le c + 1$. So $M W_j \to M W$ and $X W_j \to X W$ pointwise, with bounds $(c + 1) \abs{M}$ and $(c + 1) \abs{X}$, which are integrable.
6. By [[dominated convergence|BYNV84PF86]], $E[M W_j] \to E[M W]$ and $E[X W_j] \to E[X W]$. With step 3, this proves the claim of step 2.
7. Claim: $E[M^2] \le E[X^2]$. For $k \ge 1$, let $W_k = M \, 1_{\{\abs{M} \le k\}}$. It is $\mathcal{G}$-measurable and bounded by $k$.
8. Step 2 gives $E[M W_k] = E[X W_k]$. The left side is $E[M^2 1_{\{\abs{M} \le k\}}] = E[W_k^2]$.
9. By the [[Cauchy–Schwarz inequality|03PGHKAJG3]], $E[X W_k] \le \left(E[X^2]\right)^{1/2} \left(E[W_k^2]\right)^{1/2}$.
10. Steps 8 and 9 give $E[W_k^2] \le \left(E[X^2]\right)^{1/2} \left(E[W_k^2]\right)^{1/2}$. Since $E[W_k^2] \le k^2$ is finite, this gives $E[W_k^2] \le E[X^2]$.
11. The functions $W_k^2$ increase in $k$ to $M^2$. By the [[monotone convergence theorem|G2S6H789RG]], $E[M^2] = \lim_k E[W_k^2] \le E[X^2]$.
12. So $X - M$ and $M - \mu$ have finite second moments. Then $(X - M)^2$ is integrable, and the [[conditional variance|0F1SN93KXE]] $\operatorname{Var}(X \mid Y) = E[(X - M)^2 \mid \mathcal{G}]$ is defined.
13. Claim: $E[(X - M)(M - \mu)] = 0$. Let $V = M - \mu$, which is $\mathcal{G}$-measurable, and let $V_k = V \, 1_{\{\abs{V} \le k\}}$ for $k \ge 1$.
14. Each $V_k$ is bounded and $\mathcal{G}$-measurable. By step 2, $E[(X - M) V_k] = E[X V_k] - E[M V_k] = 0$.
15. The product $(X - M) V_k$ tends to $(X - M) V$ pointwise. It is bounded by $\abs{X - M} \abs{V}$, which is integrable by the Cauchy–Schwarz inequality and step 12.
16. By dominated convergence and step 14, $E[(X - M) V] = \lim_k E[(X - M) V_k] = 0$.
17. Write $X - \mu = (X - M) + V$. Expand the square and use linearity: $E[(X - \mu)^2] = E[(X - M)^2] + 2 E[(X - M) V] + E[V^2]$.
18. By the definition of the [[variance|007QED3E0Y]], the left side is $\operatorname{Var}(X)$. By step 16, the middle term is $0$.
19. By the [[law of total expectation|04RRB6HM00]] for the integrable variable $(X - M)^2$, $E[(X - M)^2] = E\left[E[(X - M)^2 \mid \mathcal{G}]\right] = E[\operatorname{Var}(X \mid Y)]$.
20. By the law of total expectation, $E[M] = E[X] = \mu$. So $E[V^2] = E[(M - E[M])^2] = \operatorname{Var}(E[X \mid Y])$.
21. Steps 17 to 20 give $\operatorname{Var}(X) = E[\operatorname{Var}(X \mid Y)] + \operatorname{Var}(E[X \mid Y])$.

## Idea

Write $X - E[X]$ as the deviation of $X$ from its group mean $E[X \mid Y]$, plus the deviation of the group mean from $E[X]$. The first part is orthogonal to every function of $Y$, so the cross term vanishes and the two squares add up. Most of the work checks that every term is finite.
