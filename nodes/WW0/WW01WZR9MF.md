---
tag: WW01WZR9MF
kind: example
name: Variable capture in a substitution
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: XN8TQE6SRK
    fails: [9]
    note: y is not substitutable for x in the formula, so the replacement is not an admissible substitution
uses: [NCDZ969V7X, Y3FZTH5158]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Free and bound variables
  - book: isbn:9780122384523
    locator: Section 2.4
---

## Example

Let $<$ be a binary relation symbol and let $\varphi = \forall y \, (x < y)$, so that $\operatorname{FV}(\varphi) = \set{x}$.
We show that putting $y$ for $x$ in $\varphi$ is not an admissible [[substitution|NCDZ969V7X]].

1. The variable $x$ is free in $\varphi$, by the [[definition of free variables|Y3FZTH5158]].
2. The term $y$ contains the variable $y$, which is the variable of the quantifier $\forall y$.
3. So clause 9 of the [[definition of substitution|XN8TQE6SRK]] fails, and $y$ is not substitutable for $x$ in $\varphi$.
4. The blind replacement gives $\forall y \, (y < y)$. Its free variables are $\emptyset$, while an admissible substitution would give the free variables $(\set{x} \setminus \set{x}) \cup \set{y} = \set{y}$.
5. The meanings differ. Take $\mathbb{N}$ with the symbol $<$ read as $\le$, and the value $y = 1$. The intended claim "$1 \le$ every number" is false, since $1 \le 0$ fails. The blind result $\forall y \, (y \le y)$ is true.

## Remarks

The variable $y$ of the term has been captured by the quantifier $\forall y$.
The capture changed a formula about one element into a sentence about the whole structure.
The repair is to rename first: $\varphi$ is alpha-equivalent to $\forall z \, (x < z)$, and $(\forall z \, (x < z))[y/x] = \forall z \, (y < z)$ says that $y$ is below every element.
With a term that avoids $y$, such as a constant $c$, there is no capture: $\varphi[c/x] = \forall y \, (c < y)$.
Capture is the reason for the side condition in the rule "from $\forall x \, \psi$ infer $\psi[t/x]$".

## Explanations

### L1 human

The claim "every number $y$ is at least $x$" talks about one number $x$.
We want to put the number called $y$ in for $x$.
Written blindly, the result is "every number $y$ is at least $y$", which is a claim about all numbers and is always true.
The new $y$ was grabbed by "every number $y$".
The fix is to call the inner letter $z$ first: "every number $z$ is at least $y$".

### L2 human

We show that capture breaks the rule "from $\forall x \, \psi$ infer $\psi[t/x]$", with $\psi = \exists y \, \neg (x = y)$ and $t = y$.

1. In a structure with at least two elements, $\forall x \, \exists y \, \neg (x = y)$ is true: for each $a$ another element $b \neq a$ exists.
2. The blind replacement of $x$ by $y$ in $\psi$ gives $\exists y \, \neg (y = y)$.
3. This sentence is false in every structure, since $y = y$ always holds.
4. So the inference with capture leads from a true sentence to a false one.

The typical use of this example is to show why every proof system states the substitutability condition.
The trap is that the bad result is a well-formed formula, so only the check of clause 9 detects the error.
