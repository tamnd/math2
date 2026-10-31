---
records:
    - id: YA5DBTQCB1
      kind: preprint
      title: Anticorrelated Noise Injection for Improved Generalization
      creators:
        - name: Antonio Orvieto
          role: author
        - name: Hans Kersting
          role: author
        - name: Frank Proske
          role: author
        - name: Francis Bach
          role: author
        - name: Aurelien Lucchi
          role: author
      date: "2022-02-06"
      subjects:
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2022-02-06"
          ids:
            arxiv: "2202.02831"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2202.02831"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: YA5M1Y9H6C
      kind: monograph
      title: A One-Semester Course on Probability
      creators:
        - name: Jolanta Misiewicz
          role: author
      date: "2025"
      expressions:
        - key: e1
          kind: edition
          date: "2025"
          ids:
            doi: 10.1007/978-3-031-86681-4
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Nature Switzerland
              date: "2025"
              ids:
                isbn:
                    - "9783031866807"
                    - "9783031866814"
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-031-86681-4
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
