---
tag: PES0S9XQZ5
kind: example
name: Applications of first-order compactness
msc: ["03C07", "03C52", "03H15", "20F50", "05C40", "06A05"]
topics: [FBWW4J1XWG]
audience: ug2
illustrates: [1NR3HAWG9D]
uses: [1NR3HAWG9D, DKFGQTRYZE, MVCH6N9SNW, MEC3ZMC4F1, RX9MB386C5, 0QFT7Z76N5, JZNQTTMG58, 0KWFFMDF8T, 01CGSJ0GNQ, PZMGQMDN25]
sources:
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: Applications
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.6
---

## Example

Here is the most famous use of the [[compactness theorem|1NR3HAWG9D]]: it builds a model of arithmetic with a number larger than $0$, $1$, $2$, and every other natural number.
The same trick then shows that "finite", "every element has finite order", "connected" and "well-ordered" cannot be said in first-order logic.
Compactness says that a set of [[sentences|DKFGQTRYZE]] has a [[model|MVCH6N9SNW]] when every finite subset has one.
All signatures below are countable, and every structure has a nonempty domain.

Every argument has three moves.
First, add new constant symbols and write down a set $\Gamma$ of sentences that describes the strange object we want.
Second, satisfy each finite part of $\Gamma$ in a familiar structure.
Third, take the model of $\Gamma$ that compactness gives and read off its properties.
Two facts help with the bookkeeping.
Adding new constants to a structure does not change the truth of the old sentences, because a sentence only looks at the symbols in it.
The sentence $\lambda_n$, which says $\exists x_1 \cdots \exists x_n \bigwedge_{i < j} \neg\, x_i = x_j$, holds exactly in the structures with at least $n$ elements.

**A number above every numeral.**
Let $L_A$ have the constant $0$, the unary function $S$, the binary functions $+$ and $\cdot$, and the binary relation $<$.
Let $\mathfrak{N} = (\mathbb{N}, 0, S, +, \cdot, <)$, and let $\operatorname{Th}(\mathfrak{N})$ be the set of $L_A$-sentences true in $\mathfrak{N}$.
The numeral $\underline{n}$ is the term $S S \cdots S 0$ with $n$ copies of $S$, and its value in $\mathfrak{N}$ is $n$.

1. Add a new constant $c$, and let $\Gamma = \operatorname{Th}(\mathfrak{N}) \cup \{ \underline{n} < c : n \in \mathbb{N} \}$.
   So $\Gamma$ asks for a model of true arithmetic in which $c$ is above $0, 1, 2, \dots$.
2. Take a finite $\Gamma_0 \subseteq \Gamma$, and let $N$ be the largest $n$ with $(\underline{n} < c) \in \Gamma_0$, or $N = 0$ if there is none.
   Read $c$ as $N + 1$ in $\mathfrak{N}$.
3. Then $\underline{n} < c$ holds for each $n \le N$, since $n < N + 1$.
   The sentences of $\operatorname{Th}(\mathfrak{N})$ stay true, since adding $c$ changes nothing.
   So $\Gamma_0$ has a model.
4. By compactness, $\Gamma$ has a model.
   Forget $c$ to get an $L_A$-structure $\mathcal{M}$, and let $a$ be the old value of $c$.
   Then $\mathcal{M}$ satisfies every sentence true in $\mathfrak{N}$.
5. Suppose $h$ is an [[isomorphism|PZMGQMDN25]] from $\mathfrak{N}$ onto $\mathcal{M}$.
   By induction on $n$, $h(n)$ is the value of $\underline{n}$ in $\mathcal{M}$, since $h(0) = 0^{\mathcal{M}}$ and $h(n + 1) = S^{\mathcal{M}}(h(n))$.
6. Since $h$ is onto, $a = h(m)$ is the value of $\underline{m}$ for some $m$.
   The sentence $\underline{m} < c$ is in $\Gamma$, so $a < a$ in $\mathcal{M}$.
   But $\forall x \, \neg\, x < x$ is true in $\mathfrak{N}$, so it is true in $\mathcal{M}$, a contradiction.

So $\mathcal{M}$ satisfies the same sentences as $\mathbb{N}$ but is not isomorphic to it.
Since the axioms of [[Peano arithmetic|0QFT7Z76N5]] are true in $\mathfrak{N}$, $\mathcal{M}$ is a [[nonstandard model of arithmetic|1QWN5CV4CG]], and $a$ is an infinite number in it.
It follows that no set $\Phi$ of first-order sentences has as its models exactly the copies of $\mathfrak{N}$: such a $\Phi$ is true in $\mathfrak{N}$, so $\mathcal{M}$ is a model of it.

**Elements of finite order.**
Use the signature $\{ \cdot, {}^{-1}, e \}$ of groups, and write $t^n$ for $t \cdot t \cdots t$ with $n$ factors.
A [[torsion group|JZNQTTMG58]] is a group in which every element has finite order.
We show that no set of sentences has the torsion groups as its exact models, that is, they do not form an [[elementary class|MEC3ZMC4F1]].

7. Suppose $\Phi$ has exactly the torsion groups as its models.
   Add a constant $c$, and let $\Gamma = \Phi \cup \{ \neg\, c^n = e : n \ge 1 \}$.
8. Take a finite $\Gamma_0 \subseteq \Gamma$, and let $N$ be the largest $n$ with $(\neg\, c^n = e) \in \Gamma_0$, or $N = 1$.
   In the group $\mathbb{Z}/(N+1)\mathbb{Z}$, read $c$ as the class of $1$.
9. Then $c^n$ is the class of $n$, which is not $0$ for $1 \le n \le N$.
   The group is finite, so it is a torsion group and satisfies $\Phi$.
   So $\Gamma_0$ has a model.
10. By compactness, $\Gamma$ has a model $(H, g)$.
    Then $H$ satisfies $\Phi$, so it is a torsion group, but $g^n \ne e$ for every $n \ge 1$.
    This contradiction shows that no such $\Phi$ exists.

**Connected graphs.**
Use one binary relation $E$, and let a graph be a model of $\forall x \, \neg E x x$ and $\forall x \forall y \, (E x y \to E y x)$.
A graph is [[connected|0KWFFMDF8T]] when any two vertices are joined by a walk.
Let $\pi_0(x, y)$ be $x = y$, let $\pi_1(x, y)$ be $E x y$, and for $k \ge 2$ let $\pi_k(x, y)$ say that some $z_1, \dots, z_{k-1}$ give a walk $x, z_1, \dots, z_{k-1}, y$.

11. Suppose $\Phi$ has exactly the connected graphs as its models.
    Add constants $c$ and $d$, and let $\Gamma = \Phi \cup \{ \neg \pi_k(c, d) : k \ge 0 \}$.
12. For a finite $\Gamma_0$, let $N$ be the largest $k$ that occurs, or $N = 0$, and take the path with vertices $0, 1, \dots, N + 1$, with $c = 0$ and $d = N + 1$.
    Each step of a walk moves by $1$, so every walk from $0$ to $N + 1$ has length at least $N + 1$.
13. The path is connected, so it satisfies $\Phi$, and it has no walk of length $k \le N$ from $c$ to $d$.
    So $\Gamma_0$ has a model.
14. By compactness, $\Gamma$ has a model $(G, a, b)$.
    Then $G$ is a connected graph, so some walk of some length $k$ joins $a$ to $b$, and $\pi_k(c, d)$ holds, against $\Gamma$.

**Finite structures.**
Let $\Sigma$ be a set of sentences with arbitrarily large finite models: for every $N$, some finite model of $\Sigma$ has at least $N$ elements.

15. Let $\Gamma = \Sigma \cup \{ \lambda_n : n \ge 2 \}$.
    A finite part mentions $\lambda_n$ only for $n \le N$, and a finite model of $\Sigma$ with at least $N$ elements satisfies it.
16. By compactness, $\Gamma$ has a model, and it is an infinite model of $\Sigma$.
17. So no set $\Phi$ has as its models exactly the finite models of $\Sigma$: such a $\Phi$ has arbitrarily large finite models, and steps 15 and 16 give it an infinite model.
    With $\Sigma$ the group axioms and the groups $\mathbb{Z}/n\mathbb{Z}$, this shows that [[finiteness of a group is not first-order|3J825EJ81F]].

**Well-orders.**
Use one binary relation $<$.
A [[well-order|01CGSJ0GNQ]] is a strict total order in which every nonempty subset has a least element.

18. Suppose $\Phi$ has exactly the well-orders as its models.
    Add constants $c_0, c_1, c_2, \dots$, and let $\Gamma = \Phi \cup \{ c_{n+1} < c_n : n \ge 0 \}$.
19. For a finite $\Gamma_0$, pick $N$ above every index that occurs, and read $c_i$ as $N - i$ in $(\mathbb{N}, <)$ for $i \le N$, and as $0$ for $i > N$.
    Each sentence $c_{n+1} < c_n$ in $\Gamma_0$ has $n + 1 \le N$, and $N - n - 1 < N - n$.
20. By compactness, $\Gamma$ has a model $(A, <, a_0, a_1, \dots)$, and $(A, <)$ is a well-order.
    But the set $\{ a_n : n \in \mathbb{N} \}$ has no least element, since $a_{n+1} < a_n$ for every $n$.

## Remarks

### What the five arguments share

Each property says that something happens after finitely many steps, with no bound on the number of steps.
A group is torsion when each element satisfies $x^1 = e$ or $x^2 = e$ or $x^3 = e$, and so on without end.
A graph is connected when any two vertices satisfy $\pi_0$ or $\pi_1$ or $\pi_2$, and so on.
A well-order has no descending chain that goes on forever.
A first-order sentence is a finite string, so it can list only finitely many of these cases, and compactness turns that limit into a counterexample.

When a bound is fixed, the property becomes first-order.
The groups of exponent dividing $n$ are the models of the group axioms and the one sentence $\forall x \, (x^n = e)$.
A graph has diameter at most $n$ exactly when it satisfies $\forall x \forall y \, (\pi_0(x, y) \lor \cdots \lor \pi_n(x, y))$.

### The complements

The complement of such a class can be elementary.
The infinite $L$-structures are exactly the models of $\{ \lambda_n : n \ge 2 \}$.
They are not the models of a single sentence $\psi$, since then $\neg \psi$ would have exactly the finite structures as models.
The torsion-free groups are the models of the group axioms and $\forall x \, (x^n = e \to x = e)$ for $n \ge 2$, but [[no finite set of sentences does the job|APF4KHZ976]].

### Arithmetic and second-order logic

The first argument shows that first-order sentences cannot fix $\mathbb{N}$ up to isomorphism.
The second-order [[Peano axioms|0QFT7Z76N5]], with induction over all subsets, do fix it.
The argument for well-orders also works with $\Phi = \operatorname{Th}(\mathbb{N}, <)$, and gives an order with the same first-order sentences as $(\mathbb{N}, <)$ that is not a well-order.
With uncountably many new constants $c_i$ and the sentences $\neg\, c_i = c_j$ for $i \ne j$, the same method gives large models of every theory with an infinite model.
That is the upward [[Löwenheim-Skolem theorem|484M0TZ1S7]].
It adds uncountably many constants, so it needs compactness for uncountable signatures, which uses the axiom of choice.

### Watch out

The model that compactness gives is a model of $\Gamma$, and it need not be the kind of object the class was about.
In the torsion argument, $(H, g)$ is not a strange torsion group; the contradiction shows that $\Phi$ never described torsion groups.

Do not conclude that single structures cannot be described.
A finite structure is fixed up to isomorphism by one sentence that names its elements and lists its operations.
It is the infinite structures, such as $\mathbb{N}$, that first-order logic cannot pin down.

### Try it

First, show that the class of fields of positive characteristic is not elementary.
Suppose $\Phi$ describes it, and add the sentences $\neg\, p \cdot 1 = 0$ for all primes $p$.
Each finite part holds in $\mathbb{Z}/q\mathbb{Z}$ for a prime $q$ larger than the primes mentioned.
So compactness gives a field of positive characteristic in which $p \cdot 1 \ne 0$ for every prime $p$, which is impossible.

Second, why does the argument for finite structures need arbitrarily large finite models?
The sentence $\neg \lambda_6$ has models of every size from $1$ to $5$, and all its models are finite, so arbitrarily large finite models are needed.

## Explanations

### L1 human

Imagine a list of rules: "there are at least 2 things", "there are at least 3 things", and so on without end.
Any 5 rules from the list can be obeyed by a finite box: if the largest says "at least 100 things", a box with 100 things works.
Compactness says that the whole list can then be obeyed at once, and a box that obeys every rule must be infinite.
So no list of first-order rules can say "there are only finitely many things".
The same trick builds a "number" that is bigger than $0$, bigger than $1$, bigger than $2$, and so on, inside a world that obeys every true law of arithmetic.

### L2 human

We run the key step of the well-order argument for one finite part.
Let $\Gamma_0 = \Phi_0 \cup \{ c_1 < c_0, \ c_2 < c_1, \ c_3 < c_2 \}$, where $\Phi_0$ is a finite part of $\Phi$.
The constants that occur are $c_0, c_1, c_2, c_3$, so $N = 3$, and we read the constants in $(\mathbb{N}, <)$ as follows.
$$c_0 = 3, \quad c_1 = 2, \quad c_2 = 1, \quad c_3 = 0.$$
Check: $2 < 3$, $1 < 2$ and $0 < 1$, so the three new sentences hold, and $(\mathbb{N}, <)$ is a well-order, so it satisfies $\Phi_0$.

Each finite part needs only a finite descending chain, and $\mathbb{N}$ has descending chains of every finite length.
The whole of $\Gamma$ needs an infinite descending chain, which no well-order has.
This is the typical use: to show that a property is not first-order, describe a failure of the property "beyond every finite stage" with new constants.

### L3 human

The applications show that elementary classes are closed under passing to a limit.
An elementary class is closed under [[ultraproducts|AX9Q86GB8M]] by [[Łoś's theorem|AGYBSTD7BG]], and a non-principal ultraproduct of the groups $\mathbb{Z}/n\mathbb{Z}$ contains an element of infinite order.
This gives a second proof for torsion groups, and similar ultraproducts give the other cases.
A logic that extends first-order logic and expresses finiteness, connectedness or well-order cannot be compact.
[[Second-order logic|G6X7SZSNC5]] expresses all three, and it is not compact.
By [[Lindström's theorem|FYZ3CJGZYV]], first-order logic is a maximal logic with compactness and the downward Löwenheim-Skolem property.
Over finite structures compactness fails, yet connectedness is still not first-order; there the proof uses [[Ehrenfeucht-Fraïssé games|2RE7YAZK8R]] instead.
