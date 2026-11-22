---
tag: TCZFSKFQ94
kind: proof
name: Proof of the existence of a vector whose annihilator is the minimal polynomial
msc: ["15A21", "15A04"]
topics: [GEBYZKYV3D]
audience: ug2
proves: QPE5Y86Y8V
methods: [0NTF6DMVAP, 0J0XBKG64S, 0ASJVEFA9J]
uses: [5VYBJYPYMW, 03NDVCSHSB, 03FKX7Z5DC, 055HT85T3S, 0VY3WPP9Y3, 0CHS7RBD39, 0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(linear_algebra)
    locator: lead section
  - book: isbn:9780135367971
    locator: Section 7.1
---

## Proof

We factor $m_T$ into prime powers, find one vector for each prime power, and show that the sum of these vectors has annihilator $m_T$.

1. If $V = 0$, then $m_T = 1$, and $v = 0$ has $m_v = 1$. So we may assume $V \ne 0$, and then $\deg m_T \ge 1$.
2. Write $m_T = p_1^{e_1} \cdots p_s^{e_s}$ with distinct monic [[irreducible polynomials|03FKX7Z5DC]] $p_j$ and $e_j \ge 1$. This factorization exists because $F[x]$ is a [[Euclidean domain|0CHS7RBD39]] and hence a [[unique factorization domain|055HT85T3S]].
3. Fix $j$. Put $r_j = m_T / p_j^{e_j}$ and $q_j = p_j^{e_j - 1} r_j = m_T / p_j$.
4. The polynomial $q_j$ is monic of degree less than $\deg m_T$. By the [[definition of the minimal polynomial|03NDVCSHSB]], $q_j(T) \ne 0$, so we can choose $x_j \in V$ with $q_j(T) x_j \ne 0$.
5. Put $u_j = r_j(T) x_j$. Then $p_j^{e_j}(T) u_j = m_T(T) x_j = 0$, because $(fg)(T) = f(T) g(T)$ for [[polynomials of an endomorphism|0E3MV6E6MG]].
6. By part 2 of the [[lemma on cyclic subspaces|5VYBJYPYMW]], $m_{u_j}$ divides $p_j^{e_j}$. By unique factorization, $m_{u_j} = p_j^{c}$ for some $c$ with $0 \le c \le e_j$.
7. Suppose that $c \le e_j - 1$. Then $p_j^{e_j - 1}(T) u_j = 0$ by part 2 of the lemma, and this says $q_j(T) x_j = 0$, against step 4. So $m_{u_j} = p_j^{e_j}$.
8. We now prove a claim: if $m_u = a$ and $m_w = b$ with $\gcd(a, b) = 1$, then $m_{u + w} = ab$.
9. First, $(ab)(T)(u + w) = b(T) a(T) u + a(T) b(T) w = 0$, because polynomials in $T$ commute. So $g = m_{u + w}$ divides $ab$.
10. Apply $b(T)$ to $g(T)(u + w) = 0$. Since $b(T) w = 0$, we get $(gb)(T) u = 0$, and so $a$ divides $gb$ by part 2 of the lemma.
11. By [[Bézout's identity|0VY3WPP9Y3]] in $F[x]$, $1 = sa + tb$ for some $s, t \in F[x]$. Then $g = sag + tbg$, and $a$ divides both terms, so $a$ divides $g$. In the same way, $b$ divides $g$.
12. Write $g = a g'$. Then $g' = s a g' + t b g' = s g + t b g'$, and $b$ divides both terms by step 11, so $b$ divides $g'$. Hence $ab$ divides $g$.
13. By steps 9 and 12, the monic polynomials $g$ and $ab$ divide each other, so $g = ab$. This proves the claim.
14. The polynomials $p_1^{e_1}, \dots, p_s^{e_s}$ are pairwise coprime, because the $p_j$ are distinct monic irreducible polynomials.
15. Let $v = u_1 + \cdots + u_s$. Apply the claim $s - 1$ times, with $a = p_1^{e_1} \cdots p_t^{e_t}$ and $b = p_{t+1}^{e_{t+1}}$ at step $t$. By induction on $t$, $m_v = p_1^{e_1} \cdots p_s^{e_s} = m_T$.

## Idea

The proof works one prime power of $m_T$ at a time.
For each prime power $p^e$ there is a vector with annihilator exactly $p^e$, since otherwise the proper divisor $m_T / p$ would kill all of $V$.
Annihilators with no common factor multiply when we add the vectors, so the sum of the chosen vectors has annihilator $m_T$.

## Variants

The lemma also follows from the [[cyclic decomposition theorem|R3Z20J19BR]]: the generator $v_r$ of the last summand has $m_{v_r} = d_r = m_T$.
Over an infinite field there is a short direct proof.
For each proper monic divisor $f$ of $m_T$, the kernel of $f(T)$ is a proper subspace, and there are only finitely many such $f$.
A vector space over an infinite field is not a finite union of proper subspaces, so some $v$ lies in none of these kernels, and then $m_v = m_T$.
