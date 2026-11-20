---
tag: F8E0PCTM2R
kind: example
name: Every man is singing by lambda conversion
msc: ["03B65", "03B40"]
topics: [NJB94B39QK]
audience: research
instance_of: [FT512R206H]
uses: [FT512R206H, BD756KR8FM, Y9B9CVY6SJ, MFV98WTF4G]
sources:
  - url: https://plato.stanford.edu/entries/montague-semantics/
    locator: Montague Semantics (SEP entry), section 4.3
---

## Example

This is the small grammar of the SEP entry, in the style of [[Montague grammar|FT512R206H]], without intensions.
The basic expressions and their translations are these:

| expression | category | type | translation |
| --- | --- | --- | --- |
| John | proper name | $e$ | $\mathbf{john}$ |
| sing | intransitive verb | $\langle e, t \rangle$ | $\mathbf{sing}$ |
| man | common noun | $\langle e, t \rangle$ | $\mathbf{man}$ |
| every | determiner | $\langle \langle e, t \rangle, \langle \langle e, t \rangle, t \rangle \rangle$ | $\lambda P \lambda Q\, \forall x\, (P(x) \to Q(x))$ |

The grammar has three rules, each with a semantic rule.

- R1 (lifting). A proper name $\alpha$ with translation $a$ is a noun phrase with translation $\lambda P\, P(a)$, of type $\langle \langle e, t \rangle, t \rangle$.
- R2. A determiner $\delta$ and a common noun $\nu$ give the noun phrase $\delta\nu$, with translation $\delta'(\nu')$.
- R3. A noun phrase $\eta$ and an intransitive verb $\beta$ give a sentence, with translation $\eta'(\beta')$.

"John is singing".

1. By R1, "John" as a noun phrase translates to $\lambda P\, P(\mathbf{john})$.
2. By R3, the sentence translates to $(\lambda P\, P(\mathbf{john}))(\mathbf{sing})$.
3. One [[beta reduction|Y9B9CVY6SJ]] gives $\mathbf{sing}(\mathbf{john})$.

"Every man is singing".

4. By R2, "every man" translates to $(\lambda P \lambda Q\, \forall x\, (P(x) \to Q(x)))(\mathbf{man})$.
5. Beta reduction gives $\lambda Q\, \forall x\, (\mathbf{man}(x) \to Q(x))$.
6. By R3, the sentence translates to $(\lambda Q\, \forall x\, (\mathbf{man}(x) \to Q(x)))(\mathbf{sing})$.
7. Beta reduction gives $\forall x\, (\mathbf{man}(x) \to \mathbf{sing}(x))$.

Each step is type-correct: in steps 2 and 6, a function of type $\langle \langle e, t \rangle, t \rangle$ is applied to an argument of type $\langle e, t \rangle$.

## Remarks

In a model with domain $D$, the noun phrase "John" denotes the set of all $X \subseteq D$ with $\mathbf{john} \in X$, and "every man" denotes the set of all $X$ with $\mathbf{man} \subseteq X$.
So both noun phrases have the same type, as [[generalized quantifiers|MFV98WTF4G]] of type $\langle 1 \rangle$.
The determiner "every" denotes the relation $\mathbf{man} \subseteq \mathbf{sing}$ between two sets, a quantifier of type $\langle 1, 1 \rangle$.
The verb has a subordinate role in the result: it occurs inside the formula, although "every man" and "sing" are on the same syntactic level.
[[Lambda abstraction|BD756KR8FM]] makes this switch of level possible.

## Explanations

### L1 human

We give each word a small piece of logic.
"Every" says "for all $x$, if $P$ then $Q$", with two holes $P$ and $Q$.
"Man" fills the first hole and "singing" fills the second, and we get "every $x$ that is a man is singing".

### L2 human

Proper names are lifted to sets of properties so that they have the same type as "every man".
Then one rule, "apply the noun phrase to the verb", works for both sentences.
Beta reduction removes the lambdas and gives the formula from a first logic course.
A trap is to think that "every man" must denote some object; it denotes a function on properties.
