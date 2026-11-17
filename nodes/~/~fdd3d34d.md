---
tag: ~fdd3d34d
kind: proof
name: Proof of Frege's theorem from Hume's principle
msc: ["03B16", "03F35"]
topics: [MDHDYV8QZW]
audience: grad
proves: J36EHBHF6J
uses: [~205409ab, VT2Q5BZEGH, 0B0KR7FH2Q, 0J0XBKG64S]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Frege%27s_theorem
    locator: Overview
  - url: https://en.wikipedia.org/wiki/Hume%27s_principle
    locator: lead section
---

## Proof

We use the notation of the [[statement|J36EHBHF6J]].
All concepts and relations below exist by the [[comprehension schema|~205409ab]].
We describe a relation $R$ with $F \approx G$ as a bijection $f$ from the $F$-objects onto the $G$-objects.
Write $F^{-y}$ for the concept $[x : F(x) \land x \neq y]$.

**Lemma E** ($\#F = 0$ exactly when nothing falls under $F$).

1. Suppose $\#F = 0 = \#[x : x \neq x]$. HP gives a bijection from the $F$-objects onto the objects $x$ with $x \neq x$.
2. No object satisfies $x \neq x$, so no object falls under $F$.
3. Conversely, suppose nothing falls under $F$. Then both conditions of $F \approx [x : x \neq x]$ are vacuous, so HP gives $\#F = 0$.

**Lemma I** (coextensive concepts have the same number).

4. If $\forall x \, (F(x) \leftrightarrow G(x))$, the relation $x = y$ is a bijection from the $F$-objects onto the $G$-objects. HP gives $\#F = \#G$.

**Sentence 1.**

5. $0 = 0$, so $P^{*=}(0, 0)$, which is $N(0)$.

**Sentence 2.**

6. Suppose $P(m, 0)$. Then some $F$ and $y$ satisfy $F(y)$ and $\#F = 0$.
7. By Lemma E, nothing falls under $F$; this contradicts $F(y)$.

**Sentence 3** ($P$ is functional).

8. Suppose $P(m, n)$ via $F, y$ and $P(m, n')$ via $G, z$. Then $\#F^{-y} = m = \#G^{-z}$.
9. HP gives a bijection $g$ from the $F^{-y}$-objects onto the $G^{-z}$-objects.
10. Extend $g$ by $y \mapsto z$. Since $F(y)$, $G(z)$, and $y, z$ are outside the domain and range of $g$, this is a bijection from the $F$-objects onto the $G$-objects.
11. HP gives $n = \#F = \#G = n'$.

**Sentence 4** ($P$ is injective).

12. Suppose $P(m, n)$ via $F, y$ and $P(m', n)$ via $G, z$. HP gives a bijection $f$ from the $F$-objects onto the $G$-objects.
13. Let $b := f(y)$ and let $a$ be the $F$-object with $f(a) = z$.
14. If $a = y$, then $f$ maps the $F^{-y}$-objects onto the $G^{-z}$-objects.
15. If $a \neq y$, then $b \neq z$. Define $h(a) := b$ and $h(x) := f(x)$ for the other $F^{-y}$-objects $x$.
16. In that case, $h$ is a bijection from the $F^{-y}$-objects onto the $G^{-z}$-objects: $f$ takes the value $b$ only at $y$, and $z$ only at $a$.
17. In both cases, HP gives $m = \#F^{-y} = \#G^{-z} = m'$.

**Lemma A** ($P^{*=}(a, b) \land P(b, c) \to P^*(a, c)$).

18. Let $X$ contain every $x$ with $P(a, x)$, and let $X$ be closed under $P$. We show $X(c)$.
19. If $a = b$, then $P(a, c)$, so $X(c)$.
20. If $P^*(a, b)$, then $X(b)$ by the definition of $P^*$, and $P(b, c)$ gives $X(c)$.
21. So $P^*(a, c)$ holds by the definition of $P^*$.

**Lemma B** ($P^*(a, c) \to \exists b \, (P^{*=}(a, b) \land P(b, c))$).

22. Let $Z := [x : \exists b \, (P^{*=}(a, b) \land P(b, x))]$.
23. If $P(a, x)$, then $Z(x)$ with $b = a$.
24. If $Z(x)$ and $P(x, y)$, then Lemma A gives $P^*(a, x)$, so $Z(y)$ with $b = x$.
25. By the definition of $P^*(a, c)$ applied to $Z$, we get $Z(c)$.

**Lemma D** ($P(a, b) \land P^*(b, c) \to P^*(a, c)$).

26. Let $Z := [x : P^*(a, x)]$. Lemma A, applied to $P^{*=}(a, a)$ and $P(a, b)$, gives $P^*(a, b)$.
27. If $P(b, x)$, then Lemma A with $P^*(a, b)$ gives $Z(x)$.
28. If $Z(x)$ and $P(x, y)$, then Lemma A gives $Z(y)$.
29. By the definition of $P^*(b, c)$ applied to $Z$, we get $Z(c)$.

**Sentence 6** (induction).

30. Assume $X(0)$ and $\forall x \, \forall y \, (N(x) \land X(x) \land P(x, y) \to X(y))$. Let $Y := [x : N(x) \land X(x)]$.
31. If $P(0, x)$, then Lemma A with $P^{*=}(0, 0)$ gives $P^*(0, x)$, so $N(x)$. The assumption with $N(0)$ and $X(0)$ gives $X(x)$. So $Y(x)$.
32. If $Y(x)$ and $P(x, y)$, then the assumption gives $X(y)$, and Lemma A gives $P^*(0, y)$. So $Y(y)$.
33. Let $N(x)$. If $x = 0$, then $X(x)$ by assumption.
34. If $P^*(0, x)$, then steps 31 and 32 and the definition of $P^*$ give $Y(x)$, so $X(x)$.

**Lemma C** ($N(n) \to \neg P^*(n, n)$).

35. We use sentence 6 with $X := [x : \neg P^*(x, x)]$.
36. Base: if $P^*(0, 0)$, Lemma B gives some $b$ with $P(b, 0)$, which contradicts sentence 2.
37. Step: let $N(x)$, $\neg P^*(x, x)$ and $P(x, y)$, and suppose $P^*(y, y)$ for a contradiction.
38. Lemma B gives $b$ with $P^{*=}(y, b)$ and $P(b, y)$. Sentence 4 with $P(x, y)$ gives $b = x$.
39. If $y = x$, then $P(x, x)$, and Lemma A gives $P^*(x, x)$, a contradiction.
40. If $P^*(y, x)$, then Lemma D with $P(x, y)$ gives $P^*(x, x)$, a contradiction.
41. So $\neg P^*(y, y)$, and sentence 6 gives $\neg P^*(n, n)$ for every $n$ with $N(n)$.

**Sentence 5** (every number has a successor).

42. Let $s(n) := \#[x : P^{*=}(x, n)]$. We prove $P(n, s(n))$ for every $n$ with $N(n)$, by sentence 6.
43. Base: take $F := [x : P^{*=}(x, 0)]$ and $y := 0$. Then $F(0)$ and $\#F = s(0)$.
44. If $F(x)$ and $x \neq 0$, then $P^*(x, 0)$, and Lemma B gives some $b$ with $P(b, 0)$. This contradicts sentence 2.
45. So nothing falls under $F^{-0}$, and Lemma E gives $\#F^{-0} = 0$. Hence $P(0, s(0))$.
46. Step: let $N(n)$, $P(n, s(n))$ and $P(n, k)$. Sentence 3 gives $k = s(n)$.
47. Take $F := [x : P^{*=}(x, k)]$ and $y := k$. Then $F(k)$ and $\#F = s(k)$.
48. It remains to show $\#F^{-k} = k$. As $k = s(n)$, by Lemma I it suffices to show $\forall x \, (F^{-k}(x) \leftrightarrow P^{*=}(x, n))$.
49. Let $F^{-k}(x)$, so $P^*(x, k)$. Lemma B gives $b$ with $P^{*=}(x, b)$ and $P(b, k)$; sentence 4 gives $b = n$. So $P^{*=}(x, n)$.
50. Let $P^{*=}(x, n)$. Lemma A with $P(n, k)$ gives $P^*(x, k)$, so $F(x)$.
51. Suppose $x = k$ there. Then $P^{*=}(k, n)$ and $P(n, k)$.
52. If $k = n$, Lemma A gives $P^*(n, n)$. If $P^*(k, n)$, Lemma D gives $P^*(n, n)$. Both contradict Lemma C, as $N(n)$.
53. So $x \neq k$, and $F^{-k}(x)$. This proves $P(k, s(k))$, and sentence 6 gives $P(n, s(n))$ for all $n$ with $N(n)$.
54. Finally, $N(n)$ and $P(n, s(n))$ give $P^*(0, s(n))$ by Lemma A, so $N(s(n))$. This proves sentence 5.

## Idea

Numbers are numbers of concepts, and $n$ follows $m$ when removing one object from a concept with number $n$ leaves number $m$.
HP turns every question about numbers into a question about bijections, and bijections can be extended or patched one object at a time.
The natural numbers are the objects reachable from $0$ by $P$, so induction holds by definition of the ancestral.
The hard part is the successor of $n$: it is the number of the numbers up to $n$, and the proof needs that no number in $N$ precedes itself.

## Variants

- Frege's own proof in the Grundgesetze defines $\#F$ as an extension and derives HP from Basic Law V first; then it works from HP.
- One can define $N$ with the weak ancestral directly, $N(n) \leftrightarrow \forall X \, ((X(0) \land \forall x \, \forall y \, (X(x) \land P(x, y) \to X(y))) \to X(n))$; the two definitions are equivalent by Lemma A.
