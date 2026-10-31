---
records:
    - id: FE1K3G7DQZ
      kind: monograph
      title: A Course in p-adic Analysis
      creators:
        - name: Alain M. Robert
          role: author
      date: "2000"
      expressions:
        - key: e1
          kind: edition
          date: "2000"
          ids:
            doi: 10.1007/978-1-4757-3254-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2000"
              ids:
                isbn:
                    - "9781441931504"
                    - "9781475732542"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-3254-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: FE1NTA4ZWY
      kind: preprint
      title: Flow Matching for Fast Posterior Sampling in Bayesian Inverse Problems
      creators:
        - name: Jan Blechschmidt
          role: author
        - name: Oliver G. Ernst
          role: author
        - name: Moritz Poguntke
          role: author
        - name: Björn Sprungk
          role: author
      date: "2026-10-01"
      subjects:
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: cs.NA
        - system: arxiv
          code: stat.CO
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-01"
          ids:
            arxiv: "2610.02377"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.02377"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
