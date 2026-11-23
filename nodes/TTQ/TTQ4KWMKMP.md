---
tag: TTQ4KWMKMP
kind: proof
name: Proof that König's lemma is equivalent to ACA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
proves: 3P2J5NWCM1
uses: [DNXCKXZZ08, K9XG0Z2N9V, 3MQ39PRCYJ]
methods: [TFQ1845T84, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/K%C5%91nig%27s_lemma
    locator: Computability aspects
---

## Proof

We prove König's lemma in $\mathsf{ACA}_0$ by walking through the nodes with extensions of every length, and we prove the reversal with a tree whose only path codes the range of a one-to-one function.

### Part 1: ACA0 proves KL

1. Let $T$ be an infinite finitely branching tree.
   [[Arithmetical comprehension|K9XG0Z2N9V]] gives the set $T^* = \{ \sigma \in T : \forall m\, \exists \tau \in T\, (\sigma \subseteq \tau \wedge \lvert \tau \rvert \ge m) \}$ of nodes with extensions of every length.
2. The empty sequence is in $T^*$.
   Finite branching and induction on $m$ for an arithmetical formula show that $T$ has finitely many nodes of length at most $m$.
   So the infinite tree $T$ has nodes of every length.
3. Let $\sigma \in T^*$, and let $b$ bound the children of $\sigma$.
   Every extension $\tau \ne \sigma$ of $\sigma$ in $T$ extends some child $\sigma v$ with $v < b$.
4. Suppose that no child of $\sigma$ is in $T^*$.
   Then each child $\sigma v$ has a bound $m_v$ on the lengths of its extensions.
   Induction on $r \le b$ for an arithmetical formula gives one bound $m$ for all $v < r$, and so for all $v < b$.
5. Then no extension of $\sigma$ has length at least $\max(m, \lvert \sigma \rvert + 1)$, against $\sigma \in T^*$.
   So some child $\sigma v$ with $v < b$ is in $T^*$.
6. Define $g(k)$ as the least $v$ with $(g {\restriction} k)\, v \in T^*$, by primitive recursion relative to $T^*$.
   By induction on $k$, using step 5, we have $g {\restriction} k \in T^*$ for all $k$, so each search ends and $g$ is a path through $T$.

### Part 2: RCA0 plus KL proves ACA0

7. By the [[range lemma|3MQ39PRCYJ]], it suffices to show that every one-to-one $f \colon \mathbb{N} \to \mathbb{N}$ has a range.
   Fix $f$.
8. Let $T$ be the set of $\sigma \in \mathbb{N}^{<\mathbb{N}}$ such that, for all $i < \lvert \sigma \rvert$, two conditions hold.
   If $\sigma(i) = 0$, then $f(j) \ne i$ for all $j < \lvert \sigma \rvert$.
   If $\sigma(i) = j + 1$, then $f(j) = i$.
9. The condition is $\Sigma^0_0$ in $f$, so $T$ exists by $\Delta^0_1$ comprehension.
   If $\sigma \in T$ and $\tau \subseteq \sigma$, the conditions for $\tau$ are weaker, so $T$ is a tree.
10. $T$ is finitely branching.
    If $\sigma v \in T$, then $v = 0$ or $v = j + 1$ with $f(j) = \lvert \sigma \rvert$, and at most one $j$ has $f(j) = \lvert \sigma \rvert$ because $f$ is one-to-one.
    So $b = j + 2$ for that $j$, or $b = 1$ if there is none, is a bound.
11. $T$ is infinite.
    For each $n$ and $i < n$, let $\sigma_n(i) = j + 1$ if $j < n$ and $f(j) = i$, and $\sigma_n(i) = 0$ otherwise.
    Then $\sigma_n \in T$ and $\lvert \sigma_n \rvert = n$.
12. $\mathrm{KL}$ gives a path $g$.
    If $g(i) = j + 1$, then $f(j) = i$, by the condition on $g {\restriction} (i + 1)$.
13. If $g(i) = 0$, then $f(j) \ne i$ for every $j$.
    To see this, take $k > \max(i, j)$ and use $g {\restriction} k \in T$.
14. So $i$ is in the range of $f$ exactly when $g(i) \ne 0$, and $\Delta^0_1$ comprehension gives the range.

## Idea

The forward proof keeps to the nodes with extensions of every length, and arithmetical comprehension makes this set.
For a computable tree, the set $T^*$ is defined by a $\Pi^0_2$ formula, which is where the strength goes.
The reversal makes a tree whose nodes guess the range of $f$ together with witnesses.
A wrong guess $j + 1$ dies at once, and a wrong guess $0$ dies as soon as the length passes the true preimage.
Only the correct guesses survive to all levels, so the unique path codes the range.

## Variants

Part 2 also shows that König's lemma for trees in which each node has at most two children implies $\mathsf{ACA}_0$.
The bound $b$ in step 10 depends on whether $\lvert \sigma \rvert$ is in the range of $f$, so it is not computable from $f$.
For this reason the same tree is not an instance of [[weak König's lemma|K5YPW1NTHZ]] after recoding.
If the tree comes with a bounding function, Part 1 can be replaced by the proof of weak König's lemma for the recoded binary tree.
