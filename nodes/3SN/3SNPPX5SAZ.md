---
tag: 3SNPPX5SAZ
kind: statement
role: theorem
name: Minimal realization
msc: [93B20, 93B15, 93C05]
uses: [WDVJXWV3RF, A9WFM77Z4P, C4HN3EAQWM, 9NSCZ2KBEB, 0E89HQATM8, EJVKSYHSMJ]
about: [WDVJXWV3RF]
sources:
  - url: https://en.wikipedia.org/wiki/Realization_(systems)
---

## Statement

Let $G$ be a proper $p \times m$ matrix of real rational functions.
A [[realization|WDVJXWV3RF]] $(A, B, C, D)$ of $G$ is called *minimal* if no realization of $G$ has smaller dimension.

1. A realization $(A, B, C, D)$ of $G$ is minimal if and only if the pair $(A, B)$ is [[controllable|A9WFM77Z4P]] and the pair $(A, C)$ is [[observable|C4HN3EAQWM]].
2. Let $(A_1, B_1, C_1, D_1)$ and $(A_2, B_2, C_2, D_2)$ be minimal realizations of $G$. Then they have the same dimension $n$, and $D_2 = D_1$. Moreover, there is a unique invertible $n \times n$ matrix $T$ with $A_2 = T A_1 T^{-1}$, $B_2 = T B_1$ and $C_2 = C_1 T^{-1}$; in particular $A_1$ and $A_2$ are [[similar|0E89HQATM8]].

## Remarks

If $(A, B)$ is not controllable or $(A, C)$ is not observable, the [[Kalman decomposition|EJVKSYHSMJ]] removes the uncontrollable or unobservable part and leaves a realization of the same $G$ of smaller dimension.
Conversely, all realizations of $G$ share the Markov parameters $C A^k B$, $k \ge 0$.
Let $(A, B, C, D)$ of dimension $n$ be controllable and observable.
Form its observability matrix $\mathcal{O}$ and its controllability matrix $\mathcal{C}$, both with $n$ blocks.
By the [[Kalman rank condition|9NSCZ2KBEB]], the product $\mathcal{O} \mathcal{C}$ has rank $n$.
The same product for a realization of dimension $n' < n$ has the same entries but rank at most $n'$, a contradiction.
For part 2, the matrix $T$ is obtained from the two controllability matrices as $T = \mathcal{C}_2 \mathcal{C}_1^{+}$, with $\mathcal{C}_1^{+}$ a right inverse of $\mathcal{C}_1$.

Example: for $G(s) = 1/(s + 1)$, the realization $A = \operatorname{diag}(-1, -2)$, $B = (1, 1)^T$, $C = (1, 0)$ is not minimal.
Its observability matrix has rows $C = (1, 0)$ and $CA = (-1, 0)$, of rank $1$, so $(A, C)$ is not observable, and indeed $A = -1$, $B = C = 1$ is a realization of dimension $1$.

The dimension of a minimal realization is the McMillan degree of $G$; it equals the rank of the Hankel matrix of the Markov parameters of $G$.

## Explanations

### L1 human

A transfer function can be produced by many state-space machines, some of them with useless extra parts.
A part that the input cannot reach, or a part that never shows in the output, can be thrown away without changing the behaviour.
The theorem says that once all such parts are gone the machine is as small as possible.
Moreover, all smallest machines are the same up to a change of coordinates of the state.

### L2 human

The theorem connects the input-output view of a system with the state-space view.
It is used to decide whether a model has redundant states.
It is also the basis of realization algorithms such as the Ho–Kalman algorithm, which builds a minimal realization from a factorisation of the Hankel matrix.
The uniqueness part shows that properties defined through $(A, B, C)$ and invariant under similarity, such as the eigenvalues of $A$, are properties of $G$ for minimal realizations.
In particular the eigenvalues of $A$ in a minimal realization are exactly the poles of $G$.
