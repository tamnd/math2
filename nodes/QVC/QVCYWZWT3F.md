---
tag: QVCYWZWT3F
kind: example
name: Quantifiers as epsilon terms
msc: ["03B10", "03F05"]
topics: [PSRDJXRW53]
audience: grad
instance_of: [TH5ZKCKN3W]
uses: [TH5ZKCKN3W, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_calculus
    locator: Epsilon operator
---

## Example

Let $R$ be a binary relation symbol, and let $\varphi = \exists x \, \forall y \, R(x, y)$.
We translate $\varphi$ into the [[epsilon calculus|TH5ZKCKN3W]] by the rules $\exists x \, A \mapsto A(\varepsilon x \, A)$ and $\forall y \, B \mapsto B(\varepsilon y \, \neg B)$, working from the inside out.

1. The inner part $\forall y \, R(x, y)$ becomes $R(x, \varepsilon y \, \neg R(x, y))$.
   Call this formula $B(x)$; it has the free variable $x$ and no quantifier.
2. The term $\varepsilon y \, \neg R(x, y)$ contains $x$ free.
   So for each $x$ it names a candidate counterexample, a $y$ with $\neg R(x, y)$ if there is one.
3. The sentence $\varphi$ is $\exists x \, B(x)$, and it becomes $B(t)$ with $t = \varepsilon x \, B(x)$.
4. Written out, $t = \varepsilon x \, R(x, \varepsilon y \, \neg R(x, y))$, and the translation of $\varphi$ is
   $$R\big( t, \varepsilon y \, \neg R(t, y) \big).$$
5. The [[substitution|NCDZ969V7X]] of $t$ for $x$ in $B(x)$ is allowed.
   Reason: $t$ is closed, so no variable of $t$ can be captured.
6. The result has no quantifiers.
   Its only binding operators are the $\varepsilon$ symbols inside the terms.

So $\varphi$ is equivalent in the epsilon calculus to a quantifier-free formula about the term $t$.

## Remarks

Check the meaning in $(\mathbb{N}, \le)$, with $R$ read as $\le$ and $\varepsilon$ read by the choice "least element, and $0$ for the empty set".
For each $x$, the set of $y$ with $\neg (x \le y)$ is $\{ 0, \dots, x - 1 \}$.
So $\varepsilon y \, \neg R(x, y)$ is $0$ for $x \ge 1$, and $0$ by default for $x = 0$.
Then $B(x)$ says $x \le 0$, and $t$ is the least such $x$, which is $0$.
The translation says $0 \le 0$, which is true, and $\varphi$ is true too, since $0$ is below every number.

## Explanations

### L1 human

"There is an $x$ related to every $y$" becomes: "the chosen candidate $t$ is related to the chosen counterexample for $t$".
If even the chosen counterexample fails to refute $t$, then nothing refutes $t$, so $t$ is related to every $y$.

### L2 human

We see why $\forall y \, B$ becomes $B(\varepsilon y \, \neg B)$.
The term $s = \varepsilon y \, \neg B$ names a $y$ where $B$ fails, if there is one.
The critical formula for $\neg B$ is $\neg B(y) \to \neg B(s)$.
So if $B(s)$ holds, then no $y$ makes $B$ fail, and $\forall y \, B$ holds; the converse is an instance of $\forall y \, B$.
The typical use is in the epsilon substitution method, which tries values for $t$ and $s$ in turn.
Watch out: nested $\varepsilon$-terms grow fast, so the translations of long formulas are large.
