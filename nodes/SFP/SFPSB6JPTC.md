---
tag: SFPSB6JPTC
kind: proof
name: Proof of the diagonal lemma by diagonal substitution
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
proves: 3PRW76471J
uses: [6M12VR1GT6, MFJXPAF0R0, 3K1AKGXF8A, 5NVA2JRHPV]
methods: [0NTF6DMVAP, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_lemma
    locator: Proof
  - book: isbn:9780521857840
---

## Proof

We build a formula $\theta(x)$ that says "$\varphi$ holds of the diagonalization of $x$", and we apply $\theta$ to its own code.
Let $\varphi(x)$ be a formula with exactly one free variable $x$.
Let $\mathrm{sub}(n, m)$ be the code of the result of putting the numeral $\underline{m}$ for the variable $x$ in the formula with code $n$.

1. Define the diagonal function $d(n) := \mathrm{sub}(n, n)$.
   If $n = \# \theta$ for a formula $\theta(x)$, then $d(n) = \# \theta(\ulcorner \theta \urcorner)$.
2. The function $\mathrm{sub}$ is [[primitive recursive|5NVA2JRHPV]], by [[arithmetization of syntax|6M12VR1GT6]].
   So $d$ is primitive recursive, and in particular computable.
3. By the representability theorem, there is a formula $D(x, y)$ with
   $$\mathsf{Q} \vdash \forall y \, (D(\underline{n}, y) \leftrightarrow y = \underline{d(n)}) \quad \text{for every } n \in \mathbb{N}.$$
4. Choose a variable $y$ that does not occur in $\varphi(x)$, and define $\theta(x) := \exists y \, (D(x, y) \wedge \varphi(y))$.
   This is a formula with the single free variable $x$.
5. Let $k := \# \theta$, and define the sentence $\psi := \theta(\underline{k})$, which is $\exists y \, (D(\underline{k}, y) \wedge \varphi(y))$.
6. By step 1, $d(k) = \# \theta(\underline{k}) = \# \psi$, so the numeral $\underline{d(k)}$ is $\ulcorner \psi \urcorner$.
7. Step 3 with $n = k$, together with step 6, gives $\mathsf{Q} \vdash \forall y \, (D(\underline{k}, y) \leftrightarrow y = \ulcorner \psi \urcorner)$.
8. Replacing a subformula by a provably equivalent one, step 7 gives
   $$\mathsf{Q} \vdash \psi \leftrightarrow \exists y \, (y = \ulcorner \psi \urcorner \wedge \varphi(y)).$$
9. In first-order logic, $\exists y \, (y = t \wedge \varphi(y)) \leftrightarrow \varphi(t)$ is valid for every closed term $t$.
   With $t = \ulcorner \psi \urcorner$ this gives $\mathsf{Q} \vdash \psi \leftrightarrow \varphi(\ulcorner \psi \urcorner)$.
10. Since $T$ contains $\mathsf{Q}$, every theorem of $\mathsf{Q}$ is a theorem of $T$, so $T \vdash \psi \leftrightarrow \varphi(\ulcorner \psi \urcorner)$.

## Idea

The trick is to let a formula talk about the result of feeding a formula its own code.
The formula $\theta(x)$ says "$\varphi$ holds of the diagonalization of $x$".
Feed $\theta$ its own code, and the diagonalization of that code is the very sentence $\psi$ we just wrote down.
So $\psi$ says "$\varphi$ holds of me", and the representability of $d$ lets $\mathsf{Q}$ prove the equivalence.
Nothing in the argument uses the consistency of $T$.

## Variants

A variant uses $\theta(x) := \forall y \, (D(x, y) \to \varphi(y))$.
Step 9 then uses the valid equivalence $\forall y \, (y = t \to \varphi(y)) \leftrightarrow \varphi(t)$.
In a language with a function symbol $\mathsf{d}$ for $d$, as in $\mathsf{PRA}$, one can take $\psi := \varphi(\mathsf{d}(\underline{k}))$ for the code $k$ of $\varphi(\mathsf{d}(x))$.
That gives the [[strong diagonal lemma|7PZDPCVK7Z]], where the fixed point is a term equation and not only an equivalence.
The same construction, read for programs instead of formulas, proves [[Kleene's recursion theorem|F3Z30M606H]].
