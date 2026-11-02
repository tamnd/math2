---
tag: TMEKPXMC7V
kind: statement
role: theorem
name: Separation principle
msc: ["93E20", 49N10, "93E11"]
uses: [DJB8MAV5BH, HR720TJZZR, Y4V154JWR7, 0TTDGTEFMN]
about: [DJB8MAV5BH]
sources:
  - url: https://en.wikipedia.org/wiki/Separation_principle
same_as:
  wikidata: Q2271572
  wikipedia: Separation principle
---

## Statement

Consider the [[linear-quadratic-Gaussian control problem|DJB8MAV5BH]] on $[0, T]$ with matrices $A, B, C, Q, R, F$, noise covariances $\Xi$ and $\Theta$, and initial mean $m_0$ and covariance $\Sigma_0$.
Let $P$ solve the [[Riccati differential equation|Y4V154JWR7]] $-P' = A^{T} P + P A - P B R^{-1} B^{T} P + Q$ with $P(T) = F$.
Let $\Sigma$ solve the filter Riccati equation $\Sigma' = A \Sigma + \Sigma A^{T} + \Xi - \Sigma C^{T} \Theta^{-1} C \Sigma$ with $\Sigma(0) = \Sigma_0$.
Let $\hat{x}$ be the Kalman–Bucy filter, the solution of
$$d\hat{x} = (A \hat{x} + B u) \, dt + \Sigma C^{T} \Theta^{-1} (dy - C \hat{x} \, dt), \qquad \hat{x}(0) = m_0.$$
Then the control $u^*(t) = -R^{-1} B^{T} P(t) \hat{x}(t)$ is admissible and optimal among all admissible controls.
Here $\hat{x}(t)$ is the [[conditional expectation|0TTDGTEFMN]] of $x(t)$ given the observations $y(s)$, $s \le t$.

## Remarks

The proof has two parts.
First, for every admissible control, the error $x - \hat{x}$ is a Gaussian process whose law does not depend on $u$, with covariance $\Sigma(t)$.
Second, writing $x = \hat{x} + (x - \hat{x})$ splits the cost into a term that does not depend on $u$ and the cost of a fully observed linear-quadratic problem for $\hat{x}$.
The [[linear-quadratic regulator|HR720TJZZR]] then gives the optimal feedback for $\hat{x}$.
The gain $R^{-1} B^{T} P$ is the same as without noise, and the filter gain $\Sigma C^{T} \Theta^{-1}$ does not depend on the cost: estimation and control separate.
A deterministic version holds for observer-based feedback of $x' = A x + B u$, $y = C x$.
With the observer $\hat{x}' = A \hat{x} + B u + L(y - C \hat{x})$ and $u = -K \hat{x}$, the error $e = x - \hat{x}$ solves $e' = (A - L C) e$.
In the coordinates $(x, e)$ the closed-loop matrix is block triangular, so its eigenvalues are those of $A - B K$ together with those of $A - L C$.
The principle depends on linear dynamics, Gaussian noise and quadratic cost; for nonlinear problems the best control may need to act so as to improve future estimates.

## Explanations

### L1 human

When you must control a system that you can only observe through noisy measurements, the separation principle gives a simple recipe.
First build the best estimate of the current state from the measurements.
Then apply the control that would be optimal if that estimate were exactly right.
For linear systems with Gaussian noise and quadratic costs, this two-step recipe is exactly optimal.

### L2 human

The estimator is the Kalman–Bucy filter and the controller is the [[linear-quadratic regulator|HR720TJZZR]] gain, and each comes from its own Riccati equation.
The two Riccati equations are dual: the filter equation is the control equation for $(A^{T}, C^{T})$ run forward in time.
In practice this lets engineers design the estimator and the controller separately.
The deterministic version is the reason why pole placement for the controller and for the observer can be done independently.
