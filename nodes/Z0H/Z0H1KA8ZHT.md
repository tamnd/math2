---
tag: Z0H1KA8ZHT
kind: example
name: The Rosser provability predicate
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
not_instance_of:
  - target: NB2BCZR40F
    note: "The formula has an extra clause after the proof relation, and the theory proves the negation of its instance at 0 = S0."
  - target: 4NBAX3VRQ7
    note: "The Rosser consistency statement is provable in the theory itself, unlike the standard consistency statement."
uses: [NB2BCZR40F, 6M12VR1GT6, TT8MXRTVBM, VM8TQ70CVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Rosser%27s_trick
    locator: lead section
  - book: isbn:9780521857840
---

## Example

The sentence $\neg (0 = S0)$ has a proof a few lines long.
Any proof of $0 = S0$, if one existed, would have to come before that short proof to count under Rosser's predicate, and the theory can check the few earlier candidates by hand.
So a consistent theory proves that $0 = S0$ is not Rosser-provable.

Let $T$ be a [[consistent|VM8TQ70CVJ]] theory that contains [[Robinson arithmetic|TT8MXRTVBM]] $\mathsf{Q}$ and has a decidable set of axioms.
Let $\mathrm{neg}$ be the primitive recursive function with $\mathrm{neg}(\# \varphi) = \# \neg \varphi$.
The Rosser provability predicate is
$$\mathrm{Prov}^{R}_T(x) := \exists y \, \big(\mathrm{Prf}_T(y, x) \wedge \forall z \le y \, \neg \mathrm{Prf}_T(z, \mathrm{neg}(x))\big).$$
It reads "there is a proof of $x$, and no proof of the negation of $x$ with a smaller or equal code".
We show that it behaves differently from the standard [[provability predicate|NB2BCZR40F]] $\mathrm{Prov}_T$, because $T$ proves the Rosser consistency statement $\neg \mathrm{Prov}^{R}_T(\ulcorner 0 = S0 \urcorner)$.

### The short proof and the finite check

1. $\mathsf{Q}$ proves $\neg (0 = S0)$, from axiom 1, $S0 \ne 0$, and the symmetry of equality.
   Let $p$ be the code of such a proof in $T$.
2. Since $p$ codes a proof of $\neg (0 = S0)$, representability gives $T \vdash \mathrm{Prf}_T(\underline{p}, \ulcorner \neg (0 = S0) \urcorner)$.
3. $T$ is consistent and proves $\neg (0 = S0)$, so no number codes a proof of $0 = S0$.
4. So for each $k \le p$, $T \vdash \neg \mathrm{Prf}_T(\underline{k}, \ulcorner 0 = S0 \urcorner)$, by representability.

### The argument inside $T$

5. We argue inside $T$ and assume $\mathrm{Prf}_T(y, \ulcorner 0 = S0 \urcorner)$ and $\forall z \le y \, \neg \mathrm{Prf}_T(z, \ulcorner \neg (0 = S0) \urcorner)$.
6. $\mathsf{Q}$ proves $y \le \underline{p} \vee \underline{p} \le y$, which is fact Q-b in [[the proof of Rosser's theorem|CZZAA0WXS3]].
7. If $\underline{p} \le y$, the second assumption with $z = \underline{p}$ gives $\neg \mathrm{Prf}_T(\underline{p}, \ulcorner \neg (0 = S0) \urcorner)$, against step 2.
8. If $y \le \underline{p}$, then $y = \underline{k}$ for some $k \le p$, by fact Q-a, against step 4.
9. Both cases give a contradiction, so $T \vdash \neg \mathrm{Prov}^{R}_T(\ulcorner 0 = S0 \urcorner)$.

## Remarks

In $\mathbb{N}$ the two predicates define the same set when $T$ is consistent.
If $T \vdash \varphi$, then $T \nvdash \neg \varphi$, so the least proof of $\varphi$ is a witness for $\mathrm{Prov}^{R}_T$, and the other direction holds by the form of the formula.
Yet $T$ proves the Rosser consistency statement and, by the [[second incompleteness theorem|4PZM5GJTR5]], not the standard one.

So the second theorem is about a formula, and not about the set of numbers the formula defines.
$\mathrm{Prov}^R_T$ satisfies the first [[derivability condition|F6H4STF9RG]], so for $T \supseteq \mathsf{PA}$ it must fail the second or the third.
The sentence of [[Rosser's theorem|DH9RQ61GVD]] uses the same extra clause, and that clause removes the need for $\omega$-consistency.

Watch out: a proof in $T$ of the Rosser consistency statement says nothing about whether $T$ is consistent.
We assumed consistency in step 3, and the theorem in $T$ follows from a finite search below $p$.

## Explanations

### L1 human

The Rosser predicate says "there is a proof of this statement, and no earlier proof of its opposite".
For the false statement $0 = 1$, its opposite $0 \ne 1$ has a short proof.
Any proof of $0 = 1$ would come after that short proof, so the Rosser predicate fails for $0 = 1$.
The theory can check this by looking only at the finitely many numbers below the short proof.

### L2 human

Fix the short proof $p$ of $0 \ne S0$.
Below $p$, the theory checks each number $k$ and finds that none is a proof of $0 = S0$.
Above $p$, every candidate proof $y$ of $0 = S0$ has the proof $p$ of the negation below it, so it does not count.
So the Rosser formula fails for $0 = S0$, and the theory proves this.
The same two cases, below a fixed numeral and above it, drive the proof of Rosser's theorem.
