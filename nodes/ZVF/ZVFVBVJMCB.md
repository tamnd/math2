---
tag: ZVFVBVJMCB
kind: statement
role: theorem
name: Montel's theorem
msc: [30D45]
uses: [QWSD2JDRP0, 0DG0Z72CQD, 0381S8Z5P0, 0JJRENWMP6, 097KNJFJ7V]
about: [JTVWRXXAKM]
sources:
  - url: https://en.wikipedia.org/wiki/Montel%27s_theorem
same_as:
  wikidata: Q535366
  wikipedia: Montel's theorem
---

## Statement

Let $U \subseteq \C$ be an open set and let $\mathcal{F}$ be a family of [[holomorphic|0DG0Z72CQD]] functions $U \to \C$.

1. Assume that $\mathcal{F}$ is locally uniformly bounded: for each compact $K \subset U$ there is $M_K$ with $\abs{f(z)} \le M_K$ for all $f \in \mathcal{F}$ and $z \in K$. Then $\mathcal{F}$ is a [[normal family|QWSD2JDRP0]].
2. Assume that $U$ is a [[domain|097KNJFJ7V]] and that there are two distinct complex numbers $a$ and $b$ that no $f \in \mathcal{F}$ takes as a value. Then each sequence in $\mathcal{F}$ has a subsequence that converges uniformly on compact subsets of $U$, either to a holomorphic function or to $\infty$.

## Remarks

Proof idea of part 1: [[Cauchy's estimates|0JJRENWMP6]] bound the derivatives uniformly on each compact set, so the family is equicontinuous there.
The [[Arzelà–Ascoli theorem|0381S8Z5P0]] on an exhausting sequence of compact sets, with a diagonal argument, gives a convergent subsequence.
Part 2, the fundamental normality test, is deeper; one proof uses the [[modular lambda function|4Z1YXT957Z]], as in the proof of [[Picard's little theorem|R2PHM118NG]].
Example: the holomorphic maps $\mathbb{D} \to \mathbb{D}$ of the unit disc form a normal family, since they are bounded by $1$.
In part 2 the limit $\infty$ cannot be excluded: the constant functions $f_n = n$ omit $0$ and $1$ for $n \ge 2$ and tend to $\infty$.
One omitted value is not enough: the functions $e^{nz}$ on $\mathbb{D}$ omit $0$, yet no subsequence converges near $0$.

## Explanations

### L1 human

Montel's theorem says that a family of holomorphic functions cannot be wild if it is bounded.
From any sequence you can always extract a subsequence that converges nicely.
For real functions this is false: $\sin(nx)$ is bounded, but no subsequence converges uniformly.
The second part says that even missing two values is enough to tame the family.

### L2 human

Part 1 is the compactness result behind existence proofs in complex analysis.
In the proof of the [[Riemann mapping theorem|02WHMEG5ZR]], one maximizes $\abs{f'(z_0)}$ over a normal family of injective maps and uses Montel to get a maximizer.
Part 2 is the basis of complex dynamics: the Fatou set of a rational map is the set where its iterates form a normal family.
It also gives a short proof of [[Picard's great theorem|08QA8QTM71]].
