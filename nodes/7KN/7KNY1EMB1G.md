---
tag: 7KNY1EMB1G
kind: example
name: A computable tree of positive measure with no computable path
msc: ["03B30", "03D32", "03F35"]
topics: [BY8AAFN7C5]
audience: research
instance_of: [BJQ77Y2QFX]
uses: [BJQ77Y2QFX, KPHM3025GW, XQENB067R3, X5KD3X3VJ3, DN5G4NAF95, TN9G24VABN, W9VYJRBF9N]
sources:
  - url: https://en.wikipedia.org/wiki/Algorithmically_random_sequence
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Additional systems
---

## Example

We build a [[computable|DN5G4NAF95]] tree $T \subseteq 2^{<\N}$ of positive measure, in the sense of [[WWKL0|KPHM3025GW]], such that no path of $T$ is computable.
We use a universal [[Martin-Löf test|X5KD3X3VJ3]], which we cite: a uniformly [[computably enumerable|TN9G24VABN]] sequence of open sets $U_1 \supseteq U_2 \supseteq \cdots$ of [[Cantor space|W9VYJRBF9N]] with $\mu(U_k) \le 2^{-k}$, such that a sequence is Martin-Löf random if and only if it lies outside $\bigcap_k U_k$.
Let $W$ be a computably enumerable set of strings with $U_1 = \bigcup_{\tau \in W} [\tau]$, and let $W[s]$ be the finite set of strings enumerated into $W$ by stage $s$.

1. Define $T = \set{\sigma : \text{no } \tau \in W[\abs{\sigma}] \text{ satisfies } \tau \preceq \sigma}$.
2. $T$ is computable: to decide $\sigma \in T$, run the enumeration of $W$ for $\abs{\sigma}$ stages and compare the finitely many strings found with $\sigma$.
3. $T$ is a tree. Let $\rho \preceq \sigma$ with $\rho \notin T$. Then some $\tau \in W[\abs{\rho}]$ has $\tau \preceq \rho$. Since $W[\abs{\rho}] \subseteq W[\abs{\sigma}]$ and $\tau \preceq \sigma$, also $\sigma \notin T$.
4. Fix $n$. A string $\sigma$ of length $n$ is outside $T$ exactly when $[\sigma] \subseteq [\tau]$ for some $\tau \in W[n]$. The cylinders $[\sigma]$ of these strings are pairwise disjoint subsets of $U_1$, each of measure $2^{-n}$. So their number is at most $2^n \mu(U_1) \le 2^{n-1}$.
5. So $\abs{T_n} \ge 2^n - 2^{n-1} = 2^{n-1}$, and $\abs{T_n} / 2^n \ge \tfrac{1}{2}$ for every $n$. $T$ has positive measure with $q = \tfrac{1}{2}$.
6. Let $f$ be a path of $T$, and suppose $f \in U_1$. Then $\tau \preceq f$ for some $\tau \in W$, enumerated at some stage $s$.
7. Take $n \ge \max(s, \abs{\tau})$. Then $\tau \in W[n]$ and $\tau \preceq f \upharpoonright n$, so $f \upharpoonright n \notin T$ by step 1. This contradicts that $f$ is a path, so $f \notin U_1$.
8. Hence $f \notin \bigcap_k U_k$, and $f$ is Martin-Löf random.
9. A computable sequence $g$ is not random: the sets $V_k = [g \upharpoonright k]$ form a Martin-Löf test with $\mu(V_k) = 2^{-k}$ and $g \in V_k$ for all $k$. So $f$ is not computable.

So $T$ is a computable tree of positive measure, and none of its paths is computable.
The computable sets form an $\omega$-model of $\mathsf{RCA}_0$, and $T$ is in this model without a path in it.
So this model does not satisfy $\mathsf{WWKL}$, and [[RCA0|XQENB067R3]] does not prove [[weak weak König's lemma|BJQ77Y2QFX]].

## Remarks

The same construction relative to a set $X$ uses a universal test relative to $X$.
It gives an $X$-computable tree of positive measure whose paths are all random relative to $X$.
This is the "only if" half of the characterization of the $\omega$-models of $\mathsf{WWKL}_0$: such a model contains, for each of its sets $X$, a set that is random relative to $X$.
The tree may have dead ends: a string can be in $T$ while all its long extensions leave $T$.
Weak weak König's lemma does not need a tree without dead ends.

## Explanations

### L1 human

A test for randomness lists patterns that a random sequence of coin flips should avoid.
One universal test catches every non-random sequence, and its first level forbids at most half of all sequences.
The tree keeps every start that the test has not yet forbidden.
So at least half of all starts survive at each length, and every infinite branch passes the test.
A sequence produced by a computer program fails some test, so no branch is computable.

### L2 human

The delay in step 1 matters, and a small case shows it.
Suppose the string $\tau = 01$ enters $W$ at stage $5$.

1. For $\abs{\sigma} \le 4$, the set $W[\abs{\sigma}]$ does not yet contain $01$, so the strings $01$, $010$, $0110$ stay in $T$.
2. For $\abs{\sigma} \ge 5$, every string that begins with $01$ is outside $T$.
3. So $0110$ is in $T$, but none of its extensions of length $5$ is in $T$: it is a dead end.

The typical use: this tree shows that a principle implies the existence of random sets, by a reduction to $\mathsf{WWKL}$.
The trap: the tree must be computable, so it may not use the whole set $W$, which is only computably enumerable; the stage bound $\abs{\sigma}$ makes the definition computable.

### L3 human

The tree $T$ is a computable approximation of the $\Pi^0_1$ class $2^\N \setminus U_1$, whose members are all random.
The argument shows that a $\Pi^0_1$ class of positive measure need not have a computable member, unlike a countable $\Pi^0_1$ class, which always has one.
Kučera's lemma gives the converse direction: every random set has a final segment in any $\Pi^0_1$ class of positive measure, so the random sets and the classes of positive measure determine each other.
