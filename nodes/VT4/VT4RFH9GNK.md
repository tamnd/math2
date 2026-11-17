---
tag: VT4RFH9GNK
kind: example
name: Generalization on a variable free in a hypothesis
msc: ["03B10", "03F03"]
topics: [H8QZY0RZXZ]
audience: ug2
not_instance_of:
  - target: QPD3X471Q1
    note: as a step in derivations from hypotheses it is not a sound rule of inference, since it leads from the true hypothesis x = 0, with x assigned 0 in the natural numbers, to the false sentence for all x, x = 0
uses: [QPD3X471Q1, BKQ3YD6SVZ, 9X08XK5RV2, 1HK0VYWTV7]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_generalization
    locator: lead section
  - book: isbn:9780122384523
  - book: isbn:9781482237726
---

## Example

Consider first-order logic in the language with the constant $0$ and equality.
A sound [[rule of inference|QPD3X471Q1]] for derivations from hypotheses must preserve truth: whenever a structure and an assignment of the variables make the premises true, they make the conclusion true.
Unrestricted [[generalization|BKQ3YD6SVZ]] is the step "from $\varphi$ infer $\forall x\, \varphi$", allowed even when $x$ occurs free in a hypothesis.
We show that this step is not sound.

1. Take the hypothesis set $\Gamma = \set{x = 0}$.
2. Line 1 of a derivation from $\Gamma$ is $x = 0$, a hypothesis.
3. Line 2 is $\forall x\, (x = 0)$, by unrestricted generalization on line 1.
4. So the unrestricted system gives $\Gamma \vdash \forall x\, (x = 0)$.
5. Take the structure $\mathbb{N}$ of the natural numbers, with $0$ read as zero, and the assignment $s$ with $s(x) = 0$.
6. Under $s$ the hypothesis $x = 0$ is true, since $s(x) = 0$.
7. The sentence $\forall x\, (x = 0)$ is false in $\mathbb{N}$, since $1 \neq 0$.
8. So the premise is true and the conclusion is false under the same structure and assignment, and $\Gamma \not\models \forall x\, (x = 0)$.

The restricted rule repairs this: in a derivation from $\Gamma$, generalization on $x$ is allowed only when $x$ does not occur free in any formula of $\Gamma$.
The restricted rule preserves [[logical consequence|1HK0VYWTV7]]: if $\Gamma \models \varphi$ and $x$ is not free in $\Gamma$, then $\Gamma \models \forall x\, \varphi$.

9. Let $\mathcal{M}, s$ make every formula of $\Gamma$ true, and let $a$ be an element of $\mathcal{M}$.
10. The assignment $s[x \mapsto a]$ agrees with $s$ on every variable other than $x$, hence on every variable free in $\Gamma$.
11. The truth value of a formula depends only on the values of its free variables, so $\mathcal{M}, s[x \mapsto a]$ makes every formula of $\Gamma$ true.
12. From $\Gamma \models \varphi$ we get that $\mathcal{M}, s[x \mapsto a]$ makes $\varphi$ true.
13. Since $a$ was arbitrary, $\mathcal{M}, s$ makes $\forall x\, \varphi$ true.

In the derivation of steps 2 and 3, $x$ is free in the hypothesis $x = 0$, so the restricted rule blocks line 2.

## Remarks

The unrestricted step still preserves validity: if $\varphi$ is true in $\mathcal{M}$ under every assignment, so is $\forall x\, \varphi$.
This is why generalization is a correct rule for derivations without hypotheses, and why some books, such as Mendelson's, keep it unrestricted.
These books read a hypothesis with free variables as true for all values of its variables, and under that reading $x = 0$ is false in $\mathbb{N}$.
The price is a restriction in the [[deduction theorem|9X08XK5RV2]]: from $\set{x = 0} \vdash \forall x\, (x = 0)$ we may not conclude $\vdash x = 0 \to \forall x\, (x = 0)$, which is not valid.

## Explanations

### L1 human

Suppose we know that a particular number $x$ is zero.
We cannot conclude that every number is zero.
Generalization says "what holds for $x$ holds for all", and this is only correct when nothing special about $x$ was assumed.
Here we assumed $x = 0$, so $x$ is a particular number, and generalizing on it is a mistake.

### L2 human

We check the same failure with a second hypothesis, $\Gamma = \set{x < 1}$, in the natural numbers with the usual order.

1. With $s(x) = 0$, the hypothesis $0 < 1$ is true.
2. Unrestricted generalization gives $\forall x\, (x < 1)$.
3. This sentence is false, since $1 < 1$ fails.
4. The restricted rule forbids the step, because $x$ is free in $x < 1$.

The typical correct use of generalization is after proving $\varphi$ about an arbitrary $x$, with no hypothesis about $x$.
A trap is to forget hypotheses that were introduced earlier in a long derivation and still contain $x$ free.
