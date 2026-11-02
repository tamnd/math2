---
tag: EJRP0VHGQE
kind: definition
name: Homotopy group with coefficients
msc: [55Q05, 55Q70]
defines: 8NAXJ0JH71
uses: [34SN01NWPS, P976WYEFMB, T9DG8DDE75, F2F143KQ2M]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_group_with_coefficients
---

## Definition

Let $k \ge 2$ and $n \ge 2$ be integers.
Let $P^n(k) = S^{n-1} \cup_k e^n$ be the space obtained by attaching an $n$-cell to $S^{n-1}$ along a map of degree $k$; it is a [[Moore space|34SN01NWPS]] $M(\Z/k, n - 1)$.
Let $X$ be a [[pointed space|T9DG8DDE75]].
The *$n$-th homotopy group of $X$ with coefficients in $\Z/k$* is the set of pointed [[homotopy classes|F2F143KQ2M]] of pointed maps
$$\pi_n(X; \Z/k) = [P^n(k), X]_*.$$

## Remarks

For $n \ge 3$ the space $P^n(k)$ is the suspension of $P^{n-1}(k)$, so $\pi_n(X; \Z/k)$ is a group.
For $n \ge 4$ it is a double suspension, so the group is abelian.
For $n = 2$ the set $\pi_2(X; \Z/k)$ is in general only a pointed set.

For $n \ge 3$ the cofibre sequence $S^{n-1} \xrightarrow{k} S^{n-1} \to P^n(k)$ gives a short exact sequence
$$0 \to \pi_n(X) \otimes \Z/k \to \pi_n(X; \Z/k) \to \set{x \in \pi_{n-1}(X) : kx = 0} \to 0,$$
where $\pi_n(X)$ is the ordinary [[homotopy group|P976WYEFMB]].

Example: for $X = S^n$ with $n \ge 3$, $\pi_n(S^n) \otimes \Z/k \cong \Z/k$ and $\pi_{n-1}(S^n) = 0$, so $\pi_n(S^n; \Z/k) \cong \Z/k$.

Non-example: maps from $S^n$ to $X$ do not give $\pi_n(X; \Z/k)$, since $S^n$ is not a Moore space $M(\Z/k, n-1)$; its homology in degree $n - 1$ is $0$ for $n \ge 2$, not $\Z/k$.
