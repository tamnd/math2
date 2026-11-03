---
tag: SCY6X79XVP
kind: statement
role: theorem
name: Pole placement theorem
msc: [93B55, 93B52, 93C05]
uses: [AWDQ3ES2S3, A9WFM77Z4P, 9NSCZ2KBEB, 0VSSPAFM2C, 0BQAA2BK3Q, EJVKSYHSMJ]
about: [AWDQ3ES2S3, A9WFM77Z4P]
sources:
  - url: https://en.wikipedia.org/wiki/Full_state_feedback
---

## Statement

Let $A \in \R^{n \times n}$ and $B \in \R^{n \times m}$.
The following are equivalent.

1. The pair $(A, B)$ is [[controllable|A9WFM77Z4P]].
2. For every monic real polynomial $p$ of degree $n$, some [[full state feedback|AWDQ3ES2S3]] gain $K \in \R^{m \times n}$ makes $p$ the [[characteristic polynomial|0VSSPAFM2C]] of $A - BK$.

Equivalently, let $(A, B)$ be controllable and let $\Lambda$ be a list of $n$ complex numbers, with multiplicities, that is closed under complex conjugation.
Then $\Lambda$ is the list of [[eigenvalues|0BQAA2BK3Q]] of $A - BK$ for some real $K$.

## Remarks

For $m = 1$, controllability lets one change coordinates to the controllable canonical form, in which $A$ is a companion matrix and $B = e_n$.
There $A - BK$ is again a companion matrix whose last row is the last row of $A$ minus $K$.
So its characteristic polynomial can be made equal to any $p$, and $K$ is unique.
For $m > 1$, one first finds a feedback $u = -K_0 x + g w$ that makes the system controllable from the single input $w$, and then applies the case $m = 1$.
If $(A, B)$ is not controllable, the [[Kalman decomposition|EJVKSYHSMJ]] shows that the eigenvalues of the uncontrollable part are eigenvalues of $A - BK$ for every $K$, so 2 fails.

Example: for $x_1' = x_2$, $x_2' = u$, the gain $K = (k_1, k_2)$ gives the characteristic polynomial $s^2 + k_2 s + k_1$, which equals any prescribed $s^2 + a_1 s + a_0$ for $K = (a_0, a_1)$.
For $A = \operatorname{diag}(1, 2)$ and $B = (1, 0)^T$, the pair is not controllable, and $2$ is an eigenvalue of $A - BK$ for every $K$, since the second row of $A - BK$ is $(0, 2)$.

## Explanations

### L1 human

The eigenvalues of the closed loop decide how fast and in what manner a controlled system settles: slowly or quickly, with or without oscillation, or not at all.
The theorem says that if every part of the system can be influenced by the input, then feedback of the state can give the closed loop any eigenvalues we want.
If some part cannot be influenced, its behaviour stays as it is, whatever feedback is used.

### L2 human

The theorem shows that [[controllability|A9WFM77Z4P]], checked by the [[Kalman rank condition|9NSCZ2KBEB]], is exactly the condition for arbitrary eigenvalue assignment.
In particular a controllable system can always be stabilised by a linear state feedback; the weaker condition that only the unstable part be controllable is stabilisability.
For a single input the gain is unique and is given by Ackermann's formula.
By duality, applied to $(A^T, C^T)$, the eigenvalues of $A - LC$ can be assigned arbitrarily exactly when $(A, C)$ is observable, which is the basis of observer design.
