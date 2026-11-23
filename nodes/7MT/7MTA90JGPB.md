---
tag: 7MTA90JGPB
kind: example
name: A list that affirms the consequent is not a derivation in L
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
not_instance_of:
  - target: 1MGMQX43B8
    note: the list infers p from p → q and q, which is not modus ponens and not any rule of the Hilbert system L, so the list is not a derivation in L
illustrates: [J7KFCFQRBT]
uses: [1MGMQX43B8, 0Y0MQYST0M, J7KFCFQRBT, H31CS3HK5P]
sources:
  - url: https://en.wikipedia.org/wiki/Affirming_the_consequent
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

A derivation must follow the rules exactly, and a step that only looks like modus ponens is not allowed.
Let $p$ and $q$ be propositional variables, and let $\Gamma = \{ p \to q, \ q \}$.
Consider the list of three formulas
$$p \to q, \qquad q, \qquad p,$$
offered as a derivation of $p$ from $\Gamma$ in the [[Hilbert system|1MGMQX43B8]] L.
Its last line is justified by "from $p \to q$ and $q$, infer $p$", which is [[affirming the consequent|J7KFCFQRBT]].
We check each line against the definition of a derivation in L.

1. Line 1, $p \to q$, is a member of $\Gamma$, so it is allowed.
2. Line 2, $q$, is a member of $\Gamma$, so it is allowed.
3. Line 3, $p$, is not an axiom of L, because every instance of A1, A2 and A3 is an implication and $p$ is a variable.
4. Line 3 is not a member of $\Gamma$.
5. Line 3 does not follow by [[modus ponens|0Y0MQYST0M]] from earlier lines.
   That needs an earlier line of the form $\alpha \to p$, and the earlier lines are $p \to q$ and $q$.

So line 3 meets none of the three conditions, and the list is not a derivation in L.

## Remarks

### No derivation exists at all

The failure is not only a fault of this list: no derivation of $p$ from $\Gamma$ exists.
Take the [[truth assignment|H31CS3HK5P]] $v$ with $v(p) = 0$ and $v(q) = 1$.
Then
$$v(p \to q) = 0 \to 1 = 1, \qquad v(q) = 1, \qquad v(p) = 0.$$
By the [[soundness theorem for propositional logic|XD629S54CS]], every formula derivable from $\Gamma$ is true under every assignment that makes all of $\Gamma$ true.
So $\Gamma \nvdash p$.

### What changes when the step is reversed

Change $\Gamma$ to $\{ p \to q, \ p \}$ and the list to $p \to q$, $p$, $q$.
This list is a derivation, since line 3 follows by modus ponens from lines 2 and 1.
If we added "affirming the consequent" as a rule, L would become unsound, because the rule leads from the true premises above to the false formula $p$.

## Explanations

### L1 human

A Hilbert system has only one way to get a new line: from "$A$" and "if $A$ then $B$", write "$B$".
The list here goes the wrong way: from "if $p$ then $q$" and "$q$", it writes "$p$".
In words: "if it rains, the street is wet; the street is wet; so it rains".
The street can be wet for another reason, so the step is not safe, and the system does not allow it.

### L2 human

We test a second list with the same error, from $\Delta = \{ \neg p \to q, \ q \}$.
Lines 1 and 2 are the hypotheses $\neg p \to q$ and $q$, and line 3 is $\neg p$, claimed "from lines 1 and 2".
The formula $\neg p$ is not an implication, so it is not an axiom, and it is not in $\Delta$.
No earlier line has the form $\alpha \to \neg p$, so modus ponens does not apply either.
Under $v(p) = 1$ and $v(q) = 1$ both hypotheses are true and $\neg p$ is false, so $\Delta \nvdash \neg p$ by soundness.
The trap is to accept a line because its formula seems true in the intended reading; in L only the form of the lines matters.
