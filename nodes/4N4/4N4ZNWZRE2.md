---
tag: 4N4ZNWZRE2
kind: counterexample
name: McKinsey formula
msc: ["03B45", "03C95"]
topics: [SPQVNPZDTB]
audience: research
uses: [3RYBWYPJVD, NGHWZ9Y7ZV, 484M0TZ1S7, 8WZF9SBP39, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: Common normal modal logics
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Counterexample

The *McKinsey formula* is
$$\mathrm{M} = \square \lozenge p \to \lozenge \square p.$$
It looks as simple as the axioms 4 or T, yet no first-order condition on frames says what it says.

**Claim.** No first-order sentence $\alpha$ in the language with one binary symbol $R$ satisfies $\mathfrak{F} \models \mathrm{M} \iff \mathfrak{F} \models \alpha$ for every Kripke frame $\mathfrak{F}$.
So $\mathrm{M}$ is a modal formula without a first-order frame [[correspondent|3RYBWYPJVD]].

We use the frame $\mathfrak{F} = (W, R)$ with these worlds and arrows:

- a root $w$, worlds $v_n$, $v_n^0$ and $v_n^1$ for each $n \in \mathbb{N}$, and a world $z_f$ for each function $f \colon \mathbb{N} \to \{0, 1\}$;
- the arrows $w R v_n$, $w R z_f$, $v_n R v_n^0$, $v_n R v_n^1$, $v_n^i R v_n^i$, and $z_f R v_n^{f(n)}$ for every $n$.

1. Each $v_n^i$ sees only itself, so at $v_n^i$ both $\square \lozenge p$ and $\lozenge \square p$ are equivalent to $p$, and $\mathrm{M}$ holds.
2. At $v_n$ or $z_f$, every successor is some $v_m^i$.
   If $\square \lozenge p$ holds there, every successor satisfies $p$, and so also $\square p$, so $\lozenge \square p$ holds.
3. At $w$, suppose $\square \lozenge p$ holds under some valuation.
   Then each $v_n$ has a successor with $p$, so there is a function $f$ with $v_n^{f(n)} \models p$ for every $n$.
4. Every successor of $z_f$ then satisfies $p$ and sees only itself, so $z_f \models \square p$ and $w \models \lozenge \square p$.
   With steps 1 to 3, this gives $\mathfrak{F} \models \mathrm{M}$.
5. The language has one binary symbol, so it is countable.
   By the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]], $\mathfrak{F}$ has a countable [[elementary substructure|8WZF9SBP39]] $\mathfrak{F}'$ that contains $w$ and every $v_n$ and $v_n^i$.
6. $\mathfrak{F}'$ contains only countably many worlds $z_f$.
   List them as $z_{f_0}, z_{f_1}, \dots$, with repetitions if needed; if there is none, the next steps hold with no $z$-worlds.
7. Define $h \colon \mathbb{N} \to \{0, 1\}$ by $h(2k) = 1 - f_k(2k)$ and $h(2k + 1) = f_k(2k + 1)$.
   On $\mathfrak{F}'$, let $V(p) = \{ v_n^{h(n)} : n \in \mathbb{N} \}$.
8. Each $v_n$ sees $v_n^{h(n)}$, where $p$ holds, and $v_n^{1 - h(n)}$, where $p$ fails.
   So $v_n \models \lozenge p$ and $v_n \not\models \square p$.
9. Each $z_{f_k}$ sees $v_{2k+1}^{f_k(2k+1)}$, where $p$ holds by the choice of $h$.
   It also sees $v_{2k}^{f_k(2k)}$, where $p$ fails, since $f_k(2k) \neq h(2k)$.
   So $z_{f_k} \models \lozenge p$ and $z_{f_k} \not\models \square p$.
10. The successors of $w$ in $\mathfrak{F}'$ are the $v_n$ and the $z_{f_k}$.
    By steps 8 and 9, $w \models \square \lozenge p$ and $w \not\models \lozenge \square p$, so $\mathfrak{F}' \not\models \mathrm{M}$.
11. If $\alpha$ corresponded to $\mathrm{M}$, then $\mathfrak{F} \models \alpha$ by step 4.
    Elementary substructures satisfy the same sentences, so $\mathfrak{F}' \models \alpha$ and $\mathfrak{F}' \models \mathrm{M}$, against step 10.

## Remarks

### What the argument uses

The proof uses one property of first-order classes only: they are closed under elementary substructures.
Frame validity of $\mathrm{M}$ is not, because a countable substructure loses most of the "choice worlds" $z_f$.
There are $2^{\aleph_0}$ of them in $\mathfrak{F}$, and step 7 is a diagonal argument that finds a choice the substructure missed.
The trap is the difference between frames and models: on one fixed model, $\mathrm{M}$ is a first-order condition through the standard translation, with a unary predicate for $p$.
Only the quantifier over all valuations, which is second-order, makes it undefinable.

### Where the formula sits

The logic $\mathsf{S4.1}$ is $\mathsf{S4} \oplus \mathrm{M}$; see [[common modal axiom schemata|FDFQFWPM4X]].
$\mathrm{M}$ is not a [[Sahlqvist formula|S4SSDMETJM]], since its antecedent $\square \lozenge p$ has a diamond under a box.
Like every modally definable class, its frame class is closed under bounded morphic images, generated subframes and disjoint unions, and it reflects ultrafilter extensions, as the [[Goldblatt-Thomason theorem|GX5E3GNRCS]] requires.
It is not closed under elementary equivalence, by the claim.

### Canonicity

Whether $\mathrm{M}$ is canonical was open for a long time.
The logic $\mathsf{K4} \oplus \mathrm{M}$ is canonical.
Robert Goldblatt proved in 1991 that $\mathsf{K} \oplus \mathrm{M}$ is not canonical.

### History

Johan van Benthem and Robert Goldblatt proved independently, both in 1975, that $\mathrm{M}$ is not first-order definable.
Van Benthem's argument is model-theoretic, with compactness and the Löwenheim-Skolem theorem, and the proof above uses its Löwenheim-Skolem part.

## Explanations

### L1 human

The McKinsey axiom says: if from here every next step can still reach a true point, then some next step makes the statement true at every point after it.
The frame above makes the axiom true by offering one path for every way of choosing among infinitely many pairs.
There are uncountably many such choices.
A smaller copy of the frame, with only countably many of them, misses one, and the axiom fails there.
First-order logic cannot tell the two frames apart, so it cannot express the axiom.

### L2 human

Here is a finite model of the same mechanism.
Let $w$ see $v_0$ and $v_1$, let each $v_n$ see $v_n^0$ and $v_n^1$, and let each $v_n^i$ see only itself.
Add four worlds $z_f$, one for each $f \colon \{0, 1\} \to \{0, 1\}$, each seen from $w$, with $z_f$ seeing $v_0^{f(0)}$ and $v_1^{f(1)}$.
Let $p$ be true exactly at $v_0^1$ and $v_1^0$.
The world $z_f$ with $f(0) = 1$ and $f(1) = 0$ has $\square p$, so $\lozenge \square p$ holds at $w$.
Now delete that world and the world $z_g$ with $g(0) = 0$ and $g(1) = 1$, which sees no $p$-world at all.
The two remaining $z$-worlds each see one $p$-world and one world without $p$, and so do $v_0$ and $v_1$.
So $\square \lozenge p$ holds and $\lozenge \square p$ fails at $w$, and $\mathrm{M}$ fails.
In the infinite frame, step 7 chooses $h$ so that no $z$-world of $\mathfrak{F}'$ has $f = h$ or $f = 1 - h$, which is exactly this deletion.
