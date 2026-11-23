---
tag: DBDNYXA7ME
kind: statement
role: theorem
name: Hennessy-Milner theorem
msc: ["03B45", "68Q85"]
topics: [SPQVNPZDTB]
audience: grad
uses: [7T740SFHHV, TKFFTAX30E, NGHWZ9Y7ZV]
about: [X27BR4YP2Y, C3RZY20ETK]
proofs: [Y79T9EYZ2G]
history:
  first_stated: "Hennessy and Milner, 1980, On observing nondeterminism and concurrency (ICALP)"
  notes: "Journal version: Algebraic laws for nondeterminism and concurrency, Journal of the ACM, 1985. Stated for labeled transition systems and Hennessy-Milner logic."
sources:
  - url: https://en.wikipedia.org/wiki/Hennessy%E2%80%93Milner_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: Bisimulation and modal logic
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Statement

Let $w$ have two successors, $v_1$ with $p$ true and $v_2$ with $q$ true, and let $w'$ have one successor $v'$ with only $p$ true.
Spoiler's move from $w$ to $v_2$ has no good answer, because $v'$ fails $q$, and that failure turns into the formula $\lozenge q$, true at $w$ and false at $w'$.
The Hennessy-Milner theorem says that this always happens when each world has finitely many successors: if no formula separates two worlds, they are bisimilar.

Let $\mathfrak{M} = (W, R, V)$ and $\mathfrak{M}' = (W', R', V')$ be Kripke models, as in [[Kripke semantics|NGHWZ9Y7ZV]].
Write $w \equiv w'$ when $\mathfrak{M}, w$ and $\mathfrak{M}', w'$ satisfy the same basic modal formulas.
A model is *image-finite* if every world has only finitely many successors.
A model is *modally saturated* (m-saturated) if the following holds for every world $w$ and every set $\Sigma$ of modal formulas.
If every finite subset of $\Sigma$ is true at some successor of $w$, then all of $\Sigma$ is true at some successor of $w$.

1. If $\mathfrak{M}$ and $\mathfrak{M}'$ are image-finite, then for all $w \in W$ and $w' \in W'$, $w \equiv w'$ if and only if $w \mathrel{\underline{\leftrightarrow}} w'$.
2. If $\mathfrak{M}$ and $\mathfrak{M}'$ are m-saturated, then for all $w \in W$ and $w' \in W'$, $w \equiv w'$ if and only if $w \mathrel{\underline{\leftrightarrow}} w'$.

In both cases the relation $\equiv$ is itself a [[bisimulation|7T740SFHHV]] when it is nonempty.
The direction from bisimilarity to $\equiv$ is [[bisimulation invariance|TKFFTAX30E]], which holds for all models.

## Remarks

### Why image-finiteness is needed

Without image-finiteness, two worlds can agree on every formula and still fail to be bisimilar.
Let every variable be false everywhere.
Let $\mathfrak{M}$ have a root $r$ and, for each $n \geq 1$, a path $r R a^n_1 R a^n_2 R \cdots R a^n_n$, all these worlds distinct.
Let $\mathfrak{M}'$ have a root $r'$ with the same paths $r' R' b^n_1 R' \cdots R' b^n_n$, plus one path $r' R' c_1 R' c_2 R' c_3 \cdots$ that never ends.
Let $h(x) \in \mathbb{N} \cup \{\infty\}$ be the supremum of the lengths of paths that start at $x$.
So $h(a^n_k) = h(b^n_k) = n - k$, and $h(c_k) = \infty$.

First, the roots agree on all formulas.
By induction on $d$, two non-root worlds $x$, $y$ with $\min(h(x), d) = \min(h(y), d)$ agree on all formulas of depth at most $d$.
For $d = 0$ there is nothing to check, since all variables are false.
For the step, either both worlds have no successor, or both have a unique successor, and the successors satisfy the same condition for $d$.
At the roots, each successor $b^n_1$ of $r'$ is matched by $a^n_1$, and $c_1$ is matched, up to depth $d$, by $a^{d+1}_1$.
So $r$ and $r'$ agree on formulas of every depth, and $r \equiv r'$.

### Why image-finiteness is needed, continued

Second, the roots are not bisimilar.
A world $x$ with $h(x)$ finite is never bisimilar to any $c_k$, by induction on $h(x)$.
If $h(x) = 0$, the move $c_k R' c_{k+1}$ has no answer.
If $h(x) = j + 1$, any answer $x'$ has $h(x') \leq j$, and $x'$ is not bisimilar to $c_{k+1}$ by induction.
So a bisimulation containing $(r, r')$ would have to answer $r' R' c_1$ with some $a^n_1$ bisimilar to $c_1$, which is impossible.

In item 2, saturation cannot be dropped, for the same reason.
At $r$, every finite part of $\Sigma = \{\square^n \lozenge \top : n \in \mathbb{N}\}$ holds at a successor $a^n_1$ with $n$ large, but no successor satisfies all of $\Sigma$, so $\mathfrak{M}$ is not m-saturated.

### What it gives you

On finite models, modal equivalence and bisimilarity coincide.
So the largest bisimulation of a finite model can be computed by partition refinement, and two finite models can be compared in polynomial time.
Every image-finite model can be shrunk to its bisimulation contraction, the quotient by $\equiv$, without changing the theory of any world.
The m-saturated form is the step that the [[van Benthem characterization theorem|Y89MGMWE4H]] needs.

### The converse

Image-finiteness is sufficient, not necessary.
A root with infinitely many successors, none of which has a successor or a true atom, is not image-finite, and there $\equiv$ is still a bisimulation.

### Generalizations

For labeled transition systems the theorem holds for Hennessy-Milner logic, with one modality $\langle a \rangle$ for each action $a$.
Without any finiteness condition, modal equivalence in the infinitary language with arbitrary conjunctions coincides with bisimilarity on all models.
The m-saturated version applies in particular to $\omega$-saturated first-order structures read as Kripke models.

## History

Matthew Hennessy and Robin Milner proved the theorem for labeled transition systems and the logic now called Hennessy-Milner logic, in a paper at ICALP 1980.
The journal version appeared in the Journal of the ACM in 1985.

## Explanations

### L1 human

Compare two machines that offer only finitely many choices at each step, using tests.
A test is a finite question such as "can you take a step and then do two different things".
The theorem says that two such machines pass the same tests exactly when each can copy the other step by step forever.
If one machine can do something the other cannot copy, some finite test catches it.

### L2 human

Let us extract a separating formula from a failed copy, for the worlds $w$ and $w'$ of the opening.
Spoiler plays $w R v_2$, and the only answer is $v'$.
The worlds $v_2$ and $v'$ differ on $q$, so $\psi = q$ is true at $v_2$ and false at every successor of $w'$.
Then
$$\mathfrak{M}, w \models \lozenge q \qquad \text{and} \qquad \mathfrak{M}', w' \not\models \lozenge q.$$
If $w'$ had several successors $v'_1, \ldots, v'_n$, we would pick a formula $\psi_i$ true at $v_2$ and false at $v'_i$, and use $\lozenge(\psi_1 \wedge \cdots \wedge \psi_n)$.
This is the typical use: a model checker can test the formula, and it certifies that two finite systems differ.
Watch out: the conjunction must be finite, and that is exactly where image-finiteness enters, as the counterexample in the Remarks shows.

### L3 human

The theorem says that the modal language is strong enough to describe bisimilarity on image-finite structures.
In first-order model theory, the analogue is that elementary equivalence implies isomorphism for finite structures, with $\omega$-saturation playing the role of m-saturation.
The theorem is a base step for the [[van Benthem characterization theorem|Y89MGMWE4H]], and for the use of modal logics as specification languages in process theory and [[model checking|VNY0VXVZ53]].
