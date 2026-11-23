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

We replace the $k$-th listed axiom by $k + 1$ copies of itself joined by $\land$, so that long axioms come late and a bounded search decides membership.
We use the Hilbert system $H$ of Enderton: $\neg$ and $\to$ are primitive, the only rule is [[modus ponens|0Y0MQYST0M]], and every [[tautology|05006AJ7DZ]] is a logical axiom.
The conjunction $\alpha \land \beta$ abbreviates $\neg (\alpha \to \neg \beta)$.
For a sentence $\sigma$ put $\sigma^{(0)} = \sigma$ and $\sigma^{(k+1)} = (\sigma^{(k)} \land \sigma)$.
We write $|\tau|$ for the number of symbols of a string $\tau$.
Let $T$ be a computably enumerable set of $L$-sentences.

1. If $T = \emptyset$, then $A = \emptyset$ is decidable and has the same theorems as $T$, and there is nothing more to show.
   From now on, let $T$ be nonempty.
2. A nonempty [[computably enumerable|TN9G24VABN]] set is the range of a total computable function.
   So there is a computable map $k \mapsto \sigma_k$ from $\mathbb{N}$ onto $T$, with repetitions allowed.
3. Define $A = \{ \sigma_k^{(k)} : k \in \mathbb{N} \}$.
   Each $\sigma_k^{(k)}$ is a sentence, because it is built from the sentence $\sigma_k$ with $\neg$ and $\to$ only.
4. Length: for every sentence $\sigma$ and every $k$, $|\sigma^{(k)}| \ge k + 1$.
   For $k = 0$ this holds because $|\sigma| \ge 1$.
   The string $\sigma^{(k+1)}$ contains $\sigma^{(k)}$ and at least one more symbol, so $|\sigma^{(k+1)}| \ge |\sigma^{(k)}| + 1 \ge k + 2$.
5. Computability: the map $(\sigma, k) \mapsto \sigma^{(k)}$ is computable.
   A program applies the string operation $\alpha \mapsto \neg (\alpha \to \neg \sigma)$ to $\sigma$, $k$ times.
6. Equivalence: for every truth assignment $v$, the value of $\sigma^{(k)}$ equals the value of $\sigma$.
   We use induction on $k$, and for $k = 0$ the two strings are equal.
   By the truth tables, $\neg (\alpha \to \neg \beta)$ is true exactly when $\alpha$ and $\beta$ are both true, so with $\alpha = \sigma^{(k)}$, $\beta = \sigma$ and the induction hypothesis, $\sigma^{(k+1)}$ has the value of $\sigma$.
7. By step 6, $(\sigma^{(k)} \to \sigma)$ and $(\sigma \to \sigma^{(k)})$ are tautologies, so they are logical axioms of $H$.
   Hence $\sigma_k^{(k)}$ and $\sigma_k$ are logically equivalent, which proves the claim on equivalence.
8. $A \vdash \sigma_k$ for every $k$.
   The list $\sigma_k^{(k)}$, $(\sigma_k^{(k)} \to \sigma_k)$, $\sigma_k$ is a derivation from $A$: the first entry is in $A$, the second is an axiom by step 7, and the third comes by modus ponens.
9. $T \vdash \sigma_k^{(k)}$ for every $k$, by the derivation $\sigma_k$, $(\sigma_k \to \sigma_k^{(k)})$, $\sigma_k^{(k)}$ from $T$.
10. Transitivity: if $\Gamma$ derives every member of $\Delta$ and $\Delta \vdash \varphi$, then $\Gamma \vdash \varphi$.
    Take a derivation of $\varphi$ from $\Delta$, and insert before each entry used as a member of $\Delta$ a derivation of it from $\Gamma$.
    Modus ponens steps keep their premises earlier in the list, so the result is a derivation of $\varphi$ from $\Gamma$.
11. Same theorems: if $T \vdash \varphi$, then $A \vdash \varphi$ by steps 8 and 10, since every member of $T$ is some $\sigma_k$.
    In the same way, steps 9 and 10 turn $A \vdash \varphi$ into $T \vdash \varphi$.
12. Decision procedure for $A$: given a string $\tau$, compute $\ell = |\tau|$.
    For each $k = 0, 1, \dots, \ell - 1$, compute $\sigma_k$ by step 2 and $\sigma_k^{(k)}$ by step 5, and compare it with $\tau$ symbol by symbol.
    Answer "yes" if one of them equals $\tau$, and "no" otherwise.
13. The procedure stops on every input, because it tries $\ell$ values of $k$ and each computation stops, since the map of step 2 is total.
14. The procedure is correct.
    A "yes" means $\tau = \sigma_k^{(k)}$ for some $k$, so $\tau \in A$.
    Conversely, if $\tau = \sigma_k^{(k)}$, then step 4 gives $\ell \ge k + 1$, so $k < \ell$ and the procedure finds $\tau$.
15. So $A$ is a decidable set with the same theorems as $T$, and its sentences are equivalent one for one to those of $T$.
    This proves the theorem.

## Idea

An enumeration lists the members of $T$, but it may list a short sentence very late, so $T$ itself may not be decidable.
The proof pads the $k$-th listed sentence into a conjunction of $k + 1$ copies.
The padded sentence says the same thing and has more than $k$ symbols.
So a sentence with $\ell$ symbols can only be among the first $\ell$ new axioms, and a search of bounded length decides membership.
The padding changes no theorems, because each copy is equivalent to the original by a tautology.

## Variants

A semantic proof of step 11 uses models instead of derivations.
A structure satisfies $\sigma_k^{(k)}$ exactly when it satisfies $\sigma_k$, so $A$ and $T$ have the same models.
By the soundness theorem and Gödel's completeness theorem, they then have the same theorems.

A refinement takes as the number of copies of $\sigma_k$ the number of steps that the enumeration needs to print $\sigma_k$.
The membership test then needs only loops whose length is fixed in advance, so $A$ is primitive recursive.

Any other padding that keeps equivalence and makes the length grow works the same way.
For example, $\sigma_k \land \theta^{(k)}$, for a fixed valid sentence $\theta$ such as $\forall x \, x = x$, gives a decidable axiom set with the same theorems as $T$.
