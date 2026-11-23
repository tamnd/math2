---
tag: ZT57RJVD9X
kind: proof
name: Proof that Robinson arithmetic is essentially undecidable by diagonalization
aliases: [diagonal-proof-of-essential-undecidability-of-q]
msc: ["03B25", "03F30"]
topics: [E4AVTNWE9E]
audience: grad
proves: RZ42PP37MD
methods: [0J0XBKG64S, 0WCP0PVET6]
uses: [3K1AKGXF8A, HWC687ES0Q, PPGD5KW8JC, MFJXPAF0R0, 3PRW76471J, X9WYNYE29C]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Representability in Q
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: lead section
---

## Proof

We assume a decision procedure for a consistent extension of $\mathsf{Q}$, build from it a computable diagonal set, and let $\mathsf{Q}$ represent that set to get a contradiction.

### The cited result

The proof uses one result from the theory of incompleteness, the representability theorem, which we cite.
For every [[computable set|PPGD5KW8JC]] $D \subseteq \mathbb{N}$, there is an $L_A$-formula $\delta(x)$ with one free variable such that, for every $n \in \mathbb{N}$, $n \in D$ implies $\mathsf{Q} \vdash \delta(\bar{n})$, and $n \notin D$ implies $\mathsf{Q} \vdash \neg \delta(\bar{n})$.
Here $\bar{n}$ is the numeral $S \cdots S 0$ with $n$ copies of $S$.

### The diagonal set

1. Let $T$ be a consistent theory in $L_A$ with $\mathsf{Q} \subseteq T$.
   Suppose, for a contradiction, that $T$ is decidable.
2. By a [[Gödel numbering|MFJXPAF0R0]], list all $L_A$-formulas with exactly the free variable $x$ as $\varphi_0(x), \varphi_1(x), \ldots$.
   The map $n \mapsto \varphi_n$ is computable.
3. Let $D = \{n \in \mathbb{N} : \varphi_n(\bar{n}) \notin T\}$.
4. The map $n \mapsto \varphi_n(\bar{n})$ is computable, since it substitutes a numeral into a listed formula.
5. Since $T$ is decidable, membership of $\varphi_n(\bar{n})$ in $T$ is computable.
   So $D$ is a computable set.
6. By the representability theorem, there is a formula $\delta(x)$ that represents $D$ in $\mathsf{Q}$.
7. The formula $\delta(x)$ occurs in the list of step 2.
   Let $d$ be its index, so $\delta = \varphi_d$.

### The two cases

8. Case 1: $d \in D$.
   By step 6, $\mathsf{Q} \vdash \varphi_d(\bar{d})$.
9. Since $\mathsf{Q} \subseteq T$ and $T$ is closed under consequence, $\varphi_d(\bar{d}) \in T$.
10. By the definition of $D$ in step 3, $d \notin D$.
    This contradicts the case assumption.
11. Case 2: $d \notin D$.
    By the definition of $D$, $\varphi_d(\bar{d}) \in T$.
12. By step 6, $\mathsf{Q} \vdash \neg \varphi_d(\bar{d})$, so $\neg \varphi_d(\bar{d}) \in T$.
13. Then $T$ contains a sentence and its negation, so $T$ is inconsistent.
    This contradicts step 1.
14. Both cases lead to a contradiction, so $T$ is not decidable.
15. Since $T$ was an arbitrary consistent extension of $\mathsf{Q}$ in $L_A$, $\mathsf{Q}$ is essentially undecidable.

## Idea

If a consistent extension $T$ of $\mathsf{Q}$ were decidable, the diagonal set $D$ of indices $n$ whose formula fails at its own numeral would be computable.
Then $\mathsf{Q}$ would represent $D$ by some formula $\varphi_d$, and asking whether $d \in D$ gives a contradiction either way.
This is Cantor's diagonal method and the liar paradox, made precise by representability.

## Variants

The [[diagonal lemma|3PRW76471J]] gives a sentence $\gamma$ with $\mathsf{Q} \vdash \gamma \leftrightarrow \neg \delta(\ulcorner \gamma \urcorner)$, where $\delta$ represents the set of codes of members of $T$.
The same two cases then give the contradiction.

A proof through computability works for extensions $T$ that prove no false $\Sigma_1$ sentence.
Since $\mathsf{Q}$ proves every true $\Sigma_1$ sentence, a number $n$ is then in the halting set exactly when $T$ proves the $\Sigma_1$ sentence that says so.
The general case needs the representability argument above.

The same argument shows the stronger fact that $\{\sigma : \mathsf{Q} \vdash \sigma\}$ and $\{\sigma : \mathsf{Q} \vdash \neg \sigma\}$ are computably inseparable.
Replace "$\varphi_n(\bar{n}) \notin T$" in step 3 by "$\varphi_n(\bar{n}) \notin C$" for a computable set $C$ that would separate them.
