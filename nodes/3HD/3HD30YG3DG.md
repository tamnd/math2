---
tag: 3HD30YG3DG
kind: statement
role: theorem
name: Löb's theorem
msc: [03F40, 03F45]
uses: [0QFT7Z76N5, MFJXPAF0R0, DKFGQTRYZE, 92SWXST1ZM, TN9G24VABN]
about: [MFJXPAF0R0]
sources:
  - url: https://en.wikipedia.org/wiki/Löb's_theorem
same_as:
  wikidata: Q204884
  wikipedia: Löb's theorem
---

## Statement

Let $T$ be a [[theory|92SWXST1ZM]] in the language of arithmetic that contains the [[Peano axioms|0QFT7Z76N5]] and whose set of axioms is [[computably enumerable|TN9G24VABN]].
Let $\mathrm{Prov}_T(x)$ be the standard provability predicate of $T$ for a [[Gödel numbering|MFJXPAF0R0]].
For every [[sentence|DKFGQTRYZE]] $\varphi$, if $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$, then $T \vdash \varphi$.

## Remarks

Proof idea: by the [[diagonal lemma|3PRW76471J]] there is $\psi$ with $T \vdash \psi \leftrightarrow (\mathrm{Prov}_T(\ulcorner \psi \urcorner) \to \varphi)$.
The derivability conditions of $\mathrm{Prov}_T$, which $T$ proves, give $T \vdash \mathrm{Prov}_T(\ulcorner \psi \urcorner) \to \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
With the hypothesis this yields $T \vdash \mathrm{Prov}_T(\ulcorner \psi \urcorner) \to \varphi$, hence $T \vdash \psi$, hence $T \vdash \mathrm{Prov}_T(\ulcorner \psi \urcorner)$, and finally $T \vdash \varphi$.

Example: take $\varphi$ to be $0 = S0$.
If $T$ proved $\mathrm{Con}(T)$, that is, $\neg \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, then $T$ would prove $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner) \to 0 = S0$, and so $T \vdash 0 = S0$.
So a consistent $T$ does not prove its own consistency, which is the second of [[Gödel's incompleteness theorems|X9WYNYE29C]].
Another consequence: the sentence that says "I am provable" is provable, which answers a question of Henkin.

## Explanations

### L1 human

A theory can never prove "if I prove $\varphi$, then $\varphi$ is true" unless it already proves $\varphi$ itself.
So a theory cannot vouch for its own soundness, even one sentence at a time.

### L2 human

Löb's theorem generalizes the second incompleteness theorem, as the example shows.
Its formalized version, $\square(\square p \to p) \to \square p$, is the characteristic axiom of the modal [[provability logic|WJK0YA4GP2]] $\mathsf{GL}$, read with $\square$ as "it is provable in $T$ that".
