---
tag: QAWDC7SWKC
kind: statement
role: theorem
name: Murray–von Neumann classification of factors
msc: [46L36, 46L10]
uses: [PSFWQVZ0FS, 1VC7EJ1ZBZ, GGDSF85JPD, 0B8KZRT28M, HM2HHE3J51, BMDG4JQPEH]
about: [PSFWQVZ0FS]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_algebra
    locator: Factors
---

## Statement

Let $M$ be a [[von Neumann algebra|PSFWQVZ0FS]] on a separable complex Hilbert space, with [[commutant|1VC7EJ1ZBZ]] $M'$.
Assume that $M$ is a factor, that is, its center $M \cap M'$ is $\C I$.
For [[orthogonal projections|0B8KZRT28M]] $p, q \in M$, write $p \sim q$ if there is a [[partial isometry|GGDSF85JPD]] $v \in M$ with $v^*v = p$ and $vv^* = q$.
Write $p \precsim q$ if $p \sim q_0$ for some projection $q_0 \in M$ with $q_0 \le q$.
Call $p$ finite if $p \sim q_0 \le p$ implies $q_0 = p$.
Then:

1. for all projections $p, q \in M$, $p \precsim q$ or $q \precsim p$;
2. there is a dimension function $D$ from the projections of $M$ to $[0, \infty]$. It is unique up to a positive scalar factor. It satisfies: $p \precsim q$ if and only if $D(p) \le D(q)$. Also $D(p + q) = D(p) + D(q)$ when $pq = 0$. And $D(p) < \infty$ if and only if $p$ is finite;
3. after normalization, the range of $D$ is exactly one of the following sets, which defines the type of $M$. The set $\set{0, 1, \dots, n}$ gives type $\mathrm{I}_n$, for $n \ge 1$. The set $\set{0, 1, 2, \dots, \infty}$ gives type $\mathrm{I}_\infty$. The interval $[0, 1]$ gives type $\mathrm{II}_1$. The interval $[0, \infty]$ gives type $\mathrm{II}_\infty$. The set $\set{0, \infty}$ gives type $\mathrm{III}$;
4. $M$ has type $\mathrm{I}_n$ or $\mathrm{I}_\infty$ if and only if $M \cong B(K)$ for a [[Hilbert space|HM2HHE3J51]] $K$ of dimension $n$ or $\aleph_0$, respectively. Here $B(K)$ is the [[algebra of bounded operators|BMDG4JQPEH]] on $K$.

## Remarks

The comparison in part 1 comes from a maximality argument.
Take a maximal family of pairwise orthogonal equivalent pieces of $p$ and $q$.
It exhausts $p$ or $q$, since otherwise, in a factor, the two remainders would contain further equivalent nonzero pieces.
The dimension function $D$ is built by cutting projections into many equivalent pieces and counting, much as a length is measured with smaller and smaller rulers.
In type $\mathrm{II}_1$, $D$ is the restriction of the unique faithful normal tracial state to the projections.

Examples: $M_n(\C)$ has type $\mathrm{I}_n$, with $D(p) = \rank p$.
The [[hyperfinite type II1 factor|NZ4NY8SK1C]] has type $\mathrm{II}_1$.
The tensor product of a type $\mathrm{II}_1$ factor with $B(\ell^2)$ has type $\mathrm{II}_\infty$.
Factors of type $\mathrm{III}$ also exist; they admit no nonzero normal semifinite trace.

The hypothesis that $M$ is a factor is needed: for the non-factor $M = \C \oplus \C$ acting diagonally on $\C^2$, the two projections $(1, 0)$ and $(0, 1)$ are not comparable, so part 1 fails.

## Explanations

### L1 human

In a factor one can compare the "sizes" of projections, like comparing the dimensions of subspaces.
Murray and von Neumann showed that this size takes values in only five kinds of ranges.
For matrices the sizes are whole numbers, as dimensions should be.
In type $\mathrm{II}_1$ factors the sizes fill the whole interval $[0,1]$, giving "continuous dimension".
In type $\mathrm{III}$ factors every nonzero projection is infinite.

### L2 human

Every von Neumann algebra on a separable Hilbert space is a direct integral of factors, so factors are the building blocks of the theory.
The classification by types is the first step; the next steps distinguish factors within one type.
Type $\mathrm{I}$ factors are completely understood by part 4.
Type $\mathrm{III}$ factors are further divided by Connes into types $\mathrm{III}_\lambda$, $0 \le \lambda \le 1$, using [[Tomita–Takesaki theory|NBR81PR7E5]].
Type $\mathrm{II}_1$ factors carry a trace and are studied through subfactors and free probability.
