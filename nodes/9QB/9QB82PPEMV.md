---
tag: 9QB82PPEMV
kind: example
name: Image compression by the SVD
msc: ["15A18", "65F55", "94A08"]
topics: [K0FNC6CWZN]
audience: ug2
instance_of: [000NPTMX6J]
illustrates: [JJT6GC055J]
uses: [000NPTMX6J, 09VMDSRXWJ, JJT6GC055J, JT8Q204E4R, 6VXM1T8PG7]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
    locator: lead section
---

## Example

A space probe must send a photo home over a very slow radio link, so every number it sends is expensive.
A gray-scale image of $m \times n$ pixels is an $m \times n$ matrix $A$ of brightness values.
Instead of all $m n$ entries, the probe can send a few layers of the image, the largest terms of its [[singular value decomposition|000NPTMX6J]].
We compute these layers for a small image, and we find out how much storage they need and how large the error is.
As a tiny image, take
$$A = \begin{pmatrix} 8 & 4 & 6 & 2 \\ 6 & 2 & 8 & 4 \\ 4 & 8 & 2 & 6 \\ 2 & 6 & 4 & 8 \end{pmatrix}.$$

1. Let $v_1 = \tfrac12 (1, 1, 1, 1)$, $v_2 = \tfrac12 (1, -1, 1, -1)$, $v_3 = \tfrac12 (1, 1, -1, -1)$ and $v_4 = \tfrac12 (1, -1, -1, 1)$.
   Let $u_1 = \tfrac12 (1, 1, 1, 1)$, $u_2 = \tfrac12 (1, 1, -1, -1)$ and $u_3 = \tfrac12 (1, -1, 1, -1)$.
   Both lists are orthonormal, because each vector has length $1$ and two different vectors have dot product $0$.
2. Multiply out: $A v_1 = (10, 10, 10, 10) = 20\, u_1$, $A v_2 = (4, 4, -4, -4) = 8\, u_2$, $A v_3 = (2, -2, 2, -2) = 4\, u_3$ and $A v_4 = 0$.
3. Since $v_1, \dots, v_4$ is an orthonormal basis, step 2 gives the SVD
$$A = 20\, u_1 v_1^{\mathsf T} + 8\, u_2 v_2^{\mathsf T} + 4\, u_3 v_3^{\mathsf T}.$$
   The [[singular values|09VMDSRXWJ]] are $20$, $8$, $4$ and $0$, and $A$ has rank $3$.
4. The total energy is $\norm{A}_F^2 = 20^2 + 8^2 + 4^2 = 480$, which equals the sum of the squares of the $16$ entries.
   This is the [[Frobenius norm|JT8Q204E4R]] in terms of the singular values.
5. The first layer $A_1 = 20\, u_1 v_1^{\mathsf T}$ is the matrix with all entries $5$, the mean brightness.
6. Two layers give
$$A_2 = A_1 + 8\, u_2 v_2^{\mathsf T} = \begin{pmatrix} 7 & 3 & 7 & 3 \\ 7 & 3 & 7 & 3 \\ 3 & 7 & 3 & 7 \\ 3 & 7 & 3 & 7 \end{pmatrix}.$$
   This shows the main pattern: the top two rows are bright in columns $1$ and $3$, and the bottom two rows are bright in columns $2$ and $4$.
7. By the [[Eckart-Young-Mirsky theorem|JJT6GC055J]], $\norm{A - A_1}_2 = \sigma_2 = 8$ and $\norm{A - A_1}_F = \sqrt{64 + 16} = \sqrt{80} \approx 8.94$.
   Also $\norm{A - A_2}_2 = \norm{A - A_2}_F = \sigma_3 = 4$.
   Check: $A - A_2 = 4\, u_3 v_3^{\mathsf T}$ has all entries $\pm 1$, so its Frobenius norm is $\sqrt{16} = 4$.
8. By the same theorem, no matrix of rank at most $2$ is closer to $A$ than $A_2$, in either norm.
9. A rank $k$ approximation needs $k$ singular values, $k$ vectors $u_i$ of length $m$ and $k$ vectors $v_i$ of length $n$.
   That is $k (m + n + 1)$ numbers instead of $m n$, and here $A_1$ needs $9$ numbers instead of $16$.
10. For a realistic $1000 \times 800$ image and $k = 50$, the storage is $50 \cdot 1801 = 90\,050$ numbers instead of $800\,000$, about $11.3\%$.
11. The approximation $A_2$ keeps the share $(400 + 64)/480 \approx 96.7\%$ of the energy, and its relative Frobenius error is $4 / \sqrt{480} \approx 0.18$.

## Remarks

### What the example shows

The singular values measure how much each layer contributes.
The error of truncation is known exactly from the dropped singular values, with no need to compare the images pixel by pixel.
For real photographs, the singular values often decay fast, so a small $k$ gives an acceptable picture.

### Change the image

If the image is $A_2$ itself, with the entries $7$ and $3$, then $\sigma_3 = 0$, and two layers store it exactly.
A random noise image has singular values of similar size, and no small $k$ gives a good approximation.

### Watch out: storage can grow

For $k \ge m n / (m + n + 1)$, the compressed form is no smaller than the image.
For the $4 \times 4$ example this bound is $16 / 9 \approx 1.8$, and $k = 2$ already needs $18$ numbers, more than $16$.
Compression by the SVD pays off only when $k$ is small compared with $m$ and $n$.

### Where the theory lives

The SVD is not the method of JPEG.
It needs a new basis for each image, which must be stored, while the cosine basis of JPEG is fixed, as in [[change of basis in signal and image processing|6NANBCYMG2]].
The fast algorithms for the SVD of large matrices belong to numerical linear algebra.

### Try it

First, find the best rank $1$ approximation of $B = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$ and its error.
The singular values are $3$ and $1$, so $B_1 = \begin{pmatrix} 3 & 0 \\ 0 & 0 \end{pmatrix}$, and the error in both norms is $\sigma_2 = 1$.

Second, find the storage share for a $500 \times 500$ image with $k = 20$.
It is $20 \cdot 1001 = 20\,020$ numbers instead of $250\,000$, about $8\%$.

## Explanations

### L1 human

A picture is a big table of numbers, one for each pixel.
Many pictures are made of a few simple layers: a background, a big shape, and fine details.
The SVD finds these layers and sorts them by importance.
Keeping only the first few layers gives a picture that looks almost the same and needs much less storage.
In the small example, two layers out of three keep about $97\%$ of the energy of the picture.

### L2 human

To compress an image matrix $A$ by the SVD, do these steps.

1. Compute the SVD $A = \sum_i \sigma_i u_i v_i^{\mathsf T}$, with $\sigma_1 \ge \sigma_2 \ge \cdots$.
2. Choose $k$, for example the smallest $k$ for which $\sigma_{k+1}^2 + \sigma_{k+2}^2 + \cdots$ is below a fixed share of $\norm{A}_F^2$.
3. Store $\sigma_i$, $u_i$ and $v_i$ for $i \le k$, which costs $k (m + n + 1)$ numbers.
4. Rebuild $A_k = \sum_{i \le k} \sigma_i u_i v_i^{\mathsf T}$.

The typical use is a first model of data compression and of noise reduction, and the same idea underlies principal component analysis.

### L3 human

The Eckart-Young-Mirsky theorem holds for every unitarily invariant norm, and it is the reason why truncated SVD is the standard low-rank approximation.
For a color image, one can treat each color channel separately, or use a tensor decomposition of the $m \times n \times 3$ array, where the best approximation of low rank need not exist.
Randomized algorithms compute $A_k$ for large $A$ with about $O(m n k)$ operations.
In statistics, the same truncation is principal component analysis, and in information retrieval it is latent semantic analysis.
