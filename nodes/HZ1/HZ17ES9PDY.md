---
tag: HZ17ES9PDY
kind: concept
name: Dialectica interpretation
msc: ["03F10", "03F25", "03F50"]
topics: [8XY7JYZKFW]
audience: grad
uses: [CK8ZQRN183, RXHJPVMPJH, 5NVA2JRHPV, ZREF8MTYNW, A4WR995XZP, HGJVM49PA4]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Formula translation
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Proof translation (soundness)
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Characterisation principles
same_as:
  wikidata: Q5270518
  wikipedia: Dialectica interpretation
---

## Summary

The Dialectica interpretation turns each statement of arithmetic into a game of one move for each player, and it turns each intuitionistic proof into a program that wins the game.
Take the statement that every number has a half, rounded down:
$$\forall n\, \exists m\, (2m \le n < 2m + 2).$$
Its interpretation asks for a function $f$ with $2 f(n) \le n < 2 f(n) + 2$ for every $n$, and the program $f(n) = \lfloor n / 2 \rfloor$ wins.
Check: $f(7) = 3$, and $6 \le 7 < 8$.

In general the interpretation assigns to each formula $A$ of [[Heyting arithmetic|CK8ZQRN183]] a formula of one fixed shape:
$$A^D = \exists x\, \forall y\, A_D(x, y).$$
Here $x$ and $y$ are tuples of variables of finite type, $A_D$ is quantifier-free, and the [[definition|ZREF8MTYNW]] gives the clauses.
For a formula $\forall x\, \exists y\, A(x, y)$ with $A$ quantifier-free, the result is $\exists f\, \forall x\, A(x, f x)$, as in the example.
Gödel's [[soundness theorem|6QFRG42QQR]] says that if HA proves $A$, then terms $t$ of [[Gödel's system T|A4WR995XZP]] satisfy $\mathsf{T} \vdash A_D(t, y)$.
So a proof hands over its witnesses as programs built from [[primitive recursion|5NVA2JRHPV]] in higher types.

## Motivation

Hilbert asked for proofs of consistency by finitary means.
Gentzen proved the consistency of PA with induction up to the ordinal $\varepsilon_0$.
Gödel looked for a different extension of finitary reasoning: computation with functions of higher type, but with no quantifiers over them.
The Dialectica interpretation is the result, and it reduces the consistency of HA to the consistency of the quantifier-free theory T.
After a [[double-negation translation|HGJVM49PA4]] it does the same for PA.

The method also does real work on proofs.
From a proof of $\forall n\, \exists m\, \varphi(n, m)$ it extracts a program that computes $m$ from $n$, and from a proof with more quantifiers it extracts a functional that answers every challenge.
The same idea returns in the [[no-counterexample interpretation|4BCD1EM542]], in Spector's extension to analysis by [[bar recursion|8CCG6F2FAT]], and in Kohlenbach's [[proof mining|XR1JXQG1CD]].

## Notation

We write $\mathbb{N}$ for the type of natural numbers and $\sigma \to \tau$ for the type of functions from $\sigma$ to $\tau$.
Many books write $0$ for $\mathbb{N}$, $1$ for $\mathbb{N} \to \mathbb{N}$ and $2$ for $(\mathbb{N} \to \mathbb{N}) \to \mathbb{N}$, so read "type $0$" as "numbers", not as the number zero.
In $A^D = \exists x\, \forall y\, A_D(x, y)$ the tuple $x$ is the witness and the tuple $y$ is the challenge, or counterexample.
$\mathsf{HA}^\omega$ is Heyting arithmetic in all finite types, $\mathsf{WE}\text{-}\mathsf{HA}^\omega$ is its weakly extensional form, and $\mathsf{PA}^\omega$ is the classical version.

## Remarks

### A first interpretation

In the opening example the formula $2m \le n < 2m + 2$ is quantifier-free, so it is its own interpretation, with no witness and no challenge.
The clause for $\exists m$ adds $m$ to the witness, and the clause for $\forall n$ turns that witness into a function of $n$.
This is the Skolem form of the statement, with the extra demand that the Skolem function be a term of T.

A universal quantifier after the existential one stays a challenge.
For $\forall x\, \exists y\, \forall z\, B(x, y, z)$ with $B$ quantifier-free, the interpretation is this:
$$\exists f\, \forall x, z\, B(x, f x, z).$$
So the witness $f x$ must work for every $z$ at once.
For $\forall n\, \exists m\, \forall k\, (m \le n + k)$ the function $f n = n$ wins, since $n \le n + k$ for every $k$.

### Implications send challenges backward

The interesting clause is the one for $\to$.
Take the lemma "every number has a larger number" and the conclusion "some number is larger than $5$":
$$\forall n\, \exists m\, (n < m) \to \exists k\, (5 < k).$$
The premise has witness $f$ and challenge $n$, and the conclusion has witness $k$ and no challenge.
So the interpretation asks for two functionals: $U$, which turns a witness $f$ of the premise into a witness of the conclusion, and $Y$, which says at which point $n$ the premise is needed.
The matrix to prove is $Y f < f(Y f) \to 5 < U f$.
The terms $Y f = 5$ and $U f = f(5)$ win: if $5 < f(5)$, then $5 < U f$.

Witnesses flow forward from the premise to the conclusion, and challenges flow backward from the conclusion to the premise.
In general, with $A^D = \exists x\, \forall y\, A_D(x, y)$ and $B^D = \exists u\, \forall v\, B_D(u, v)$, the clause reads
$$(A \to B)^D = \exists U, Y\, \forall x, v\, \bigl( A_D(x, Y x v) \to B_D(U x, v) \bigr).$$
Negation $\neg A$ is $A \to 0 = 1$, so its interpretation is $\exists Y\, \forall x\, \neg A_D(x, Y x)$.

### What the interpretation verifies

The [[soundness theorem|6QFRG42QQR]] gives witnesses for every theorem of HA, and also for a larger theory.
It adds three principles to $\mathsf{WE}\text{-}\mathsf{HA}^\omega$, each for all finite types.
The axiom of choice $\mathrm{AC}$ is the schema $\forall x\, \exists y\, A(x, y) \to \exists Y\, \forall x\, A(x, Y x)$, for every formula $A$.
Markov's principle $\mathrm{MP}$ is $\neg \neg \exists x\, A_0(x) \to \exists x\, A_0(x)$, for quantifier-free $A_0$ and a tuple $x$.
Independence of premise for universal premises, $\mathrm{IP}_\forall$, is the schema below, for quantifier-free $A_0$ and any $B$, with $y$ not free in $A_0$:
$$\bigl( \forall x\, A_0(x) \to \exists y\, B(y) \bigr) \to \exists y\, \bigl( \forall x\, A_0(x) \to B(y) \bigr).$$
The characterization theorem says that $\mathsf{WE}\text{-}\mathsf{HA}^\omega + \mathrm{AC} + \mathrm{MP} + \mathrm{IP}_\forall$ proves $A \leftrightarrow A^D$ for every formula $A$.

Two small cases show how the witnesses look.
[[Markov's principle is witnessed by the identity|9YVRTGXKZF]], because the interpretation of $\neg \neg \exists m\, \varphi(m)$ already contains the number $m$.
[[Contraction for a universal formula|XWHF8SMTEF]] needs a definition by cases on the quantifier-free matrix, and this is where decidability of atomic formulas enters.

### What it cannot interpret

[[Excluded middle for the halting problem|9NTJJMPZ29]] has no witness in T.
The formula $\forall n\, (\exists k\, P(n, k) \vee \neg \exists k\, P(n, k))$, with $P$ the halting relation, would need a function that picks the true side for each $n$, and that function would decide the halting problem.
So the interpretation cannot be applied to a classical proof as it stands.

Full extensionality in all finite types fails too.
Howard showed that its interpretation has no witness in T, and this is why the theory in the characterization theorem is only weakly extensional.

### From PA to system T

For a classical proof we first apply the Gödel-Gentzen [[negative translation|HGJVM49PA4]], and then the Dialectica interpretation.
If PA proves $\forall n\, \exists m\, \varphi(n, m)$ with $\varphi$ quantifier-free, then HA proves $\forall n\, \neg \neg \exists m\, \varphi(n, m)$.
The interpretation of $\neg \neg \exists m\, \varphi$ is $\exists m\, \neg \neg \varphi$, so soundness gives a closed term $t$ of type $\mathbb{N} \to \mathbb{N}$ with $\mathsf{T} \vdash \varphi(n, t\, n)$.

Two consequences follow at once.
First, $\bot^D$ is $\bot$, so a proof of $0 = 1$ in PA would give one in T, and PA is consistent if T is.
Second, every provably total function of PA is defined by a term of T, and so it is $\alpha$-recursive for some $\alpha < \varepsilon_0$.

### Watch out

The most common slip is to interpret a classical proof directly.
With excluded middle in the proof, the witness would decide the halting problem, as above, so the negative translation must come first.

A second slip is to let the witness of a conclusion depend on everything.
In $(A \to B)^D$ the term $U x$ sees only the witness $x$ of the premise, while the backward term $Y x v$ also sees the challenge $v$.
If you let $U$ depend on $v$, false statements get witnesses.
For $0 = 0 \to \exists u\, \forall v\, (v \le u)$ the term $U v = v$ would win, although no number is above every $v$.

A third slip is to forget decidability.
The proof uses $A \to A \wedge A$, and its witness must test $A_D$ at a point, so quantifier-free formulas must be decidable in T.

### History

Gödel published the interpretation in 1958, in the journal *Dialectica*, which gave it its name.
Spector extended it to classical analysis with [[bar recursion|8CCG6F2FAT]] in a paper of 1962.
Kreisel used functional interpretations to extract bounds from proofs, and Kohlenbach developed this into [[proof mining|XR1JXQG1CD]] in the 1990s and 2000s.

### Try it

First, give the interpretation of $\exists m\, \forall n\, (m \le n)$ and a witness.
The formula is already of the form $\exists x\, \forall y$, so it is its own interpretation, and the number $m = 0$ wins against every challenge $n$.

Second, interpret $\forall n\, \exists m\, (n < m) \to \exists k\, (10 < k)$ and find $U$ and $Y$.
The matrix is $Y f < f(Y f) \to 10 < U f$, and $Y f = 10$ with $U f = f(10)$ wins.

## Explanations

### L1 human

Read each statement as a game between a prover and a doubter.
The prover makes one move $x$, the doubter answers with one move $y$, and a simple check $A_D(x, y)$ says who wins.
For "every number has a larger one", the prover moves first with a rule $f$, the doubter names a number $n$, and the check is $n < f(n)$.
The rule $f(n) = n + 1$ wins every time.
A proof of the statement gives such a rule as a program, and every program of this kind stops.

### L2 human

Here is a proof that uses a lemma twice.
The lemma is $\forall n\, \exists m\, (n < m)$, and we prove $\forall n\, \exists m\, (n + 1 < m)$: apply the lemma to $n$ to get $m_1 > n$, then apply it to $m_1$ to get $m_2 > m_1 \ge n + 1$.
The interpretation of "lemma implies theorem" asks for $U$ and $Y$ with
$$Y f n < f(Y f n) \to n + 1 < U f n.$$
The forward part is the composite $U f n = f(f(n))$.
The backward part must name one point at which the lemma is tested, but the proof used the lemma at two points, $n$ and $f(n)$.
So we choose by cases: $Y f n = f(n)$ if $n < f(n)$, and $Y f n = n$ otherwise.

Check the first case: the premise $f(n) < f(f(n))$ and $n + 1 \le f(n)$ give $n + 1 < f(f(n))$.
In the second case the premise $n < f(n)$ is false, so the implication holds.
For $f(n) = n + 1$ we land in the first case with $U f n = n + 2$.
The lesson is the typical one: each use of a lemma becomes a forward composition, and each repeated use becomes a test that picks the challenge.

### L3 human

The Dialectica interpretation is the model of a functional interpretation: formulas become pairs of types, of witnesses and of challenges, and proofs become terms.
De Paiva's Dialectica categories make this structure categorical, and they are models of linear logic, which explains the special role of contraction.
Variants include Shoenfield's form for classical arithmetic, the Diller-Nahm variant, which collects finitely many challenges instead of choosing one, Kohlenbach's monotone interpretation and the bounded functional interpretation of Ferreira and Oliva.
With [[bar recursion|8CCG6F2FAT]] it reaches classical analysis by [[Spector's theorem|DSQJ1RA71N]].
Composed with the negative translation, it shows that PA proves no more $\Pi^0_2$ sentences than HA, a result that [[Friedman's A-translation|6CCK0TT69P]] gives in another way.
