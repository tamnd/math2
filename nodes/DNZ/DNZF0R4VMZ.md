---
tag: DNZF0R4VMZ
kind: counterexample
name: The finitely supported sequences in l2 are not complemented by their orthogonal complement
msc: [46C05, 15A63]
topics: [8GQVME4SZZ]
audience: ug2
uses: [079D68S3AW, 08P6T2WH6R, 0QEAJB91GZ, T5Q51M5BAK]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_space
    locator: Orthogonal complements and projections
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Properties
---

## Counterexample

Let $\ell^2$ be the space of real sequences $x = (x_1, x_2, \dots)$ with $\sum_n x_n^2 < \infty$, with the inner product $\ip{x}{y} = \sum_n x_n y_n$, as in [[the sequence spaces|08P6T2WH6R]].
Let $c_{00}$ be the set of sequences with only finitely many nonzero entries, and let $e_n$ be the sequence with $1$ in place $n$ and $0$ elsewhere.
We show that $\ell^2 \ne c_{00} \oplus c_{00}^\perp$ and that $(c_{00}^\perp)^\perp \ne c_{00}$.

1. The set $c_{00}$ is a subspace of $\ell^2$. A finitely supported sequence has a finite sum of squares, $0 \in c_{00}$, and a linear combination of two finitely supported sequences is finitely supported.
2. Each $e_n$ lies in $c_{00}$, since it has one nonzero entry.
3. Let $x \in c_{00}^\perp$. Then $x_n = \ip{x}{e_n} = 0$ for every $n$, by step 2. So $x = 0$, and $c_{00}^\perp = \{0\}$.
4. Hence $c_{00} + c_{00}^\perp = c_{00}$.
5. Let $y = (1, \tfrac{1}{2}, \tfrac{1}{3}, \dots)$, so $y_n = 1/n$. The series $\sum_n 1/n^2$ converges, so $y \in \ell^2$. Every entry of $y$ is nonzero, so $y \notin c_{00}$.
6. By steps 4 and 5, $c_{00} + c_{00}^\perp \ne \ell^2$. So the [[orthogonal decomposition|0SP7P0G7KQ]] fails for $c_{00}$.
7. By step 3 and part 6 of the [[basic properties|T5Q51M5BAK]], $(c_{00}^\perp)^\perp = \{0\}^\perp = \ell^2$. By step 5 this is not $c_{00}$, so the [[double orthogonal complement|0PXN9G4MX1]] formula fails too.
8. The subspace $c_{00}$ is not closed. Let $y^{(N)} = (1, \tfrac{1}{2}, \dots, \tfrac{1}{N}, 0, 0, \dots)$, which lies in $c_{00}$. Then $\norm{y - y^{(N)}}^2 = \sum_{n > N} 1/n^2$ is the tail of a convergent series, so it tends to $0$, and $y$ lies in the [[closure|0QEAJB91GZ]] of $c_{00}$ but not in $c_{00}$.

## Remarks

The space $c_{00}$ is infinite-dimensional, so the hypothesis "$U$ is finite-dimensional" of the decomposition theorem fails.
The same truncation as in step 8 works for every $x \in \ell^2$, so the closure of $c_{00}$ is all of $\ell^2$.
That agrees with the rule $(U^\perp)^\perp = \overline{U}$ in a Hilbert space.

Why is closedness the exact condition?
Each set $S^\perp$ is closed, because $x \mapsto \ip{x}{s}$ is continuous, so a subspace with $U = (U^\perp)^\perp$ must be closed.
Now suppose that $V = U \oplus U^\perp$, take $x \in (U^\perp)^\perp$, and write $x = u + u'$ with $u \in U$ and $u' \in U^\perp$.
Then $u' = x - u$ lies in $(U^\perp)^\perp$, since $U \subseteq (U^\perp)^\perp$, and also in $U^\perp$, so $\ip{u'}{u'} = 0$ and $x = u$.
So the decomposition forces $U = (U^\perp)^\perp$, and hence forces $U$ to be closed.
Conversely, for a closed $U$ the [[Hilbert projection theorem|J5YNTHQMFX]] gives a closest point of $U$ to each $v$, and $v$ minus that point lies in $U^\perp$.

## Explanations

### L1 human

In infinite dimension a subspace can be so large that no nonzero vector is at a right angle to it, and still not fill the whole space.
The sequences that stop after finitely many terms form such a subspace inside $\ell^2$.
The sequence $1, \tfrac{1}{2}, \tfrac{1}{3}, \dots$ never stops, so it is not in the subspace, and yet it is not at a right angle to the subspace either.

### L2 human

The proof of the finite-dimensional theorem breaks at one step: $c_{00}$ has no finite orthonormal basis.
The natural guess for the part of $y$ in $c_{00}$ is $\sum_n \ip{y}{e_n} e_n$, and that infinite sum is $y$ itself, which lies outside $c_{00}$.
So the would-be projection leaves the subspace.
Watch out: in finite dimension every subspace is closed, but in infinite dimension many subspaces are not, and the theorems about complements need closedness there.
