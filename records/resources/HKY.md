---
records:
    - id: HKYC4MDQER
      kind: problem-set
      title: IMO 2015
      date: "2015"
      expressions:
        - key: e1
          kind: edition
          date: "2015"
      relations:
        - kind: part_of
          to: 931689K6X2
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: "2015"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: HKYRZSZPEC
      kind: preprint
      title: Minimax Rates for Estimating Powered Sliced Wasserstein Functionals
      creators:
        - name: Binh Thuan Tran
          role: author
      date: "2026-10-08"
      subjects:
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-08"
          ids:
            arxiv: "2610.12740"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.12740"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
