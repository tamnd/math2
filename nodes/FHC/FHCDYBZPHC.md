---
tag: FHCDYBZPHC
kind: example
name: The Herbrand models of a recursive pair of clauses
msc: ["03B10", "68N17"]
topics: [NJDME6F845]
audience: ug2
instance_of: [HKW429DSDK]
uses: [JAKSE2A1D4, 7XKWHMNGQH, 1WTCZB4DVB]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Example

Let $L = \{ 0, s, P \}$, with $0$ a constant, $s$ unary and $P$ a unary relation symbol.
The [[Herbrand universe|7XKWHMNGQH]] is $\{ s^n(0) : n \in \mathbb{N} \}$, and the Herbrand base is $\{ P(s^n(0)) : n \in \mathbb{N} \}$.
Let
$$\Sigma = \{ P(0), \ \forall x \, (P(x) \to P(s(s(x)))) \}.$$
We find all [[Herbrand models|JAKSE2A1D4]] $\mathcal{H}_I$ of $\Sigma$, where $I$ is a set of ground atoms.

1. $\mathcal{H}_I \models P(0)$ if and only if $P(0) \in I$, because $0$ denotes itself.
2. Under the assignment $x \mapsto s^n(0)$, the term $s(s(x))$ has the value $s^{n+2}(0)$.
   So, by the clauses for $\forall$ and $\to$ of [[satisfaction|1WTCZB4DVB]], the second sentence holds exactly when, for every $n$, $P(s^n(0)) \in I$ implies $P(s^{n+2}(0)) \in I$.
3. Let $E = \{ P(s^{2k}(0)) : k \in \mathbb{N} \}$.
   If $\mathcal{H}_I \models \Sigma$, then $E \subseteq I$, by step 1 and induction on $k$ with step 2.
4. Conversely, $\mathcal{H}_E \models \Sigma$, because $P(0) \in E$, and if $n$ is even, then $n + 2$ is even.
5. For any $I \supseteq E$, step 2 shows that $\mathcal{H}_I \models \Sigma$ exactly when $I$ is closed under $P(s^n(0)) \mapsto P(s^{n+2}(0))$.

So the Herbrand models of $\Sigma$ are the sets $I \supseteq E$ that are closed under adding $2$ to the exponent, and the least one is $E$.
Three of them are $E$ itself, the whole base $B(L)$, and $E \cup \{ P(s^n(0)) : n \geq 7 \}$.

## Remarks

The example shows that a set of definite clauses has a least Herbrand model, here the "even numbers".
In logic programming, $\Sigma$ is the program `p(0). p(s(s(X))) :- p(X).`, and its meaning is the least Herbrand model $E$.
The query $P(s^3(0))$ fails, because $P(s^3(0)) \notin E$, although $P(s^3(0))$ is true in other Herbrand models, such as $B(L)$.

"True in the least Herbrand model" and "true in every model" differ for sentences in general.
For example, $\exists x \, \neg P(x)$ is true in $\mathcal{H}_E$, with the witness $s(0)$, but it is false in $\mathcal{H}_{B(L)}$, where every atom is true.
For ground atoms the two notions agree: $P(s^n(0))$ follows from $\Sigma$ if and only if $n$ is even.

Change the second clause to $\forall x \, (P(x) \to P(s(x)))$, and the least Herbrand model becomes the whole base, the set of all atoms.

## Explanations

### L1 human

The rules say: $0$ has property $P$, and whenever a number has $P$, so does the number two steps later.
The smallest choice that obeys the rules gives $P$ to $0, 2, 4, 6$, and so on, and to nothing else.
Larger choices are allowed too, but every choice must contain all the even numbers.

### L2 human

We check that $I = E \cup \{ P(s(0)) \}$ is not a Herbrand model of $\Sigma$.
Give $x$ the value $s(0)$.
Then $P(x)$ holds, because $P(s(0)) \in I$, so the second sentence needs $P(s^3(0)) \in I$, which fails.
Adding all the odd atoms, as in $B(L)$, repairs the model.
The typical use is to compute the meaning of a recursive logic program.
Watch out: the least Herbrand model is not the only model; it is the intersection of all the Herbrand models.
