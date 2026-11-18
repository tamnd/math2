---
tag: P2TG6SR5EN
kind: example
name: The halting set is not Δ0-definable
msc: ["03F30", "03D10"]
topics: [RA380RWEC0]
audience: research
not_instance_of:
  - target: FYGWNXETVJ
    note: every Δ0-definable set is computable, and the halting set is not computable
uses: [FYGWNXETVJ, GE43CSZTS9, PPGD5KW8JC, Z7TN2B35B0, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Halting_problem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Rudimentary_function
    locator: lead section
---

## Example

Let $K = \set{e \in \N : \text{the program with code } e \text{ halts on input } e}$ be the halting set.
We show that $K$ is not a $\Delta_0$-definable set, so it is not in the [[linear-time hierarchy|FYGWNXETVJ]].

1. Claim: for every [[$\Delta_0$ formula|GE43CSZTS9]] $\theta(\bar x)$, an algorithm decides $\N \models \theta(\bar n)$ from $\bar n$. We prove it by [[structural induction|12MQ2NJ29A]] on $\theta$.
2. Atomic $\theta$: compute the values of the terms and compare them.
3. $\neg \theta_1$ and $\theta_1 \land \theta_2$: run the algorithms for $\theta_1$ and $\theta_2$.
4. $\exists y < t(\bar x) \, \theta_1(y, \bar x)$: compute $m = t(\bar n)$, then run the algorithm for $\theta_1(k, \bar n)$ for $k = 0, \dots, m - 1$. The search is finite.
5. $\forall y < t(\bar x) \, \theta_1$: the same search, with "all" in place of "some".
6. So every $\Delta_0$-definable set is [[computable|PPGD5KW8JC]].
7. $K$ is not computable, by the [[undecidability of the halting problem|Z7TN2B35B0]].
8. By steps 6 and 7, no $\Delta_0$ formula defines $K$.

## Remarks

The halting set is $\Sigma_1$-definable: $e \in K$ if and only if some number codes a halting computation of program $e$ on input $e$.
So one unbounded existential quantifier is enough to leave the $\Delta_0$ sets.
A computable set can also fail to be $\Delta_0$-definable: Myhill's theorem puts all $\Delta_0$ sets in linear space, and some computable sets need more space.
If the search for a halting computation is cut off at a computable bound, the resulting set is computable.
So the unbounded search is what makes $K$ undecidable.

## Explanations

### L1 human

A bounded property can be checked by a search that stops after a known number of steps.
Whether a program ever stops cannot be checked this way, because nobody knows in advance how long to wait.
Turing proved that no method at all decides this question for every program.
So the halting property is not bounded.

### L2 human

We compare a bounded and an unbounded version.

1. For $\theta(n) := \exists y < n + 1 \, (y \cdot y = n)$, the algorithm of step 4 tests $y = 0, 1, \dots, n$. For $n = 10$ it makes $11$ tests and answers "no".
2. Let $H(e, s)$ say that program $e$ on input $e$ halts within $s$ steps. An algorithm decides $H(e, s)$ by simulating $s$ steps.
3. Then $K = \set{e : \exists s \, H(e, s)}$, and the search over $s$ has no bound given in advance.
4. If some computable function $b$ gave a bound $s \le b(e)$, the search would be finite and $K$ would be computable. Step 7 of the example rules this out.

The typical use is to separate the $\Delta_0$ sets from the $\Sigma_1$ sets.
A trap is to think that every decidable set is $\Delta_0$: decidability is necessary, not sufficient.
