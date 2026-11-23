---
tag: CZZAA0WXS3
kind: proof
name: Proof of Rosser's theorem
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
proves: DH9RQ61GVD
uses: [3K1AKGXF8A, TT8MXRTVBM, VK6WWSDMXK, 6M12VR1GT6, 3PRW76471J, Z0H1KA8ZHT]
methods: [0J0XBKG64S, 0ASJVEFA9J, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Rosser%27s_trick
    locator: Rosser sentence
  - book: isbn:9780521857840
  - book: isbn:9780521701464
---

## Proof

Suppose the first proof of $\neg R$ has code $q = 1000$.
To prove $R$, the theory must handle every candidate proof $y$ of $R$: those below $1000$ it checks one at a time, and those above $1000$ come after the proof $q$.
The only work is to show that $\mathsf{Q}$ can split every $y$ into these two cases, and the first steps do this.

Write $\underline{n}$ for the [[numeral|VK6WWSDMXK]] of $n$, and $x \le y$ for $\exists v \, (v + x = y)$.
The axioms of [[Robinson arithmetic|3K1AKGXF8A]] are numbered as in [[its axiom list|TT8MXRTVBM]]: (1) $Sx \ne 0$, (2) $Sx = Sy \to x = y$, (3) $x \ne 0 \to \exists y \, (x = Sy)$, (4) $x + 0 = x$, (5) $x + Sy = S(x + y)$.

### Facts about $\mathsf{Q}$

Each fact is a scheme, with one sentence for each $n \in \mathbb{N}$.

1. (Q-c) $\mathsf{Q} \vdash \underline{m} + \underline{k} = \underline{m + k}$ for all $m, k$.
   By induction on $k$, axiom 4 gives $k = 0$, and axiom 5 gives the step.
2. (Q-d) $\mathsf{Q} \vdash \forall u \, (Su + \underline{k} = S(u + \underline{k}))$.
   For $k = 0$ both sides equal $Su$ by axiom 4.
   For the step, $Su + S\underline{k} = S(Su + \underline{k}) = S(S(u + \underline{k})) = S(u + S\underline{k})$, by axiom 5, the induction hypothesis and axiom 5.
3. (Q-a) $\mathsf{Q} \vdash \forall x \, (x \le \underline{n} \to x = \underline{0} \vee \cdots \vee x = \underline{n})$, by induction on $n$ in steps 4 and 5.
4. Case $n = 0$: assume $v + x = 0$.
   If $x \ne 0$, axiom 3 gives $x = Su$, and axiom 5 gives $S(v + u) = 0$, against axiom 1, so $x = 0$.
5. Case $n + 1$: assume $v + x = S\underline{n}$ and $x \ne 0$.
   Axiom 3 gives $x = Su$, axiom 5 gives $S(v + u) = S\underline{n}$, and axiom 2 gives $v + u = \underline{n}$.
   By the induction hypothesis $u = \underline{k}$ for some $k \le n$, so $x = \underline{k + 1}$.
6. (Q-b) $\mathsf{Q} \vdash \forall x \, (x \le \underline{n} \vee \underline{n} \le x)$, by induction on $n$ in steps 7 to 9.
7. Case $n = 0$: axiom 4 gives $x + 0 = x$, so $0 \le x$ with $v := x$.
8. Case $n + 1$, first half: by the induction hypothesis, $x \le \underline{n}$ or $\underline{n} \le x$.
   If $x \le \underline{n}$, then $x = \underline{k}$ with $k \le n$ by Q-a, and $\underline{n + 1 - k} + x = \underline{n + 1}$ by Q-c, so $x \le \underline{n + 1}$.
9. Case $n + 1$, second half: assume $v + \underline{n} = x$.
   If $v = 0$, then $x = \underline{n}$ by Q-c, and $x \le \underline{n + 1}$ by step 8.
   If $v \ne 0$, then $v = Su$ by axiom 3, and by axiom 5 and Q-d, $u + S\underline{n} = S(u + \underline{n}) = Su + \underline{n} = x$, so $\underline{n + 1} \le x$.

### Setup

10. By [[arithmetization of syntax|6M12VR1GT6]], let $\mathrm{Prf}_T(y, x)$ represent in $\mathsf{Q}$ the relation "$y$ codes a proof in $T$ of the formula with code $x$".
    Let $\mathrm{neg}$ be the computable function with $\mathrm{neg}(\# \varphi) = \# \neg \varphi$, used as a term through a formula that represents it.
11. Let $\rho(x) := \forall y \, \big(\mathrm{Prf}_T(y, x) \to \exists z \, (z \le y \wedge \mathrm{Prf}_T(z, \mathrm{neg}(x)))\big)$.
    This is $\neg \mathrm{Prov}^{R}_T(x)$ up to logical equivalence.
12. The [[diagonal lemma|3PRW76471J]] gives $R$ with $\mathsf{Q} \vdash R \leftrightarrow \rho(\ulcorner R \urcorner)$.
    Write $\underline{r}$ for $\ulcorner R \urcorner$ and $\underline{r'}$ for $\ulcorner \neg R \urcorner$, so that $\mathsf{Q} \vdash \mathrm{neg}(\underline{r}) = \underline{r'}$.

### Part 1: $T \nvdash R$

13. Assume $T \vdash R$, and let $p$ code a proof of $R$.
    By representability, $T \vdash \mathrm{Prf}_T(\underline{p}, \underline{r})$.
14. $T$ is consistent and proves $R$, so no number codes a proof of $\neg R$.
    By representability, $T \vdash \neg \mathrm{Prf}_T(\underline{k}, \underline{r'})$ for each $k \le p$.
15. By Q-a and step 14, $T \vdash \neg \exists z \, (z \le \underline{p} \wedge \mathrm{Prf}_T(z, \underline{r'}))$.
16. Steps 13 and 15 refute the instance $y := \underline{p}$ of $\rho(\underline{r})$.
    So $T \vdash \neg \rho(\underline{r})$, and $T \vdash \neg R$ by step 12.
17. Steps 13 and 16 make $T$ inconsistent, so $T \nvdash R$.

### Part 2: $T \nvdash \neg R$

18. Assume $T \vdash \neg R$, and let $q$ code a proof of $\neg R$.
    By representability, $T \vdash \mathrm{Prf}_T(\underline{q}, \underline{r'})$.
19. $T$ is consistent and proves $\neg R$, so no number codes a proof of $R$.
    By representability, $T \vdash \neg \mathrm{Prf}_T(\underline{k}, \underline{r})$ for each $k \le q$.
20. We argue in $T$ for an arbitrary $y$ with $\mathrm{Prf}_T(y, \underline{r})$.
    By Q-b, $y \le \underline{q}$ or $\underline{q} \le y$.
21. If $y \le \underline{q}$, then $y = \underline{k}$ with $k \le q$ by Q-a, which contradicts step 19.
22. If $\underline{q} \le y$, then $z := \underline{q}$ satisfies $z \le y \wedge \mathrm{Prf}_T(z, \underline{r'})$ by step 18.
23. So $T \vdash \rho(\underline{r})$, and $T \vdash R$ by step 12.
    With the assumption of step 18, $T$ is inconsistent, so $T \nvdash \neg R$.

## Idea

The sentence $R$ asks which comes first, a proof of $R$ or a proof of $\neg R$.
An actual proof of either sentence has a standard code, and $\mathsf{Q}$ can check all codes below a standard number one by one.
So a proof of $R$ yields a refutation of $R$, and a proof of $\neg R$ yields a proof of $R$.
Only the facts Q-a and Q-b about numerals are needed, and no $\omega$-consistency.

Watch out: Q-b is not the statement $\forall x \, \forall y \, (x \le y \vee y \le x)$, which $\mathsf{Q}$ does not prove.
It is one sentence for each numeral $\underline{n}$, and the proof only ever compares $y$ with the numeral $\underline{q}$ or $\underline{p}$.

## Variants

The facts Q-a and Q-b are also used for the representation of minimization in [[arithmetization of syntax|6M12VR1GT6]].
The example on the [[Rosser provability predicate|Z0H1KA8ZHT]] uses the same two facts to show that $T$ proves the Rosser consistency statement.
Another proof uses two computably enumerable sets that no decidable set separates, and a formula that represents their separation in $\mathsf{Q}$.
