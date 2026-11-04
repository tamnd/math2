---
tag: EPTH7116AX
kind: proof
name: Proof that the cumulative distribution function determines the distribution, by the π-λ theorem
msc: ["60E05"]
proves: 0JEVZAFDY6
uses: [0QB913WM5E, 0VGMEBVW1M, 0ZYBZ34RT2, 0BVHZXWKCD, 04WSW8T3SY, AQN6ZN66NK, 69460Z6DMW, BBHM1A36M7, 0464Z0JP2E, 0X8HBKCSYB, 01ZQQDCERP, 0G5AV9Q4RR, 0A3GWZ86AY, 0STX0WRDNG, 0DS9KWFDK2, 08G4XH86JC, 0ZG61TFBES]
sources:
  - url: https://en.wikipedia.org/wiki/Pi-system
---

## Proof

We show that the half-lines form a π-system that generates the Borel sets, and then apply Dynkin's π-λ theorem.

1. Let $\mu$ and $\nu$ be [[probability distributions|0QB913WM5E]] on $\R$ with its [[Borel σ-algebra|0BVHZXWKCD]] $\mathcal{B}(\R)$. Assume $\mu((-\infty, x]) = \nu((-\infty, x])$ for all $x \in \R$.
2. Let $\mathcal{P} = \set{(-\infty, x] : x \in \R}$. It is nonempty, and $(-\infty, x] \cap (-\infty, y] = (-\infty, \min(x, y)] \in \mathcal{P}$. So $\mathcal{P}$ is a [[π-system|AQN6ZN66NK]].
3. Let $\sigma(\mathcal{P})$ be the smallest [[σ-algebra|04WSW8T3SY]] on $\R$ that contains $\mathcal{P}$.
4. Each $(-\infty, x]$ is [[closed|0G5AV9Q4RR]], because its complement $(x, \infty)$ is [[open|01ZQQDCERP]]. So $(-\infty, x] \in \mathcal{B}(\R)$, and hence $\sigma(\mathcal{P}) \subseteq \mathcal{B}(\R)$.
5. Let $a < b$. Then $(a, b] = (-\infty, b] \cap (-\infty, a]^c$ lies in $\sigma(\mathcal{P})$. The same formula with $b \le a$ gives $\varnothing \in \sigma(\mathcal{P})$.
6. We claim $(a, b) = \bigcup_{n \ge 1} (a, b - 1/n]$. Each set on the right lies in $(a, b)$. If $a < x < b$, the [[Archimedean property|0A3GWZ86AY]] gives $n$ with $n (b - x) > 1$, so $x \le b - 1/n$.
7. By steps 5 and 6, every open interval $(a, b)$ with $a < b$ lies in $\sigma(\mathcal{P})$.
8. Let $U \subseteq \R$ be open. Let $J$ be the set of pairs $(q, r) \in \Q \times \Q$ with $q < r$ and $(q, r) \subseteq U$.
9. The set $\Q$ is [[countable|0DS9KWFDK2]], so $\Q \times \Q$ is [[countable|08G4XH86JC]]. An injection of $\Q \times \Q$ into $\N$ restricts to $J$, so $J$ is [[countable|0ZG61TFBES]].
10. We claim $U = \bigcup_{(q, r) \in J} (q, r)$. The inclusion $\supseteq$ holds by the choice of $J$.
11. For $\subseteq$, let $x \in U$. Since $U$ is open in $\R$, there is $\varepsilon > 0$ with $(x - \varepsilon, x + \varepsilon) \subseteq U$.
12. By the [[density of the rationals|0STX0WRDNG]], there are rationals $q$ and $r$ with $x - \varepsilon < q < x < r < x + \varepsilon$. Then $(q, r) \in J$ and $x \in (q, r)$.
13. By steps 7, 9 and 10, $U$ is a countable union of sets in $\sigma(\mathcal{P})$, or $U = \varnothing$. So $U \in \sigma(\mathcal{P})$.
14. Thus $\sigma(\mathcal{P})$ is a σ-algebra that contains every open set, so $\mathcal{B}(\R) \subseteq \sigma(\mathcal{P})$. With step 4, $\sigma(\mathcal{P}) = \mathcal{B}(\R)$.
15. Let $\mathcal{D} = \set{B \in \mathcal{B}(\R) : \mu(B) = \nu(B)}$. By the hypothesis, $\mathcal{P} \subseteq \mathcal{D}$.
16. The triples $(\R, \mathcal{B}(\R), \mu)$ and $(\R, \mathcal{B}(\R), \nu)$ are [[probability spaces|0ZYBZ34RT2]], because $\mu$ and $\nu$ are [[probability measures|0VGMEBVW1M]]. So the results on probability spaces apply to them.
17. $\R \in \mathcal{D}$, because $\mu(\R) = 1 = \nu(\R)$.
18. Let $A, B \in \mathcal{D}$ with $A \subseteq B$. By [[monotonicity of probability|0464Z0JP2E]], $\mu(B \setminus A) = \mu(B) - \mu(A) = \nu(B) - \nu(A) = \nu(B \setminus A)$. So $B \setminus A \in \mathcal{D}$.
19. Let $A_1 \subseteq A_2 \subseteq \cdots$ be sets in $\mathcal{D}$ with union $A$. By [[continuity from below|0X8HBKCSYB]], $\mu(A) = \lim_n \mu(A_n) = \lim_n \nu(A_n) = \nu(A)$. So $A \in \mathcal{D}$.
20. By steps 17 to 19, $\mathcal{D}$ is a [[Dynkin system|69460Z6DMW]] on $\R$.
21. By [[Dynkin's π-λ theorem|BBHM1A36M7]] and steps 2, 15 and 20, $\sigma(\mathcal{P}) \subseteq \mathcal{D}$.
22. By step 14, $\mathcal{B}(\R) \subseteq \mathcal{D}$. So $\mu(B) = \nu(B)$ for each Borel set $B \subseteq \R$.

## Idea

The sets on which two probability measures agree are closed under differences of nested sets and increasing unions, so they form a Dynkin system. The half-lines are closed under intersection and generate all Borel sets. Dynkin's π-λ theorem then spreads the agreement from the half-lines to all Borel sets.
