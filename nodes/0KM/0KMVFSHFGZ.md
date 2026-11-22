---
tag: 0KMVFSHFGZ
kind: statement
role: theorem
name: Strong induction
aliases: [complete-induction, course-of-values-induction]
msc: ["03F30", "00A35"]
topics: [EEH2F76CYQ]
audience: school
about: [0ASJVEFA9J, 0MWKJ44V5A]
uses: [0ASJVEFA9J, 0Y9H52BT03]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Complete (strong) induction
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Equivalence with ordinary induction
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Statement

Strong induction lets a proof of the case $n$ use every earlier case, and not only the case $n - 1$.

Let $P(n)$ be a property of [[natural numbers|0MWKJ44V5A]] $n$, and let $<$ be the usual [[order on the natural numbers|0Y9H52BT03]].
Suppose that for each natural number $n$ the following holds: if $P(k)$ holds for every natural number $k < n$, then $P(n)$ holds.
Then $P(n)$ holds for every natural number $n$.

The hypothesis is the *strong induction step*, and the assumption "$P(k)$ for every $k < n$" is the *strong induction hypothesis*.

## Remarks

### A first proof by strong induction

Here is the theorem that shows why the method exists: every integer $n \ge 2$ has a prime factor.
Let $n \ge 2$, and assume that every integer $k$ with $2 \le k < n$ has a prime factor.
If $n$ is prime, then $n$ itself is a prime factor of $n$.
If $n$ is not prime, then $n = ab$ with $1 < a < n$.
The hypothesis applies to $a$, so some prime $p$ divides $a$, and then $p$ also divides $n = ab$.
In both cases $n$ has a prime factor, so strong induction from the base $2$ proves the theorem.

Look at the case $n = 2$.
No integer $k$ satisfies $2 \le k < 2$, so the hypothesis gives nothing, and the proof must handle $2$ with no help.
It does, because $2$ is prime and the first case applies.
Check with a number: for $n = 91 = 7 \cdot 13$ the proof uses the case $a = 7$, which is far below $90$.
Ordinary [[induction|0ASJVEFA9J]] would give us only the case $90$, and a prime factor of $90$ says nothing about $91$.
The same idea, applied to both factors, shows that [[every integer above 1 is a product of primes|818MZC1FYJ]].
The [[minimal counterexample|JGRCNPKNGG]] method gives [[the same prime factor theorem|VSHHBWWXVX]] in another form.

### Why the method is valid

Strong induction is ordinary induction applied to a stronger property.
Let $Q(n)$ say "$P(k)$ holds for every $k < n$".
Then $Q(0)$ holds because there is no $k < 0$.
If $Q(n)$ holds, the strong step gives $P(n)$, and together these give $Q(n + 1)$, because the numbers below $n + 1$ are the numbers below $n$ and $n$ itself.
So ordinary induction proves $Q(n)$ for every $n$, and the strong step turns each $Q(n)$ into $P(n)$.
The [[proof from ordinary induction|C54QYDXFP3]] writes this out from the Peano axioms.

### No separate base case, but zero still counts

The statement has no base case, and that is not a mistake.
For $n = 0$ the strong hypothesis is empty, so the step itself must prove $P(0)$ with no assumptions.
In practice the general argument often fails for the smallest values of $n$, and those values are then proved on their own.
They are written as base cases, but logically they are parts of the step.

### Other forms

The method starts at any base $n_0$: if for each $n \ge n_0$ the cases $P(k)$ with $n_0 \le k < n$ give $P(n)$, then $P(n)$ holds for all $n \ge n_0$.
To see this, apply the statement to $R(m) = P(n_0 + m)$.

A step that reaches back $j$ places needs $j$ base cases.
Suppose $P(n_0), \ldots, P(n_0 + j - 1)$ hold, and for each $n \ge n_0 + j$ the cases $P(n - j), \ldots, P(n - 1)$ give $P(n)$.
Then $P(n)$ holds for all $n \ge n_0$, since each $n$ is a base case or at least $n_0 + j$.
[[Postage with stamps of 4 and 5 cents|HQQGKAXCSW]] reaches back four places and has four base cases, and the [[bound $F_n < 2^n$|3ZDPCTKC9M]] reaches back two places and has two.

In the language of sets the statement reads: if $A \subseteq \mathbb{N}$ and, for each $n$, $\{k : k < n\} \subseteq A$ implies $n \in A$, then $A = \mathbb{N}$.

### When to choose it

Choose strong induction when the reduction of the case $n$ lands on a smaller case whose position you cannot predict.
A factor of $n$, the number $n - 2^m$, or the pieces of a split all have this property.
When the reduction always lands on $n - 1$, ordinary induction is enough and reads more simply.

### Why each hypothesis is needed

The step must hold at $n = 0$.
The property "$n \ge 1$" satisfies the step at every $n \ge 1$, because it is true there, and it fails at $0$.

The step must hold at every $n$, not only from some point on.
The property "$n \ne 5$" satisfies the step at every $n \ne 5$, and it fails at $5$.

The hypothesis may use only cases $k < n$.
An argument that proves $P(n)$ from $P(n + 1)$ proves nothing, because the chain of cases never reaches a starting point.
[[Upward recursion|CCNEXYJDC0]] shows the same failure for definitions.

### Strong is not stronger

Ordinary induction is a special case, because its step uses only $P(n - 1)$, one of the cases $k < n$.
Conversely, the argument above derives strong induction from ordinary induction.
So the two principles prove exactly the same theorems, and together with the [[well-ordering principle|01BX15HSRR]] they are equivalent; the [[equivalence of induction and well-ordering|J2P9FWBP3Q]] names the base theory.
The word "strong" describes what a proof may assume, not what it can prove.
The well-ordering principle itself follows from strong induction by the [[proof with the property $n \notin A$|QPX5Z5YFH8]], and [[infinite descent|0EFYCFHYFG]] is strong induction in contrapositive form.

### Watch out

A step that uses two earlier cases needs two base cases.
Suppose a proof of $F_n < 2^n$ uses $F_n = F_{n - 1} + F_{n - 2}$ and checks only $F_0 = 0 < 1$.
For $n = 1$ the step would need $F_{-1}$, which does not exist, so $P(1)$ is left unproved.
The correct move is to check $F_1 = 1 < 2$ as a second base case and to run the step from $n = 2$.
A step that splits $n$ as $a + b$ with $a, b < n$ fails at $n = 1$ in the same way, and the [[false proof that $2n = 0$|32AP5ZDMJJ]] uses exactly that gap.

### Names and Lean

"Strong induction", "complete induction", "course-of-values induction" and "the second principle of induction" all name this statement.
Ordinary induction is then called "weak induction" or "the first principle".
Mathlib states strong induction on $\mathbb{N}$ as `Nat.strong_induction_on`, and the tactic `induction n using Nat.strong_induction_on with n ih` starts a proof of this form.

### Try it

First, prove by strong induction that every $n \ge 1$ can be written as $2^a \cdot m$ with $m$ odd.
If $n$ is odd, take $a = 0$ and $m = n$; if $n$ is even, apply the hypothesis to $n / 2 < n$ and raise $a$ by one.

Second, which base cases does a step from $n - 3$ to $n$ need when the claim starts at $n_0 = 8$?
It needs $8$, $9$ and $10$, because those are the values whose case $n - 3$ lies below $8$.

## History

Strong induction developed together with ordinary [[induction|0ASJVEFA9J]], and textbooks present it as a variant of that method rather than as a separate discovery.

## Explanations

### L1 human

In ordinary induction, the proof for a number may use only the number just before it.
In strong induction, it may use all the numbers before it.
This helps when a number breaks into smaller pieces that are not "one less".
For example, $12 = 3 \times 4$, and facts about $3$ and $4$ can give the fact about $12$.
By the time we reach $12$, every number below $12$ is already settled, so we may use any of them.

### L2 human

We prove that every natural number $n \ge 1$ is a sum of distinct powers of $2$.
Let $n \ge 1$, and assume the claim for every $k$ with $1 \le k < n$.
Let $2^m$ be the largest power of $2$ with $2^m \le n$, so that $n < 2^{m + 1}$.
If $n = 2^m$, the sum has one term, and we are done.
Otherwise put $k = n - 2^m$, which satisfies $1 \le k < n$, so $k$ is a sum of distinct powers of $2$.
Also $k < 2^{m + 1} - 2^m = 2^m$, so every power in the sum for $k$ is less than $2^m$.
Then $n = 2^m + k$ is a sum of distinct powers of $2$.
For example, with $n = 13$:
$$13 = 8 + 5, \qquad 5 = 4 + 1, \qquad 13 = 8 + 4 + 1.$$
Check: $8 + 4 + 1 = 13$, and the three powers are distinct.

The case used is $n - 2^m$, whose distance from $n$ changes with $n$, and that is the typical reason to choose strong induction.
Watch out: without the bound $k < 2^m$, the power $2^m$ could appear twice, and the sum would not be a sum of distinct powers.

### L3 human

Strong induction on $\mathbb{N}$ is the special case of well-founded induction for the relation $<$.
For any well-founded relation $R$ on a set $X$, if each $x$ has property $P$ whenever all its $R$-predecessors have it, then every element of $X$ has $P$; Mathlib states this as `WellFounded.induction`.
This includes induction over $\mathbb{N} \times \mathbb{N}$ in [[lexicographic order|0B68KNPGCG]], [[structural induction|12MQ2NJ29A]] over trees, and transfinite induction over the ordinals.
In computability theory the same pattern defines functions by course-of-values recursion, where $f(n)$ may depend on all the values $f(0), \ldots, f(n - 1)$.
In type theory strong induction is derived from the recursor `Nat.rec` of the natural numbers, by the same stronger property $Q(n)$ as above.
