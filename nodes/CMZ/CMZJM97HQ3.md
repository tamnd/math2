---
tag: CMZJM97HQ3
kind: example
name: A Δ0 truth predicate in Robinson arithmetic
msc: ["03F30"]
topics: [HXHHWY3328]
audience: grad
instance_of: [Y2MF1EZAM7]
uses: [Y2MF1EZAM7, 3K1AKGXF8A, 6M12VR1GT6, PPGD5KW8JC, WP27CABPA4]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
    locator: Metamathematics
  - book: isbn:9780521857840
---

## Example

A $\Delta_0$ sentence is a sentence whose quantifiers are all bounded, of the form $\forall x \le t$ or $\exists x \le t$ for a term $t$.
For instance, $\forall x \le \underline{3} \, (x \cdot x \ne \underline{5})$ is a true $\Delta_0$ sentence: the squares of $0, 1, 2, 3$ are $0, 1, 4, 9$.
We build a formula $\mathrm{Tr}_0(x)$ that is a [[partial truth predicate|Y2MF1EZAM7]] for $\Delta_0$ sentences in [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$.
That is, $\mathsf{Q} \vdash \mathrm{Tr}_0(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every $\Delta_0$ sentence $\varphi$.

1. The truth of a $\Delta_0$ sentence in $\mathbb{N}$ can be computed.
   Evaluate the closed terms, and check each bounded quantifier by a finite search, as in the instance above.
2. So the set $D := \{ \# \varphi : \varphi \text{ is a true } \Delta_0 \text{ sentence} \}$ is [[decidable|PPGD5KW8JC]].
3. By the representability theorem, some formula $\mathrm{Tr}_0(x)$ represents $D$ in $\mathsf{Q}$.
   So $\mathsf{Q} \vdash \mathrm{Tr}_0(\underline{n})$ when $n \in D$, and $\mathsf{Q} \vdash \neg \mathrm{Tr}_0(\underline{n})$ when $n \notin D$.
4. $\mathsf{Q}$ proves every true $\Delta_0$ sentence, by [[Σ1-completeness|69234Z1V00]].
5. Let $\varphi$ be a true $\Delta_0$ sentence.
   By step 3, $\mathsf{Q} \vdash \mathrm{Tr}_0(\ulcorner \varphi \urcorner)$, and by step 4, $\mathsf{Q} \vdash \varphi$.
   Two theorems are provably equivalent, so $\mathsf{Q}$ proves the biconditional.
6. Let $\varphi$ be a false $\Delta_0$ sentence.
   Then $\neg \varphi$ is a true $\Delta_0$ sentence, so $\mathsf{Q} \vdash \neg \varphi$ by step 4.
   Also $\mathsf{Q} \vdash \neg \mathrm{Tr}_0(\ulcorner \varphi \urcorner)$ by step 3, so $\mathsf{Q}$ proves the biconditional.
7. Steps 5 and 6 cover every $\Delta_0$ sentence, so $\mathsf{Q} \vdash \mathrm{Tr}_0(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for each of them.

## Remarks

The construction uses only two facts: $\mathsf{Q}$ decides every $\Delta_0$ sentence, and $\mathsf{Q}$ represents every decidable set.
So it works for any decidable set of sentences that $\mathsf{Q}$ decides one by one.

The result is a list of theorems, one for each sentence.
It does not give the general statement "for all $\Delta_0$ formulas and all assignments, $\mathrm{Sat}$ obeys the Tarski conditions" as one theorem of $\mathsf{Q}$.
That uniform version needs a satisfaction formula for formulas with free variables and some induction, as in $\mathsf{I}\Sigma_1$.
It is the base case for the $\Sigma_n$ truth predicates built on the concept page.

## Explanations

### L1 human

A sentence that only talks about numbers below fixed bounds can be checked by a finite computation.
For example, "no number from $0$ to $3$ has square $5$" is checked by squaring four numbers.
Robinson arithmetic proves each such true sentence and refutes each false one.
So a formula that describes the checking procedure says correctly, and provably, which of these sentences are true.

### L2 human

We test the construction on $\varphi := \exists x \le \underline{2} \, (x + x = \underline{4})$.
The search gives $0 + 0 = 0$, $1 + 1 = 2$ and $2 + 2 = 4$, so $\varphi$ is true and $\# \varphi \in D$.
Representability gives $\mathsf{Q} \vdash \mathrm{Tr}_0(\ulcorner \varphi \urcorner)$, and $\Sigma_1$-completeness gives $\mathsf{Q} \vdash \varphi$, so $\mathsf{Q}$ proves the biconditional.
The typical use is as the base case for $\Sigma_n$ truth predicates.
Watch out: the argument works one sentence at a time, and it does not prove the biconditional for all formulas uniformly.
