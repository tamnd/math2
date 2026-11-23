---
tag: E5T2PT5Z1P
kind: proof
name: Proof of the representation of AGM revision by total preorders
msc: ["03B42", "68T27"]
topics: [CQM9SRN8PM]
audience: research
proves: KV8J5H7KF2
uses: [Y05YQN7HGQ, 0VABYWJWH9]
methods: [0NTF6DMVAP, 0WCP0PVET6, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Belief_revision
    locator: Conditions equivalent to the AGM postulates
  - book: isbn:9780262071093
    locator: Gärdenfors, Knowledge in Flux
---

## Proof

We prove each direction by working with sets of models, first from a preorder to the postulates, then from the postulates to a preorder.
We use the notation of [[the representation theorem|KV8J5H7KF2]], and the postulates are numbered as in [[AGM belief revision|Y05YQN7HGQ]].
Since the language is finite, each $S \subseteq \Omega$ is $\mathrm{Mod}(\mathrm{form}(S))$ for some formula $\mathrm{form}(S)$, and a belief set is determined by its set of models.
We write $\mathrm{form}(x, y)$ for $\mathrm{form}(\{x, y\})$, and $\mathrm{M}(\varphi)$ for $\mathrm{Mod}(K * \varphi)$.

### From a ranking to postulates 1 to 6

Let $\le$ be a total preorder on $\Omega$ that is faithful to $K$.

1. Define $K * \varphi$ as the set of formulas true in all of $\min(\mathrm{Mod}(\varphi), \le)$.
   Postulate 1 holds, since such a set is closed under consequence.
2. Postulate 2 holds, since $\min(\mathrm{Mod}(\varphi), \le) \subseteq \mathrm{Mod}(\varphi)$.
3. Postulate 6 holds, since the definition depends only on $\mathrm{Mod}(\varphi)$.
4. For postulate 5, let $\varphi$ be consistent, so $\mathrm{Mod}(\varphi)$ is finite and nonempty.
   A total preorder on a finite nonempty set has a minimal element, so $K * \varphi$ is consistent.
5. For postulates 3 and 4, first let $\neg\varphi \in K$.
   Then $K + \varphi$ is inconsistent, so postulate 3 holds and postulate 4 has nothing to check.
6. Now let $\neg\varphi \notin K$, so $\mathrm{Mod}(K) \cap \mathrm{Mod}(\varphi) \neq \emptyset$.
   By faithfulness each $x$ in this set has $x \le y$ for every $y$, so $x$ is minimal in $\mathrm{Mod}(\varphi)$.
7. Each $y \in \mathrm{Mod}(\varphi) \setminus \mathrm{Mod}(K)$ has $x < y$ for such an $x$, so $y$ is not minimal.
8. So $\min(\mathrm{Mod}(\varphi), \le) = \mathrm{Mod}(K) \cap \mathrm{Mod}(\varphi) = \mathrm{Mod}(K + \varphi)$.
   Hence $K * \varphi = K + \varphi$, which gives postulates 3 and 4.
### From a ranking to postulates 7 and 8

9. For postulate 7, put $A = \mathrm{Mod}(\varphi)$ and $B = \mathrm{Mod}(\psi)$, and let $x \in \min(A, \le) \cap B$.
10. Then $x \in A \cap B$ and $x \le y$ for all $y \in A \cap B$, so $x \in \min(A \cap B, \le)$.
    So $\min(A, \le) \cap B \subseteq \min(A \cap B, \le)$, which is postulate 7 in terms of models.
11. For postulate 8, suppose that $\neg\psi \notin K * \varphi$, so some $z$ lies in $\min(A, \le) \cap B$, and let $y \in \min(A \cap B, \le)$.
12. Then $y \le z$, since $z \in A \cap B$, and $z \le a$ for every $a \in A$.
    Transitivity gives $y \le a$ for every $a \in A$, so $y \in \min(A, \le) \cap B$.
13. So $\min(A \cap B, \le) \subseteq \min(A, \le) \cap B$, which is postulate 8.

### From the postulates to a total preorder

Now let $*$ satisfy the eight postulates for $K$.

14. We prove a restriction lemma: if $T \subseteq S \subseteq \Omega$ and $\mathrm{M}(\mathrm{form}(S)) \cap T \neq \emptyset$, then $\mathrm{M}(\mathrm{form}(T)) = \mathrm{M}(\mathrm{form}(S)) \cap T$.
15. The formula $\mathrm{form}(S) \wedge \mathrm{form}(T)$ is equivalent to $\mathrm{form}(T)$, so postulate 6 lets us revise by either.
    Postulate 7 then gives $\mathrm{M}(\mathrm{form}(S)) \cap T \subseteq \mathrm{M}(\mathrm{form}(T))$.
16. The hypothesis says that $\neg\mathrm{form}(T) \notin K * \mathrm{form}(S)$, so postulate 8 gives the other inclusion.
17. Define $x \le y$ if and only if $x \in \mathrm{M}(\mathrm{form}(x, y))$.
18. The relation is total: $\mathrm{M}(\mathrm{form}(x, y))$ is a subset of $\{x, y\}$ by postulate 2, and nonempty by postulate 5.
    So $x \le y$ or $y \le x$.
19. For transitivity, let $x \le y$ and $y \le z$, and put $S = \mathrm{M}(\mathrm{form}(x, y, z))$.
    This is a nonempty subset of $\{x, y, z\}$ by postulates 2 and 5.
20. Suppose first that $S \cap \{x, y\} \neq \emptyset$.
    The lemma gives $S \cap \{x, y\} = \mathrm{M}(\mathrm{form}(x, y))$, which contains $x$, so $x \in S$.
21. Then $x \in S \cap \{x, z\}$, and the lemma gives $\mathrm{M}(\mathrm{form}(x, z)) = S \cap \{x, z\}$, which contains $x$.
    So $x \le z$.
22. Suppose instead that $S \cap \{x, y\} = \emptyset$.
    Then $S = \{z\}$ with $z \neq y$, and the lemma with $T = \{y, z\}$ gives $\mathrm{M}(\mathrm{form}(y, z)) = \{z\}$.
23. So $y \notin \mathrm{M}(\mathrm{form}(y, z))$, which contradicts $y \le z$, and this case cannot occur.
### Minimal models and faithfulness

24. Now we show that revision selects the minimal models.
    Let $A = \mathrm{Mod}(\varphi)$ and $M = \mathrm{M}(\varphi)$; if $A = \emptyset$, then $M = \emptyset = \min(A, \le)$ by postulate 2.
25. Let $A \neq \emptyset$, so $M \subseteq A$ is nonempty by postulates 2 and 5, and let $x \in M$ and $y \in A$.
26. The lemma with $S = A$ and $T = \{x, y\}$ gives $\mathrm{M}(\mathrm{form}(x, y)) = M \cap \{x, y\}$, which contains $x$.
    So $x \le y$ for all $y \in A$, and $x \in \min(A, \le)$.
27. Conversely, let $x \in \min(A, \le)$ and pick $m \in M$.
    The lemma with $T = \{x, m\}$ gives $\mathrm{M}(\mathrm{form}(x, m)) = M \cap \{x, m\}$.
28. Since $x \le m$, the point $x$ lies in this set, so $x \in M$.
    Hence $M = \min(A, \le)$.
29. Finally, faithfulness: let $x \in \mathrm{Mod}(K)$ and $y \in \Omega$.
    Then $\mathrm{form}(x, y)$ is consistent with $K$, so postulates 3 and 4 give $K * \mathrm{form}(x, y) = K + \mathrm{form}(x, y)$.
30. So $\mathrm{M}(\mathrm{form}(x, y)) = \mathrm{Mod}(K) \cap \{x, y\}$.
    If $y \in \mathrm{Mod}(K)$, this set is $\{x, y\}$, and so $x \le y$ and $y \le x$.
31. If $y \notin \mathrm{Mod}(K)$, this set is $\{x\}$, so $x \le y$ and not $y \le x$.
    Hence $\le$ is faithful to $K$, and both directions of the theorem are proved.

## Idea

The ranking is read off from revisions by two-world formulas: $x \le y$ means that revision by "$x$ or $y$" keeps $x$.
Postulates 7 and 8 together say that revising by a smaller set is the same as revising by a larger set and then cutting down, as long as the cut leaves something.
This restriction lemma does all the work: it gives transitivity and the formula with minimal models.
Postulates 3 and 4 then put the models of $K$ at the bottom of the ranking.

## Variants

Grove's proof for an arbitrary language works with maximal consistent sets and builds the spheres from revisions, with a limit assumption in place of finiteness.
Another route reads postulates 7 and 8 as Arrow's conditions on a choice function over finite sets of worlds.
Arrow's classical result that such choice functions come from total preorders then gives the ranking at once.
