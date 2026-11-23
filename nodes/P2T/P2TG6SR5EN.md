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

A bounded formula can always be checked by a search that stops: to decide $\exists y < 50 \, (y \cdot y = 49)$, you try at most $50$ values.
The question "does program $e$ halt on input $e$?" has no such bound, because nobody knows in advance how many steps to wait.
That difference is the whole reason why the halting set is not $\Delta_0$-definable.

In exact terms, let $K = \{ e \in \mathbb{N} : \text{the program with code } e \text{ halts on input } e \}$ be the halting set.
We show that $K$ is not $\Delta_0$-definable, so it is not in the [[linear-time hierarchy|FYGWNXETVJ]].

1. We claim that for every [[$\Delta_0$ formula|GE43CSZTS9]] $\theta(\bar x)$, an algorithm decides $\mathbb{N} \models \theta(\bar n)$ from $\bar n$.
   We prove it by [[structural induction|12MQ2NJ29A]] on $\theta$.
2. For an atomic $\theta$, the algorithm computes the values of the terms and compares them.
3. For $\neg \theta_1$ and $\theta_1 \land \theta_2$, it runs the algorithms for $\theta_1$ and $\theta_2$, which exist by the induction hypothesis, and combines the answers.
4. For $\exists y < t(\bar x) \, \theta_1(y, \bar x)$, it computes $m = t(\bar n)$ and runs the algorithm for $\theta_1(k, \bar n)$ for $k = 0, \dots, m - 1$.
   The search has $m$ rounds, so it stops.
5. For $\forall y < t(\bar x) \, \theta_1$, it runs the same search and asks that all answers be "yes".
6. So every $\Delta_0$-definable set is [[computable|PPGD5KW8JC]].
7. The set $K$ is not computable, by the [[undecidability of the halting problem|Z7TN2B35B0]].
8. By steps 6 and 7, no $\Delta_0$ formula defines $K$.

## Remarks

The halting set is $\Sigma_1$-definable: $e \in K$ if and only if some number codes a halting computation of program $e$ on input $e$.
So one unbounded existential quantifier is enough to leave the $\Delta_0$ sets.
If the search for a halting computation is cut off at a computable bound $b(e)$, the resulting set is computable, so the missing bound is what makes $K$ undecidable.

Watch out: the converse of step 6 is false.
A computable set can fail to be $\Delta_0$-definable, because every $\Delta_0$ set is decidable in linear space, and the space hierarchy theorem gives computable sets that need more space.
So computability is necessary for $\Delta_0$-definability, but not sufficient.

## Explanations

### L1 human

A bounded property can be checked by a search that stops after a known number of steps.
Whether a program ever stops cannot be checked this way, because nobody knows in advance how long to wait.
Turing proved that no method at all decides this question for every program.
So the halting property is not bounded.

### L2 human

We compare a bounded question with an unbounded one.
For $\theta(n) = \exists y < n + 1 \, (y \cdot y = n)$, the algorithm of step 4 tests $y = 0, 1, \dots, n$, so for $n = 10$ it makes $11$ tests and answers "no".
Now let $H(e, s)$ say that program $e$ on input $e$ halts within $s$ steps, which an algorithm decides by simulating $s$ steps.
The halting set is the projection below, and the search over $s$ has no bound given in advance:
$$K = \{ e : \exists s \, H(e, s) \}.$$
If a computable function $b$ gave a bound $s \le b(e)$ for every $e \in K$, the search would be finite and $K$ would be computable, which step 7 rules out.

The typical use of this non-example is to separate the $\Delta_0$ sets from the $\Sigma_1$ sets, the first step of the [[arithmetical hierarchy|7CVJCQKY41]].
