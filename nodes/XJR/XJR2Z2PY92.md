---
tag: XJR2Z2PY92
kind: proof
name: Proof of Kripke incompleteness
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
proves: W67YJQTT50
uses: [NGHWZ9Y7ZV, 6W9MEGN982, F5WN5GCAEQ]
methods: [0NTF6DMVAP, 0ASJVEFA9J, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: General frame semantics
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Completeness
---

## Proof

We show that $\mathrm{vB}$ and $\mathrm{E}$ agree on Kripke frames, then build a general frame that validates $\mathrm{vB}$ and refutes $\mathrm{E}$, and then combine the two facts.
We write $\mathrm{vB}$ for $\square \lozenge \top \to \square(\square(\square p \to p) \to p)$ and $\mathrm{E}$ for $\square \lozenge \top \to \square \bot$.

### Part A: the Kripke frames of vB

1. Let $(W, R)$ be a frame, let $y \in W$, and let $V(p) = W \setminus \{y\}$.
   Then $y \not\models p$.
2. Let $y R z$.
   If $z \neq y$, then $z \models p$.
   If $z = y$, then $y \not\models \square p$, because $y R y$ and $y \not\models p$.
   In both cases $z \models \square p \to p$.
3. So $y \models \square(\square p \to p)$, and $y \not\models \square(\square p \to p) \to p$ under $V$.
4. Hence the formula $\square(\square(\square p \to p) \to p)$ holds at a world $x$ under all valuations if and only if $x$ has no successor.
   The "only if" direction is step 3 applied to a successor $y$ of $x$, and the "if" direction is vacuous truth.
5. The antecedent $\square \lozenge \top$ has no variables, so its truth at $x$ does not depend on the valuation.
   So $(W, R) \models \mathrm{vB}$ if and only if every world with $\square \lozenge \top$ has no successor, that is, if and only if $(W, R) \models \mathrm{E}$.

### Part B: a general frame that refutes E

6. Let $W = \mathbb{N} \cup \{\infty, \omega\}$, with two new points $\infty$ and $\omega$.
   Let $m R n$ for $m > n$ in $\mathbb{N}$, let $\infty R n$ for every $n \in \mathbb{N}$, and let $\infty R \infty$ and $\omega R \infty$, with no other arrows.
7. Let $A$ be the family of sets $X \subseteq W$ such that $X \cap (\mathbb{N} \cup \{\infty\})$ is either a finite subset of $\mathbb{N}$ (type 1) or a cofinite subset of $\mathbb{N} \cup \{\infty\}$ that contains $\infty$ (type 2).
   The point $\omega$ may be in $X$ or not.
8. $A$ is closed under unions and complements, because a union with a set of type 2 has type 2, and complement exchanges the two types.
9. We check closure under $m_R$, using that the predecessors of $n \in \mathbb{N}$ are the $m > n$ and $\infty$, the predecessors of $\infty$ are $\infty$ and $\omega$, and $\omega$ has none.
   If $X \subseteq \{\omega\}$, then $m_R(X) = \emptyset$.
10. If $X$ has type 1 and meets $\mathbb{N}$, let $k = \min (X \cap \mathbb{N})$.
    Then $m_R(X) = \{ m \in \mathbb{N} : m > k \} \cup \{\infty\}$, which has type 2.
11. If $X$ has type 2, then $m_R(X)$ contains $\infty$, $\omega$ and every $m > \min(X \cap \mathbb{N})$, so it has type 2.
12. So $\mathfrak{g} = (W, R, A)$ is a [[general frame|6W9MEGN982]].
13. $\mathfrak{g}$ refutes $\mathrm{E}$ at $\omega$.
    The only successor of $\omega$ is $\infty$, and $\infty R \infty$, so $\omega \models \square \lozenge \top$.
    But $\omega$ has a successor, so $\omega \not\models \square \bot$.

### Part B, continued: the frame validates KvB

14. Now we show $\mathfrak{g} \models \mathrm{vB}$ at every world except $\omega$.
    The world $0$ has no successor, so the consequent holds there.
    Every $n \geq 1$, and also $\infty$, sees $0$, which has no successor, so the antecedent $\square \lozenge \top$ fails there.
15. It remains to check $\omega$.
    Its only successor is $\infty$, so we need $\infty \models \square(\square p \to p) \to p$ for every admissible $V(p)$.
16. Assume $\infty \models \square(\square p \to p)$.
    Then $n \models \square p \to p$ for every $n \in \mathbb{N}$, since $\infty$ sees every $n$.
17. By strong induction on $n$, every $n \in \mathbb{N}$ satisfies $p$.
    If all $m < n$ satisfy $p$, then $n \models \square p$, since the successors of $n$ are the $m < n$, and step 16 gives $n \models p$.
18. So $V(p) \supseteq \mathbb{N}$.
    Then $V(p) \cap (\mathbb{N} \cup \{\infty\})$ is infinite, so by step 7 it has type 2 and contains $\infty$, and $\infty \models p$.
19. Validity on a general frame is closed under modus ponens and necessitation, by the truth definition.
    It is closed under uniform substitution, because the truth set of any formula under an admissible valuation is admissible, by steps 8 to 11.
20. The axioms of $\mathsf{K}$ are valid on every general frame.
    So every theorem of $\mathsf{KvB}$ is valid on $\mathfrak{g}$, and $\mathrm{E} \notin \mathsf{KvB}$ by step 13.

### Part C: incompleteness

21. Suppose, for a contradiction, that $\mathsf{KvB}$ is the logic of a class $\mathsf{C}$ of Kripke frames.
    Every frame in $\mathsf{C}$ validates $\mathrm{vB}$, so it validates $\mathrm{E}$ by Part A.
22. Then $\mathrm{E}$ is valid on every frame of $\mathsf{C}$, so $\mathrm{E} \in \mathsf{KvB}$, against Part B.
    So $\mathsf{KvB}$ is Kripke incomplete.

## Idea

On a Kripke frame you can always refute $\square(\square p \to p) \to p$ at a chosen world, by making $p$ false there and nowhere else.
So $\mathrm{vB}$ collapses to the variable-free formula $\mathrm{E}$ on every Kripke frame.
A general frame can forbid that valuation, and here it does, because the set $W \setminus \{\infty\}$ is not admissible.
In the frame of Part B, once $p$ holds on all of $\mathbb{N}$ it is forced to hold at $\infty$, and so $\mathrm{vB}$ survives at $\omega$ while $\mathrm{E}$ fails there.
Watch out: validity on $\mathfrak{g}$ counts admissible valuations only.
Under the valuation $V(p) = W \setminus \{\infty\}$, which is not admissible, $\mathrm{vB}$ fails at $\omega$, exactly as in Part A.

## Variants

The general frame of Part B is the [[finite and cofinite frame on the natural numbers|F5WN5GCAEQ]], with the order reversed, a point at infinity $\infty$, and one extra point $\omega$ above it.
Thomason's and Fine's original examples use more involved frames, and Fine's logic is an extension of $\mathsf{S4}$.
An algebraic version of the proof shows that the complex algebra $\mathfrak{g}^*$ lies in the variety of $\mathsf{KvB}$, while no complex algebra of a Kripke frame separates $\mathrm{vB}$ from $\mathrm{E}$.
