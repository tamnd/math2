---
tag: N3HQ3NWER5
kind: definition
name: Luenberger observer
msc: [93B53, 93C05]
defines: N1NX5VFS56
uses: [TQ7E9S194T, 6J9MPVHSMF, C4HN3EAQWM, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/State_observer
---

## Definition

Let $A \in \R^{n \times n}$, $B \in \R^{n \times m}$, $C \in \R^{p \times n}$ and $D \in \R^{p \times m}$, and consider the [[linear time-invariant system|6J9MPVHSMF]] $x' = Ax + Bu$, $y = Cx + Du$.
Let $L \in \R^{n \times p}$ be a matrix such that every [[eigenvalue|0BQAA2BK3Q]] of $A - LC$ has negative real part.
The *Luenberger observer* with gain $L$ is the system
$$\hat{x}' = A \hat{x} + B u + L \big( y - C \hat{x} - D u \big),$$
with state $\hat{x}(t) \in \R^n$, the estimate of $x(t)$.

## Remarks

The error $e = x - \hat{x}$ satisfies $e' = (A - LC) e$, so $e(t) = e^{(A - LC)t} e(0) \to 0$ for every initial error and every input.
So the Luenberger observer is a [[state observer|TQ7E9S194T]].
The eigenvalues of $A - LC$ can be prescribed arbitrarily, closed under conjugation, if and only if $(A, C)$ is [[observable|C4HN3EAQWM]].
This is pole placement for the dual pair $(A^T, C^T)$.

Example: for $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, $C = (1, 0)$, $D = 0$ and $L = (l_1, l_2)^T$,
$$A - LC = \begin{pmatrix} -l_1 & 1 \\ -l_2 & 0 \end{pmatrix}, \qquad \det(sI - (A - LC)) = s^2 + l_1 s + l_2.$$
The gain $L = (2, 1)^T$ gives $(s + 1)^2$, so it defines a Luenberger observer.

Non-example: $L = 0$ fails the eigenvalue condition for this system, since $A$ has the eigenvalue $0$; the error then satisfies $e' = Ae$ and need not tend to $0$.

The reduced-order Luenberger observer estimates only the part of the state that is not measured directly.
