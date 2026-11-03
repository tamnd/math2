---
tag: A9F03FK1BJ
kind: definition
name: Gerchberg–Saxton algorithm
msc: [78A46, 65T50]
defines: D2DJNYGS0N
uses: [TJ9XPJ65YX, 0ZZRSX91QR]
sources:
  - url: https://en.wikipedia.org/wiki/Gerchberg%E2%80%93Saxton_algorithm
---

## Definition

Let $N \ge 1$, let $\mathcal{F}$ be the unitary [[discrete Fourier transform|TJ9XPJ65YX]] on $\C^N$, and let $a, b \in [0, \infty)^N$ be given amplitudes.
For $z \in \C$, let $\operatorname{ph}(z) = z / \abs{z}$ if $z \ne 0$ and $\operatorname{ph}(0) = 1$, applied entrywise to vectors.
The *Gerchberg–Saxton algorithm* starts from a phase vector $p_0 \in \C^N$ with $\abs{(p_0)_j} = 1$ for all $j$.
For $k = 0, 1, 2, \dots$ it computes:

1. $g_k = a \odot p_k$, where $\odot$ is the entrywise product;
2. $G_k = \mathcal{F} g_k$ and $G'_k = b \odot \operatorname{ph}(G_k)$;
3. $g'_k = \mathcal{F}^{-1} G'_k$ and $p_{k+1} = \operatorname{ph}(g'_k)$.

It stops after a fixed number of steps or when the error $E_k = \norm{\abs{\mathcal{F} g_k} - b}$ is small.

## Remarks

The aim is a vector $g$ with $\abs{g} = a$ and $\abs{\mathcal{F} g} = b$ entrywise.
The map $\operatorname{ph}$ keeps the [[argument|0ZZRSX91QR]] of each entry and sets its modulus to $1$.
Each step projects onto the set of vectors with the prescribed amplitude in one of the two planes.
Since $\mathcal{F}$ is unitary, the error $E_k$ does not increase from one step to the next.
It need not tend to $0$: the iteration can stagnate at a vector that does not solve the problem.

Example: take $N = 1$, where $\mathcal{F}$ is the identity, and $a = b = (1)$.
Then $g_0 = p_0$ already satisfies both constraints, and $E_0 = 0$.

Non-example: for $N = 1$ with $a = (1)$ and $b = (2)$, no vector satisfies both constraints, and the iterates stay at error $E_k = 1$.
So a run of the algorithm does not certify that a solution exists.
