---
records:
    - id: B0NK570T01
      kind: monograph
      title: Exercises in Modules and Rings
      creators:
        - name: T. Y. Lam
          role: author
      date: "2007"
      expressions:
        - key: e1
          kind: edition
          date: "2007"
          ids:
            doi: 10.1007/978-0-387-48899-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2007"
              ids:
                isbn:
                    - "9780387988504"
                    - "9780387488998"
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-48899-8
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: B0NV0JBAKB
      kind: preprint
      title: Projection-Free Algorithms for Nonsmooth Stochastic Convex-Concave Saddle-Point Problems
      creators:
        - name: Khanh-Hung Giang-Tran
          role: author
        - name: Soroosh Shafiee
          role: author
      date: "2026-09-28"
      subjects:
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-28"
          ids:
            arxiv: "2609.35275"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.35275"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
