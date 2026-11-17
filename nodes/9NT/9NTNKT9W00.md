---
tag: 9NTNKT9W00
kind: proof
name: Proof of Craig's theorem by padding conjunctions
msc: ["03B25", "03D25"]
topics: [FBWW4J1XWG]
audience: grad
proves: 6AN62NQ8AN
uses: [TN9G24VABN, PPGD5KW8JC, 05006AJ7DZ, 0Y0MQYST0M, 3ANXZC3BEG]
methods: [X5HG1RNWQX, 0ASJVEFA9J, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Craig%27s_theorem
    locator: Recursive axiomatization
---

## Proof

We use the Hilbert system $H$ of Enderton: the connectives $\neg$ and $\to$ are primitive, and the only rule is [[modus ponens|0Y0MQYST0M]].
Every [[tautology|05006AJ7DZ]] is a logical axiom of $H$.
The conjunction $\alpha \land \beta$ is an abbreviation of $\neg (\alpha \to \neg \beta)$.
For a sentence $\sigma$ define $\sigma^{(0)} = \sigma$ and $\sigma^{(k+1)} = (\sigma^{(k)} \land \sigma)$, that is, $\neg (\sigma^{(k)} \to \neg \sigma)$.
We write $|\tau|$ for the number of symbols of a string $\tau$.
Let $T$ be a computably enumerable set of $L$-sentences, as in the statement.

1. If $T = \emptyset$, then $A = \emptyset$ is decidable and has the same theorems as $T$, and the claim on logical equivalence holds because both sets are empty. From now on, let $T$ be nonempty.
2. A nonempty [[computably enumerable|TN9G24VABN]] set is the range of a total computable function. So there is a computable map $k \mapsto \sigma_k$ from $\N$ onto $T$. Repetitions are allowed.
3. Define $A = \set{\sigma_k^{(k)} : k \in \N}$. Each $\sigma_k^{(k)}$ is a sentence, because it is built from the sentence $\sigma_k$ with $\neg$ and $\to$ only.
4. Length. For every sentence $\sigma$ and every $k$, $|\sigma^{(k)}| \ge k + 1$. We use induction on $k$. For $k = 0$, $|\sigma| \ge 1$. The string $\sigma^{(k+1)}$ contains $\sigma^{(k)}$ and at least one more symbol, so $|\sigma^{(k+1)}| \ge |\sigma^{(k)}| + 1 \ge k + 2$.
5. Computability. The map $(\sigma, k) \mapsto \sigma^{(k)}$ is computable: a program applies $k$ times the string operation $\alpha \mapsto \neg (\alpha \to \neg \sigma)$ to $\sigma$.
6. Equivalence. Let $v$ be a truth assignment for the prime formulas, and $\bar{v}$ its extension to all formulas. We show $\bar{v}(\sigma^{(k)}) = \bar{v}(\sigma)$ by induction on $k$. The case $k = 0$ holds because $\sigma^{(0)} = \sigma$.
7. By the truth tables of $\neg$ and $\to$, $\bar{v}(\neg (\alpha \to \neg \beta))$ is true exactly when $\bar{v}(\alpha)$ and $\bar{v}(\beta)$ are both true. With $\alpha = \sigma^{(k)}$, $\beta = \sigma$ and the induction hypothesis $\bar{v}(\sigma^{(k)}) = \bar{v}(\sigma)$, this gives $\bar{v}(\sigma^{(k+1)}) = \bar{v}(\sigma)$.
8. By steps 6 and 7, the formulas $(\sigma^{(k)} \to \sigma)$ and $(\sigma \to \sigma^{(k)})$ are tautologies. So they are logical axioms of $H$, and $\sigma^{(k)}$ and $\sigma$ are logically equivalent. This proves the claim on logical equivalence, with $\sigma_k \in T$ and $\sigma_k^{(k)} \in A$.
9. $A \vdash \sigma_k$ for every $k$. The list $\sigma_k^{(k)}$, $(\sigma_k^{(k)} \to \sigma_k)$, $\sigma_k$ is a derivation from $A$: the first entry lies in $A$, the second is an axiom by step 8, and the third comes by modus ponens.
10. $T \vdash \sigma_k^{(k)}$ for every $k$. The list $\sigma_k$, $(\sigma_k \to \sigma_k^{(k)})$, $\sigma_k^{(k)}$ is a derivation from $T$, for the same reasons.
11. Transitivity. Let $\Gamma \vdash \delta$ for every $\delta \in \Delta$, and let $\Delta \vdash \varphi$. Take a derivation of $\varphi$ from $\Delta$, and replace each entry that is used as a member of $\Delta$ by a derivation of it from $\Gamma$.
12. The new list is a derivation from $\Gamma$. Each inserted entry is justified inside its inserted derivation, and each old entry that came by modus ponens still has its two premises earlier in the list. Its last entry is $\varphi$, so $\Gamma \vdash \varphi$.
13. Same theorems. Let $T \vdash \varphi$. Every member of $T$ is some $\sigma_k$, so $A$ derives every member of $T$ by step 9, and $A \vdash \varphi$ by steps 11 and 12. In the same way, steps 10, 11 and 12 turn $A \vdash \varphi$ into $T \vdash \varphi$.
14. Decision procedure for $A$. Given a string $\tau$, compute $\ell = |\tau|$. For each $k = 0, 1, \dots, \ell - 1$, compute $\sigma_k$ by step 2 and $\sigma_k^{(k)}$ by step 5, and compare $\sigma_k^{(k)}$ with $\tau$ symbol by symbol. Answer "yes" if one of them equals $\tau$, and "no" otherwise.
15. The procedure stops on every input. It runs through $\ell$ values of $k$, and for each one it runs computations that stop, because the map of step 2 is total.
16. The procedure is correct. If it answers "yes", then $\tau = \sigma_k^{(k)}$ for some $k$, so $\tau \in A$. If $\tau \in A$, then $\tau = \sigma_k^{(k)}$ for some $k$, and step 4 gives $\ell = |\tau| \ge k + 1$. So $k < \ell$, and the procedure finds $\tau$ and answers "yes".
17. By steps 14 to 16, $A$ is a decidable set. By steps 8 and 13, $A$ has the same theorems as $T$, and each sentence of $A$ is logically equivalent to a sentence of $T$ and conversely. This proves the theorem.

## Idea

An enumeration of $T$ lists its members, but it may list a short sentence very late, so the set $T$ itself may not be decidable.
The proof replaces the $k$-th listed sentence by a conjunction of $k + 1$ copies of it, which says the same thing and has length greater than $k$.
Then a sentence of length $\ell$ can only be one of the first $\ell$ new axioms, and a bounded search decides membership.
The copies change nothing in the theorems, because each copy is equivalent to the original by a tautology.

## Variants

A semantic proof of step 13 uses models instead of derivations.
A structure satisfies $\sigma_k^{(k)}$ exactly when it satisfies $\sigma_k$, so $A$ and $T$ have the same models.
By the soundness theorem and Gödel's completeness theorem, they then have the same theorems.

A refinement chooses the number of copies of $\sigma_k$ to be the number of steps that the enumeration needs to output $\sigma_k$.
The test for membership then needs only loops whose length is bounded in advance, and $A$ is primitive recursive.

Any other padding that keeps equivalence and makes the length grow works in the same way.
For example, $\sigma_k \land \theta^{(k)}$ for a fixed valid sentence $\theta$ such as $\forall x \, x = x$ gives a decidable axiom set with the same theorems as $T$, by a similar proof.
