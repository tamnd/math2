---
tag: PJ5X9TN6W4
kind: example
name: Embedding an induction axiom into the ω-system
msc: ["03F05", "03F15"]
topics: [XTTKZTYDSD]
audience: grad
instance_of: [XAMKAB1BZM]
uses: [1QD0KDDGYJ, 0QFT7Z76N5, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Theories with proof-theoretic ordinal ε0
---

## Example

Let $A(x)$ be a formula with only $x$ free, and let $r = \operatorname{rk}(A(\bar 0))$.
In the notation of [[the ω-rule|XAMKAB1BZM]], the closed instance of the [[induction schema|1QD0KDDGYJ]] for $A$ is the following formula $I_A$.
$$I_A := \neg A(\bar 0) \vee E \vee \forall x \, A(x), \qquad E := \exists x \, (A(x) \wedge \neg A(Sx))$$
A sequent is read as the disjunction of its members, so $I_A$ corresponds to the sequent $\neg A(\bar 0), E, \forall x \, A(x)$.
We show that this sequent has a cut-free derivation of height $\omega + 1$, and $I_A$ one of height $\omega + 5$.
The closed terms $S\bar n$ and $\overline{n+1}$ have the same value, so we exchange them freely.

### The tautology lemma

The lemma says $\vdash^{2 \operatorname{rk}(B)}_0 \Gamma, \neg B, B$ for every closed $B$ and every $\Gamma$, and we prove it by induction on $B$.
If $B$ is a literal, one of $B$ and $\neg B$ is true, so the sequent is an axiom of height $0$.
If $B = C \wedge D$, then $\neg B = \neg C \vee \neg D$.
From $\neg C, C$ the ($\vee$) rule gives $\neg B, C$, and in the same way we get $\neg B, D$.
The ($\wedge$) rule gives $\neg B, B$, so the height grows by $2$ while the rank grows by $1$, and the case $C \vee D$ is symmetric.
If $B = \forall x \, C(x)$, then $\neg B = \exists x \, \neg C(x)$.
From $\neg C(\bar n), C(\bar n)$ the ($\exists$) rule gives $\neg B, C(\bar n)$ for each $n$, and the ω-rule gives $\neg B, B$.
Again the height grows by $2$, and the case $\exists$ is symmetric.

### The derivation of the induction instance

1. Let $\Delta_n$ be the sequent $\neg A(\bar 0), E, A(\bar n)$.
   We show $\vdash^{2r + 2n}_0 \Delta_n$ by [[induction|0ASJVEFA9J]] on $n$.
2. Case $n = 0$: $\Delta_0$ contains $\neg A(\bar 0)$ and $A(\bar 0)$, so the tautology lemma gives height $2r$.
3. Step from $n$ to $n + 1$: weaken $\Delta_n$ by $A(\overline{n+1})$, and take $\neg A(\overline{n+1}), A(\overline{n+1})$ from the tautology lemma, also weakened.
4. The ($\wedge$) rule on $A(\bar n)$ and $\neg A(S\bar n)$ gives $\neg A(\bar 0), E, A(\overline{n+1}), A(\bar n) \wedge \neg A(S\bar n)$, with height at most $2r + 2n + 1$.
5. The ($\exists$) rule with witness $\bar n$ turns $A(\bar n) \wedge \neg A(S\bar n)$ into $E$, which is already in the sequent.
   This gives $\Delta_{n+1}$ with height $2r + 2n + 2$.
6. The ω-rule applied to all $\Delta_n$ gives $\neg A(\bar 0), E, \forall x \, A(x)$, with height $\sup_n (2r + 2n) + 1 = \omega + 1$.
7. Four ($\vee$) steps give $I_A$.
   Two of them join $E$ and $\forall x \, A(x)$ into $E \vee \forall x \, A(x)$, and two more join $\neg A(\bar 0)$ to it, so the height is $\omega + 5$.

## Remarks

The height $\omega + 1$ does not depend on $A$.
The rank $r$ only shifts the finite heights $2r + 2n$, and their supremum is $\omega$ for every $r$.
This is why every PA-proof embeds with a height $\omega + m$ for a finite $m$: each induction axiom costs one ω-rule on top of finite derivations.

In PA, induction is an axiom.
In the ω-system it is a theorem, and the infinitely many premises do the work that the axiom did.
If $A$ has more free variables, the same derivation works for each choice of numerals for them.

## Explanations

### L1 human

The induction principle says: if a property holds for $0$ and passes from each number to the next, then it holds for all numbers.
In the infinite system we prove the property for $0$, then for $1$, then for $2$, each with a finite derivation that is two steps longer than the one before.
One application of the ω-rule collects all of them.
The length of the result is just past the first infinite ordinal $\omega$.

### L2 human

We run the derivation for $A(x) := (x = x)$, a literal, so $r = 0$.

1. $\Delta_0 = \neg A(\bar 0), E, A(\bar 0)$ is an axiom of height $0$, since $0 = 0$ is a true literal.
2. $\Delta_1$ has height $2$: one ($\wedge$) step and one ($\exists$) step on top of $\Delta_0$ and an axiom.
3. In the same way $\Delta_n$ has height $2n$.
4. The ω-rule gives the sequent with height $\omega + 1$, and four ($\vee$) steps give $I_A$ with height $\omega + 5$.

Here each $A(\bar n)$ is itself an axiom, so a shorter derivation exists, but the general recipe does not use this.
The typical use is the embedding lemma for PA, where each induction axiom is replaced by a derivation of this kind.
Watch out: the heights $2r + 2n$ are finite but unbounded, so the ω-rule step needs height $\omega + 1$, and no finite height will do.
