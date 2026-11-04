---
tag: J9J2RW0BFN
kind: proof
name: Proof of the intercept theorem with vectors
msc: [51M04]
proves: 0M1GFS6PVA
uses: [0MP9BCF6DP, 0NPPGHQNXQ, 0XKBKGTCPC, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Intercept_theorem
    locator: Scalar multiplication in vector spaces
---

## Proof

We write all points with vectors from $S$ and compare coefficients.

1. Two distinct [[lines|0MP9BCF6DP]] meet in at most one point, because exactly one line passes through two distinct points. So $\ell_1 \cap \ell_2 = \set{S}$.
2. Write $\ell_1 = \set{P_0 + \tau w : \tau \in \R}$ with $w \neq 0$. Then $S = P_0 + \tau_1 w$ and $A = P_0 + \tau_2 w$ with $\tau_1 \neq \tau_2$, since $A \neq S$.
3. Let $p = A - S = (\tau_2 - \tau_1) w \neq 0$. Each point $P_0 + \tau w$ equals $S + \frac{\tau - \tau_1}{\tau_2 - \tau_1} p$. So $\ell_1 = \set{S + \sigma p : \sigma \in \R}$.
4. In the same way, with $q = C - S \neq 0$, we get $\ell_2 = \set{S + \sigma q : \sigma \in \R}$.
5. The vectors $p$ and $q$ are [[linearly independent|0CRMGPAH83]]. Otherwise $q = \mu p$ for a real $\mu$, so $C \in \ell_1$. Then $C \in \ell_1 \cap \ell_2$ and $C \neq S$, against step 1.
6. By steps 3 and 4, $B = S + s p$ and $D = S + t q$ for real numbers $s$ and $t$. Since $B \neq S$ and $D \neq S$, we have $s \neq 0$ and $t \neq 0$.
7. By step 5, $C - A = q - p \neq 0$ and $D - B = t q - s p \neq 0$. So $C - A$ and $D - B$ are direction vectors of the lines $AC$ and $BD$.
8. Two lines are parallel when they have the same direction vectors, up to a nonzero factor. So $D - B = \mu (C - A)$ for a real $\mu$.
9. Step 8 says $t q - s p = \mu q - \mu p$, that is $(t - \mu) q + (\mu - s) p = 0$. By step 5, $t = \mu$ and $s = \mu$. So $s = t$.
10. With the [[Euclidean distance|0NPPGHQNXQ]] and the [[length|0XKBKGTCPC]], $\abs{SB} = \norm{s p} = \abs{s} \, \abs{SA}$ and $\abs{SD} = \norm{s q} = \abs{s} \, \abs{SC}$.
11. Also $\abs{BD} = \norm{s q - s p} = \abs{s} \, \norm{q - p} = \abs{s} \, \abs{AC}$.
12. All of $\abs{SB}$, $\abs{SD}$ and $\abs{BD}$ are positive, by steps 6 and 7. Dividing, each of the three quotients $\frac{\abs{SA}}{\abs{SB}}$, $\frac{\abs{SC}}{\abs{SD}}$ and $\frac{\abs{AC}}{\abs{BD}}$ equals $\frac{1}{\abs{s}}$.
13. Hence $\dfrac{\abs{SA}}{\abs{SB}} = \dfrac{\abs{SC}}{\abs{SD}} = \dfrac{\abs{AC}}{\abs{BD}}$.

## Idea

From $S$, the points $B$ and $D$ are multiples $s p$ and $t q$ of the vectors to $A$ and $C$. The parallel condition forces $s = t$, because $p$ and $q$ point in independent directions. So one scaling by $s$ maps $A$, $C$ to $B$, $D$, and every length scales by $\abs{s}$.
