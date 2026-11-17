---
tag: NJ1RCSBQ27
kind: example
name: Arithmetic as the metalanguage of its own truth
msc: ["03B99", "03F40"]
topics: [H8QZY0RZXZ]
audience: ug3
not_instance_of:
  - target: D9G8M42GKC
    note: a metalanguage for the truth of the sentences of arithmetic must define the set of true sentences, and no formula of arithmetic defines it, so arithmetic cannot be its own truth metalanguage
uses: [D9G8M42GKC, MFJXPAF0R0, 3PRW76471J, YRV6SYK2BY, 3K1AKGXF8A, DYAB23WA1X]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski%27s_undefinability_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Metalanguage
    locator: lead section
  - book: isbn:9780521857840
---

## Example

Let $L_A$ be the first-order language of arithmetic with $0$, $S$, $+$, $\cdot$ and $=$, and let $\mathcal{N}$ be the standard structure of the natural numbers.
Fix a [[Gödel numbering|MFJXPAF0R0]], and let $\ulcorner \varphi \urcorner$ be the numeral of the code of $\varphi$; here the corners are Gödel corners, not Quine corners.
We ask whether $L_A$ can serve as its own metalanguage for truth, that is, whether some formula $\mathrm{True}(x)$ of $L_A$ satisfies, for every sentence $\varphi$ of $L_A$,
$$\mathcal{N} \models \mathrm{True}(\ulcorner \varphi \urcorner) \iff \mathcal{N} \models \varphi.$$
We show that no such formula exists.

1. Suppose, for a contradiction, that $\mathrm{True}(x)$ is such a formula.
2. $\neg \mathrm{True}(x)$ is a formula with one free variable $x$.
3. The [[diagonal lemma|3PRW76471J]], applied to [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$ and to $\neg \mathrm{True}(x)$, gives a sentence $\lambda$ with $\mathsf{Q} \vdash \lambda \leftrightarrow \neg \mathrm{True}(\ulcorner \lambda \urcorner)$.
4. Every axiom of $\mathsf{Q}$ is true in $\mathcal{N}$, so by soundness every theorem of $\mathsf{Q}$ is true in $\mathcal{N}$. Hence $\mathcal{N} \models \lambda \iff \mathcal{N} \not\models \mathrm{True}(\ulcorner \lambda \urcorner)$.
5. Step 1 with $\varphi = \lambda$ gives $\mathcal{N} \models \mathrm{True}(\ulcorner \lambda \urcorner) \iff \mathcal{N} \models \lambda$.
6. Steps 4 and 5 give $\mathcal{N} \models \lambda \iff \mathcal{N} \not\models \lambda$, which is impossible.
7. So no formula $\mathrm{True}(x)$ exists. This is [[Tarski's undefinability theorem|YRV6SYK2BY]].

A metalanguage for the semantics of $L_A$ must be able to say "$\varphi$ is true in $\mathcal{N}$" for every sentence $\varphi$.
By step 7, $L_A$ cannot do this, so the pair ($L_A$ as object language, $L_A$ as truth metalanguage) is not an instance of [[object language and metalanguage|D9G8M42GKC]].

## Remarks

The sentence $\lambda$ says of itself, through its code, "I am not true", so the argument is a precise form of the [[liar sentence|DYAB23WA1X]].
The example does not say that $L_A$ cannot speak about its own syntax.
The property "$\varphi$ is provable in $\mathsf{PA}$" is expressed by a formula $\mathrm{Prov}(x)$ of $L_A$, and this is the basis of the incompleteness theorems.
So arithmetic is a metalanguage for its own syntax but not for its own truth.
Truth for $L_A$ can be defined in a richer metalanguage, for example in set theory, or in $L_A$ extended by a new predicate $T$ with axioms for it.
For each fixed $n$, truth for the sentences of complexity $\Sigma_n$ is definable in $L_A$; only truth for all sentences is not.

## Explanations

### L1 human

A language can talk about its own words: English has the word "word", and it can say that "cat" has three letters.
The trouble starts when a language tries to define which of its own sentences are true.
Then we can build a sentence that says "this sentence is not true".
If it is true, it is not true, and if it is not true, it is true.
For the language of arithmetic this argument is a theorem: arithmetic cannot define its own truth, and truth must be defined in a richer language.

### L2 human

We check the step from the diagonal lemma to the contradiction with truth values.

1. Write $A$ for "$\lambda$ is true in $\mathcal{N}$" and $B$ for "$\mathrm{True}(\ulcorner \lambda \urcorner)$ is true in $\mathcal{N}$".
2. Step 4 says that $A$ holds exactly when $B$ fails.
3. Step 5 says that $B$ holds exactly when $A$ holds.
4. If $A$ holds, then $B$ holds by step 3, and then $A$ fails by step 2.
5. If $A$ fails, then $B$ fails by step 3, and then $A$ holds by step 2.
6. Both cases are impossible, so the assumption of step 1 is false.

The typical use of this example is to explain why a theory of truth needs a metalanguage above the object language.
A trap is to conclude that arithmetic cannot describe its own provability: provability is definable, and only truth is not.
