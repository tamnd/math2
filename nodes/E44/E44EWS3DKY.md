---
tag: E44EWS3DKY
kind: definition
name: State observer
msc: [93B53, 93C05]
defines: TQ7E9S194T
uses: [6J9MPVHSMF, C4HN3EAQWM, PE9HCFHXB5]
sources:
  - url: https://en.wikipedia.org/wiki/State_observer
---

## Definition

Let $A \in \R^{n \times n}$, $B \in \R^{n \times m}$ and $C \in \R^{p \times n}$, and consider the [[linear time-invariant system|6J9MPVHSMF]] $x' = Ax + Bu$ with measured output $y = Cx$.
Let $q \ge 0$, and let $F, G, H, M, N$ be constant real matrices of matching sizes.
Consider the linear system
$$z' = F z + G y + H u, \qquad \hat{x} = M z + N y,$$
with state $z(t) \in \R^q$.
It is a *(linear asymptotic) state observer* if
$$\lim_{t \to \infty} \big( \hat{x}(t) - x(t) \big) = 0$$
for all initial states $x(0) \in \R^n$, $z(0) \in \R^q$ and every locally integrable input $u$.
The signal $\hat{x}$ is the *state estimate*.

## Remarks

The observer uses only the signals $u$ and $y$, never $x$ itself.
A linear state observer exists if and only if the pair $(A, C)$ is [[detectable|PE9HCFHXB5]], that is, every unstable mode is visible in the output.
In particular it exists when $(A, C)$ is [[observable|C4HN3EAQWM]].
The standard choice $q = n$, $F = A - LC$, $G = L$, $H = B$, $M = I$, $N = 0$ is the Luenberger observer.

Example: for $x_1' = x_2$, $x_2' = u$, $y = x_1$, the system $z' = Az + Bu + L(y - Cz)$ with $L = (2, 1)^T$ and $\hat{x} = z$ is an observer.
The error $e = x - z$ satisfies $e' = (A - LC)e$ with $A - LC = \begin{pmatrix} -2 & 1 \\ -1 & 0 \end{pmatrix}$, whose characteristic polynomial is $(s + 1)^2$, so $e(t) \to 0$.

Non-example: the open-loop copy $z' = Az + Bu$, $\hat{x} = z$ of the same system is not an observer.
Its error satisfies $e' = Ae$, and for $e(0) = (1, 0)^T$ the error stays $(1, 0)^T$ for all time.

Observers are also defined for nonlinear systems, with the same convergence requirement.
