---
tag: 9XXBTE8HDD
kind: proof
name: Proof that almost sure convergence implies convergence in probability
msc: [60F15]
proves: 0SVN6X695K
uses: [04P7D63W8P, 0EFDDXTVD6, 0X8HBKCSYB]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_of_convergence_of_random_variables
    locator: Convergence almost surely implies convergence in probability
---

## Proof

We bound the event of a large deviation at time $n$ by the event of a large deviation at some time $m \ge n$.

1. Let $C = \set{\omega \in \Omega : \lim_{n \to \infty} X_n(\omega) = X(\omega)}$. By [[almost sure convergence|04P7D63W8P]], $P(C) = 1$.
2. Fix $\varepsilon > 0$. For $n \ge 1$, let $A_n = \bigcup_{m \ge n} \set{\abs{X_m - X} > \varepsilon}$. Each $A_n$ is an event, as a countable union of events.
3. The sets decrease: $A_1 \supseteq A_2 \supseteq \cdots$, because the union defining $A_{n+1}$ runs over fewer indices. Let $A = \bigcap_{n \ge 1} A_n$.
4. Claim: $A \cap C = \varnothing$. Let $\omega \in C$. Since $X_m(\omega) \to X(\omega)$, there is $N$ with $\abs{X_m(\omega) - X(\omega)} \le \varepsilon$ for all $m \ge N$.
5. Then $\omega \notin A_N$, so $\omega \notin A$. This proves the claim.
6. By step 4, $A \subseteq \Omega \setminus C$. So $P(A) \le 1 - P(C) = 0$.
7. By the [[continuity of probability|0X8HBKCSYB]] from above, $P(A_n) \to P(A) = 0$.
8. For each $n$, $\set{\abs{X_n - X} > \varepsilon} \subseteq A_n$, since $m = n$ appears in the union. So $0 \le P(\abs{X_n - X} > \varepsilon) \le P(A_n)$.
9. By steps 7 and 8, $P(\abs{X_n - X} > \varepsilon) \to 0$. Since $\varepsilon > 0$ was arbitrary, $X_n \to X$ [[in probability|0EFDDXTVD6]].

## Idea

If $X_n$ is far from $X$ at time $n$, then it is far from $X$ at some time after $n$. The events "far at some time after $n$" shrink to the event "far infinitely often", which has probability $0$ when the sequence converges almost surely.
