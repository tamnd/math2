---
tag: EMK23RRKPR
kind: example
name: The Socrates syllogism is not valid in the propositional calculus
msc: ["03B05", "03B10"]
topics: [JDK63589SA]
audience: ug1
not_instance_of:
  - target: 09K9MWD2QQ
    note: the argument is valid only because of the words "all" and "is a", which the propositional calculus cannot express
uses: [1HK0VYWTV7, 086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Propositional_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
---

## Example

The most famous valid argument of all is invisible to the propositional calculus.
Here it is.
All humans are mortal.
Socrates is a human.
So Socrates is mortal.
The argument is correct, but its propositional form is not a valid [[logical consequence|1HK0VYWTV7]].

1. None of the three sentences has "not", "and", "or", "if ... then" or "if and only if" as its main word.
   So each sentence is an atom of propositional logic.
2. The three sentences are different, so they get three different variables $p$, $q$ and $r$.
3. The propositional form of the argument is
   $$\{ p, q \} \models r .$$
4. The valuation with $v(p) = 1$, $v(q) = 1$ and $v(r) = 0$ makes both premises true and the conclusion false.
5. So $\{ p, q \} \not\models r$, and the form is not valid.

In [[first-order logic|086QKPF0A6]] the same argument has the form
$$\forall x\, (H(x) \to M(x)),\ H(s) \models M(s),$$
where $H$ means "is a human", $M$ means "is mortal" and $s$ names Socrates.
In each structure where both premises are true, the first premise holds for the element named $s$, so $H(s) \to M(s)$ is true.
Since $H(s)$ is also true, the table of $\to$ makes $M(s)$ true, so the first-order form is valid.

## Remarks

The example shows the limit of the propositional calculus.
It sees how sentences are joined by connectives, but not what is inside an atomic sentence.
The word "all" and the link between "humans" in the first premise and "a human" in the second carry the argument, and the propositional language has no symbols for them.

A small change brings the argument back inside propositional logic.
If we replace the first premise by "if Socrates is a human, then Socrates is mortal", the form becomes $\{ q \to r,\ q \} \models r$.
This form is valid, by modus ponens.

Watch out.
"Not valid in the propositional calculus" does not mean "wrong".
The argument is correct; it only needs a stronger logic to show it.

## Explanations

### L1 human

The argument "all humans are mortal, Socrates is a human, so Socrates is mortal" is correct.
But propositional logic sees only three separate sentences, with no "and", "or", "not" or "if" between them.
For propositional logic, three separate sentences can be true, true and false.
So it cannot see why the conclusion must be true.
A stronger logic with the words "all" and "some" can see it.

### L2 human

The typical use is to decide which logic an argument needs.
Take "if the number is even, it is not prime unless it is two; the number is even and is not two; so it is not prime".
With $e$ for "the number is even", $t$ for "it is two" and $q$ for "it is prime", the form is
$$\{ e \to (\neg q \lor t),\ e \land \neg t \} \models \neg q .$$
A valuation that makes both premises true has $e = 1$ and $t = 0$, so the first premise forces $\neg q \lor 0 = 1$, that is, $q = 0$.
Check: then $\neg q = 1$, so this argument is valid by its propositional form, unlike the Socrates syllogism.
