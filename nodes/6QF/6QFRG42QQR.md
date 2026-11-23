---
tag: 6QFRG42QQR
kind: statement
role: theorem
name: Soundness of the Dialectica interpretation
msc: ["03F10", "03F25", "03F30"]
topics: [8XY7JYZKFW]
audience: grad
uses: [ZREF8MTYNW, A4WR995XZP, RXHJPVMPJH, 0QFT7Z76N5, WC4TDGEWZR, 9NTJJMPZ29]
about: [HZ17ES9PDY, CK8ZQRN183]
proofs: [X79VFTRT8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Proof translation (soundness)
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Characterisation principles
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Classical logic
history:
  first_stated: "Kurt Gödel, 1958"
  notes: "Gödel published the interpretation and its soundness in the journal Dialectica in 1958."
---

## Statement

The theorem says that every proof in Heyting arithmetic yields explicit terms of system T that win the game of its conclusion, and that after a negative translation every $\Pi^0_2$ theorem of Peano arithmetic yields a program for its witness.

Let T be [[Gödel's system T|A4WR995XZP]] as a quantifier-free theory, and let $A \mapsto A^D = \exists x\, \forall y\, A_D(x, y)$ be the [[Dialectica interpretation|ZREF8MTYNW]].
Here $x$ and $y$ are tuples of variables of finite type, and $A_D(x, y)$ is a quantifier-free formula of T.
The symbols $+$ and $\cdot$ of [[Heyting arithmetic|RXHJPVMPJH]] are read as their defining terms in T.

**Theorem (Gödel).**

1. Let $A$ be a formula of HA with free variables among $a_1, \dots, a_k$.
   If $\mathsf{HA} \vdash A$, then there is a tuple $t$ of terms of T, with free variables among $a_1, \dots, a_k$, such that $\mathsf{T} \vdash A_D(t, y)$.
2. Let $\varphi(n, m)$ be quantifier-free.
   If [[Peano arithmetic|0QFT7Z76N5]] proves $\forall n\, \exists m\, \varphi(n, m)$, then a closed term $t$ of type $\mathbb{N} \to \mathbb{N}$ satisfies $\mathsf{T} \vdash \varphi(n, t\, n)$.
3. Part 1 holds with $\mathsf{WE}\text{-}\mathsf{HA}^\omega + \mathrm{AC} + \mathrm{MP} + \mathrm{IP}_\forall$ in place of HA, with terms whose free variables are among those of $A$.

In part 3, $\mathsf{WE}\text{-}\mathsf{HA}^\omega$ is weakly extensional Heyting arithmetic in all finite types.
$\mathrm{AC}$ is the axiom of choice in all finite types, $\mathrm{MP}$ is Markov's principle for quantifier-free formulas, and $\mathrm{IP}_\forall$ is independence of premise for universal premises.
Their exact forms are given with the [[Dialectica interpretation|HZ17ES9PDY]].
The [[proof|X79VFTRT8Y]] covers parts 1 and 2, and part 3 is cited.

## Remarks

### Why each hypothesis is needed

Part 1 fails with PA in place of HA.
The [[halting example|9NTJJMPZ29]] is a theorem of PA whose interpretation has no witness in T, because the witness would decide the halting problem.
This is why part 2 goes through the negative translation first.

In part 2 the matrix $\varphi$ must be quantifier-free.
For a theorem $\forall n\, \exists m\, \forall k\, \psi$ the method gives only a functional that answers a counterexample function, not a function of $n$.
The [[non-conservativity example|HVHEKG9FA5]] for $\Pi^0_3$ sentences shows that no computable $m$ exists in general.

Part 3 needs weak extensionality.
Howard showed that the axiom of full extensionality in all finite types has no witness in T.

### What it gives you

The theorem gives a consistency proof.
The formula $0 = 1$ is atomic, so it is its own interpretation, and a proof of it in HA or PA would give $\mathsf{T} \vdash 0 = 1$.

It also bounds the strength of PA.
Every provably total function of PA is defined by a closed term of type $\mathbb{N} \to \mathbb{N}$ in T, so it is $\alpha$-recursive for some $\alpha < \varepsilon_0$.
And it shows that PA and HA prove the same $\Pi^0_2$ sentences, as [[Friedman's theorem|PY679V9MVR]] also does.

### The converse

The converse of part 1 is false: T may verify $A_D(t, y)$ although HA does not prove $A$.
[[Markov's principle|9YVRTGXKZF]] $\neg \neg \exists m\, \varphi(m) \to \exists m\, \varphi(m)$ is witnessed by the identity, but HA does not prove it.
For the larger theory there is a converse in another sense: $\mathsf{WE}\text{-}\mathsf{HA}^\omega + \mathrm{AC} + \mathrm{MP} + \mathrm{IP}_\forall$ proves $A \leftrightarrow A^D$ for every $A$.

### Generalizations

With [[bar recursion|8CCG6F2FAT]] added to T, the interpretation reaches classical analysis with countable choice, by [[Spector's theorem|DSQJ1RA71N]].
The monotone variant asks only for majorants of the witnesses, and it is the base of [[proof mining|XR1JXQG1CD]].
If the recursors of T are restricted to low types, the interpretation covers fragments of PA; with recursion at type $\mathbb{N}$ only it covers $\mathrm{I}\Sigma_1$, which gives one proof of [[Parsons's theorem|2VYJXZZDGB]].

## History

Gödel published the interpretation and its soundness in 1958, in the journal *Dialectica*.
Spector extended it to classical analysis in a paper of 1962.
Howard later showed that full extensionality has no witness in T.

## Explanations

### L1 human

The theorem says that every proof in intuitionistic arithmetic contains a program.
The program wins a game: for each statement, it answers every challenge of an opponent.
For example, a proof that every number $n$ has a prime above it contains a program that takes $n$ and outputs such a prime.
The programs use only counted loops, so they always stop.

### L2 human

We follow part 2 for the theorem $\forall n\, \exists m\, (n < m)$ of PA, with $<$ a primitive recursive relation.
The [[Gödel-Gentzen theorem|WC4TDGEWZR]] turns the classical proof into an intuitionistic proof of $\forall n\, \neg \neg \exists m\, (n < m)$.
The interpretation of $\neg \neg \exists m\, (n < m)$ is $\exists m\, \neg \neg (n < m)$, and the clause for $\forall$ turns it into this formula:
$$\exists f\, \forall n\, \neg \neg (n < f n).$$
Part 1 gives a term $t$ with $\mathsf{T} \vdash \neg \neg (n < t\, n)$, and since $n < t\, n$ is decidable, $\mathsf{T} \vdash n < t\, n$.
For the usual proof the term is $t = \lambda n.\, S\, n$.

The typical use is the extraction of an algorithm from a classical proof.
Watch out: the term mirrors the proof, so a proof with a lot of induction can give a term whose value grows very fast, even when a small witness exists.

### L3 human

The theorem shows that the computational content of arithmetic is primitive recursion in all finite types.
Its proof translates derivations into terms, much like the Curry-Howard correspondence, but it needs decidable atomic formulas to handle contraction.
Through the negative translation it measures PA by T, and so by the ordinal $\varepsilon_0$, which matches [[ordinal analysis|XTTKZTYDSD]].
Spector's extension by bar recursion and the monotone and bounded variants carry the method to analysis and to [[proof mining|XR1JXQG1CD]].
